import numpy as np
import numpy.lib.recfunctions as rf
from pypcd import pypcd
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from matplotlib import animation, rc
import matplotlib.pyplot as plt

from IPython.display import display, Math, Latex, Markdown, HTML


def pcl_from_pcd(file: str) -> np.ndarray:
    """Loads pointclouds from pcd files

    Parameters
    ----------
        file (str): .pcd file
    Returns:
        pcl (np.ndarray): pointcloud as a numpy array of shape [n_points, m_channles]
    """
    assert file[-3:] == "pcd", 'Only "pcd" format is accepted.'
    pcd = pypcd.PointCloud.from_path(file)
    pcd = np.asarray(pcd.pc_data)
    return rf.structured_to_unstructured(pcd)


def plot_pcd(ax, points, **kwargs):
    ax.scatter(points[:, 0], points[:, 1], **kwargs)


def plot_grid(ax, ndt, color="blue"):
    x_min, y_min = ndt.bbox[0]
    x_max, y_max = ndt.bbox[1]
    num_voxels_x = int(np.ceil((x_max - x_min) / ndt.x_step))
    num_voxels_y = int(np.ceil((y_max - y_min) / ndt.y_step))
    xs = np.linspace(x_min, x_max, num_voxels_x)
    ys = np.linspace(y_min, y_max, num_voxels_y)

    for x in xs:
        ax.plot([x, x], [y_min, y_max], color=color)

    for y in ys:
        ax.plot([x_min, x_max], [y, y], color=color)


def plot_ndt(ax, ndt, plot_points=False):
    # Generate a grid of points to evaluate the distribution
    x_min, y_min = ndt.bbox[0]
    x_max, y_max = ndt.bbox[1]
    xs = np.linspace(x_min, x_max, 1000)
    ys = np.linspace(y_min, y_max, 1000)
    X, Y = np.meshgrid(xs, ys)
    pos = np.stack([X, Y], axis=2)
    Z = np.zeros_like(X)
    scatter = None
    for i, row in enumerate(ndt.grid):
        for j, cell in enumerate(row):
            if len(cell.points) < 1:
                continue

            if plot_points:
                label = None
                if i == len(ndt.grid)-1 and j == len(row)-1:
                    label = "Target or map"
                scatter =plot_pcd(ax, cell.points, color="red", label=label)

            # Calculate the probability density function of the distribution at each point
            try:
                mean = cell.mean
                cov = cell.cov
                rv = multivariate_normal(mean, cov)
                Z += rv.pdf(pos)
            except:
                pass

    im = ax.imshow(Z, extent=[xs.min(), xs.max(), ys.min(), ys.max()])
    plt.colorbar(im)

    # Plot desired grid
    plot_grid(ax, ndt, color="blue")

    return ax


def animate_icp_results(P, Q, R_list, t_list, corresp_values, xlim, ylim):
    """A function used to animate the iterative processes we use."""
    fig = plt.figure(figsize=(10, 6))
    anim_ax = fig.add_subplot(111)
    anim_ax.set(xlim=xlim, ylim=ylim)
    anim_ax.set_aspect("equal")
    anim_ax.set_title("Iteration 0")
    anim_ax.grid(True)
    plt.close()
    x_q, y_q, z_q = Q
    x_p, y_p, z_p = P
    # draw initial correspondeces
    corresp_lines = []
    for i in range(Q.shape[1]):
        corresp_lines.append(anim_ax.plot([], [], "grey")[0])
    # Prepare Q data.
    (Q_line,) = anim_ax.plot(x_q, y_q, "o", color="orangered", label="Source")
    # prepare empty line for moved data
    (P_line,) = anim_ax.plot(x_p, y_p, "o", color="#336699", label="Target")
    anim_ax.legend()
    def animate(frame):
        anim_ax.set_title(f"Iteration {frame}")
        Rn = R_list[frame]
        tn = t_list[frame]
        Pn = Rn.dot(P) + tn
        x_p, y_p, z_p = Pn
        P_line.set_data(x_p, y_p)
        draw_inc_corresp(Pn, Q, corresp_values[frame])
        return (P_line,)

    def draw_inc_corresp(points_from, points_to, correspondences):
        for corr_idx, (i, j) in enumerate(correspondences):
            x = [points_from[0, i], points_to[0, j]]
            y = [points_from[1, i], points_to[1, j]]
            corresp_lines[corr_idx].set_data(x, y)

    anim = animation.FuncAnimation(
        fig, animate, frames=len(R_list) - 1, interval=500, blit=True
    )
    return HTML(anim.to_jshtml())

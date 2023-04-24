Localization Project
=============================

The project task is to achieve the localization for a car driving within a simulated environment, covering a minimum distance of 170m from its starting position, while keeping the distance pose error within 1.2m. To accomplish this, you will make use of pointclouds extracted from a simulated car equipped with a lidar, which provides regular lidar scans. Additionally, there is an existing point cloud map "map.pcd" available, extracted from the CARLA simulator. You can achieve localization for the car by using point registration matching between the map and the scans.

We have prepared a few hands-on examples for you all to explore, which will help you grasp the concepts we've covered in the lesson more effectively.

In addition to that, we are sharing Dockerfiles with you so you can comfortably develop your algorithms on your own computers. To get started, kindly refer to the [build instructions](./README.md#build-instructions) for a step-by-step guide on how to utilize them properly.

Notice that you can open all jupyter notebooks inside vscode without using the browser.
---

Build Instructions.
-------------------

### Installation

#### **Windows**

1. Install Visual Studio Code.
2. Install Dev Container extension of Visual Studio Code.
3. Install WSL (please check that you are using WSL 2).
4. Install [Vcxsrv](https://sourceforge.net/projects/vcxsrv/)
5. Install [Docker for Windows](https://www.docker.com/).

##### **GPU support**

- Install the latest [NVIDIA driver](https://www.nvidia.com/download/index.aspx)

#### **Linux**

1. Install Visual Studio Code.
2. Install remote ssh extension of Visual Studio Code.
3. Install [Docker for Linux](https://docs.docker.com/engine/install/ubuntu/).

##### **GPU support**

- Install the latest NVIDIA driver
- Install [NVIDIA docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)

### Project Set Up

#### **Windows**

**Make sure that docker engine is running**

1. Open **vcxsrv** (xlaunch program).
2. Select **Multiple windows** and next.

![xlaunch](https://user-images.githubusercontent.com/27258035/225385489-d8c58607-d8f9-4e29-96c8-0801a3e1a883.png)

4. Select **Start no client** and next.
5. Mark **Disable access control** (IMPORTANT)

 ![disable](https://user-images.githubusercontent.com/27258035/225386074-df1976a5-6257-4533-997e-d6d770f1335b.png)

Copy the display that appears when you pose the mouse on the taskbar *(example:28147-PC:0.0)*

![display_name](https://user-images.githubusercontent.com/27258035/225386808-374ddbc7-4baa-4bad-9b16-482213a0213b.png)

9. Open the project in VSCode folder (ctrl+k ctrl+o).
10. Open and uncomment the line **"-e", "DISPLAY=\\",** and change the display name with your display name.
11. Open controls palette clicking the green button in the lower left part of vscode

![vscode](https://user-images.githubusercontent.com/27258035/224482432-78a084f5-ef82-4b42-9028-26e23701bf19.png)

13. Select the option, **Reopen in container**.
![image](https://user-images.githubusercontent.com/27258035/224482946-05fd6d80-fb4d-4888-8af1-6c43b3e0bb60.png)

15. Check that display is forwarded by typing xclock on a new terminal inside vscode.
16. Start developing your algorithms.

##### **CPU support**

- go to [.devcontainer/.devcontainer.json](.devcontainer/devcontainer.json#9)
- Uncomment the line "dockerfile": "../Dockerfile\_CPU"
- Comment the line "dockerfile": "../Dockerfile\_GPU"

##### **GPU support**

- go to [.devcontainer/.devcontainer.json](.devcontainer/devcontainer.json#10)
- Uncomment the line **"dockerfile": "../Dockerfile\_GPU"**
- Uncomment the line **"--gpus", "all",**
- Comment the line "dockerfile": "../Dockerfile\_CPU"
- Check you are using cuda by typing ` nvidia-smi` on a vscode terminal.

#### **Linux**

**Make sure that docker engine is running**

1. Open project in VSCode folder (ctrl+k ctrl+o).
2. Open controls panel clicking the green buttom in the lower left part of vs code.
3. Select the option, **Reopen in container**.
4. Start developing your algorithms.

##### **CPU support**

- go to [.devcontainer/.devcontainer.json](.devcontainer/devcontainer.json#9)
- Uncomment the line "dockerfile": "../Dockerfile\_CPU"
- Comment the line "dockerfile": "../Dockerfile\_GPU"

##### **GPU support**

- go to [.devcontainer/.devcontainer.json](.devcontainer/devcontainer.json#10)
- Uncomment the line **"dockerfile": "../Dockerfile\_GPU"**
- Uncomment the line **"--gpus", "all",**
- Comment the line "dockerfile": "../Dockerfile\_CPU"
- Check you are using cuda by typing ` nvidia-smi` on a vscode terminal.

---

Project Instructions
--------------------

For this assignment, you will be required to complete three subtasks, which are:

1. **ICP Localization:** This involves using the Iterative Closest Points (ICP) method to perform 3D localization.
2. **NDT Localization:** This involves using the Normal Distribution Transform (NDT) algorithm to perform 3D localization.
3. **Analysis:** This task requires you to compare the results obtained from the first two tasks.

To complete each task, you have the option of using either C++ or Python. We recommend using the PCL library in C++ to carry out these tasks.


### 1 ICP Localization

In the ICP localization part of the project you will perform the localization of the car in the given map using the Iterative Closest Point algorithm. You can use the libraries provided by PCL library in c++ or Open3D in Python. This part of the project involves implementing the following series of tasks:

- Load the map from the map.pcd file.
- Iteritatively go through each frame and localize the car in the given map.
- Extract point cloud information from the dataset provided.
- Downsample the pointcloud with a voxel grid filter.
- Configure the ICP module to localize the vehicle.
- Use performance measures to evaluate the localization effectiviness.
- Remember that to pass this task, the maximum lateral error cannot be bigger than 1.2 meters.
- Also evaluate the computing time. There is not a harsh requirement here, but should be analized.

By completing these tasks, you'll gain valuable experience in configuring and utilizing ICP for real-world applications.

### 2 NDT Localization.

In the ICP localization part of the project you will perform the localization of the car in the given map using the Normal Distribution Transform (NDT) algorithm. You can use the libraries provided by PCL library in c++ or Open3D in Python. This part of the project involves implementing the following series of tasks:

- Load the map from the map.pcd file.
- Iteritatively go through each frame and localize the car in the given map.
- Extract point cloud information from the dataset provided.
- Downsample the pointcloud with a voxel grid filter.
- Configure the NDT module to localize the vehicle.
- Use performance measures to evaluate the localization effectiviness.
- Remember that to pass this task, the maximum lateral error cannot be bigger than 1.2 meters.
- Also evaluate the computing time. There is not a harsh requirement here, but should be analized.

By completing these tasks, you'll gain valuable experience in configuring and utilizing ICP for real-world applications.

---

Dataset
-------

You will have to work on the dataset provided [here](https://drive.google.com/file/d/19XqBbQ6Ha3Xt_SmLVpq04Bh8UjJgxZHo/view?usp=share_link).

You will be provided with a dataset consisting of a map of a simulated environment stored in the "map.pcd" file and point clouds captured by a lidar while driving through the environment in the files "frame_\<frame_number>".

To calculate the lateral error, we have provided you with the real poses of the car through the driving in a file called "ground_truth.csv".This file has the information of the position and rotation of the car in every frame.

---

Submission Template
-------------------

The submission must be done in a zip file containing the implemented code and a report in a **PDF** with the following specifications:

### Project Overview

This section should contain a brief description of the project and what you are trying to achieve.

### Set up

This section should contain a brief description of the steps to follow to run the code. There must be a detailed explanation of how to run the implemented code so we can see run them on our local machine.

### ICP Localization

This section should describe the code utilized for ICP localization, specifically:

- Brief explanation of the ICP algorithm. 
- Module configuration and selected parameters.
- Performance metrics attained on the provided dataset.
- Runnable code that demonstrates the localization working and a visual representation of the results using a visualization library.

### Multi-Object Tracking.

This section should describe the code utilized for NDT localization, specifically:

- Brief explanation of the NDT algorithm. 
- Module configuration and selected parameters.
- Performance metrics attained on the provided dataset.
- Runnable code that demonstrates the localization working and a visual representation of the results using a visualization library.

### Analysis

This section should include a extensive analysis and comparison of both algorithms, including:

- Error through frames
- Maximum error
- Computation time
- Complexity

Please note that your report should be in PDF format, and your submission should include the implemented code and any additional materials necessary for us to replicate your results.

Good luck with your task! 🚀👍
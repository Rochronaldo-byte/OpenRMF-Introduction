# OpenRMF--Introduction
🚀 Getting Started with OpenRMF (Robot Middleware Framework)

OpenRMF (Open-source Robotics Middleware Framework) orchestrates fleets of robots in shared environments like airports, warehouses, and hospitals. It allows simulation, scheduling, and real-time fleet management using **ROS 2** and Gazebo.  

This guide helps you  **set up, run simulations, and dispatch tasks for demo robots**.

---

## **Clone the RMF Demos**

```bash
mkdir -p ~/rmf_ws/src
cd ~/rmf_ws/src
git clone https://github.com/open-rmf/rmf_demos.git

## **Install Dependencies**
cd ~/rmf_ws
rosdep update
rosdep install --from-paths src --ignore-src -y
python3 -m pip install -U colcon-common-extensions


## **Build Workspace**
cd ~/rmf_ws
colcon build --symlink-install
source install/setup.bash

## **Launch File**
ros2 launch rmf_demos_gz office.launch.xml


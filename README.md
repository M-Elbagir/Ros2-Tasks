# ROS 2 Practice Projects

This project contains two small ROS 2 exercises. The first demonstrates publisher-subscriber communication, and the second uses a Python script to draw a square in turtlesim.

## 1. PubSub

- `talker` publishes a string on `topic`
- `listener` reads from the same topic

Creation process:

1. Create a ROS 2 Python package with `ros2 pkg create --build-type ament_python pubsub`.
2. Add a publisher node called `talker` and a subscriber node called `listener`.
3. Build the package and run both nodes in separate terminals.

Run:

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python pubsub
cd ~/ros2_ws
source /opt/ros/humble/setup.bash
colcon build --packages-select pubsub
source install/setup.bash
ros2 run pubsub talker
```

In another terminal:

```bash
cd ~/ros2_ws
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 run pubsub listener
```

## 2. Turtle Square Pattern

Creation process:

1. Start `turtlesim` so the turtle window is available.
2. Create a Python script named `turtle_square.py`.
3. Use a timer to move the turtle forward for a few steps, then turn, and repeat until a square is drawn.

- `turtle_square.py`: moves straight for a few timer steps, then turns, so the turtle draws a square

Run:

```bash
source /opt/ros/humble/setup.bash
ros2 run turtlesim turtlesim_node
```

Then in another terminal:

```bash
source /opt/ros/humble/setup.bash
python3 /home/mo/turtle_scripts/turtle_square.py
```
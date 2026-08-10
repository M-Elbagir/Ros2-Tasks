# ROS 2 Practice Projects

## PubSub

Location: `/home/mo/ros2_ws/src/pubsub`

- `talker` publishes a string on `topic`
- `listener` reads the same topic

Create and run:

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

## Turtle Scripts

Location: `/home/mo/turtle_scripts`

- `turtle_circle.py`: moves forward and turns continuously, so the turtle draws a circle
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
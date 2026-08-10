"""A ROS 2 node that publishes incrementing string messages."""

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import String


class MinimalPublisher(Node):
    """Publish a message to the `topic` topic once per second."""

    def __init__(self) -> None:
        super().__init__("minimal_publisher")
        self.publisher_ = self.create_publisher(String, "topic", 10)
        self.count_ = 0
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self) -> None:
        message = String()
        message.data = f"Hi from Smart Methods: {self.count_}"
        self.publisher_.publish(message)
        self.get_logger().info(f'Publishing: "{message.data}"')
        self.count_ += 1


def main(args=None) -> None:
    """Run the publisher node."""
    rclpy.init(args=args)
    node = MinimalPublisher()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

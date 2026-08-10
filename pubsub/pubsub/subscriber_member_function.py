"""A ROS 2 node that logs received string messages."""

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import String


class MinimalSubscriber(Node):
    """Subscribe to messages published on the `topic` topic."""

    def __init__(self) -> None:
        super().__init__("minimal_subscriber")
        self.subscription = self.create_subscription(
            String, "topic", self.listener_callback, 10
        )

    def listener_callback(self, message: String) -> None:
        """Log a received message."""
        self.get_logger().info(f'I heard: "{message.data}"')


def main(args=None) -> None:
    """Run the subscriber node."""
    rclpy.init(args=args)
    node = MinimalSubscriber()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

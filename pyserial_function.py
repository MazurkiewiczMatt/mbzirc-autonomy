import rclpy
from rclpy.node import Node


class SerialNode(Node):
    def __init__(self):
        super().__init__('serialnode')
        self.timer = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('Serial Node is working')

def main(args=None):
    rclpy.init(args=args)
    serialnode = SerialNode()
    rclpy.spin(serialnode)

if __name__ == '__main__':
    main()

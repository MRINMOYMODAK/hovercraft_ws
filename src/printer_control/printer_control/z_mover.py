import rclpy
from rclpy.node import Node
import time
import os

class ZMover(Node):
    def __init__(self):
        super().__init__('z_mover_node')
        self.z_position = 50  # Start at 50 mm
        self.max_z = 400      # Maximum Z position
        self.min_z = 50       # Minimum Z position
        self.timer = self.create_timer(2.0, self.move_z)  # Timer to call move_z() every 2 seconds

    def move_z(self):
        # Send G-code command to move the Z-axis
        self.get_logger().info(f'Moving Z-axis to {self.z_position} mm')

        # Here you would interface with your 3D printer to send the G-code command.
        # For this example, we're just printing to the log.
        os.system(f'echo "G1 Z{self.z_position}" > /dev/ttyUSB0')  # Example for sending to printer via serial (adjust as needed)

        # Update Z position for the next movement (increment by 10 mm)
        self.z_position += 10
        if self.z_position > self.max_z:
            self.z_position = self.min_z  # Reset to minimum Z position once max is reached

def main(args=None):
    rclpy.init(args=args)
    z_mover = ZMover()
    rclpy.spin(z_mover)

    z_mover.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

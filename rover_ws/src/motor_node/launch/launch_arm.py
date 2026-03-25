from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    ld.add_action(DeclareLaunchArgument(
        'ee_serial_port',
        default_value='/dev/ttyACM2',
        description='Serial port for end effector ESP32'
    ))

    # Joystick node
    ld.add_action(Node(
        package='joy',
        executable='joy_node',
        name='joy_node',
        #parameters=[{'autorepeat_rate': 0.0}],
        output='screen'
    ))

    # SocketCAN bridge
    ld.add_action(Node(
        package='nobleo_socketcan_bridge',
        executable='socketcan_bridge',
        name='socketcan_bridge',
        output='screen',
        parameters=[{'interface': 'can1'}]
    ))

    # Motor controller
    ld.add_action(Node(
        package='motor_node',
        executable='start_controller',
        name='motor_controller',
        parameters=[{'ee_serial_port': LaunchConfiguration('ee_serial_port')}],
        output='screen'
    ))

    return ld

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    # # Joystick node
    # ld.add_action(Node(
    #     package='joy',
    #     executable='joy_node',
    #     name='joy_node',
    #     #parameters=[{'autorepeat_rate': 0.0}],
    #     output='screen'
    # ))

    # WebSocket bridge for GUI
    ld.add_action(Node(
        package='rosbridge_server',
        executable='rosbridge_websocket',
        name='rosbridge_websocket',
        parameters=[{'port': 9091}],
        output='screen'
    ))

    # SocketCAN bridge
    ld.add_action(Node(
        package='nobleo_socketcan_bridge',
        executable='socketcan_bridge',
        name='socketcan_bridge',
        output='screen'
    ))

    # Motor controller
    ld.add_action(Node(
        package='motor_node',
        executable='start_controller',
        name='motor_controller',
        output='screen'
    ))

    return ld

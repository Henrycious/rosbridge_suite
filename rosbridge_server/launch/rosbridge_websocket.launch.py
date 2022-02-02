import os
from re import M

from ament_index_python import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.actions import GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.substitutions import TextSubstitution
from launch_ros.actions import Node
from launch_ros.actions import PushRosNamespace
import subprocess

def generate_launch_description():
    ############
    ## config ##
    ############

    port=9090
    address='' 
    ssl=False
    certfile=''
    keyfile=''

    retry_startup_delay=5.0
    fragment_timeout=600
    delay_between_messages=0
    max_message_size=10000000
    unregister_timeout=10

    use_compression=False

    topics_glob=''
    service_glob=''
    params_glob=''
    bson_only_mode=False

    websocket_publish = Node(
        package='rosbridge_server',
        executable='rosbridge_websocket',
        name='websocket_publish_port_9090',
        parameters=[{
            'port': port,
            'address': address,
            'ssl': ssl,     
            'certfile': certfile,
            'keyfile': keyfile,
            'retry_startup_delay':retry_startup_delay,
            'fragment_timeout':fragment_timeout,
            'delay_between_messages':delay_between_messages,
            'max_message_size':max_message_size,
            'unregister_timeout':unregister_timeout,
            'use_compression':use_compression,
            'topics_glob':topics_glob,
            'service_glob':service_glob,
            'params_glob':params_glob,
            'bson_only_mode':bson_only_mode,
        }]
    )
    rosapi = Node(
        package='rosapi',
        executable='rosapi_node',
        name='rosapi',
        parameters=[{
            'topics_glob':topics_glob,
            'service_glob':service_glob,
            'params_glob':params_glob,
        }]
    )

    return LaunchDescription([
        websocket_publish,
        rosapi,
    ])


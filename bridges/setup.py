from setuptools import setup

package_name = 'bridges'

setup(
    name=package_name,
    version='2.8.0',
    packages=[package_name],
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name],
        ),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Roch Ronaldo',
    maintainer_email='roch4619@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            (
                'fleet_socketio_bridge='
                'bridges.fleet_socketio_bridge:main',
                'fleet_robotmanager_mqtt_bridge='
                'bridges.fleet_robotmanager_mqtt_bridge:main',
            ),
        ],
    },
)

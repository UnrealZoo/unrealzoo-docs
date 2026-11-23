# Drivable Vehicles


# 🚗Cars

Class Name: BP_BaseCar_C

| BP_function | input  | output  | help |
| --- | --- | --- | --- |
| set_move | {angular} {velocity} |  | control the object for a single step with angle and linear velocity: |
| set_stop |  |  | stop the car with handbrake |
| nav_to_goal | {x} {y} {z} |  | Assign the agent a navigation goal, and use Nav mesh to calculate the legal path and control the target moving to the goal. (The goal has to be reachable in the environment.) |
|  |  |  |  |
| set_speed | {speed} |  | set the max velocity of the agent object |
| set_interval | {value} |  | set the interval of the time to simulate animation. value: 1 ~ 1000 |
| set_acc | {acceleration} |  | set the max acceleration of the agent object |
| set_phy  | {value} |  | simulate physics, 0: turn off, 1 :turn on |
| set_cam  | {x} {y} {z} {row} {pitch} {yaw}  |  | set the camera pose relative to the actor |
| set_app  | {id} |  | set the appearance of the agent object, id: 0~2 |
| set_viewport |  |  | After executing this command, the Game window will display the agent's first-person perspective. Enter the command again to switch the window to display the free-roaming perspective. |
| enter_exit_car | {player index} |  | Human character interactions with cars involve standing near the car door. When the character stands close to the door and executes the corresponding command with the character index, it triggers animations for entering and exiting the car, which can be repeated by executing the command again |



# 🏍️Motorbikes

Class Name: MotorBikes_C

| BP_function | input  | output  | help |
| --- | --- | --- | --- |
| set_move | {angular} {velocity} |  | control the object for a single step with angle and linear velocity: |
| nav_to_goal | {x} {y} {z} |  | Assign the agent a navigation goal, and use Nav mesh to calculate the legal path and control the target moving to the goal. (The goal has to be reachable in the environment.) |
| set_speed | {speed} |  | set the max velocity of the agent object |
| set_interval | {value} |  | set the interval of the time to simulate animation. value: 1 ~ 1000 |
| set_app  | {id} |  | set the appearance of the agent object, id: 0~8 |
| set_viewport |  |  | After executing this command, the Game window will display the agent's first-person perspective. Enter the command again to switch the window to display the free-roaming perspective. |





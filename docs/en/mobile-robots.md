# Mobile Robots

Mobile Rbots share the same class with human characters (BP_character_C), developers could directly use set_app to change the mesh into robotdog(id:20~33).


| BP_function | input  | output  | help |
| --- | --- | --- | --- |
| set_move | {angular} {velocity} |  | control the object for a single step with angle and linear velocity: |
| nav_to_goal | {x} {y} {z} |  | Assign the agent a navigation goal, and use Navmesh and AI-controller built-in plugin to automatically control its movement to reach the goal via the shortest path. (The goal has to be reachable in the environment.) |
| nav_to_target | {target_object} {distance} |  | Assign the current agent to a target_object, utilize Navmesh and AI controller to dynamically follow the target_object, stopping at a specified distance from it |
| nav_random |  |  | control agent randomly wandering around |
| set_speed | {speed} |  | set the max velocity of the agent object |
| set_interval | {value} |  | set the interval of the time to simulate animation. value: 1 ~ 1000 |
| set_acc | {acceleration} |  | set the max acceleration of the agent object |
| set_phy  | {value} |  | simulate physics, 0: turn off, 1 :turn on |
| set_cam  | {x} {y} {z} {row} {pitch} {yaw}  |  | set the camera pose relative to the actor |
| set_app  | {id} |  | set the appearance of the agent object, id: 20~33 |
| set_photo_mode |  |  | Switch the perspective to the first-person view of the agent. Change it back to the third-person view while executing the command a second time. |
| generate_nav_goal |  | { ”nav_goal”: “X=0.00 Y=0.00 Z=0.00” } | generate a reachable goal location around the agent, return the location. |
|  |  |  |  |
| get_hit |  | { ”hitresult”: “true(or false)” } | get the hit flag(with other target or static object) of the agent object, return true or false. |
| get_speed |  | { ”speed”: “0.000” } | get the agent’s linear velocity, return value |
| get_angle |  | { ”angle”: “0.000” } | get the agent’s angular velocity, return value |
|  |  |  |  |




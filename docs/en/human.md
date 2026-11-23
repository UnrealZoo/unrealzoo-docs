# Human


Class Name: BP_Character_C 

New added animation (lie down, climb, crouch, slide, etc)

vbp {instance_name} {bp_function} {args 1} {args2}...

| BP_function | input  | output  | help |
| --- | --- | --- | --- |
| set_move | {angular} {velocity} |  | control the object for a single step with angle and linear velocity: |
| nav_to_goal | {x} {y} {z} |  | Assign the agent a navigation goal, and use Navmesh and AI-controller built-in plugin to automatically control its movement to reach the goal via the shortest path. (The goal has to be reachable in the environment.) |
| nav_random | {radius} {loop} | { ”random_location”:  “X=0.00 Y=0.00 Z=0.00” } | control agent randomly wandering around. Agent randomly selects a point within its own radius range for navigation. The loop parameter controls whether continuous navigation is performed.(True for continuous navigation). Return with the randomly sampled location. |
| set_speed | {speed} |  | set the max velocity of the agent object |
| set_interval | {value} |  | set the interval of the time to simulate animation. value: 1 ~ 1000 |
| set_acc | {acceleration} |  | set the max acceleration of the agent object |
| set_phy  | {value} |  | simulate physics, 0: turn off, 1 :turn on |
| set_cam  | {x} {y} {z} {row} {pitch} {yaw}  |  | set the camera pose relative to the actor |
| set_app  | {id} |  | set the appearance of the agent object, id: 0~19 |
| set_viewport |  |  | After executing this command, the Game window will display the agent's first-person perspective. Enter the command again to switch the window to display the free-roaming perspective. |
| generate_nav_goal | {radius} | { ”nav_goal”: “X=0.00 Y=0.00 Z=0.00” } | generate a reachable goal location around the agent radius, return the location. |
|  |  |  |  |
| get_hit |  | { ”hitresult”: “true(or false)” } | get the hit flag(with other target or static object) of the agent object, return true or false. |
| get_speed |  | { ”speed”: “0.000” } | get the agent’s linear velocity, return value |
| get_angle |  | { ”angle”: “0.000” } | get the agent’s angular velocity, return value |
|  set_jump |  |  | The agent displays a jumping animation, demonstrating a crossing motion when encountering obstacles that can be overcome. |
| set_crouch |  |  | The agent demonstrates a crouching animation, which, when paired with the set_move action, enables a crouching walking animation. |
| set_liedown | {Direction_Frontback} {Direction_Rightleft} |  | The agent displays a near-death falling animation, with the direction of the fall controlled by two parameters: "Direction_Frontback" and "Direction_Rightleft". For example, (100, 0) indicates falling forward, while (-100, 0) indicates falling backward. |
| set_standup |  |  | The agent demonstrates an animation transitioning from a near-death fallen state to standing up, with the direction of the stand-up automatically matching the previous fall direction. |
| set_open_door | {1/0} |  | The agent open/close the door.(1 for open, 0 for close) |
| set_pickup |  |  | The agent pick/drop a item. |





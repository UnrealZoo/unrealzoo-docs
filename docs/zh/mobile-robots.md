# 移动机器人

移动机器人与人类角色共享同一个类（BP_character_C），开发者可以直接使用 set_app 将网格体更改为机器狗（id:20~33）。


| BP_function | input  | output  | help |
| --- | --- | --- | --- |
| set_move | {angular} {velocity} |  | 通过角度和线速度控制对象执行单步移动： |
| nav_to_goal | {x} {y} {z} |  | 为智能体分配一个导航目标，使用 Navmesh 和内置的 AI-controller 插件自动控制其移动，通过最短路径到达目标。（目标必须在环境中可达。） |
| nav_to_target | {target_object} {distance} |  | 将当前智能体分配到一个 target_object，利用 Navmesh 和 AI controller 动态跟随 target_object，并在距离其指定距离处停止 |
| nav_random |  |  | 控制智能体随机游走 |
| set_speed | {speed} |  | 设置智能体对象的最大速度 |
| set_interval | {value} |  | 设置模拟动画的时间间隔。value: 1 ~ 1000 |
| set_acc | {acceleration} |  | 设置智能体对象的最大加速度 |
| set_phy  | {value} |  | 模拟物理，0：关闭，1：开启 |
| set_cam  | {x} {y} {z} {row} {pitch} {yaw}  |  | 设置相机相对于 actor 的位姿 |
| set_app  | {id} |  | 设置智能体对象的外观，id: 20~33 |
| set_photo_mode |  |  | 将视角切换为智能体的第一人称视角。再次执行该命令时切换回第三人称视角。 |
| generate_nav_goal |  | { ”nav_goal”: “X=0.00 Y=0.00 Z=0.00” } | 在智能体周围生成一个可达的目标位置，返回该位置。 |
|  |  |  |  |
| get_hit |  | { ”hitresult”: “true(or false)” } | 获取智能体对象（与其他目标或静态物体）的碰撞标志，返回 true 或 false。 |
| get_speed |  | { ”speed”: “0.000” } | 获取智能体的线速度，返回该值 |
| get_angle |  | { ”angle”: “0.000” } | 获取智能体的角速度，返回该值 |
|  |  |  |  |
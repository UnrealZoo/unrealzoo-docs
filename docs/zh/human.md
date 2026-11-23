# Human

类名：BP_Character_C

新增动画（躺下、攀爬、蹲下、滑行等）

vbp {instance_name} {bp_function} {args 1} {args2}…

| BP_function | 输入 | 输出 | 说明 |
| --- | --- | --- | --- |
| set_move | {angular} {velocity} |  | 通过角度和线速度控制对象进行单步移动。 |
| nav_to_goal | {x} {y} {z} |  | 为智能体分配导航目标，利用 Navmesh 和 AI-controller 内置插件自动控制其沿最短路径到达目标。（目标必须在环境中可达。） |
| nav_random | {radius} {loop} | { "random_location": "X=0.00 Y=0.00 Z=0.00" } | 控制智能体随机游走。智能体在自身半径范围内随机选择一点进行导航。loop 参数控制是否连续导航（True 表示连续导航）。返回随机采样的位置。 |
| set_speed | {speed} |  | 设置智能体对象的最大速度。 |
| set_interval | {value} |  | 设置模拟动画的时间间隔。value：1 ~ 1000 |
| set_acc | {acceleration} |  | 设置智能体对象的最大加速度。 |
| set_phy | {value} |  | 模拟物理，0：关闭，1：开启 |
| set_cam | {x} {y} {z} {row} {pitch} {yaw} |  | 设置相机相对于 actor 的位姿。 |
| set_app | {id} |  | 设置智能体对象的外观，id：0~19 |
| set_viewport |  |  | 执行此命令后，Game 窗口将显示智能体的第一人称视角。再次输入该命令可将窗口切换为自由漫游视角。 |
| generate_nav_goal | {radius} | { "nav_goal": "X=0.00 Y=0.00 Z=0.00" } | 在智能体半径范围内生成一个可达的目标位置，返回该位置。 |
|  |  |  |  |
| get_hit |  | { "hitresult": "true(or false)" } | 获取智能体对象的碰撞标志（与其他目标或静态对象），返回 true 或 false。 |
| get_speed |  | { "speed": "0.000" } | 获取智能体的线速度，返回该值。 |
| get_angle |  | { "angle": "0.000" } | 获取智能体的角速度，返回该值。 |
| set_jump |  |  | 智能体显示跳跃动画，在遇到可跨越的障碍物时展示跨越动作。 |
| set_crouch |  |  | 智能体展示蹲下动画，与 set_move 动作配合使用时，可启用蹲行动画。 |
| set_liedown | {Direction_Frontback} {Direction_Rightleft} |  | 智能体显示濒死倒下动画，倒下方向由两个参数控制：“Direction_Frontback”和“Direction_Rightleft”。例如，(100, 0) 表示向前倒下，(-100, 0) 表示向后倒下。 |
| set_standup |  |  | 智能体展示从濒死倒下状态过渡到站起的动画，站起方向自动匹配之前的倒下方向。 |
| set_open_door | {1/0} |  | 智能体打开/关闭门。（1 表示打开，0 表示关闭） |
| set_pickup |  |  | 智能体拾取/放下物品。 |
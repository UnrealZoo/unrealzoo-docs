# 可驾驶车辆


# 🚗汽车

类名：BP_BaseCar_C

| BP_function | 输入  | 输出  | 说明 |
| --- | --- | --- | --- |
| set_move | {angular} {velocity} |  | 使用角度和线速度控制物体执行单步移动： |
| set_stop |  |  | 使用手刹使汽车停止 |
| nav_to_goal | {x} {y} {z} |  | 为智能体分配一个导航目标，并使用 Nav mesh 计算合法路径并控制目标移动至该目标。（目标必须在环境中可达。） |
|  |  |  |  |
| set_speed | {speed} |  | 设置智能体对象的最大速度 |
| set_interval | {value} |  | 设置模拟动画的时间间隔。value：1 ~ 1000 |
| set_acc | {acceleration} |  | 设置智能体对象的最大加速度 |
| set_phy  | {value} |  | 模拟物理效果，0：关闭，1：开启 |
| set_cam  | {x} {y} {z} {row} {pitch} {yaw}  |  | 设置相机相对于 actor 的位姿 |
| set_app  | {id} |  | 设置智能体对象的外观，id：0~2 |
| set_viewport |  |  | 执行此命令后，Game 窗口将显示智能体的第一人称视角。再次输入该命令可将窗口切换为自由漫游视角。 |
| enter_exit_car | {player index} |  | 人类角色与汽车的交互需要站在车门附近。当角色靠近车门并使用角色索引执行相应命令时，会触发进入和退出汽车的动画，再次执行该命令可重复触发 |



# 🏍️摩托车

类名：MotorBikes_C

| BP_function | 输入  | 输出  | 说明 |
| --- | --- | --- | --- |
| set_move | {angular} {velocity} |  | 使用角度和线速度控制物体执行单步移动： |
| nav_to_goal | {x} {y} {z} |  | 为智能体分配一个导航目标，并使用 Nav mesh 计算合法路径并控制目标移动至该目标。（目标必须在环境中可达。） |
| set_speed | {speed} |  | 设置智能体对象的最大速度 |
| set_interval | {value} |  | 设置模拟动画的时间间隔。value：1 ~ 1000 |
| set_app  | {id} |  | 设置智能体对象的外观，id：0~8 |
| set_viewport |  |  | 执行此命令后，Game 窗口将显示智能体的第一人称视角。再次输入该命令可将窗口切换为自由漫游视角。 |
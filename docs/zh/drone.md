# Drone

类名：BP_Drone01_C

| BP_function | 输入 | 输出 | 说明 |
| --- | --- | --- | --- |
| set_move | {x} {y} {z} {yaw} |  | 通过各轴（x、y、z、yaw）的力控制物体，取值范围为 -1 到 1 |
| set_rotation | {yaw} |  | 设置无人机在世界坐标系中的绝对旋转位置 |
| set_speed | {speed} |  | 设置智能体对象的最大速度 |
| set_interval | {value} |  | 设置模拟动画的时间间隔。value：1 ~ 1000 |
| set_acc | {acceleration} |  | 设置智能体对象的最大加速度 |
| set_phy  | {value} |  | 模拟物理，0：关闭，1：开启 |
| set_cam | {x} {y} {z} {row} {pitch} {yaw}  |  | 设置相机相对于 actor 的位姿 |
| set_viewport |  |  | 执行此命令后，Game 窗口将显示智能体的第一人称视角；再次输入该命令可将窗口切换为自由漫游视角 |
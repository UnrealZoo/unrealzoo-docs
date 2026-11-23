# Gym 环境工具包

## 包装器

此外还提供若干包装器，可用于以不同方式修改环境。

### ConfigUE

- ConfigUEWrapper 用于配置 Unreal Engine 二进制的启动设置，可设置 Unreal Engine 环境的各类参数，例如离屏渲染、观测分辨率、通信协议、docker 等。
```python
from gym_unrealcv.envs.wrappers import configUE 
configUE.ConfigUEWrapper(env, docker=False, resolution=(160, 160), display=None,
                         offscreen=False, use_opengl=False, nullrhi=False, 
                         gpu_id=None, sleep_time=5, comm_mode='tcp')
```

### TimeDilation

- TimeDilationWrapper 用于控制 Unreal Engine 环境中仿真的速度，适用于为不同任务模拟各种 FPS 情况。
```python
from gym_unrealcv.envs.wrappers import time_dilation
env = time_dilation.TimeDilationWrapper(env, reference_fps=30, update_steps=60) 
```

### EarlyDone

- EarlyDoneWrapper 用于根据特定条件提前结束 episode。用户可针对不同任务修改源代码。该包装器可防止 episode 运行时间过长。
```python
from gym_unrealcv.envs.wrappers import early_done
env = early_done.EarlyDoneWrapper(env, max_lost_steps=100)
```

### RandomPopulation

- RandomPopulationWrapper 会用指定数量的智能体随机填充环境：
```python
env = augmentation.RandomPopulationWrapper(env, num_min=5, num_max=10, random_target=False)
```
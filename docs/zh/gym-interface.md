# Gym 接口

> 📌 Gym_unrealcv 是一个 Python 库，提供了将 Unreal Engine（UE4/UE5）与 OpenAI 的 Gym 结合使用的接口。它允许你使用 Unreal Engine 和 UnrealCV 创建强化学习环境。

# 1. 安装：

你可以在源码文件夹中使用 pip 安装 gym_unrealcv：

pip install -e .


# 2. 创建环境：

要创建环境，你可以使用 gym.make() 函数并传入你想要创建的环境的 ID。例如：

```python
import gym 
import gym_unrealcv
env = gym.make('UnrealTrack-SuburbNeighborhood_Day-ContinuousMask-v0') # build an environment
# Environment Name: Unreal{Task}-{Scene_Name}-{Action Space}{Observation Space}-{version}
```

本页介绍在 UnrealZoo-Gym 中创建环境实例的命名约定。理解此格式对于正确初始化训练环境至关重要。

## 📝 命名格式

```plain text
Unreal{task}-{MapName}-{ActionSpace}{ObservationType}-v{version}
```

## 📊 参数参考

### {task} - 任务类型

  - Track - 视觉跟踪任务（跟随移动目标）
  - Navigation - 导航任务（到达目的地）
  - Rendezvous - 多智能体会合任务
  - Rescue - 搜索与救援任务
### {ActionSpace} - 动作空间

  - Discrete - 离散动作空间（预定义动作）
  - Continuous - 连续动作空间（直接控制值）
  - Mixed - 混合动作空间（支持交互动作：拾取、放下、攀爬等）
### {ObservationType} - 观测类型

  - Color - RGB 彩色图像
  - Depth - 深度图
  - Rgbd - RGB + 深度组合
  - Gray - 灰度图像
  - CG - 计算机图形渲染
  - Mask - 对象分割掩码
  - MaskDepth - 掩码 + 深度组合
  - ColorMask - 颜色 + 掩码组合
  - Pose - 智能体位姿（位置 + 旋转）
## 💡 使用示例

以下是一些常见的环境配置：

### 示例 1：基础视觉跟踪

```python
import gym
import gym_unrealcv

# Visual tracking with continuous control, RGB observation
env = gym.make('UnrealTrack-track_train-ContinuousColor-v0')

# Same task with discrete actions
env = gym.make('UnrealTrack-track_train-DiscreteColor-v0')
```

### 示例 2：带交互动作的导航

```python
# Navigation with mixed action space (supports pick/drop/climb)
env = gym.make('UnrealNavigation-Demo_Roof-MixedColor-v0')

# Navigation with RGB-D observation
env = gym.make('UnrealNavigation-Old_Town-MixedRgbd-v0')
```

### 示例 3：带位姿的动物跟踪

```python
# Track an animal with pose observation instead of images
env = gym.make('UnrealTrack-Greek_Island-ContinuousPose-v0')
```

## 🗺️ 可用地图名称

请参阅 Scene Gallery 获取可用地图及其支持任务的完整列表。

> 📌 提示：如果你需要拾取物体、攀爬或进入车辆等交互动作，请使用 Mixed 动作空间。只有 Mixed 支持这些高级交互。

## 🔄 版本号

版本号（v0-v5）控制 track_train 地图的环境增强：

  - v0 - 默认，无增强
  - v1-v5 - 各种增强因素（光照、障碍物、布局、纹理）

# 3. 与环境交互：

你可以使用 step() 和 reset() 方法与环境交互。step() 方法接收一个动作并返回观测、奖励、完成标志（指示回合是否结束）以及 info（额外信息，可用于调试）。reset() 方法将环境重置为初始状态并返回初始观测。

```python
obs = env.reset() # reset the environment and get the initial observation

action = env.action_space.sample() # Sample a random action

# take the action and get the reward and new observation from the environment
obs, reward, done, info = env.step(action) 
```

# 4. 渲染环境：

如果你想可视化环境，可以使用 render() 方法，或使用 cv2.imshow() 方法可视化观测数据。

```python
img = env.render(mode='rgb_array')
img = img[..., ::-1]  # bgr->rgb
cv2.imshow('show', img)

obs, rewards, done, info = env.step(actions)
cv2.imshow('show', obs[0])
cv2.waitKey(1)
```

# 5. 关闭环境：

完成环境使用后，你可以使用 close() 方法关闭它：


```python
env.close()
```

# 6. 工具包

我们还提供了若干 wrapper，可用于以各种方式修改环境，包括在启动时配置 UE 二进制文件、控制模拟时间、设置提前结束条件、随机化种群。

# Wrappers：

我们还提供了若干 wrapper，可用于以各种方式修改环境。

### ConfigUE

  - ConfigUEWrapper 用于配置 Unreal Engine 二进制文件的启动设置。它可用于设置 Unreal Engine 环境的各种参数，如离屏渲染、观测分辨率、通信协议、docker 等。
```python
from gym_unrealcv.envs.wrappers import configUE 
configUE.ConfigUEWrapper(env, docker=False, resolution=(160, 160), display=None,
                         offscreen=False, use_opengl=False, nullrhi=False, 
                         gpu_id=None, sleep_time=5, comm_mode='tcp')
```

### TimeDilation

  - TimeDilationWrapper 用于控制 Unreal Engine 环境中模拟的速度。这对于为不同任务模拟各种 FPS 情况非常有用。
```python
from gym_unrealcv.envs.wrappers import time_dilation
env = time_dilation.TimeDilationWrapper(env, reference_fps=30, update_steps=60) 
```

### EarlyDone

  - EarlyDoneWrapper 用于根据特定条件提前结束回合。用户可以为不同任务修改源代码。这对于防止回合运行时间过长非常有用。
### RandomPopulation

  - RandomPopulationWrapper 使用指定数量的智能体随机填充环境：
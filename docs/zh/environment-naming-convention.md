# 环境命名规范

本页介绍在 UnrealZoo-Gym 中创建环境实例的命名规范。理解该格式对于正确初始化训练环境至关重要。

## 📝 命名格式

```plain text
Unreal{task}-{MapName}-{ActionSpace}{ObservationType}-v{version}
```

## 📊 参数说明

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

# 连续控制的视觉跟踪，RGB 观测
env = gym.make('UnrealTrack-track_train-ContinuousColor-v0')

# 相同任务，离散动作
env = gym.make('UnrealTrack-track_train-DiscreteColor-v0')
```

### 示例 2：带交互动作的导航

```python
# 混合动作空间的导航（支持拾取/放下/攀爬）
env = gym.make('UnrealNavigation-Demo_Roof-MixedColor-v0')

# RGB-D 观测的导航
env = gym.make('UnrealNavigation-Old_Town-MixedRgbd-v0')
```

### 示例 3：带位姿的动物跟踪

```python
# 使用位姿观测而非图像来跟踪动物
env = gym.make('UnrealTrack-Greek_Island-ContinuousPose-v0')
```

## 🗺️ 可用地图名称

请参阅 Scene Gallery 获取可用地图及其支持任务的完整列表。

> 📌 提示：如果你需要拾取物体、攀爬或进入载具等交互动作，请使用 Mixed 动作空间。只有 Mixed 支持这些高级交互。

## 🔄 版本号

版本号（v0-v5）控制 track_train 地图的环境增强：

- v0 - 默认，无增强
- v1-v5 - 各种增强因素（光照、障碍物、布局、纹理）
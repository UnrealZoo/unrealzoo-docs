# UnrealZoo 用户指南 (v3.0)

**版本**: v3.0-stage  
**最后更新**: 2026-04-15  
**代码参考**: [CHANGELOG.md](CHANGELOG.md)

---

## 1. 什么是 UnrealZoo？

UnrealZoo 是一个基于 **Unreal Engine 5** 的强化学习仿真环境，兼容 **OpenAI Gym** 接口。

### 核心特性

| 特性 | 描述 |
|---------|-------------|
| **高保真渲染** | UE5 的 Nanite + Lumen 提供高度逼真的视觉质量 |
| **多智能体支持** | 同构/异构智能体混合，支持空地协同 |
| **丰富任务类型** | 跟踪、导航、救援、会合等 |
| **键盘交互** | 人类玩家可直接介入，支持人机协作 |
| **跨平台** | 支持 Linux / Windows / macOS |

### 架构概览

```
算法 (Python)  ←→  Gym API  ←→  UnrealCV  ←→  UE5 仿真环境
                                              (TCP/UDS)
```

---

## 2. 5 分钟快速上手（最短路径）

> **本节目标**：验证安装成功并运行第一个仿真

### 2.1 设置二进制根目录

```bash
export UnrealEnv=/your/path/to/UnrealEnv
```

### 2.2 安装项目

```bash
git clone https://github.com/UnrealZoo/unrealzoo-gym.git
cd unrealzoo-gym
pip install -e .
```

### 2.3 运行 Baseline

```bash
python example/multi_agent/baseline/multi_random_baseline.py \
  -e UnrealTrack-Map_ChemicalPlant_1-ContinuousColor-v0
```

UE5 窗口弹出且智能体开始随机移动 → **安装成功** ✓

### 2.4 尝试键盘控制

```bash
python example/navigation/keyboard/navigation_keyboard_human.py \
  -e UnrealNavigation-SuburbNeighborhood_Day-MixedColor-v0
```

按 `I/J/K/L` 移动，`F` 开门，`E` 拾取 → **交互验证成功** ✓

> 如果启动失败，请检查 `UnrealEnv` 路径和二进制执行权限（Linux：`chmod +x`）

---

## 3. 环境搭建（详细）

> **本节目标**：全面了解安装流程与配置选项

### 3.1 获取 Unreal 二进制文件

地图二进制文件可从以下渠道下载：

| 平台 | 下载链接 |
|----------|---------------|
| ModelScope | [待添加] |
| 百度网盘 | [待添加] |

下载后解压到本地路径，例如 `/media/wuk/T9/UnrealEnv/`。

### 3.2 设置环境变量

```bash
export UnrealEnv=/your/path/to/UnrealEnv
```

建议永久保存到 shell 配置中（例如 `.bashrc`）：

```bash
echo 'export UnrealEnv=/your/path/to/UnrealEnv' >> ~/.bashrc
source ~/.bashrc
```

> **替代方案**：部分 demo 脚本允许在开头手动指定路径：
> ```python
> import os
> os.environ['UnrealEnv'] = '/your/path/to/UnrealEnv'
> ```

### 3.3 环境 ID 命名规范

统一格式：

```
Unreal{Task}-{MapName}-{ActionType}{ObservationType}-v{reset}
```

**示例**：
- `UnrealTrack-Map_ChemicalPlant_1-ContinuousColor-v0`
- `UnrealNavigation-Demo_Roof-MixedColor-v0`

**字段说明**：

| 字段 | 选项 | 描述 |
|-------|---------|-------------|
| `Task` | Track / Navigation / NavigationMulti / Rendezvous / Rescue | 任务类型 |
| `ActionType` | Discrete / Continuous / Mixed | 动作空间类型 |
| `ObservationType` | Color / Depth / Rgbd / Gray / CG / Mask / Pose / ... | 观测模态 |
| `reset` | v0-v6 | 重置变体，**默认 v0** |

> ⚠️ **关于 reset 字段的说明**：
> - 仅 `FlexibleRoom` 支持 `v1-v6`（随机化背景与障碍物）
> - 其他地图统一使用 `v0`

---

## 4. 运行示例（按任务类别）

> **本节目标**：了解如何运行不同任务，并找到研究的切入点

### 4.1 Tracking（目标跟踪）

智能体跟踪移动目标（例如动物、其他智能体）。

```bash
# 自动跟踪（基础）
python example/tracking/basic/tracking_auto_basic.py \
  -e UnrealTrack-Greek_Island-ContinuousColor-v0

# NavMesh 自动目标 + PID 跟随
python example/tracking/navmesh/tracking_auto_navmesh.py \
  -e UnrealTrack-Map_ChemicalPlant_1-ContinuousColor-v0

# 键盘控制跟踪动物
python example/tracking/basic/tracking_keyboard_animal.py \
  -e UnrealTrack-Old_Town-MixedColor-v0
```

### 4.2 Navigation（导航）

智能体在环境中导航至目标点，支持交互（开门、拾取、进出车辆）。

```bash
# 人类键盘导航（含交互动作）
python example/navigation/keyboard/navigation_keyboard_human.py \
  -e UnrealNavigation-SuburbNeighborhood_Day-MixedColor-v0

# 无人机键盘导航（4D 连续控制）
python example/navigation/keyboard/navigation_keyboard_drone.py \
  -e UnrealNavigation-Demo_Roof-ContinuousColor-v0
```

### 4.3 Multi-Agent（多智能体）

多个智能体协作或执行独立任务。

```bash
# 同构多智能体随机策略 baseline
python example/multi_agent/baseline/multi_random_baseline.py \
  -e UnrealTrack-Map_ChemicalPlant_1-ContinuousColor-v0

# 键盘 + 随机策略混合
python example/multi_agent/baseline/multi_keyboard_plus_random.py \
  -e UnrealTrack-Map_ChemicalPlant_1-MixedColor-v0

# 异构空地协同（3 地面 + 1 无人机）
python example/multi_agent/HeterogeneousCooperation/Aerial-Ground-Cooperative.py \
  -e UnrealTrack-Map_ChemicalPlant_1-ContinuousColor-v0
```

---

## 5. 交互控制详解

> **本节目标**：掌握人类玩家的控制方式

### 5.1 人类导航（混合动作）

适用于 `player` 类别，支持移动 + 交互。

#### 基础移动

| 按键 | 功能 | 描述 |
|-----|----------|-------------|
| `I` | 前进 | 朝面向方向移动 |
| `K` | 后退 | 朝后方移动 |
| `J` | 左移 | 向左平移 |
| `L` | 右移 | 向右平移 |
| `↑`（上箭头） | 抬头 | 增大俯仰角 |
| `↓`（下箭头） | 低头 | 减小俯仰角 |

#### 交互动作

| 按键 | 功能 | 触发条件 | 底层 API |
|-----|----------|-------------------|----------------|
| `F` | 开门 | 距离门 **1.5m** 以内 | `vbp {player} set_open_door 1` |
| `H` | 进出车辆 | 靠近车辆 | `vbp {obj} enter_exit_car {player_index}` |
| `Ctrl` | 蹲下 | - | `vbp {player} set_crouch` |
| `E` | 拾取 | 距离物品 **1.5m** 以内 | `vbp {player} set_pickup` |
| `Space` | 跳跃 | - | `vbp {player} set_jump` |

> ⚠️ **交互要点**：靠近交互对象（1.5m 以内）并**按下对应按键**触发，而非自动触发。调整头部视角确保对象在视野内。

#### 自定义键盘映射

交互动作通过 `animation_dict` 映射到 API。可在代码中自定义按键：

```python
# 示例：修改 navigation_keyboard_human.py 中的按键映射
if event.key == pygame.K_f:  # 原 F 键开门
    action['animation'] = 'open_door'

# 改为 X 键开门
if event.key == pygame.K_x:
    action['animation'] = 'open_door'
```

可用的 `animation` 动作名称：
- `'open_door'` → `vbp {player} set_open_door {state}`
- `'enter_vehicle'` → `vbp {obj} enter_exit_car {player_index}`
- `'pickup'` → `vbp {player} set_pickup`
- `'crouch'` → `vbp {player} set_crouch`
- `'jump'` → `vbp {player} set_jump`
- `'stand'` → 站立状态
- `'liedown'` → 躺下
- `'drop'` → 丢弃

完整映射定义见：`gym_unrealcv/envs/agent/character.py`，`animation_dict`

### 5.2 无人机导航（连续动作）

适用于 `drone` 类别，4 自由度连续控制。

| 按键 | 功能 | 控制维度 |
|-----|----------|-------------------|
| `W` | 前进 | `vx`（前后速度） |
| `S` | 后退 | `vx`（前后速度） |
| `A` | 左移 | `vy`（左右速度） |
| `D` | 右移 | `vy`（左右速度） |
| `E` | 上升 | `vz`（垂直速度） |
| `Q` | 下降 | `vz`（垂直速度） |
| `J` | 左转 | `vyaw`（偏航角速度） |
| `L` | 右转 | `vyaw`（偏航角速度） |

---

## 6. Wrapper 快速参考

> **本节目标**：了解示例代码中 wrapper 的作用，并学会自定义环境行为

Wrapper 用于**在不修改环境源码的情况下动态调整环境行为**。

### 6.1 ConfigUEWrapper — 启动参数配置

控制 Unreal 二进制的启动方式。

```python
from gym_unrealcv.envs.wrappers import configUE

env = configUE.ConfigUEWrapper(
    env,
    resolution=(160, 160),    # 渲染分辨率（宽，高）
    gpu_id=0,                 # 指定 GPU ID
    offscreen=False,          # 是否离屏渲染（无窗口）
    display=None,             # 指定显示器（Linux，例如 ':0.0'）
    use_opengl=False,         # 是否使用 OpenGL（默认 Vulkan）
    nullrhi=False,            # 是否禁用渲染（纯逻辑仿真）
    render_quality=7,         # 渲染质量 0-7（7 为最高）
    use_lumen=False,          # 是否启用 Lumen 全局光照
    sleep_time=5,             # 启动后等待时间（秒）
    comm_mode='tcp'           # 通信模式：'tcp' / 'websocket'
)
```

**典型场景**：
- 多 GPU 训练：`gpu_id=0,1,2...`
- 服务器部署：`offscreen=True`
- 快速逻辑验证：`nullrhi=True`（无渲染，最快）
- 视觉质量优先：`render_quality=7, use_lumen=True`
- 性能优先：`render_quality=3, use_lumen=False`

### 6.2 RandomPopulationWrapper — 动态种群

每个 episode 随机设置智能体数量。

```python
from gym_unrealcv.envs.wrappers import augmentation

# 固定 4 个智能体
env = augmentation.RandomPopulationWrapper(env, 4, 4, random_target=False)

# 每个 episode 随机 5-10 个智能体
env = augmentation.RandomPopulationWrapper(env, 5, 10, random_target=False)
```

**典型场景**：训练策略泛化性，模拟不同人群密度。

### 6.3 TimeDilationWrapper — 仿真速度

控制 UE 仿真速度。

```python
from gym_unrealcv.envs.wrappers import time_dilation

# 目标 30 FPS，每 60 步更新
env = time_dilation.TimeDilationWrapper(env, reference_fps=30, update_steps=60)
```

**典型场景**：与外部系统同步，或加速/减速仿真。

> **完整 Wrapper API**：见 `doc/wrapper.md`

---

## 7. 智能体生成机制（v3.0 核心变更）

> **本节目标**：理解 v3.0 中的模板化生成机制，并能够自定义智能体配置

### 7.1 新旧方案对比

| 维度 | 旧方案 | 新方案（v3.0） |
|-----------|------------|-------------------|
| 配置方式 | 固定 actor 名称 + 固定数量 | 类别模板 + 运行时动态生成 |
| 可扩展性 | 扩展混合类别成本高 | 数量、类别组合与实验配置解耦 |
| 多任务复用 | 每个任务单独 JSON | 同一地图 JSON 可复用 |

### 7.2 模板化配置示例

**旧方案**（固定实例名称）：
```json
"agents": {
  "player_EP0_0": { "class_name": "bp_character_C" },
  "player_EP0_1": { "class_name": "bp_character_C" }
}
```

**新方案**（类别模板）：
```json
"agents": {
  "player": {
    "class_name": ["bp_character_C"],
    "asset_path": ["/Game/.../BP_Character.BP_Character_C"],
    "move_action": [[0, 100], [0, -100], [15, 50], [-15, 50], [30, 0], [-30, 0], [0, 0]]
  },
  "drone": {
    "class_name": ["BP_drone01_C"],
    "asset_path": ["/Game/.../BP_drone01.BP_drone01_C"],
    "move_action": [[0.5, 0, 0, 0], [-0.5, 0, 0, 0], [0, 0.5, 0, 0], [0, -0.5, 0, 0], [0, 0, 0.5, 0], [0, 0, -0.5, 0], [0, 0, 0, 1], [0, 0, 0, -1], [0, 0, 0, 0]]
  }
}
```

### 7.3 脚本侧控制

```python
# 关键：在 reset() 之前设置 agents_category
env.unwrapped.agents_category = ["player", "player", "player", "drone"]
env = augmentation.RandomPopulationWrapper(env, 4, 4, random_target=False)
obs = env.reset()
```

### 7.4 混合类别初始化规则

| `agents_category` 长度 | 行为 |
|--------------------------|----------|
| 1 | 全部使用同一类别（例如 `["player"]` 表示全部为玩家） |
| 等于种群数量 | 按槽位初始化 |
| 其他（例如 2 ≤ len < 种群数量） | **回退到第一个类别并发出警告** |

> ⚠️ **关键时机**：`agents_category` 必须在 `reset()` 之前设置，否则不会生效！

### 7.5 迁移收益

- 地图配置与实验参数解耦
- 支持动态种群变化
- 支持异构智能体混合

---

## 8. 配置与地图 JSON

> **本节目标**：理解 JSON 配置结构，并能够自定义地图与任务

### 8.1 平台自动切换

生成 JSON 时会写入三个平台字段，**运行时自动选择**：

```json
{
  "env_bin": "Linux path",
  "env_bin_win": "Windows path",
  "env_bin_mac": "macOS path"
}
```

### 8.2 完整 JSON 示例

```json
{
  "env_bin": "UnrealZoo_UE5_6_Linux_v2.0.2/Linux/UnrealZoo_UE5_6/Binaries/Linux/UnrealZoo_UE5_6",
  "env_bin_win": "UnrealZoo_UE5_6_Win64_v2.0.2/UnrealZoo_UE5_6/Binaries/Win64/UnrealZoo_UE5_6.exe",
  "env_bin_mac": "UnrealZoo_UE5_6_Mac/UnrealZoo_UE5_6/Binaries/Mac/UnrealZoo_UE5_6.app/Contents/MacOS/UnrealZoo_UE5_6",
  "agents": {
    "player": {
      "class_name": ["bp_character_C"],
      "asset_path": ["/Game/SmartLocomotion/Blueprints/BP_Character.BP_Character_C"],
      "internal_nav": true,
      "move_action": [[0, 100], [0, -100], [15, 50], [-15, 50], [30, 0], [-30, 0], [0, 0]],
      "move_action_continuous": { "high": [30, 100], "low": [-30, -100] },
      "head_action": [[0, 0, 0], [0, 30, 0], [0, -30, 0]],
      "animation_action": ["stand", "jump", "crouch", "open_door", "enter_vehicle", "pickup"]
    }
  },
  "targets": { "Point": [] }
}
```

### 8.3 导航目标配置

```json
"targets": { "Point": [] }
```

- 允许空列表但会触发警告
- 目标为空时奖励始终为 0
- 可动态设置：`env.unwrapped.set_navigation_targets(["TargetName"])`

---

## 9. FAQ

### Q1: 二进制启动失败

- 验证 `UnrealEnv` 路径是否正确
- Linux：`chmod +x /path/to/binary`
- 验证平台匹配（不要在 Windows 上混用 Linux 二进制文件）

---

## 10. 文档索引

| 文档 | 内容 |
|----------|---------|
| `example/README.md` | 完整 demo 索引 |
| `doc/wrapper.md` | 所有 Wrapper API |
| `doc/addEnv.md` | 添加自定义环境 |
| `CHANGELOG.md` | 版本变更日志 |

---

## 附录 A：`move_action` 字段详解

### Player / Animal / Car / Motorbike

2 元素数组：`[angular, velocity]`
- `angular`：角速度（度/秒）
- `velocity`：线速度（cm/秒）

```json
"move_action": [
  [0, 100],    // 前进
  [0, -100],   // 后退
  [15, 50],    // 左转前进
  [-15, 50],   // 右转前进
  [30, 0],     // 原地左转
  [-30, 0],    // 原地右转
  [0, 0]       // 停止
]
```

### Drone

4 元素数组：`[vx, vy, vz, vyaw]`
- `vx`：前后速度
- `vy`：左右速度
- `vz`：垂直速度（上升/下降）
- `vyaw`：偏航角速度

```json
"move_action": [
  [0.5, 0, 0, 0],    // 前进
  [-0.5, 0, 0, 0],   // 后退
  [0, 0.5, 0, 0],    // 右移
  [0, -0.5, 0, 0],   // 左移
  [0, 0, 0.5, 0],    // 上升
  [0, 0, -0.5, 0],   // 下降
  [0, 0, 0, 1],      // 左转
  [0, 0, 0, -1],     // 右转
  [0, 0, 0, 0]       // 悬停
]
```

完整模板定义参考：`generate_env_config.py`
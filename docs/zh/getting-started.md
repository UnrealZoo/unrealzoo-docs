# 快速开始

# 下载 UE 二进制文件

### 下载示例二进制文件

> 📌 我们提供了一个轻量级二进制文件供用户下载体验。

UE4 示例包含 6 个地图（<3GB）：


UE5 示例包含 4 个地图（约 10GB）：

> 📌 全局光照和光线追踪默认开启。

### 完整版二进制文件下载（需要超过 60GB 的存储空间）

# 安装 UnrealCV+ 客户端

```bash
pip install unrealcv
```

# 安装 UnrealZoo-Gym

从以下地址下载 unrealzoo-gym 仓库：

https://github.com/UnrealZoo/unrealzoo-gym

```bash
git clone https://github.com/UnrealZoo/unrealzoo-gym.git
cd unrealzoo-gym
pip install -e 
```


将下载的二进制文件移动到 UnrealEnv 文件夹，这是我们默认的二进制文件存放位置，文件夹结构如下：

```markdown
gym-unrealcv/
├── docs/                  
├── example/                
├── gym_unrealcv/              
│   ├── envs/    
│   |   |——agent/     
|   |   |——UnrealEnv/                    # 二进制文件默认位置
|   |   |  |——Collection_WinNoEditor/    # 二进制文件夹
|   |   |——setting/
|   |   |  |——env_config/                # 环境配置 json 文件位置  
...
generate_env_config.py                   # 生成环境配置 json 文件
...
```

# 运行示例代码

> 📌 示例二进制文件中可用的 Env_Name：

| UE4 | UE5 |
| --- | --- |
| track_train | Map_ChemicalPlant_1 |
| Greek_Island | Old_Town |
| ContainerYard_Day | MiddleEast |
| ContainerYard_Night | Demo_Roof |
| SuburbNeighborhood_Day |  |
| SuburbNeighborhood_Night |  |



### 1. 运行随机智能体

```bash
python ./example/random_agent_multi.py -e UnrealTrack-track_train-ContinuousColor-v0
```

> 📌 如果游戏启动后鼠标光标消失，请按 `（Tab 键上方的按键）将鼠标光标从游戏中释放。


### 2. 运行基于规则的跟踪智能体

```bash
python ./example/tracking_demo.py -e UnrealTrack-Greek_Island-ContinuousColor-v0
```

### 3. 运行键盘智能体

1. 控制跟踪智能体：
```bash
python ./example/keyboard_agent.py -e UnrealTrack-Old_Town-MixedColor-v0
```

> 📌 使用 "I"、"J"、"K" 和 "L" 键控制人类跟踪者，逐步紧跟目标人物。

 b. 控制导航智能体：

```bash
python ./example/keyboard_agent.py -e UnrealNavigation-Demo_Roof-MixedColor-v0
```

> 📌 使用 "I"、"J"、"K" 和 "L" 键控制智能体的移动。

空格（␣）：跳跃。

上箭头（⬆️）：向上看。

下箭头（⬇️）：向下看。

（双击"跳跃"将触发智能体攀爬）


> 📌 探索所有场景

想查看所有可用的环境？访问我们的场景画廊，浏览 100+ photo-realistic 场景，按类别筛选，为你的研究找到完美的环境。

💡 提示：你可以在场景画廊中找到完整的环境名称列表及其支持的任务。每个环境都有一个遵循我们命名规范的唯一 ID（详见环境命名规范）。

# 更新日志

# 更新日志

本文件记录了本项目所有值得注意的变更。

## [v3.0-stage] - 2026-04-13

本次阶段性更新聚焦于任务统一化、混合种群支持、键盘交互升级以及示例重组。

### 新增

- 在 `UnrealCv_base.set_population` 中新增混合类别种群初始化，支持按槽位配置类别列表，例如 `['player', 'player', 'player', 'drone']`。
- 新增基于模板的智能体动态生成流水线：
  - 环境 JSON 可以仅包含模板（无需预置智能体名称），
  - 运行时生成使用 `asset_path` + `spawn_from_path`，
  - 智能体槽位在 `set_population` 期间实例化。
- 新增异构协作示例：`example/multi_agent/HeterogeneousCooperation/Aerial-Ground-Cooperative.py`。
  - 3 个地面智能体 + 1 架无人机。
  - 无人机支持 `DronePoseTracker` 自动跟随和键盘覆盖。
  - 稳定的逐回合编队设置，无人机生成高度 +2m，以及 2x2 观测拼接。
- 新增键盘动物追踪示例：`example/tracking/basic/tracking_keyboard_animal.py`。
- 在 `generate_env_config.py` 中新增平台二进制模板工作流：
  - `ENV_BIN_TEMPLATE_LINUX`
  - `ENV_BIN_TEMPLATE_WIN`
  - `ENV_BIN_TEMPLATE_MAC`
  - 新增辅助流程，用于在 JSON 中生成各平台的 `env_bin` 字段。
- 在生成的 JSON 中新增默认导航目标模式：
  - `env.targets.Point: []`

### 变更

- 重构 `generate_env_config.py` 以支持：
  - 基于模板的二进制路径生成，
  - 使用 `asset_path` 的统一智能体模板（替代固定的预置 actor 条目），
  - UE5 备份字段复用（`height`、`safe_start`、`reset_area`）。
- 更新基础环境生成行为（`UnrealCv_base`）：
  - 支持仅模板启动和延迟种群生成，
  - 生成混合智能体时使用类别感知模板，
  - 随动态种群变化同步更新动作/观测/相机槽位。
- 更新导航环境行为（`navigation.py`、`navigationmulti.py`）：
  - 不再隐式填充目标；
  - 当 `targets.Point` 为空时发出警告；
  - 目标列表为空时执行安全的 reset/step 行为。
- 更新人类演示的键盘导航映射：
  - `F` -> 开门
  - `H` -> 进入/离开载具
  - `Ctrl` -> 蹲下
  - `E` -> 拾取
- 更新无人机键盘演示，支持 4 自由度连续控制（`vx`、`vy`、`vz`、`vyaw`）及任务介绍显示流程。
- 更新 `Character_API` 中的交互动画映射：
  - `open_door` 使用默认 `state=1`，
  - `enter_vehicle` 映射到 `enter_exit_car(player_index=0)`，
  - 标准化拾取动作映射。
- 将 `example/` 重组为更清晰的任务导向结构：
  - tracking
  - navigation
  - multi_agent
  - legacy/wip 区域
- 更新 `example/README.md`，加入新的分类示例索引。
- 更新根目录 `README.md` 的示例命令为新路径。

### 修复

- 通过统一运行时映射，修复了交互动作不匹配导致拾取动画出现 `KeyError` 的问题。
- 通过使配置生成与所需键对齐，修复了非人类模板的混合动作模式不匹配问题。
- 修复了无人机协作演示的控制优先级，使键盘输入仅在按键按下时覆盖自动追踪器。

### 兼容性说明

- 导航任务现在要求地图 JSON 中存在 `env.targets.Point`（可以为空列表）。
  - 空列表会触发警告但不会崩溃；在设置目标之前导航奖励将为 0。
- 对于生成的 JSON，用户应在运行依赖目标的导航工作流之前选择或设置导航目标。
- 混合种群场景应在种群包装器应用**之前**显式设置 `env.unwrapped.agents_category`。
  - 错误时序：`env.reset()` → `agents_category = [...]` → wrapper（将不会生效）
  - 正确时序：`agents_category = [...]` → `env.reset()` → wrapper
- 依赖固定 `agents.{name}` 预置的旧工作流应迁移到基于模板的 `agents.{category}` + 运行时种群。
  - **为何迁移**：基于模板的生成将地图 JSON 与实例数量解耦，从而无需编辑 JSON 即可实现动态种群变化和混合类别实验。

### 注意

- 部分旧示例已被移动/替换；请优先使用 `example/README.md` 中列出的新路径。

### UnrealCV+ 插件

v3.0 阶段 UnrealCV+ 重要变更摘要。

- 新增对打包应用的运行时 `PAK` 挂载支持，使得无需重建整个项目即可更轻松地扩展内容。
  - 支持挂载、卸载、列出已挂载 pak、检查挂载状态、枚举文件、枚举资产、重新扫描资产以及动态资产加载/注册。
  - Python API：
    - `mount_pak()`
    - `unmount_pak()`
    - `get_mounted_paks()`
    - `is_pak_mounted()`
    - `get_pak_files()`
    - `get_pak_assets_in_pak()`
    - `scan_pak_assets()`
    - `load_pak_asset()`
    - `get_pak_assets()`
    - `register_pak_assets()`
  - 更多信息请参见 unrealzoo 网站：`Home`->`Document`->`Import Custom Assets`。

- 新增全景相机支持，用于生成 360 度等距柱状图像。
  - 支持逐相机全景立方体分辨率以及直接将全景导出到文件。
  - Python API：
    - `set_camera_panoramic_resolution()`
    - `capture_panoramic()`

- 新增更快的 C++ 视频录制流水线，提升录制效率，使大规模采集工作流更加实用。
  - 支持直接从相机或 actor 录制，可配置输出目录、帧率、时长以及选定的录制通道。
  - Python API：
    - `start_simple_recording()`：以输出路径、FPS、时长和选定通道（如 `lit` 或 `mask`）启动录制任务。
    - `stop_recording()`：停止目标相机或采集 actor 的活动录制任务。
    - `get_use_movie_quality_rendering()` / `set_use_movie_quality_rendering()`：查询或更改录制流水线使用的全局电影级渲染开关。
    - `get_record_via_viewport()` / `set_record_via_viewport()`：查询或更改录制是否使用视口采集路径的全局开关。
    - `get_warmup_frames()` / `set_warmup_frames()`：查询或配置录制开始前渲染的全局预热帧数。
    - `get_paused_tick_interval()` / `set_paused_tick_interval()`：查询或配置全局暂停 tick 间隔（秒）。
    - `get_record_add_timestamp()` / `set_record_add_timestamp()`：查询或控制活动采集 actor 是否在录制输出中附加时间戳后缀。
    - `get_recording_paused()` / `set_recording_paused()`：查询或控制活动录制会话是否暂停。

- 改进了常见模态（如 `lit`、`mask` 和 `depth`）的采集性能。
  - 自 2025 年 12 月起，帧吞吐量持续提升，尤其是在 `BaseCamSensor` 路径上。
  - 在测试用例中，`lit` 采集吞吐量从约 `15 fps` 提升至 `20 fps`。

- 更新相机 ID 支持，在保持与现有旧版相机寻址兼容的同时，提供更新的稳定 `CID` 格式，供脚本和配置长期使用。
  - 现有 Python 相机 API 保持向后兼容。
  - 新增 Python API 显式暴露稳定的 `CID-*` 相机标识符：
    - `get_camera_list_cid()`
    - `get_camera_id_map()`
  - 旧版相机发现仍可通过以下方式使用：
    - `get_camera_list_legacy()`

- 新增标注命令支持，用于场景和 actor 标注工作流。
  - 支持标注单个 actor、标注整个世界、清除世界标注、启用/禁用标注缓存以及清除缓存的标注组件。
  - Python API：
    - `annotate_object()`
    - `annotate_world()`
    - `clear_world_annotation()`
    - `set_annotation_cache_enabled()`
    - `clear_annotation_cache()`

- 新增通过 `spawn_from_path` 从资产路径生成对象。
  - 这补充了旧的基于类的生成流程，更适合通过完整资产路径引用的运行时内容。
  - Python API：
    - `spawn_object_from_path()`
  - 当输入看起来像资产路径时，`set_new_obj()` 现在会给出更清晰的提示，并可通过 `spawn_object_from_path()` 自动重试。

---



---

# UnrealZoo v3.1 更新日志

状态：**开发快照**
版本：**v3.1**
范围基线：[`v3.0-stage`](CHANGELOG_v4.md) 之后的变更

本文档在根 README、教程、GIF 和示例索引重组之前，确定下一次 UnrealZoo 重大更新的功能边界。
它将终端用户的 UnrealZoo 功能与发布中包含的更广泛的 UnrealCV+ 平台改进区分开来。

UnrealCV+ 标签意味着某项能力首先在 UnrealZoo 构建中开发和验证。它并不意味着单独的 UnrealCV 插件，也不意味着每一项都已属于上游开源 UnrealCV 基线。请参阅官方 [UnrealCV+ 文档](https://docs.unrealcv.org/en/latest/unrealcv_plus/index.html)
和[功能概览](https://docs.unrealcv.org/en/latest/unrealcv_plus/overview.html)。

## v3.1.4 — 3D 无人机导航

- 为 `BP_Drone_customized` 新增目标导向的 3D 飞行，具备碰撞避免、路径平滑，并通过现有基于物理的飞行控制实现自动朝向。
- 新增 `nav_update_collision`，用于在 reset 期间缩放或外观变化后刷新碰撞包络，同时提供导航状态、停止和手动释放 API。
- **需要包含此功能的更新版 v3.1.4 环境包；** 仅更新 Python 仓库是不够的。请参阅[使用指南](../example/new_features/README.md#3d-drone-navigation-v314)。

## 发布亮点

| 领域 | 用户可见结果 | 推荐展示 |
|---|---|---|
| UnrealCV 渲染与采集 | 当前开发构建的[共享内存采集](https://docs.unrealcv.org/en/latest/reference/unrealzoo_capture_transport.html)在 2K 下平均 22.40 FPS，在 4K 下平均 16.25 FPS | 端到端基准对比和实时采集片段 |
| LiDAR | XYZI 观测和位姿条件化的街道建图 | 郊区街道建图 Python 示例 + GIF |
| MuJoCo | 由 MuJoCo 状态和策略控制的 Unreal 渲染 Go1 | Go1 跑酷 Python 示例 + GIF |
| 占据体素 | 用于具身智能体观测的 LINGO 兼容场景占据网格 | 配置/形状文档 + 可视化 |
| 运行时无人机视觉定制 | 切换五种生产就绪模型（带动画螺旋桨）、使用定制模板，或加载外部 Static Mesh 而无需重新生成 pawn | 外观循环示例 + GIF |
| 社交动画 | 在运行时触发新打包的角色社交动画库 | 动画循环示例 + GIF |
| 外部 3DGS 环境 | 在运行时加载用户打包的 3DGS 场景，并在其中复用 UnrealZoo 智能体和观测 | 外部场景加载工作流 + 智能体示例 |

## 新增

### UnrealZoo 功能

#### 1. LiDAR 观测与建图

- 新增相机 LiDAR 观测，返回 `N x 4` float32 XYZI 点云。
- 新增 NumPy 观测接口：

  ```text
  vget /camera/[camera_id]/lidar npy
  ```

- 新增实时 `SuburbNeighborhood_Day` SLAM 风格示例，结合玩家 RGB 视图、当前传感器局部扫描、同步相机位姿以及累积的自顶向下体素地图。
- 新增扫描诊断，用于检查预期射线网格布局、重复/顺序/范围异常、同步位姿跨度、静止一致性和地图重叠。

#### 2. MuJoCo Go1 集成

- 为 Unitree Go1 四足机器人新增 Unreal 渲染的 MuJoCo 仿真路径。
- 新增 Go1 策略控制，具有 12 维动作、3 维速度命令和 48 维策略观测。
- 新增 Go1 的速度和跑酷动力学，以及键盘、策略、位姿预览、观测可视化和 GIF 录制示例。

#### 3. 场景占据体素观测

- 新增布尔场景占据体积，采用 C 顺序轴布局 `[x, y_up, z]`。
- 新增 2 cm 分辨率的 `lingo_vis` 和 `lingo_train` 配置。
- 新增 `bounds` 和 `mesh` 体素化方法、可选动态 actor，以及相机相对原点/偏航角参数。
- 新增 NPY 观测和机器可读规范端点：

  ```text
  vget /scene/occupancy npy [profile] [method] [origin_cm x y z yaw include_dynamic]
  vget /scene/occupancy/spec [profile] [method]
  ```

#### 4. 运行时无人机视觉定制

- 新增五种生产就绪外观（带动画螺旋桨）：`spy`、`fpv`、`police`、`baba` 和 `delivery`，以及用于定制的 `template` 外观。
- 在 `BP_Drone_customized` 上切换外观不会重新生成 pawn，也不会替换其控制器、移动、物理、相机或当前任务状态。
- 新增 `set_app`、`reset_app` 和 `get_available_apps` 蓝图可调用函数。
- 新增自定义静态网格设置器，包括用于挂载 PAK 提供资产的字符串路径变体：
  `set_app_mesh_path` 和 `set_app_mesh_path_transform`。
- 外部 Static Mesh 加载旨在快速集成资产和视觉定制。它保留上述无人机系统，并按原样显示导入的几何体；不会为单个 Static Mesh 自动生成组件级动画。

#### 5. 角色社交动画

- 新增 `set_social_anim` 蓝图函数，用于运行时社交动画选择。
- 新增社交动作的 montage 播放和停止处理。
- 将 `SocialAnimsBundle2` 内容打包到 UnrealZoo 构建中，包括派对、女性和车内动画组。
- 动画名称示例包括 `AirKiss`、`DrinkAndTalk`、`FemaleLaugh`、`Reading`、`Selfy`、`SmallTalk`、`Smoking` 和 `SpeakOnPhone`。
- 输入为 `AM_` 之后区分大小写的后缀；请参阅[完整参数列表](../example/new_features/README.md#5-character-social-animations)。

#### 6. 通过动态 PAK 加载用户提供的 3DGS 环境

- 新增发布工作流，用户可将自己的 3DGS 资产导入并 cook 到外部 PAK 中，而无需重建完整的 UnrealZoo 项目。
- 新增引导式运行时工作流，用于从外部包中发现并激活兼容的 3DGS 内容。
- 加载的 3DGS 环境仍是正常的 UnrealZoo 世界：现有玩家、无人机、相机、观测和任务逻辑可以在其上生成或复用。
- 运行时加载使用已导入并 cook 的高斯泼溅资产；原始 PLY 导入是编辑器/cooking 步骤，而非环境 reset 操作。

### UnrealCV+ 用户可见改进

#### 渲染与观测性能

- 当前开发构建的[共享内存采集](https://docs.unrealcv.org/en/latest/reference/unrealzoo_capture_transport.html)在序列化端到端测试中，1080p 下平均 `23.61 FPS`，2K 下平均 `22.40 FPS`，4K 下平均 `16.25 FPS`。
- 这些数字衡量的是完整客户端采集延迟，而非未加载视口帧率；仅传输的闭源构建结果在 UnrealCV 采集传输参考文档中单独记录。
- 改进了连续观测循环、交互式智能体控制和数据集录制工作负载的响应性。
- 降低了从活动 UnrealZoo 场景采集多种视觉模态的实际成本。

#### 全景采集扩展

- 将等距柱状全景采集从 lit 输出扩展到 normal、object-mask 和 depth 模态。
- 新增可配置的全景输出分辨率。

#### 内置录制工作流

- 改进内置相机和 actor 录制工作流，以支持持续数据集采集。
- 新增用户对输出通道、帧率、时长、预热、暂停/恢复行为和输出命名的控制。

#### 相机、标注和动态内容工作流

- 新增稳定相机标识符，同时保持旧版数字相机脚本兼容。
- 扩展场景和对象标注控制，用于数据集生成。
- 新增运行时外部内容加载和资产路径生成，使用户无需重建完整项目即可扩展 UnrealZoo 环境。

#### MuJoCo 命令桥接

- 新增 UnrealCV 对象命令，用于 Go1 MuJoCo 设置、同步步进、观测获取、策略动作和策略命令。

其中若干 UnrealCV+ 能力首次出现在 v3.0 阶段。此处列出是因为本次发布将其转化为完整的用户可见工作流，而非声称每一项都是在本周期首次引入。

## 变更

- 新功能示例默认连接到已运行的 Unreal Editor/PIE 会话，而非静默启动第二个 Unreal 进程。
- 街道建图示例默认使用生成的玩家相机，并将 Unreal 世界位置视为厘米，而 LiDAR XYZ 值为米。
- 修正了新可视化示例中的 RGB 颜色还原。
- 动态内容示例区分文件系统 PAK 路径、Unreal 包路径和完整 Unreal 对象路径，而非将其视为可互换的字符串。

## 兼容性与限制

- 当传感器与相机不共位时，必须应用相机到 LiDAR 的外参。仅当该假设被明确展示时，示例才可假设为单位变换。
- Unreal Engine 位置使用厘米。LiDAR 和可视化示例暴露公制坐标；转换必须恰好执行一次。
- 占据配置是大型密集布尔数组。请选择满足任务的最小配置，并避免保留不必要的帧。
- `mesh` 占据精度取决于兼容的几何数据，对于不支持的场景资产可能回退到 bounds。
- 用户的 3DGS 包必须与目标 UnrealZoo 引擎、平台和内容要求兼容。
- 社交动画命令接受已 cook 包中存在的名称；未知名称应视为错误而非静默替换。
- UnrealCV+ 的可用性与经 UnrealZoo 测试的插件构建绑定。当脚本还需面向上游或旧版 UnrealCV 安装时，应查询命令/帮助可用性。

## 示例与媒体

- [`suburb_street_slam.py`](../example/new_features/suburb_street_slam.py)
  演示玩家控制的 LiDAR 街道建图。
- [`lidar_visualization.py`](../example/new_features/lidar_visualization.py)
  可视化单个 LiDAR 观测和累积地图。
- [`parkour/demo.py`](../example/mujoco/parkour/demo.py) 演示 Unreal 渲染场景中的 MuJoCo Go1 控制。
- [`realtime_scene_occupancy_gpu.py`](../example/new_features/realtime_scene_occupancy_gpu.py)
  在四个 GPU 实例化视图中渲染实时[共享内存](https://docs.unrealcv.org/en/latest/reference/unrealzoo_capture_transport.html)占据数据。
- [`drone_mesh_switch_demo.py`](../example/new_features/drone_mesh_switch_demo.py)
  在活动 pawn 上循环切换可用的无人机外观。
- 打包二进制命令
  `vset /action/game/level /Game/3dgs/custom_3dgs` 演示在保留 UnrealZoo 接口的同时加载外部 3DGS 关卡。

- [`lidar_street_slam.gif`](figs/new_features/lidar_street_slam.gif)：完整的 LiDAR 街道建图采集，由 MP4 转换以供 README 使用。
- [`mujoco_go1_keyboard.gif`](figs/new_features/mujoco_go1_keyboard.gif)：基础 MuJoCo Go1 键盘控制演示。
- [`mujoco_go1_parkour_third_person.gif`](figs/new_features/mujoco_go1_parkour_third_person.gif)：从第三人称视角展示的高级跑酷策略。
- [`mujoco_go1_parkour_depth.gif`](figs/new_features/mujoco_go1_parkour_depth.gif)：UnrealCV 深度图及跑酷策略使用的深度输入。
- [`drone_mesh_switch.gif`](figs/new_features/drone_mesh_switch.gif)：在活动无人机上运行时切换网格而无需重新生成 pawn。
- [`3dgs_dynamic_load.gif`](figs/new_features/3dgs_dynamic_load.gif)：在运行时加载外部 3DGS 环境，并在场景中复用 UnrealZoo 支持的 actor。
- [`social_animation.gif`](figs/new_features/social_animation.gif)：多个 UnrealZoo 角色播放运行时选择的社交动画。

环境特定使用问题和详细行为可在 [GitHub Discussions](https://github.com/UnrealZoo/gym-unrealzoo/discussions) 中讨论。

## 待办

- [ ] MuJoCo Unitree G1 集成与示例。
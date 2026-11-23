# 场景库

## 概述

UnrealZoo 目前提供 100+ 个基于 Unreal Engine 4.27 和 5.x 构建的高度逼真的 3D 场景，是面向具身智能（Embodied AI）研究的最大、最多样化的虚拟环境集合之一。这些环境涵盖从紧凑的室内空间到覆盖面积达 16 km² 的广阔户外景观。

### 🏷️ 如何使用本场景库

1. 搜索 — 使用搜索栏按名称查找特定场景
2. 筛选 — 按 UE 版本（4/5）、任务标签、场景类别等应用筛选条件
3. 选择 — 点击某个场景以查看详细信息
4. 使用 — 复制 Map Name 以构建环境 ID（参见 📋 环境命名规范）

> 📌 筛选提示
可组合多个筛选条件缩小搜索范围。例如，按“场景类别：工业”+“规模：大型”+“UE 版本：UE5”进行筛选，以查找基于 Unreal Engine 5 构建的大型工业环境。

## 标签

场景库中的每个场景都带有描述性标签，便于快速识别符合研究需求的环境。可使用这些标签筛选和搜索特定类型的场景：

- 场景类别 — 环境类型（景观、建筑、聚落、工业、设施、自然）
  - 景观 — 自然地形，包括森林、山脉、沙漠、岛屿和海滩
  - 建筑 — 历史与现代建筑、寺庙、城堡和纪念碑
  - 聚落 — 城市与郊区区域、社区、城镇和村庄
  - 工业 — 工厂、仓库、集装箱堆场和建筑工地
  - 设施 — 公共建筑、火车站、体育馆、医院和学校
  - 自然 — 公园、花园、农场和野生动物环境
- 规模 — 环境的大小（小型、中型、大型、超大型）
  - 景观🏞️ 🏙️：广阔的自然或人造区域，或城市的一部分，或整个小镇，例如山脉、森林、湖泊、城区。
  - 社区🏘️：小型社区或街区，例如住宅区、商业街。
  - 建筑🏡：单栋建筑及其周边环境，例如学校、商场。
  - 室内🚪🛏️：包含一个或多个小房间的室内空间（最多一整层），例如住宅、公寓、办公室内部。
- 风格 — 视觉风格与美学（西方、亚洲、中世纪、现代、自然、工业、科幻、古代、中东等）
- 空间结构 — 地形与布局特征（平坦、陡峭、拓扑、多层）
- 动态元素 — 动态环境元素（无、移动物体、雨、雪、风、火、流体、交互物体、光照、气体、沙尘暴）
- 智能体标签 — 支持的智能体类型（人类、动物、机器人、车辆、无人机）
- 任务标签 — 支持的任务（跟踪、导航、会合、救援）
  - 视觉跟踪 — 跟随动态目标（人类、动物、车辆、无人机）
  - 导航 — 在避障的同时到达目标目的地/物体
  - 会合 — 多智能体协调与集合任务
  - 救援 — 复杂环境中的搜索与救援任务
- UE 版本 — Unreal Engine 版本（UE4、UE5）
- 来源 — 资产来源链接（UE Marketplace、Fab 或其他下载 URL）
- 费用 — 资产在 Unreal Engine Marketplace 上的价格（免费或付费）

## 场景清单

UnrealZoo 当前提供的全部 110 个地图，以及场景画廊筛选用到的属性。**地图** 一列即环境 ID 中使用的 map name（参见 📋 环境命名规范）。

### 概览统计

| 维度 | 分布 |
|---|---|
| 地图总数 | 110 |
| UE 版本 | 未标注: 43, UE4/5: 35, UE5: 27, UE4: 5 |
| 规模 | Landscape&Urban: 35, Community: 28, Building: 22, Indoor: 15 |
| 任务 | Tracking: 96, Navigation: 59, Rendezvous: 2 |

### 完整列表

| 地图 | 类别 | 规模 | 风格 | 动态 | 智能体 | 任务 | UE | 价格 | 来源 |
|---|---|---|---|---|---|---|---|---|---|
| `Abandoned District` | Exterior, Industrial, Interior | Community | Modern, Western | Fluids, Gas, Light | Animal, Drone, Human | Navigation, Tracking | UE5 | $179.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/scans-urban-abandoned-district-day-night-scene) |
| `Ancient Ruins` | Exterior, Landscapes, Mountain, Ruins | Landscape&Urban | Asian, Nature, Western | — | Animal, Drone, Human | Tracking | UE4/5 | $19.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/ancient-ruins-modular-bonus-sounds) |
| `Arctic` | Exterior, Landscapes, Mountain | Landscape&Urban | Nature | Gas, Light | Animal, Drone, Human | Navigation, Tracking | — | $39.99 | [市场链接](https://www.unrealengine.com/marketplace/zh-CN/product/brushify-arctic-pack) |
| `Asian Medieval City` | City, Exterior, Interior | Landscape&Urban | Ancient, Asian | Fluids | Animal, Drone, Human | — | — | $84.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/modular-asian-medieval-city) |
| `Asian Temple Pack` | Exterior, Historical, Landscapes, Mountain, Religious, Temple | Landscape&Urban | Asian, Nature | None | Animal, Drone, Human | Navigation, Tracking | UE5 | $69.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/asian-temple-pack-by-meshingun-studio) |
| `Bazaar` | Exterior, Interior, Village | Community | Ancient, Middle East, Public | Sand storm | Animal, Drone, Human | — | — | $94.99 | [市场链接](https://www.fab.com/listings/cff79d2c-4b55-45a2-80fc-960193a6dfd4) |
| `Beach Wedding` | Exterior, Interior, Landscapes, Rural | Community | Modern, Nature, Western | None | Animal, Drone, Human | Tracking | UE4/5 | — | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/ef-beach-wedding) |
| `Bunker` | Industrial, Interior | Indoor | Industrial, Modern | None | Animal, Human | Tracking | — | $49.99 | [市场链接](https://www.unrealengine.com/marketplace/product/bunker) |
| `ChemicalFactory` | Exterior, Industrial, Interior | Landscape&Urban | Industrial, Modern | Gas | Drone, Human, Motorbike | Navigation, Tracking | UE5 | $119.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/chemical-refinery-plant-environment-modular-factory-environment) |
| `Chinese Landscape （navmesh  lost some area）` | Exterior, Landscapes, Mountain | Landscape&Urban | Ancient, Nature | None | Animal, Drone, Human | Navigation, Tracking | UE5 | $49.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/chinese-landscape-63-assets) |
| `ChineseWaterTown` | Exterior, Interior, Village | Community | Asian, Medieval, Public | — | Animal, Drone, Human | Tracking | UE4/5 | $14.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/chinesewatertown-ver-1) |
| `City of Brass: Gardens` | Exterior, Historical, Interior | Building | Ancient, Western | None | Animal, Drone, Human | Navigation, Tracking | UE4/5 | Free | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/c93f1fa73dad4adf9a3d09883d8c8dec) |
| `City of Brass: Palace` | Exterior, Historical, Interior | Building | Ancient, Western | None | Animal, Drone, Human | Tracking | UE4/5 | Free | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/c93f1fa73dad4adf9a3d09883d8c8dec) |
| `City of Brass: Streets` | Exterior, Historical, Interior | Building | Ancient, Western | None | Animal, Drone, Human | Navigation, Tracking | UE4/5 | Free | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/c93f1fa73dad4adf9a3d09883d8c8dec) |
| `ContainerYard_Day` | — | — | — | — | — | Navigation, Tracking | UE4 | — | — |
| `ContainerYard_Day（crash）` | Exterior, Industrial | Community | Industrial, Modern | — | Animal, Car, Drone, Human, Motorbike | Tracking | — | $39.99 | [市场链接](https://www.unrealengine.com/marketplace/product/container-yard-environment-set) |
| `ContainerYard_Night` | — | — | — | — | — | Navigation, Tracking | UE4 | — | — |
| `ContainerYard_Night` | Exterior, Industrial | Community | Industrial, Modern | — | Animal, Car, Drone, Human, Motorbike | Tracking | — | $39.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/container-yard-environment-set) |
| `Courtyard` | City, Exterior | Community | Modern, Public, Western | None | Drone, Human, Motorbike | Navigation, Tracking | UE5 | $12.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/modular-courtyard-1) |
| `Demo_Roof` | — | — | — | — | — | Navigation, Rendezvous | UE5 | — | — |
| `Desert Ruins` | Exterior, Landscapes, Mountain, Ruins | Landscape&Urban | Middle East, Nature | None | Animal, Drone, Human | Tracking | UE4/5 | $4.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/desert-ruins) |
| `Downtown West` | City, Exterior | Community | Modern, Public, Western | Wind | Animal, Car, Drone, Human, Motorbike | Navigation, Tracking | UE4/5 | Free | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/6bb93c7515e148a1a0a0ec263db67d5b) |
| `Dungeon （game mode bug）` | Castle, Historical, Interior | Building | Ancient, Western | Fire | Animal, Drone, Human | Tracking | — | Free | [市场链接](https://www.unrealengine.com/marketplace/product/dungeon-playable-demo-135-assets) |
| `Edith Finch: Cannerylew` | Industrial, Interior | Indoor | Western | Moving objects | Animal, Drone, Human | — | UE4/5 | Free | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/ef-cannery-kingdom) |
| `Edith Finch: House Grounds` | Exterior, Forest, Landscapes | Landscape&Urban | Ancient, Nature | None | Animal, Drone, Human, Motorbike | Tracking | UE4/5 | Free | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/ef-cannery-kingdom) |
| `Edith Finch: LowPoly Kingdom` | Exterior, Historical | Building | Ancient, Western | Fluids | Animal, Drone, Human | Tracking | UE4/5 | Free | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/ef-cannery-kingdom) |
| `Egyptian Pyramid` | Exterior, Historical, Interior | Landscape&Urban | Ancient, Middle East, Nature, Public | None | Human | Navigation, Tracking | UE5 | $84.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/egyptian-pyramid-modular-kit-nanite) |
| `English College` | Educational, Exterior, Facilities | Community | Ancient, Public, Western | None | Animal, Drone, Human | Navigation, Tracking | UE5 | Free | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/english-college-level-4-sample) |
| `Fantasy Cave` | Cave, Exterior, Historical, Interior, Landscapes | Building | Ancient, Nature | — | Animal, Drone, Human | Tracking | — | $39.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/c42d6bbfa3bc4150b9970a1687e1cc41) |
| `Fantasy Medieval Castle` | Castle, Exterior, Historical, Landscapes, Mountain | Landscape&Urban | Medieval, Nature, Western | Gas | Animal, Drone, Human | Tracking | UE4/5 | $59.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/fantasy-castle-kit) |
| `FlexibleRoom` | Interior | Indoor | Synthesis | Interactive Object | Animal, Car, Drone, Human, Motorbike | Navigation, Tracking | — | Free | — |
| `Forest Gas Station` | Commercial, Exterior, Facilities, Interior, Public | Building | Modern, Public | — | Animal, Car, Drone, Human, Motorbike | Navigation | UE5 | $34.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/forest-gas-station) |
| `Gothic Day` | Castle, Exterior, Historical, Interior | Community | Medieval, Western | Light | Animal, Drone, Human | Navigation, Tracking | — | $34.99 | [市场链接](https://www.unrealengine.com/marketplace/zh-CN/product/modular-gothic-fantasy-environment) |
| `Gothic Night` | Castle, Exterior, Historical, Interior | Community | Medieval, Western | Light | Animal, Drone, Human | Navigation, Tracking | — | $34.99 | [市场链接](https://www.unrealengine.com/marketplace/product/modular-gothic-fantasy-environment) |
| `Grass Hills` | Exterior, Landscapes, Mountain | Landscape&Urban | Ancient, Nature | — | Animal, Drone, Human | Tracking | UE4/5 | $19.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/ancient-ruins-modular-bonus-sounds) |
| `Greek Island` | Exterior, Interior, Island, Landscapes | Landscape&Urban | Ancient, Public, Western | Fluids, Moving objects, Wind | Animal, Car, Drone, Human, Motorbike | Navigation, Tracking | UE4/5 | $84.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/greek-island) |
| `Greek_Island` | — | — | — | — | — | Navigation, Tracking | UE4 | — | — |
| `Holding Cells` | Facilities, Institutions, Interior | Indoor | Modern | Interactive Object | Animal, Human | Navigation, Tracking | — | $4.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/qa-holding-cells) |
| `Hospital` | Facilities, Institutions, Interior, Public | Indoor | Modern, Public | None | Human | Tracking | UE4/5 | $11.99 | [市场链接](https://www.unrealengine.com/marketplace/product/hospital-inside) |
| `Industrial Hangar` | Exterior, Industrial, Interior | Community | Industrial, Modern | — | Car, Drone, Human, Motorbike | Navigation, Tracking | UE5 | $119.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/industrial-area-hangar) |
| `Infinity Blade: Castle (1)` | Castle, Exterior, Historical, Interior | Building | Ancient, Nature, Western | None | Animal, Drone, Human | Tracking | UE4/5 | Free | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/infinity-blade-castle) |
| `Infinity Blade: Castle (2)` | Castle, Historical, Interior | Indoor | Medieval, Western | None | Animal, Drone, Human | Tracking | UE4/5 | Free | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/infinity-blade-castle) |
| `Infinity Blade: Temple (1)` | Exterior, Historical, Religious, Temple | Building | Ancient, Asian | None | Animal, Drone, Human | Navigation, Tracking | UE4/5 | Free | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/infinity-blade-temple) |
| `Infinity Blade: Temple (2)` | Exterior, Historical, Religious, Temple | Building | Ancient, Middle East | None | Animal, Drone, Human | Tracking | UE4/5 | Free | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/infinity-blade-temple) |
| `Infinity Blade: Temple (3)` | Exterior, Historical, Religious, Temple | Building | Ancient, Middle East | Wind | Animal, Drone, Human | Tracking | UE4/5 | Free | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/infinity-blade-temple) |
| `InfinityWeather-Desert` | Exterior, Landscapes, Mountain | Landscape&Urban | Nature | Interactive Object, Sand storm, Wind | Animal, Drone, Human | Navigation, Tracking | — | $159.99 | [市场链接](https://www.unrealengine.com/marketplace/zh-CN/product/infinity-weather) |
| `InfinityWeather-Rain` | Exterior, Landscapes, Mountain | Landscape&Urban | Modern, Nature | Interactive Object, Light, Rain, Wind | Animal, Drone, Human | Navigation, Tracking | — | $159.99 | [市场链接](https://www.unrealengine.com/marketplace/zh-CN/product/infinity-weather) |
| `InfinityWeather-Snow` | Exterior, Landscapes, Mountain | Landscape&Urban | Nature | Snow, Wind | Animal, Drone, Human | Navigation, Tracking | — | $159.99 | [市场链接](https://www.unrealengine.com/marketplace/zh-CN/product/infinity-weather) |
| `Korean Traditional Palace` | Exterior, Historical, Interior, Palace | Community | Ancient, Asian, Public | None | Animal, Human | Navigation, Tracking | UE5 | Free | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/hwaseong-haenggung-korean-traditional-palace) |
| `Lighthouse Island` | Exterior, Historical, Interior, Island, Landscapes, Rendering Imcompatable | Landscape&Urban | Nature | Fluids | Animal, Car, Drone, Human | Navigation, Tracking | UE5 | $79.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/lighthouse-island-high-quality-environment) |
| `Lookout Tower` | Exterior, Forest, Interior, Landscapes | Landscape&Urban | Nature, Western | None | Animal, Car, Drone, Human, Motorbike | — | — | $59.99 | [市场链接](https://www.fab.com/listings/3340d712-649b-4788-bfc1-8137c1db4afa) |
| `Low Poly Medieval Interior` | Interior | Indoor | Medieval, Western | Fire | Animal, Human | Navigation, Tracking | — | $69.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/low-poly-medieval-interior-and-constructions) |
| `Map_ChemicalPlant_1` | — | — | — | — | — | Navigation, Tracking | UE5 | — | — |
| `Medieval Castle` | Castle, Exterior, Forest, Historical, Interior, Lake, Landscapes, Mountain | Landscape&Urban | Medieval, Nature, Western | — | Animal, Drone, Human | Tracking | UE4/5 | $39.99 | [市场链接](https://www.unrealengine.com/marketplace/product/medieval-castle-modular-vol) |
| `Medieval Nature Environment` | Castle, Exterior, Historical, Interior, Landscapes, Mountain, Religious | Landscape&Urban | Medieval, Nature, Western | Moving objects | Animal, Drone, Human | Navigation, Tracking | UE4/5 | $79.99 | [市场链接](https://www.unrealengine.com/marketplace/zh-CN/product/modular-medieval-environment) |
| `Medieval Town Daytime` | Exterior, Interior, Village | Community | Ancient, Public, Western | Interactive Object | Animal, Human | Navigation, Tracking | — | $39.99 | [市场链接](https://www.unrealengine.com/marketplace/zh-CN/product/modular-medieval-town-with-interior) |
| `Medieval Town Nighttime` | Exterior, Interior, Village | Community | Ancient, Public, Western | Interactive Object | Animal, Human | Tracking | — | $39.99 | [市场链接](https://www.unrealengine.com/marketplace/zh-CN/product/modular-medieval-town-with-interior) |
| `Middle East` | City, Exterior | Landscape&Urban | Middle East, Modern, Public | Gas | Car, Drone, Human, Motorbike | Navigation, Tracking | UE5 | $39.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/middle-east) |
| `MiddleEast` | — | — | — | — | — | Navigation, Tracking | UE5 | — | — |
| `Modular Building Set` | City, Exterior, Interior | Community | Modern, Western | None | Animal, Car, Drone, Human, Motorbike | Tracking | UE4/5 | Free | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/modular-building-set) |
| `Modular Hotel Corridor` | Commercial, Facilities, Interior | Indoor | Modern, Public, Western | Interactive Object | Human | Navigation, Tracking | UE5 | $49.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/hotel-corridor) |
| `Modular Industrial Area` | Exterior, Industrial, Interior | Community | Industrial, Modern | None | Animal, Drone, Human | Tracking | UE4/5 | $29.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/modular-industrial-area) |
| `Modular Neighborhood` | Exterior, Interior, Village | Community | Modern, Western | Fluids | Animal, Car, Drone, Human, Motorbike | Navigation, Tracking | — | $49.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/modular-neighborhood-pack) |
| `Modular Old Town` | Exterior, Interior, Village | Community | Ancient, Western | None | Animal, Drone, Human | — | — | $64.99 | [市场链接](https://www.fab.com/listings/82e45a3a-9ec3-4ecf-a22c-c016b5f6f9db) |
| `Modular SciFi Season 1` | Industrial, Interior | Building | Modern, Science Fiction | — | Animal, Human | Navigation, Tracking | — | Free | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/modular-scifi-season-1-starter-bundle) |
| `Modular SciFi Village` | Exterior, Interior, Village | Community | Sci-fi | — | Animal, Drone, Human | Navigation, Tracking | — | $14.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/modular-sci-fi-village) |
| `Modular Temple Plaza` | Exterior, Historical, Interior, Religious, Temple | Community | Ancient, Middle East, Public | None | Animal, Drone, Human | Tracking | UE4/5 | $49.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/modular-temple-plaza-4k-pbr) |
| `Modular Urban City Asset Megapack` | City, Exterior, Interior | Landscape&Urban | Asian, Modern, Public | Gas | Car, Drone, Human, Mobile robot, Motorbike | Navigation, Tracking | — | $139.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/modular-urban-city-asset-megapack) |
| `Modular Victorian City` | City, Exterior | Landscape&Urban | Modern, Public, Western | — | Animal, Car, Drone, Human, Motorbike | Tracking | — | $199.99 | [市场链接](https://www.unrealengine.com/marketplace/zh-CN/product/next-gen-modular-victorian-neoclassical-city-bundle-exterior-interior) |
| `Museum Environment` | Educational, Facilities, Interior, Public | Building | Western | None | Human | Navigation, Tracking | UE5 | $59.99 | [市场链接](https://www.fab.com/listings/32aca4d1-84c0-4ad9-950c-9dde7995dca8) |
| `Old Factory` | Exterior, Industrial, Interior | Community | Industrial, Modern | — | Animal, Drone, Human, Motorbike | Tracking | — | $10.99 | [市场链接](https://www.unrealengine.com/marketplace/product/old-factory-01) |
| `Old_Town` | — | — | — | — | — | Navigation, Rendezvous, Tracking | UE5 | — | — |
| `Opera House Kit` | Educational, Facilities, Interior, Public | Indoor | Ancient, Public, Western | None | Human | Navigation, Tracking | UE5 | $59.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/opera-house-kit) |
| `Operating Room` | Facilities, Institutions, Interior | Indoor | Modern | — | Human | — | — | $89.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/operating-room-pack?sessionInvalidated=true) |
| `ParkingLot （cannot load）` | Facilities, Interior, Public | Indoor | Modern, Public | None | Animal, Car, Human, Motorbike | Navigation, Tracking | — | $14.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/qa-modular-parking) |
| `Pirate Stilt Village Island（navmesh unbuild）` | Exterior, Interior, Island, Landscapes, Village | Landscape&Urban | Ancient, Asian, Nature | Fluids, Wind | Drone, Human | Navigation, Tracking | UE5 | $74.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/pirate-stilt-village-island-modular-pack) |
| `Platformer factory （game mode bug）` | Industrial, Interior | Building | Industrial, Modern | None | Drone, Human | Navigation, Tracking | — | $14.99 | [市场链接](https://www.unrealengine.com/marketplace/zh-CN/product/side-scroller-modular-industrial-area) |
| `Platformer Hangar` | Industrial, Interior | Building | Industrial, Modern | — | Drone, Human | Tracking | — | $8.99 | [市场链接](https://www.unrealengine.com/marketplace/zh-CN/product/side-scroller-modular-industrial-area) |
| `Post-Soviet Village` | Exterior, Interior, Village | Landscape&Urban | Modern, Western | Snow | Animal, Car, Drone, Human, Motorbike | — | — | $24.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/post-soviet-village) |
| `Rocket Launch Command Center` | Industrial, Interior | Building | Modern | Interactive Object | Human | Navigation, Tracking | UE5 | $29.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/rocket-launch-command-center) |
| `Rocky Swampy Planet（navmesh lost some area）` | Exterior, Interior, Landscapes, Mountain | Landscape&Urban | Nature, Science Fiction | None | Drone, Human | — | UE5 | Free | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/modular-sci-fi-indoor-outdoor-environment-pack-rocky-swampy-planet) |
| `Roof-City Pack` | City, Exterior | Community | Modern | Gas | Drone, Human | Navigation, Tracking | UE5 | $89.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/roof-city-pack) |
| `RuralAustralia(1)` | Exterior, Landscapes, Rural | Landscape&Urban | Modern, Nature, Western | Wind | Animal, Car, Drone, Human, Motorbike | Tracking | — | Free | [市场链接](https://www.unrealengine.com/marketplace/zh-CN/product/rural-australia) |
| `RuralAustralia(2)` | Exterior, Landscapes, Rural | Landscape&Urban | Nature, Western | Fluids, Moving objects, Wind | Animal, Car, Drone, Human, Motorbike | Tracking | — | Free | [市场链接](https://www.unrealengine.com/marketplace/zh-CN/product/rural-australia) |
| `RuralAustralia(3)` | Exterior, Landscapes, Rural | Landscape&Urban | Nature, Western | Wind | Animal, Drone, Human | Tracking | — | Free | [市场链接](https://www.unrealengine.com/marketplace/zh-CN/product/rural-australia) |
| `Russian Winter Town` | City, Exterior, Interior | Landscape&Urban | Modern, Western | Gas, Snow | Animal, Car, Drone, Human, Motorbike | — | — | $4.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/russian-winter-town) |
| `School Gym` | Educational, Facilities, Interior, Public, Rendering Imcompatable | Indoor | Modern, Public | Interactive Object | Human | Tracking | UE4/5 | $14.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/school-gym) |
| `Science Fiction Valley Town` | Exterior, Interior, Village | Landscape&Urban | Science Fiction | Gas, Moving objects, Wind | Human | — | UE5 | $119.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/science-fiction-valley-town) |
| `Soul Cave` | Cave, Interior, Landscapes | Building | Nature | Fluids | Animal, Drone, Human | Tracking | — | Free | [市场链接](https://www.unrealengine.com/marketplace/product/soul-cave) |
| `Stone Pine Forest` | Exterior, Forest, Landscapes | Landscape&Urban | Nature, Public, Western | Fluids, Gas, Wind | Car, Drone, Human, Motorbike | Navigation, Tracking | — | $74.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/stone-pine-forest) |
| `StorageHouse` | Industrial, Interior | Indoor | Industrial, Modern | None | Drone, Human | Navigation, Tracking | — | $39.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/storage-house-set) |
| `SuburbNeighborhood_Day` | — | — | — | — | — | Navigation, Tracking | UE4 | — | — |
| `SuburbNeighborhood_Day` | Exterior, Interior, Village | Community | Modern, Western | Interactive Object | Animal, Car, Drone, Human, Motorbike | Navigation, Tracking | UE4/5 | $79.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/suburb-neighborhood-house-pack-modular) |
| `SuburbNeighborhood_Night` | — | — | — | — | — | Navigation, Tracking | UE4 | — | — |
| `SuburbNeighborhood_Night` | Exterior, Interior, Village | Community | Modern, Western | Interactive Object | Animal, Car, Drone, Human, Motorbike | Tracking | — | $79.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/suburb-neighborhood-house-pack-modular) |
| `Sunset Medieval Town` | Castle, Exterior, Historical, Interior, Landscapes, Mountain | Landscape&Urban | Ancient, Western | Fire, Interactive Object | Animal, Drone, Human | Tracking | UE4/5 | $4.99 | [市场链接](https://www.unrealengine.com/marketplace/product/sunset-modular-medieval-brick-buildings) |
| `Supermarket` | Commercial, Exterior, Facilities, Interior, Public, Rendering Imcompatable | Building | Modern, Public, Western | None | Animal, Human | Navigation, Tracking | UE4/5 | $49.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/supermarket) |
| `Swimming Pool` | Educational, Facilities, Interior, Public | Building | Modern, Public | Fluids | Drone, Human | Navigation, Tracking | — | $44.99 | [市场链接](https://www.unrealengine.com/marketplace/zh-CN/product/modular-swimming-pool-megapack) |
| `Temples of Cambodia - Ruins` | Exterior, Historical, Interior, Religious, Temple | Community | Ancient, Asian, Nature, Public | Fluids | Animal, Drone, Human | Navigation, Tracking | UE5 | $99.00 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/vp-temples-of-cambodia-ruins-exterior-and-interior) |
| `Tokyo Stylized Environment` | City, Exterior, Interior | Landscape&Urban | Asian, Modern | — | Animal, Car, Drone, Human, Motorbike | — | UE5 | $49.99 | [市场链接](https://www.fab.com/listings/9eec7a8a-b17c-4b89-a0d9-369a6ed5ac8c) |
| `track_train` | — | — | — | — | — | — | — | — | — |
| `Ultimate Farming` | Exterior, Interior, Landscapes, Rural | Community | Nature, Western | Wind | Animal, Drone, Human | Tracking | — | $84.99 | [市场链接](https://www.unrealengine.com/marketplace/zh-CN/product/ultimate-farming) |
| `UnderGround Parking` | Facilities, Interior, Public | Indoor | Modern, Public | — | Animal, Human | Tracking | UE4/5 | $74.99 | [市场链接](https://www.unrealengine.com/marketplace/zh-CN/product/atmospheric-modular-underground-car-park-hallways) |
| `University Classroom` | Educational, Interior | Indoor | Modern, Public, Western | None | Human | Navigation, Tracking | UE5 | $49.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/university-classroom-interior-environment-school-room) |
| `Venice-fast building` | City, Exterior | Landscape&Urban | Modern, Public, Western | Fluids | Animal, Drone, Human, Motorbike | Navigation, Tracking | UE4/5 | $19.99 | [市场链接](https://www.fab.com/listings/a6123fc7-2fa6-4350-a9cf-503a71e5e991) |
| `Victorian Train Station` | Facilities, Interior, Public, Rendering Imcompatable | Building | Modern, Public, Western | None | Animal, Human | Navigation, Tracking | UE4/5 | $49.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/victorian-train-station-and-railroad-modular-set) |
| `Watermills` | Exterior, Forest, Interior, Landscapes | Building | — | Fluids, Moving objects | Animal, Human | Tracking | UE4/5 | $69.99 | [市场链接](https://www.unrealengine.com/marketplace/product/watermills-nature-environment) |
| `WildWest` | Exterior, Village | Community | Steampunk, Western | Gas, Moving objects | Animal, Drone, Human | Tracking | UE4/5 | $49.99 | [市场链接](https://www.unrealengine.com/marketplace/product/wild-west-city-wild-west-town-wild-west-sky-city-town) |
| `Winter Racing Track` | Exterior, Forest, Landscapes, Mountain | Landscape&Urban | Modern, Nature | — | Animal, Car, Drone, Human, Motorbike | Tracking | — | $12.99 | [市场链接](https://www.unrealengine.com/marketplace/product/racing-track-winter-landscape) |
| `World Football Stadium` | Educational, Exterior, Facilities, Public, Rendering Imcompatable | Building | Modern, Public | — | Animal, Drone, Human | Navigation, Tracking | UE4/5 | $49.99 | [市场链接](https://www.unrealengine.com/marketplace/en-US/product/world-soccer-stadium) |

### 按类别浏览

- **Exterior** (76): `Abandoned District`, `Ancient Ruins`, `Arctic`, `Asian Medieval City`, `Asian Temple Pack`, `Bazaar`, `Beach Wedding`, `ChemicalFactory`, `Chinese Landscape （navmesh  lost some area）`, `ChineseWaterTown`, `City of Brass: Gardens`, `City of Brass: Palace`, `City of Brass: Streets`, `ContainerYard_Day（crash）`, `ContainerYard_Night`, `Courtyard`, `Desert Ruins`, `Downtown West`, `Edith Finch: House Grounds`, `Edith Finch: LowPoly Kingdom`, `Egyptian Pyramid`, `English College`, `Fantasy Cave`, `Fantasy Medieval Castle`, `Forest Gas Station`, `Gothic Day`, `Gothic Night`, `Grass Hills`, `Greek Island`, `Industrial Hangar`, `Infinity Blade: Castle (1)`, `Infinity Blade: Temple (1)`, `Infinity Blade: Temple (2)`, `Infinity Blade: Temple (3)`, `InfinityWeather-Desert`, `InfinityWeather-Rain`, `InfinityWeather-Snow`, `Korean Traditional Palace`, `Lighthouse Island`, `Lookout Tower`, `Medieval Castle`, `Medieval Nature Environment`, `Medieval Town Daytime`, `Medieval Town Nighttime`, `Middle East`, `Modular Building Set`, `Modular Industrial Area`, `Modular Neighborhood`, `Modular Old Town`, `Modular SciFi Village`, `Modular Temple Plaza`, `Modular Urban City Asset Megapack`, `Modular Victorian City`, `Old Factory`, `Pirate Stilt Village Island（navmesh unbuild）`, `Post-Soviet Village`, `Rocky Swampy Planet（navmesh lost some area）`, `Roof-City Pack`, `RuralAustralia(1)`, `RuralAustralia(2)`, `RuralAustralia(3)`, `Russian Winter Town`, `Science Fiction Valley Town`, `Stone Pine Forest`, `SuburbNeighborhood_Day`, `SuburbNeighborhood_Night`, `Sunset Medieval Town`, `Supermarket`, `Temples of Cambodia - Ruins`, `Tokyo Stylized Environment`, `Ultimate Farming`, `Venice-fast building`, `Watermills`, `WildWest`, `Winter Racing Track`, `World Football Stadium`
- **Interior** (69): `Abandoned District`, `Asian Medieval City`, `Bazaar`, `Beach Wedding`, `Bunker`, `ChemicalFactory`, `ChineseWaterTown`, `City of Brass: Gardens`, `City of Brass: Palace`, `City of Brass: Streets`, `Dungeon （game mode bug）`, `Edith Finch: Cannerylew`, `Egyptian Pyramid`, `Fantasy Cave`, `FlexibleRoom`, `Forest Gas Station`, `Gothic Day`, `Gothic Night`, `Greek Island`, `Holding Cells`, `Hospital`, `Industrial Hangar`, `Infinity Blade: Castle (1)`, `Infinity Blade: Castle (2)`, `Korean Traditional Palace`, `Lighthouse Island`, `Lookout Tower`, `Low Poly Medieval Interior`, `Medieval Castle`, `Medieval Nature Environment`, `Medieval Town Daytime`, `Medieval Town Nighttime`, `Modular Building Set`, `Modular Hotel Corridor`, `Modular Industrial Area`, `Modular Neighborhood`, `Modular Old Town`, `Modular SciFi Season 1`, `Modular SciFi Village`, `Modular Temple Plaza`, `Modular Urban City Asset Megapack`, `Museum Environment`, `Old Factory`, `Opera House Kit`, `Operating Room`, `ParkingLot （cannot load）`, `Pirate Stilt Village Island（navmesh unbuild）`, `Platformer factory （game mode bug）`, `Platformer Hangar`, `Post-Soviet Village`, `Rocket Launch Command Center`, `Rocky Swampy Planet（navmesh lost some area）`, `Russian Winter Town`, `School Gym`, `Science Fiction Valley Town`, `Soul Cave`, `StorageHouse`, `SuburbNeighborhood_Day`, `SuburbNeighborhood_Night`, `Sunset Medieval Town`, `Supermarket`, `Swimming Pool`, `Temples of Cambodia - Ruins`, `Tokyo Stylized Environment`, `Ultimate Farming`, `UnderGround Parking`, `University Classroom`, `Victorian Train Station`, `Watermills`
- **Landscapes** (29): `Ancient Ruins`, `Arctic`, `Asian Temple Pack`, `Beach Wedding`, `Chinese Landscape （navmesh  lost some area）`, `Desert Ruins`, `Edith Finch: House Grounds`, `Fantasy Cave`, `Fantasy Medieval Castle`, `Grass Hills`, `Greek Island`, `InfinityWeather-Desert`, `InfinityWeather-Rain`, `InfinityWeather-Snow`, `Lighthouse Island`, `Lookout Tower`, `Medieval Castle`, `Medieval Nature Environment`, `Pirate Stilt Village Island（navmesh unbuild）`, `Rocky Swampy Planet（navmesh lost some area）`, `RuralAustralia(1)`, `RuralAustralia(2)`, `RuralAustralia(3)`, `Soul Cave`, `Stone Pine Forest`, `Sunset Medieval Town`, `Ultimate Farming`, `Watermills`, `Winter Racing Track`
- **Historical** (23): `Asian Temple Pack`, `City of Brass: Gardens`, `City of Brass: Palace`, `City of Brass: Streets`, `Dungeon （game mode bug）`, `Edith Finch: LowPoly Kingdom`, `Egyptian Pyramid`, `Fantasy Cave`, `Fantasy Medieval Castle`, `Gothic Day`, `Gothic Night`, `Infinity Blade: Castle (1)`, `Infinity Blade: Castle (2)`, `Infinity Blade: Temple (1)`, `Infinity Blade: Temple (2)`, `Infinity Blade: Temple (3)`, `Korean Traditional Palace`, `Lighthouse Island`, `Medieval Castle`, `Medieval Nature Environment`, `Modular Temple Plaza`, `Sunset Medieval Town`, `Temples of Cambodia - Ruins`
- **Facilities** (15): `English College`, `Forest Gas Station`, `Holding Cells`, `Hospital`, `Modular Hotel Corridor`, `Museum Environment`, `Opera House Kit`, `Operating Room`, `ParkingLot （cannot load）`, `School Gym`, `Supermarket`, `Swimming Pool`, `UnderGround Parking`, `Victorian Train Station`, `World Football Stadium`
- **Mountain** (15): `Ancient Ruins`, `Arctic`, `Asian Temple Pack`, `Chinese Landscape （navmesh  lost some area）`, `Desert Ruins`, `Fantasy Medieval Castle`, `Grass Hills`, `InfinityWeather-Desert`, `InfinityWeather-Rain`, `InfinityWeather-Snow`, `Medieval Castle`, `Medieval Nature Environment`, `Rocky Swampy Planet（navmesh lost some area）`, `Sunset Medieval Town`, `Winter Racing Track`
- **Industrial** (14): `Abandoned District`, `Bunker`, `ChemicalFactory`, `ContainerYard_Day（crash）`, `ContainerYard_Night`, `Edith Finch: Cannerylew`, `Industrial Hangar`, `Modular Industrial Area`, `Modular SciFi Season 1`, `Old Factory`, `Platformer factory （game mode bug）`, `Platformer Hangar`, `Rocket Launch Command Center`, `StorageHouse`
- **Village** (13): `Bazaar`, `ChineseWaterTown`, `Medieval Town Daytime`, `Medieval Town Nighttime`, `Modular Neighborhood`, `Modular Old Town`, `Modular SciFi Village`, `Pirate Stilt Village Island（navmesh unbuild）`, `Post-Soviet Village`, `Science Fiction Valley Town`, `SuburbNeighborhood_Day`, `SuburbNeighborhood_Night`, `WildWest`
- **City** (11): `Asian Medieval City`, `Courtyard`, `Downtown West`, `Middle East`, `Modular Building Set`, `Modular Urban City Asset Megapack`, `Modular Victorian City`, `Roof-City Pack`, `Russian Winter Town`, `Tokyo Stylized Environment`, `Venice-fast building`
- **Public** (11): `Forest Gas Station`, `Hospital`, `Museum Environment`, `Opera House Kit`, `ParkingLot （cannot load）`, `School Gym`, `Supermarket`, `Swimming Pool`, `UnderGround Parking`, `Victorian Train Station`, `World Football Stadium`
- **Uncategorized** (10): `ContainerYard_Day`, `ContainerYard_Night`, `Demo_Roof`, `Greek_Island`, `Map_ChemicalPlant_1`, `MiddleEast`, `Old_Town`, `SuburbNeighborhood_Day`, `SuburbNeighborhood_Night`, `track_train`
- **Castle** (9): `Dungeon （game mode bug）`, `Fantasy Medieval Castle`, `Gothic Day`, `Gothic Night`, `Infinity Blade: Castle (1)`, `Infinity Blade: Castle (2)`, `Medieval Castle`, `Medieval Nature Environment`, `Sunset Medieval Town`
- **Educational** (7): `English College`, `Museum Environment`, `Opera House Kit`, `School Gym`, `Swimming Pool`, `University Classroom`, `World Football Stadium`
- **Religious** (7): `Asian Temple Pack`, `Infinity Blade: Temple (1)`, `Infinity Blade: Temple (2)`, `Infinity Blade: Temple (3)`, `Medieval Nature Environment`, `Modular Temple Plaza`, `Temples of Cambodia - Ruins`
- **Forest** (6): `Edith Finch: House Grounds`, `Lookout Tower`, `Medieval Castle`, `Stone Pine Forest`, `Watermills`, `Winter Racing Track`
- **Temple** (6): `Asian Temple Pack`, `Infinity Blade: Temple (1)`, `Infinity Blade: Temple (2)`, `Infinity Blade: Temple (3)`, `Modular Temple Plaza`, `Temples of Cambodia - Ruins`
- **Rendering Imcompatable** (5): `Lighthouse Island`, `School Gym`, `Supermarket`, `Victorian Train Station`, `World Football Stadium`
- **Rural** (5): `Beach Wedding`, `RuralAustralia(1)`, `RuralAustralia(2)`, `RuralAustralia(3)`, `Ultimate Farming`
- **Commercial** (3): `Forest Gas Station`, `Modular Hotel Corridor`, `Supermarket`
- **Institutions** (3): `Holding Cells`, `Hospital`, `Operating Room`
- **Island** (3): `Greek Island`, `Lighthouse Island`, `Pirate Stilt Village Island（navmesh unbuild）`
- **Cave** (2): `Fantasy Cave`, `Soul Cave`
- **Ruins** (2): `Ancient Ruins`, `Desert Ruins`
- **Lake** (1): `Medieval Castle`
- **Palace** (1): `Korean Traditional Palace`

!!! note "地图名区分大小写"
    请严格按表中名称填写（如 `Demo_Roof`、`GreekIsland`）。属性来自 Notion 场景画廊的人工标注；空白表示未标注。

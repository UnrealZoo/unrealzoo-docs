# What's New

> **UnrealZoo v3.1 expands the v3.0 foundation** with faster visual observation, 3-D perception, physics-driven robots, runtime agent customization, and externally packaged environments.

> **Now, all three platform binaries (Win/Linux/MacOs) are released!**

###  v3.1 Feature Updates

| Feature | Status | Description |
|------|------|----------------------------------------|
| **Faster UnrealCV Capture** |  Enhanced | Standard-camera **capture throughput** reaches **53.46 FPS at 2K** and **29.59 FPS at 4K** (up to 6.31×); **serialized end-to-end acquisition** averages **22.40 FPS at 2K** and **16.25 FPS at 4K** |
| **LiDAR Observation** |  Added | XYZI point-cloud observations with a player-controlled street-mapping example |
| **Occupancy Voxel Observation** |  Added | LINGO-compatible boolean occupancy grids with bounds- and mesh-based modes |
| **Expanded Panorama Observation** |  Added | Extended panoramic modalities for embodied perception and dataset collection |
| **[Shared-Memory Observation Transport](https://docs.unrealcv.org/en/latest/reference/unrealzoo_capture_transport.html)** |  Added | Lower-latency access to raw camera and occupancy observations |
| **[Runtime Reflection](https://docs.unrealcv.org/en/latest/unrealcv_plus/reference/runtime-reflection.html)** |  Added | JSON-based inspection, property access, and function invocation for supported Unreal objects |
| **[Cine Camera Controls](https://docs.unrealcv.org/en/latest/reference/cine_camera.html)** |  Added | Physical camera settings, manual focus control, and derived intrinsics |
| **[MQRC Capture](https://docs.unrealcv.org/en/latest/unrealcv_plus/reference/mqrc-rendering.html)** |  Added | High-quality lit capture with explicit rendering and post-process controls |
| **MuJoCo Robot Physics** |  Added | Go1 locomotion and vision-based Parkour, plus pretrained Micro Duck biped control |
| **Runtime Drone Visual Customization** |  Added | Switch among five production-ready models with animated propellers, use a template appearance, or load a compatible external Static Mesh without respawning the drone |
| **[3D Drone Navigation](example/new_features/README.md)** | v3.1.4 | Goal-directed flight with collision avoidance, smooth paths, automatic heading, and collision-envelope updates after resizing; **requires the updated v3.1.4 environment package containing this feature** |
| **Social Animation** |  Added | Select newly packaged party, everyday, and in-car character animations at runtime |
| **External 3DGS Environments** |  Added | Dynamically load user-packaged 3DGS assets and reuse UnrealZoo agents, cameras, and task APIs |
| **Runtime MCP** |  Added | Connect an MCP-compatible agent to a running UnrealZoo environment for scene inspection and task control |

 [v3.1 Changelog](doc/CHANGELOG_v3.1.md) ·  [v3.1 Feature Guide](example/new_features/README.md) ·  [UnrealCV+ Documentation](https://docs.unrealcv.org/en/latest/unrealcv_plus/index.html)

>  **Command reference:** The complete UnrealCV+ command list is available in the [Commands Reference](https://docs.unrealcv.org/en/latest/unrealcv_plus/reference/commands.html).

** v3.0 Core Updates**

> **UnrealZoo v3.0 is released!** This is our biggest update yet, bringing complete heterogeneous multi-agent collaboration capabilities, out-of-the-box interaction systems, and a comprehensive upgrade to the UnrealCV+ Plugin.

| Feature | Status | Description |
|------|------|----------------------------------------|
| **Heterogeneous Multi-Agent Collaboration** |  Released | Ground + UAV formation following (UE built-in navigation / Python external navigation API examples) |
| **Template-based Agent Spawn** |  Released | Runtime dynamic agent generation with mixed category support |
| **Enhanced Interaction System** |  Released | Door open / vehicle enter-exit / pickup / crouch / jump / climb, with API-keyboard mapping for easy understanding |
| **NavMesh Path Planning** |  Released | Calculate shortest path waypoints via API, support autonomous agent navigation control and waypoint export |
| **VLN Baseline Examples** |  Added | Integrates Uni-NaVid, ViNT/NoMaD, and StreamVLN with UnrealZoo navigation via a shared `env.step()` example. See [VLN Baseline README](example/VLN_Baseline/README.md) |

###  Version & Package Compatibility

| Code branch | Binary package | UE version | Status | Recommended use | Download |
|---|---|---:|---|---|---|
| **v3.1** | **Latest UE5.7 Full Package** | 5.7 | **Current / Recommended** | Latest perception, Go1, Runtime MCP, customization, and external 3DGS features | [ModelScope](https://modelscope.cn/datasets/UnrealZoo/UnrealZoo-UE5/files) · [Hugging Face](https://huggingface.co/datasets/UnrealZoo/UnrealZoo_UE5) |
| **v3.0** | UE5.6 Full Package | 5.6 | Previous stable release | Multi-agent tasks and established v3.0 workflows | [ModelScope](https://modelscope.cn/datasets/UnrealZoo/UnrealZoo-UE5/tree/master/UnrealZoo_UE5_6_v3.0.0) |
| **v2.0** | UE5 / UE4 Demo Package | UE5 / UE4 | Legacy | Compatibility with older tutorials and demo scenes | [UE5 package](https://modelscope.cn/datasets/UnrealZoo/UnrealZoo-UE5/files) · [UE4 package](https://modelscope.cn/datasets/UnrealZoo/UnrealZoo-UE4/files) |

The recommended v3.1 UE5.7 package is approximately **70 GB**.

###  Development History

**Click to view historical updates**

#### 2024-12: Paper Release
-  Paper: [UnrealZoo: Enriching Photo-realistic Virtual Worlds for Embodied AI](https://arxiv.org/abs/2412.20977)
-  Website: [unrealzoo.github.io](https://unrealzoo.github.io/)
-  Notion Docs: [Scene Gallery](https://www.notion.so/Scene-Gallery-a801475ff98943159da66f641f4c38b2)

#### 2025-01: UE5.6 Full Environment Package
-  100+ scenes, 67GB full package
-  Chaos physics system (vehicles, collisions, explosions, fire)
-  Object interaction system (pickup/drop)
-  Appearance switching system (player/animal categories merged)
-  Cross-platform binary support (Win/Mac/Linux auto-configuration)
-  ModelScope China mirror (high-speed download channel)

#### 2026-04: v3.0 Official Release
-  Heterogeneous multi-agent collaboration
-  Template-based Agent Spawn
-  Full enhanced interaction system demo code (API-keyboard mapping)
-  NavMesh path planning and task application demo code
-  UnrealCV+ Plugin comprehensive upgrade

#### 2026: v3.1 Feature Update
-  Faster UnrealCV visual observation and recording workflows
-  LiDAR and occupancy voxel observations
-  MuJoCo robot simulation examples for Go1 and Micro Duck
-  User-packaged 3DGS environment support
-  Runtime drone visual customization with animated built-in models and external Static Mesh support
-  Expanded character social animations

[View v3.1 Changelog](doc/CHANGELOG_v3.1.md)

---

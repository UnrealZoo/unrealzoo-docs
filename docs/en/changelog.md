# Changelog

# Changelog

All notable changes to this project are documented in this file.

## [v3.0-stage] - 2026-04-13

This stage update focuses on task unification, mixed-population support, keyboard interaction upgrades, and demo re-organization.

### Added

- Added mixed-category population initialization in `UnrealCv_base.set_population`, supporting per-slot category lists such as `['player', 'player', 'player', 'drone']`.
- Added template-based dynamic spawn pipeline for agents:
  - environment JSON can be template-only (no pre-placed agent names),
  - runtime spawn uses `asset_path` + `spawn_from_path`,
  - agent slots are materialized during `set_population`.
- Added heterogeneous cooperation demo: `example/multi_agent/HeterogeneousCooperation/Aerial-Ground-Cooperative.py`.
  - 3 ground agents + 1 drone.
  - Drone supports `DronePoseTracker` auto-follow and keyboard override.
  - Stable per-episode formation setup, +2m drone spawn height, and 2x2 observation mosaic.
- Added keyboard animal tracking demo: `example/tracking/basic/tracking_keyboard_animal.py`.
- Added platform binary template workflow in `generate_env_config.py`:
  - `ENV_BIN_TEMPLATE_LINUX`
  - `ENV_BIN_TEMPLATE_WIN`
  - `ENV_BIN_TEMPLATE_MAC`
  - New helper flow to generate per-platform `env_bin` fields in JSON.
- Added default navigation target schema in generated JSON:
  - `env.targets.Point: []`

### Changed

- Refactored `generate_env_config.py` to support:
  - template-based binary path generation,
  - unified agent templates with `asset_path` (instead of fixed pre-placed actor entries),
  - UE5 backup field reuse (`height`, `safe_start`, `reset_area`).
- Updated base environment spawn behavior (`UnrealCv_base`):
  - supports template-only startup and delayed population spawn,
  - uses category-aware templates when spawning mixed agents,
  - updates action/observation/camera slots together with dynamic population changes.
- Updated navigation env behavior (`navigation.py`, `navigationmulti.py`):
  - no implicit target filling;
  - warning when `targets.Point` is empty;
  - safe reset/step behavior when target list is empty.
- Updated keyboard navigation mappings for human demos:
  - `F` -> open door
  - `H` -> enter/exit vehicle
  - `Ctrl` -> crouch
  - `E` -> pickup
- Updated drone keyboard demo for 4-DOF continuous control (`vx`, `vy`, `vz`, `vyaw`) and task intro display flow.
- Updated interaction animation mappings in `Character_API`:
  - `open_door` uses default `state=1`,
  - `enter_vehicle` mapped to `enter_exit_car(player_index=0)`,
  - standardized pickup action mapping.
- Reorganized `example/` into clearer task-oriented structure:
  - tracking
  - navigation
  - multi_agent
  - legacy/wip areas
- Updated `example/README.md` with new categorized demo index.
- Updated root `README.md` example commands to the new paths.

### Fixed

- Fixed interaction action mismatch causing `KeyError` for pickup animation by unifying runtime mapping.
- Fixed mixed-action schema mismatch for non-human templates by aligning config generation with required keys.
- Fixed drone cooperation demo control priority so keyboard input overrides auto tracker only while keys are pressed.

### Compatibility Notes

- Navigation tasks now expect `env.targets.Point` to exist in map JSON (can be empty list).
  - Empty list triggers a warning but does not crash; navigation reward will be 0 until targets are set.
- For generated JSONs, users should select or set navigation targets before running target-dependent navigation workflows.
- Mixed-population scenarios should explicitly set `env.unwrapped.agents_category` **before** population wrappers apply.
  - Incorrect timing: `env.reset()` → `agents_category = [...]` → wrapper (will not work)
  - Correct timing: `agents_category = [...]` → `env.reset()` → wrapper
- Older workflows that relied on fixed `agents.{name}` pre-placement should migrate to template-based `agents.{category}` + runtime population.
  - **Why migrate**: Template-based spawn decouples map JSON from instance count, enabling dynamic population changes and mixed-category experiments without editing JSON.

### Note

- Some legacy demos were moved/replaced; prefer new paths listed in `example/README.md`.

### UnrealCV+ Plugin

Summary of notable UnrealCV+ changes in v3.0 stage.

- Added runtime `PAK` mounting support for packaged applications, making it easier to extend content without rebuilding the whole project.
  - Supports mount, unmount, mounted pak listing, mount-state checks, file enumeration, asset enumeration, asset rescanning, and dynamic asset loading/registration.
  - Python APIs:
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
  - See unrealzoo website: `Home`->`Document`->`Import Custom Assets` for more information.

- Added panoramic camera support for 360-degree equirectangular image generation.
  - Supports per-camera panorama cube resolution and direct panorama export to file.
  - Python APIs:
    - `set_camera_panoramic_resolution()`
    - `capture_panoramic()`

- Added a faster C++ video recording pipeline, improving recording efficiency and making large-scale capture workflows more practical.
  - Supports direct recording from a camera or actor, configurable output directory, frame rate, duration, and selected recording channels.
  - Python APIs:
    - `start_simple_recording()`: start a recording job with output path, FPS, duration, and selected channels such as `lit` or `mask`.
    - `stop_recording()`: stop an active recording job for the target camera or capture actor.
    - `get_use_movie_quality_rendering()` / `set_use_movie_quality_rendering()`: query or change the global movie-quality rendering switch used by the recording pipeline.
    - `get_record_via_viewport()` / `set_record_via_viewport()`: query or change the global switch for whether recording uses the viewport capture path.
    - `get_warmup_frames()` / `set_warmup_frames()`: query or configure the global number of warmup frames rendered before recording starts.
    - `get_paused_tick_interval()` / `set_paused_tick_interval()`: query or configure the global paused tick interval in seconds.
    - `get_record_add_timestamp()` / `set_record_add_timestamp()`: query or control whether an active capture actor appends a timestamp suffix to recorded outputs.
    - `get_recording_paused()` / `set_recording_paused()`: query or control whether an active recording session is paused.

- Improved capture performance for common modalities such as `lit`, `mask`, and `depth`.
  - Since December 2025, frame throughput has been steadily improved, especially around the `BaseCamSensor` path.
  - In test cases, `lit` capture throughput improved from roughly `15 fps` to `20 fps`.

- Updated camera ID support to remain compatible with existing legacy camera addressing while also providing the newer stable `CID` format for long-term use in scripts and configurations.
  - Existing Python camera APIs remain backward compatible.
  - New Python APIs expose stable `CID-*` camera identifiers explicitly:
    - `get_camera_list_cid()`
    - `get_camera_id_map()`
  - Legacy camera discovery remains available through:
    - `get_camera_list_legacy()`

- Added annotation command support for scene and actor labeling workflows.
  - Supports annotating a single actor, annotating the whole world, clearing world annotation, enabling/disabling annotation cache, and clearing cached annotation components.
  - Python APIs:
    - `annotate_object()`
    - `annotate_world()`
    - `clear_world_annotation()`
    - `set_annotation_cache_enabled()`
    - `clear_annotation_cache()`

- Added object spawning from asset paths via `spawn_from_path`.
  - This complements the older class-based spawn flow and is better suited for runtime content referenced by full asset path.
  - Python APIs:
    - `spawn_object_from_path()`
  - `set_new_obj()` now gives a clearer hint when the input looks like an asset path, and can automatically retry via `spawn_object_from_path()`.

---



---

# UnrealZoo v3.1 Changelog

Status: **Development snapshot**  
Version: **v3.1**
Scope baseline: changes after [`v3.0-stage`](CHANGELOG_v4.md)

This document fixes the feature boundary for the next major UnrealZoo update
before the root README, tutorials, GIFs, and example index are reorganized.
It separates end-user UnrealZoo features from the broader UnrealCV+ platform
improvements included in the release.

The UnrealCV+ label means that a capability is developed and validated first
with UnrealZoo builds. It does not imply a separate UnrealCV plugin or that
every item is already part of the upstream open-source UnrealCV baseline. See
the official [UnrealCV+ documentation](https://docs.unrealcv.org/en/latest/unrealcv_plus/index.html)
and [feature overview](https://docs.unrealcv.org/en/latest/unrealcv_plus/overview.html).

## v3.1.4 — 3D drone navigation

- Added goal-directed 3D flight for `BP_Drone_customized`, with collision
  avoidance, path smoothing, and automatic heading through the existing
  physics-based flight controls.
- Added `nav_update_collision` to refresh the collision envelope after scale
  or appearance changes during reset, alongside navigation status, stop, and
  manual-release APIs.
- **Requires the updated v3.1.4 environment package containing this feature;**
  updating the Python repository alone is insufficient. See the
  [usage guide](../example/new_features/README.md#3d-drone-navigation-v314).

## Release highlights

| Area | User-facing result | Recommended showcase |
|---|---|---|
| UnrealCV rendering and capture | Current development-build [shared-memory acquisition](https://docs.unrealcv.org/en/latest/reference/unrealzoo_capture_transport.html) averages 22.40 FPS at 2K and 16.25 FPS at 4K | End-to-end benchmark comparison and real-time capture clip |
| LiDAR | XYZI observations and pose-conditioned street mapping | Suburb street-mapping Python demo + GIF |
| MuJoCo | Unreal-rendered Go1 driven by MuJoCo state and policy control | Go1 parkour Python demo + GIF |
| Occupancy voxels | LINGO-compatible scene occupancy grids for embodied-agent observation | Profile/shape documentation + visualization |
| Runtime drone visual customization | Switch five production-ready models with animated propellers, use a customization template, or load an external Static Mesh without respawning the pawn | Appearance-cycle demo + GIF |
| Social animation | Trigger the newly packaged character social-animation library at runtime | Animation-cycle demo + GIF |
| External 3DGS environment | Load a user's packaged 3DGS scene at runtime and reuse UnrealZoo agents and observations in it | External-scene loading workflow + agent demo |

## Added

### UnrealZoo features

#### 1. LiDAR observation and mapping

- Added a camera LiDAR observation that returns an `N x 4` float32 XYZI point
  cloud.
- Added a NumPy observation interface:

  ```text
  vget /camera/[camera_id]/lidar npy
  ```

- Added a live `SuburbNeighborhood_Day` SLAM-style example that combines the
  player RGB view, the current sensor-local scan, the synchronized camera pose,
  and an accumulated top-down voxel map.
- Added scan diagnostics for expected ray-grid layout, duplicate/order/range
  anomalies, synchronized pose span, stationary consistency, and map overlap.

#### 2. MuJoCo Go1 integration

- Added an Unreal-rendered MuJoCo simulation path for the Unitree Go1
  quadruped.
- Added Go1 policy control with a 12-D action, a 3-D velocity command, and a
  48-D policy observation.
- Added velocity and parkour dynamics for Go1, together with keyboard, policy,
  pose-preview, observation-visualization, and GIF-recording examples.

#### 3. Scene occupancy voxel observation

- Added boolean scene occupancy volumes with C-order axis layout
  `[x, y_up, z]`.
- Added `lingo_vis` and `lingo_train` profiles at 2 cm resolution.
- Added `bounds` and `mesh` voxelization methods, optional dynamic actors, and
  camera-relative origin/yaw arguments.
- Added NPY observation and machine-readable specification endpoints:

  ```text
  vget /scene/occupancy npy [profile] [method] [origin_cm x y z yaw include_dynamic]
  vget /scene/occupancy/spec [profile] [method]
  ```

#### 4. Runtime drone visual customization

- Added five production-ready appearances with animated propellers: `spy`,
  `fpv`, `police`, `baba`, and `delivery`, plus the `template` appearance for
  customization.
- Appearance switching on `BP_Drone_customized` does not respawn the pawn or
  replace its controller, movement, physics, camera, or current task state.
- Added `set_app`, `reset_app`, and `get_available_apps` Blueprint-callable
  functions.
- Added custom static-mesh setters, including string-path variants for assets
  supplied by a mounted PAK:
  `set_app_mesh_path` and `set_app_mesh_path_transform`.
- External Static Mesh loading is intended for rapid asset integration and
  visual customization. It preserves the drone systems above and displays the
  imported geometry as authored; component-level animations are not generated
  automatically for a single Static Mesh.

#### 5. Character social animations

- Added the `set_social_anim` Blueprint function for runtime social-animation
  selection.
- Added montage playback and stop handling for social actions.
- Packaged the `SocialAnimsBundle2` content with the UnrealZoo build, including
  party, female, and in-car animation groups.
- Animation-name examples include `AirKiss`, `DrinkAndTalk`, `FemaleLaugh`,
  `Reading`, `Selfy`, `SmallTalk`, `Smoking`, and `SpeakOnPhone`.
- The input is the case-sensitive suffix after `AM_`; see the
  [complete argument list](../example/new_features/README.md#5-character-social-animations).

#### 6. User-supplied 3DGS environments through dynamic PAK loading

- Added a release workflow in which users import and cook their own 3DGS asset
  into an external PAK instead of rebuilding the complete UnrealZoo project.
- Added a guided runtime workflow for discovering and activating compatible
  3DGS content from an external package.
- The loaded 3DGS environment remains a normal UnrealZoo world: existing
  players, drones, cameras, observations, and task logic can be spawned or
  reused on top of it.
- Runtime loading consumes an already imported and cooked Gaussian-splat asset;
  raw PLY import is an editor/cooking step, not an environment-reset operation.

### UnrealCV+ user-facing improvements

#### Rendering and observation performance

- Current development-build [shared-memory acquisition](https://docs.unrealcv.org/en/latest/reference/unrealzoo_capture_transport.html) averages `23.61 FPS` at
  1080p, `22.40 FPS` at 2K, and `16.25 FPS` at 4K in serialized end-to-end tests.
- These figures measure complete client acquisition latency, not unloaded
  viewport frame rate; transport-only closed-build results are documented
  separately in the UnrealCV capture-transport reference.
- Improved responsiveness for continuous observation loops, interactive agent
  control, and dataset recording workloads.
- Reduced the practical cost of collecting multiple visual modalities from an
  active UnrealZoo scene.

#### Panoramic capture extensions

- Extended equirectangular panoramic capture beyond lit output to normal,
  object-mask, and depth modalities.
- Added configurable panoramic output resolution.

#### Built-in recording workflow

- Improved the built-in camera and actor recording workflow for sustained
  dataset capture.
- Added user controls for output channels, frame rate, duration, warm-up,
  pause/resume behavior, and output naming.

#### Camera, annotation, and dynamic content workflows

- Added stable camera identifiers while keeping legacy numeric camera scripts
  compatible.
- Expanded scene and object annotation controls for dataset generation.
- Added runtime external-content loading and asset-path spawning so users can
  extend an UnrealZoo environment without rebuilding the complete project.

#### MuJoCo command bridge

- Added UnrealCV object commands for Go1 MuJoCo setup, synchronous stepping,
  observation retrieval, policy action, and policy command.

Several of these UnrealCV+ capabilities first appeared during the v3.0 stage.
They are listed here because this release turns them into complete user-facing
workflows, rather than claiming that every item was first introduced in this
cycle.

## Changed

- New feature examples attach to an already running Unreal Editor/PIE session
  by default instead of silently launching a second Unreal process.
- The street-mapping example defaults to the spawned player camera and treats
  Unreal world positions as centimetres while LiDAR XYZ values are metres.
- Corrected RGB colour reproduction in the new visualization examples.
- Dynamic content examples distinguish filesystem PAK paths, Unreal package
  paths, and full Unreal object paths instead of treating them as
  interchangeable strings.

## Compatibility and limitations

- Camera-to-LiDAR extrinsics must be applied when the sensor is not colocated
  with the camera. A demo may assume identity only when that assumption is
  explicitly shown.
- Unreal Engine locations use centimetres. LiDAR and visualization examples
  expose metric coordinates; conversions must occur exactly once.
- Occupancy profiles are large dense boolean arrays. Select the smallest
  profile that satisfies the task and avoid retaining unnecessary frames.
- `mesh` occupancy accuracy depends on compatible geometry data and may fall
  back to bounds for unsupported scene assets.
- A user 3DGS package must be compatible with the target UnrealZoo engine,
  platform, and content requirements.
- The social-animation command accepts names that exist in the cooked bundle;
  unknown names should be treated as errors rather than silently substituted.
- UnrealCV+ availability is tied to the UnrealZoo-tested plugin build. Scripts
  should query command/help availability when they also target upstream or
  older UnrealCV installations.

## Examples and media

- [`suburb_street_slam.py`](../example/new_features/suburb_street_slam.py)
  demonstrates player-controlled LiDAR street mapping.
- [`lidar_visualization.py`](../example/new_features/lidar_visualization.py)
  visualizes individual LiDAR observations and accumulated maps.
- [`parkour/demo.py`](../example/mujoco/parkour/demo.py) demonstrates MuJoCo Go1
  control in an Unreal-rendered scene.
- [`realtime_scene_occupancy_gpu.py`](../example/new_features/realtime_scene_occupancy_gpu.py)
  renders live [shared-memory](https://docs.unrealcv.org/en/latest/reference/unrealzoo_capture_transport.html) occupancy data in four GPU-instanced views.
- [`drone_mesh_switch_demo.py`](../example/new_features/drone_mesh_switch_demo.py)
  cycles the available drone appearances on a live pawn.
- The packaged-binary command
  `vset /action/game/level /Game/3dgs/custom_3dgs` demonstrates loading an
  external 3DGS level while retaining the UnrealZoo interfaces.

- [`lidar_street_slam.gif`](https://github.com/UnrealZoo/unrealzoo-gym/blob/v3.1/doc/figs/new_features/lidar_street_slam.gif): full
  LiDAR street-mapping capture converted from MP4 for README use.
- [`mujoco_go1_keyboard.gif`](https://github.com/UnrealZoo/unrealzoo-gym/blob/v3.1/doc/figs/new_features/mujoco_go1_keyboard.gif): basic
  MuJoCo Go1 keyboard-control demonstration.
- [`mujoco_go1_parkour_third_person.gif`](https://github.com/UnrealZoo/unrealzoo-gym/blob/v3.1/doc/figs/new_features/mujoco_go1_parkour_third_person.gif):
  advanced parkour policy shown from a third-person view.
- [`mujoco_go1_parkour_depth.gif`](https://github.com/UnrealZoo/unrealzoo-gym/blob/v3.1/doc/figs/new_features/mujoco_go1_parkour_depth.gif):
  UnrealCV depth and the depth input used by the parkour policy.
- [`drone_mesh_switch.gif`](https://github.com/UnrealZoo/unrealzoo-gym/blob/v3.1/doc/figs/new_features/drone_mesh_switch.gif): runtime
  mesh switching on a live drone without respawning the pawn.
- [`3dgs_dynamic_load.gif`](https://github.com/UnrealZoo/unrealzoo-gym/blob/v3.1/doc/figs/new_features/3dgs_dynamic_load.gif): an
  external 3DGS environment loaded at runtime with an UnrealZoo-supported
  actor reused in the scene.
- [`social_animation.gif`](https://github.com/UnrealZoo/unrealzoo-gym/blob/v3.1/doc/figs/new_features/social_animation.gif): multiple
  UnrealZoo characters playing runtime-selected social animations.

Environment-specific usage questions and detailed behavior can be discussed in
[GitHub Discussions](https://github.com/UnrealZoo/gym-unrealzoo/discussions).

## TODO

- [ ] MuJoCo Unitree G1 integration and examples.

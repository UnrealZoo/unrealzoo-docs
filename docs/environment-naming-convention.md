# Environment Naming Convention

This page describes the naming convention for creating environment instances in UnrealZoo-Gym. Understanding this format is essential for correctly initializing your training environments.

## 📝 Naming Format

```plain text
Unreal{task}-{MapName}-{ActionSpace}{ObservationType}-v{version}
```

## 📊 Parameter Reference

### {task} - Task Type

- Track - Visual tracking task (follow a moving target)
- Navigation - Navigation task (reach a destination)
- Rendezvous - Multi-agent rendezvous task
- Rescue - Search and rescue task
### {ActionSpace} - Action Space

- Discrete - Discrete action space (predefined actions)
- Continuous - Continuous action space (direct control values)
- Mixed - Mixed action space (supports interactive actions: pick, drop, climb, etc.)
### {ObservationType} - Observation Type

- Color - RGB color image
- Depth - Depth map
- Rgbd - RGB + Depth combined
- Gray - Grayscale image
- CG - Computer graphics rendering
- Mask - Object segmentation mask
- MaskDepth - Mask + Depth combined
- ColorMask - Color + Mask combined
- Pose - Agent pose (position + rotation)
## 💡 Usage Examples

Here are some common environment configurations:

### Example 1: Basic Visual Tracking

```python
import gym
import gym_unrealcv

# Visual tracking with continuous control, RGB observation
env = gym.make('UnrealTrack-track_train-ContinuousColor-v0')

# Same task with discrete actions
env = gym.make('UnrealTrack-track_train-DiscreteColor-v0')
```

### Example 2: Navigation with Interactive Actions

```python
# Navigation with mixed action space (supports pick/drop/climb)
env = gym.make('UnrealNavigation-Demo_Roof-MixedColor-v0')

# Navigation with RGB-D observation
env = gym.make('UnrealNavigation-Old_Town-MixedRgbd-v0')
```

### Example 3: Animal Tracking with Pose

```python
# Track an animal with pose observation instead of images
env = gym.make('UnrealTrack-Greek_Island-ContinuousPose-v0')
```

## 🗺️ Available Map Names

See Scene Gallery for the complete list of available maps and their supported tasks.

> 📌 Tip: Use Mixed action space if you need interactive actions like picking up objects, climbing, or entering vehicles. Only Mixed supports these advanced interactions.

## 🔄 Version Numbers

The version number (v0-v5) controls environment augmentation for the track_train map:

- v0 - Default, no augmentation
- v1-v5 - Various augmentation factors (lighting, obstacles, layout, textures)


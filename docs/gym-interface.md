# Gym Interface

> 📌 Gym_unrealcv is a Python library that provides an interface for using Unreal Engine (UE4/UE5) with OpenAI's Gym. It allows you to create reinforcement learning environments using Unreal Engine and UnrealCV.

# 1. Installation: 

You can install gym_unrealcv using pip in the source folder:

pip install -e .


# 2. Creating an Environment: 

To create an environment, you can use the gym.make() function with the ID of the environment you want to create. For example:

```python
import gym 
import gym_unrealcv
env = gym.make('UnrealTrack-SuburbNeighborhood_Day-ContinuousMask-v0') # build an environment
# Environment Name: Unreal{Task}-{Scene_Name}-{Action Space}{Observation Space}-{version}
```

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

# 3. Interacting with the Environment: 

You can interact with the environment using the step() and reset() methods. The step() method takes an action and returns an observation, a reward, a done flag (indicating if the episode is over), and info (extra information which can be useful for debugging). The reset() method resets the environment to its initial state and returns the initial observation.

```python
obs = env.reset() # reset the environment and get the initial observation

action = env.action_space.sample() # Sample a random action

# take the action and get the reward and new observation from the environment
obs, reward, done, info = env.step(action) 
```

# 4. Rendering the Environment: 

If you want to visualize the environment, you can use the render() method, or use cv2.imshow() method to visualize the observation data.

```python
img = env.render(mode='rgb_array')
img = img[..., ::-1]  # bgr->rgb
cv2.imshow('show', img)

obs, rewards, done, info = env.step(actions)
cv2.imshow('show', obs[0])
cv2.waitKey(1)
```

# 5. Closing the Environment:

 Once you're done with the environment, you can close it using the close() method:


```python
env.close()
```

# 6. Toolkits

We also provide several wrappers that you can use to modify the environment in various ways, including configuring the UE binaries while launching, control the simulated time,  set early done condition, randomize the populations.

# Wrappers: 

We also provide several wrappers that you can use to modify the environment in various ways. 

### ConfigUE

  - The ConfigUEWrapper is used to configure the launching settings of Unreal Engine Binaries. It can be used to set various parameters of the Unreal Engine environment such as offscreen rendering, observation resolution, communication protocol, docker, etc. 
```python
from gym_unrealcv.envs.wrappers import configUE 
configUE.ConfigUEWrapper(env, docker=False, resolution=(160, 160), display=None,
                         offscreen=False, use_opengl=False, nullrhi=False, 
                         gpu_id=None, sleep_time=5, comm_mode='tcp')
```

### TimeDilation

  - The TimeDilationWrapper is used to control the speed of the simulation in the Unreal Engine environment. This can be useful for simulating various FPS situations for different tasks.
```python
from gym_unrealcv.envs.wrappers import time_dilation
env = time_dilation.TimeDilationWrapper(env, reference_fps=30, update_steps=60) 
```

### EarlyDone

  - The EarlyDoneWrapper is used to end the episode early based on certain conditions. Users could modify the source code for different tasks. This can be useful for preventing episodes from running for too long.
### RandomPopulation

  - The RandomPopulationWrapper randomly populates the environment with a specified number of agents:



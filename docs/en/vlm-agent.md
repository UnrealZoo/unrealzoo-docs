# VLM Agent

Here we show the examplar sequneces of GPT-4o agent on real time, comparing with RL agent, to demonstrate the limitations of the current agents.

# Embodied Visual Tracking

The agent is required to dynamically track the person in the image.


## RL Agent

<video controls loop muted playsinline preload="none" title="                                     SuburbNeighborhood" poster="../assets/Offline_Suburb.jpg" src="../assets/Offline_Suburb.mp4" style="max-width:100%;border-radius:6px"></video>

## GPT-4o Agent with Real-time Mode

The environment and target will keep running while the GPT is responding to the instructions. The agent easily loses the target from the view due to the latency of the response.

<video controls playsinline preload="metadata" width="640" src="../assets/GPT_tracking_5.mp4" style="max-width:100%"></video>

## GPT-4o Agent with Step- wise Pause Mode

The environment and target are paused while waiting for the GPT response. The agent could keep tracking the target for a while, however, such setting is unrealistic in real-world.

<video controls playsinline preload="metadata" width="640" src="../assets/GPT_tracking_stepwise.mp4" style="max-width:100%"></video>

# Visual Navigation

The agent is required to navigate to a set of wooden boxes in the environment, as illustrated in the following picture.

![               Target object     ](assets/image.png)

## RL Agent

We have trained an end-to-end visual navigation model, enabling the agent to adapt to environmental structures through jumping, crouching, walking, and running, and to quickly reach the target location.

<video controls loop muted playsinline preload="none" title="A success case by RL-based agent (1)" poster="../assets/output.jpg" src="../assets/output.mp4" style="max-width:100%;border-radius:6px"></video>


## GPT-4o Agent

The GPT-4o receives the first-person observation and the target’s relative coordinates as observation. The agent can perform turn, jump, and moving actions to navigate to the destination over obstacles. 

<video controls playsinline preload="metadata" width="640" src="../assets/gpt_navigation_2.mp4" style="max-width:100%"></video>


<video controls playsinline preload="metadata" width="640" src="../assets/gpt_nav_failure_2.mp4" style="max-width:100%"></video>

### Failure Case Analysis：

<video controls loop muted playsinline preload="none" title="The key frame sequence led to failure. When the target is positioned to the front of the agent, the agent  predicts two continuous "Turn right" rather than "Turn left" to bypass the front wire fence, causing it to miss the entrance. This misstep ultimately results in the agent being blocked by the wire fence later in the sequence" poster="../assets/gpt_nav_failure_2.jpg" src="../assets/gpt_nav_failure_2.mp4" style="max-width:100%;border-radius:6px"></video>

When we provide the relative direction to the target, GPT struggles with analyzing the environment effectively and, at critical moments, provides inappropriate suggestions. This can lead to suboptimal decision-making, especially in dynamic and complex scenarios. Accumulated errors will eventually lead to task failure. For example, in the video, the agent moved correctly at the beginning, but it predicted the wrong direction for bypassing the front obstacles(wire fence), missing the entrance to the target area. Later, when it encountered a wire fence, the accumulated error ultimately led to failure.



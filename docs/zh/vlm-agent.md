# VLM Agent

此处展示 GPT-4o agent 在实时模式下的示例序列，并与 RL agent 进行对比，以说明当前 agent 的局限性。

# Embodied Visual Tracking

agent 需要动态跟踪图像中的人物。

## RL Agent

<video controls loop muted playsinline preload="none" title="                                     郊区社区" poster="../../assets/Offline_Suburb.jpg" src="../../assets/Offline_Suburb.mp4" style="max-width:100%;border-radius:6px"></video>

## 实时模式下的 GPT-4o Agent

当 GPT 响应指令时，环境和目标将持续运行。由于响应延迟，agent 很容易从视野中丢失目标。

<video controls playsinline preload="metadata" width="640" src="../../assets/GPT_tracking_5.mp4" style="max-width:100%"></video>

## 逐步暂停模式下的 GPT-4o Agent

在等待 GPT 响应时，环境和目标处于暂停状态。agent 可以在一段时间内持续跟踪目标，但此类设定在真实世界中并不现实。

<video controls playsinline preload="metadata" width="640" src="../../assets/GPT_tracking_stepwise.mp4" style="max-width:100%"></video>

# Visual Navigation

agent 需要导航至环境中一组木箱处，如下图所示。

![               目标物体     ](assets/image.png)

## RL Agent

我们训练了一个端到端视觉导航模型，使 agent 能够通过跳跃、蹲伏、行走和奔跑来适应环境结构，并快速到达目标位置。

<video controls loop muted playsinline preload="none" title="RL agent 的成功案例 (1)" poster="../../assets/output.jpg" src="../../assets/output.mp4" style="max-width:100%;border-radius:6px"></video>


## GPT-4o Agent

GPT-4o 接收第一人称观测和目标相对坐标作为输入。agent 可以执行转向、跳跃和移动动作，越过障碍物导航至目的地。

<video controls playsinline preload="metadata" width="640" src="../../assets/gpt_navigation_2.mp4" style="max-width:100%"></video>


<video controls playsinline preload="metadata" width="640" src="../../assets/gpt_nav_failure_2.mp4" style="max-width:100%"></video>

### 失败案例分析：

<video controls loop muted playsinline preload="none" title="导致失败的关键帧序列。当目标位于 agent 前方时，agent 预测了两次连续的"右转"而非"左转"来绕过前方铁丝网，导致其错过入口。这一失误最终导致 agent 在序列后续阶段被铁丝网阻挡" poster="../../assets/gpt_nav_failure_2.jpg" src="../../assets/gpt_nav_failure_2.mp4" style="max-width:100%;border-radius:6px"></video>

当我们提供目标的相对方向时，GPT 难以有效分析环境，并在关键时刻给出不恰当的建议。这可能导致次优决策，尤其在动态复杂场景中。累积误差最终将导致任务失败。例如，在视频中，agent 起初移动正确，但预测了错误的绕行前方障碍物（铁丝网）的方向，错过了目标区域的入口。随后当其遇到铁丝网时，累积误差最终导致失败。
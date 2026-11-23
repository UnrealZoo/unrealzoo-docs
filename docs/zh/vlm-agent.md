# VLM 智能体

> 本页面对应 Notion 中尚在撰写的内容，现基于 UnrealZoo 仓库已有材料补充。

UnrealZoo 支持将视觉-语言模型（VLM）智能体接入高度逼真的环境，进行具身推理、任务控制与评测。

## 相关能力

- **EmbRACE-3K**：面向语言引导具身推理的 3,000+ 任务数据集，在 UnrealZoo 复杂环境中评测 VLM 智能体。[[Paper](https://arxiv.org/abs/2507.10548)] [[Homepage](https://mxllc.github.io/EmbRACE-3K/)]
- **Runtime MCP（v3.1）**：将 MCP 兼容的智能体连接到运行中的 UnrealZoo 环境，用于场景检查与任务控制。
- **ROCKET-2**：跨视角目标对齐与视觉运动策略的仿真训练。[[Paper](https://arxiv.org/abs/2503.02505)] [[Homepage](https://craftjarvis.github.io/ROCKET-2/)]

## 相关研究

| 工作 | 说明 |
|---|---|
| VLM Can Be a Good Assistant（IROS 2025） | 用自我改进的 VLM 增强具身视觉追踪 |
| TrackVLA（CoRL 2025） | 野外具身视觉追踪的 VLA 模型 |
| TrackVLA++（ICRA 2026） | 释放 VLA 模型在具身视觉追踪中的推理与记忆能力 |

> 💡 详细 VLM 智能体的接入与评测流程待补充，可参考上述论文与 EmbRACE-3K 基准。
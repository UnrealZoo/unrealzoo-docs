# Active Visual Tracking

✨We use embodied visual tracking tasks to benchmark embodied vision agents in complex dynamic environments.

## Introduction:

Embodied visual tracking is a challenging task that requires an agent to dynamically follow a moving target within a 3D environment, leveraging first-person vision and continuous interaction with the surroundings. We rely on the UnrealZoo platform to benchmark agents under realistic, ever-changing conditions to assess their robustness, adaptability, and generalization across diverse scenes.

UnrealZoo provides a wide collection of photorealistic, richly varied environments, as the playground for embodied AI agents. The diversity of settings and agents enables researchers to push embodied AI to new levels of capability, testing in scenarios that go beyond simple indoor navigation.

### UnrealZoo Key Features for Embodied Visual Tracking

- **Photo-realistic Dynamic Environments:** Designed to simulate a range of real-world challenges, including occlusions, dynamic lighting, irregular terrains, and multi-level structures.

- **Multi-Agent Scenarios:** Agents must navigate and track targets in dynamic settings with multiple moving agents and objects, promoting collaborative tracking for applications like rescue missions or surveillance.

- **Customizable Environment APIs:** Our improved API makes it easy for users to set up complex tracking tasks and interactions between the agent and its environment, including time dilation wrappers for control frequency tuning.

- **Data Collection API:** Users can collect visual datasets directly from the environment using UnrealCV+ with color, object masks, surface normals, and depth data capture.

## Evaluate Tracking Agents in UnrealZoo

Below are examples of the tracking agents' first-person views in four kinds of scenes:

📌Interior Scenes:

Agents deal with frequent low-level obstacles and narrow pathways, testing their occlusion handling and precise movements.

![Offline UndergroundParking](assets/avt_interior_1.gif)

![Offline Bunker](assets/avt_interior_2.gif)

![LV Soul Cave](assets/avt_interior_3.gif)

![Offline Storagehouse](assets/avt_interior_4.gif)

📌Palaces:

Agents face multi-level structures and intricate designs, where mastering spatial awareness is essential.

![Brass Gardens](assets/avt_palaces_1.gif)

![Eastern Garden](assets/avt_palaces_2.gif)

![Offline Western Garden](assets/avt_palaces_3.gif)

![Offline Modular SciFi Season](assets/avt_palaces_4.gif)

📌Wilds:

Irregular terrains and changing light conditions simulate outdoor tracking under unpredictable conditions.

![Output](assets/avt_wilds_1.gif)

![Offline Greek Island](assets/avt_wilds_2.gif)

![EF Gus](assets/avt_wilds_3.gif)

![Offline SnowMap](assets/avt_wilds_4.gif)

📌Modern Scenes:

These high-fidelity scenes represent real-world environments, such as Factories and parking lots, requiring agents to adapt to detailed and dense surroundings.

![Offline Industrial Area](assets/avt_modern_1.gif)

![Offline Downtown West](assets/avt_modern_2.gif)

![ContainerYard Day](assets/avt_modern_3.gif)

![Offline Suburb](assets/avt_modern_4.gif)


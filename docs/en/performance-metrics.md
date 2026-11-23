# Performance Metrics

| Metric | Value | Description |
|------|------|------|
| **Scene Scale** | 16 km² | Maximum single scene area |
| **Scene Count** | 100+ | Pre-built photo-realistic scenes |
| **Agent Count** | 10+ | Real-time interaction in same scene |
| **Standard Capture Throughput** | 53.46 FPS at 2K; 29.59 FPS at 4K | Camera-capture throughput benchmark; up to 6.31× speedup |
| **Serialized End-to-End Acquisition** | 22.40 FPS at 2K; 16.25 FPS at 4K | Complete serialized acquisition benchmark; not the full Gym step rate |
| **Physics Engine** | Chaos | Native physics in the current UE5.7 package |
| **Package Size** | ~70 GB | Recommended v3.1 UE5.7 full package |
| **Download Channels** | ModelScope + Hugging Face | Primary package mirrors |

Capture-throughput and serialized end-to-end values measure different parts of
the observation workflow and should not be compared as the same metric. Actual
Gym step performance also depends on the scene, enabled modalities, agent count,
and hardware. See the [v3.1 changelog](doc/CHANGELOG_v3.1.md) for the recorded
benchmark scope.

---

# New NuGet packages

Hourly lists of packages newly created on
[nuget.org](https://www.nuget.org/), built from the [v3 catalog](
https://api.nuget.org/v3/catalog0/index.json) of every package operation
nuget.org publishes. Each package touched in the window is checked against
its registration index, whose earliest `published` timestamp decides whether
the package was created inside the window.
A GitHub Actions workflow runs every hour, fetches the packages created since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-nuget-packages-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-23 16:18 UTC

New packages created between 2026-11-23 15:22 UTC and 2026-11-23 16:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-23T16-18-56-938683Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-23 15:26:07 | [StudioElf.SiteAgent.Contracts](https://www.nuget.org/packages/StudioElf.SiteAgent.Contracts) | 1.1.0 | StudioElf | Contract SDK for StudioElf SiteAgent module-data providers. Implement ISiteAgen… |
| 2026-11-23 15:37:53 | [Paradise.Encore](https://www.nuget.org/packages/Paradise.Encore) | 0.1.2 | ParadiseEngine | A dependency-free .NET audio engine for games: a 48 kHz stereo mixer for a tabl… |
| 2026-11-23 15:37:56 | [Paradise.Encore.Sdl](https://www.nuget.org/packages/Paradise.Encore.Sdl) | 0.1.2 | ParadiseEngine | SDL3 device output for Paradise.Encore: plays the mixer through the default pla… |
| 2026-11-23 15:39:04 | [AIKernel.Providers.Flux.Cuda](https://www.nuget.org/packages/AIKernel.Providers.Flux.Cuda) | 0.1.5 | Takuya Sogawa | Windows x64 FLUX.2 klein 4B prompt image editing on NVIDIA CUDA with AIKernel-b… |
| 2026-11-23 15:54:36 | [Esatto.Umbraco.Backoffice.Build](https://www.nuget.org/packages/Esatto.Umbraco.Backoffice.Build) | 1.0.0 | Carl Schéle | Build for Umbraco: a Content-section dashboard that shows which build is deploy… |
| 2026-11-23 15:57:35 | [ChunkShift.Patching](https://www.nuget.org/packages/ChunkShift.Patching) | 0.1.1 | MrFr3di | Verified binary patches over ChunkShift manifests: reuse planning, CSP patch cr… |
| 2026-11-23 15:57:59 | [Ambysto.Kit.License](https://www.nuget.org/packages/Ambysto.Kit.License) | 0.1.2 | Ambysto | Offline verification of Ambysto license keys (format 1): AMB- key texts and .am… |
| 2026-11-23 15:59:02 | [Ambysto.Kit.Safety](https://www.nuget.org/packages/Ambysto.Kit.Safety) | 0.2.0 | Ambysto | The file-safety gate for Ambysto apps on Windows: decides whether an item may b… |
| 2026-11-23 16:08:30 | [VisionFlow.Core](https://www.nuget.org/packages/VisionFlow.Core) | 1.0.0 | VisualStudio | VisionFlow 核心模型、DAG 调度与运行引擎接口。 |
| 2026-11-23 16:08:37 | [VisionFlow.Data](https://www.nuget.org/packages/VisionFlow.Data) | 1.0.0 | VisualStudio | VisionFlow 数据层：日志、运行历史与本地存储。 |
| 2026-11-23 16:08:40 | [VisionFlow.Algorithms](https://www.nuget.org/packages/VisionFlow.Algorithms) | 1.0.0 | VisualStudio | VisionFlow 算法节点集合：匹配、检测、测量、标定、脚本与深度学习。 |
| 2026-11-23 16:08:43 | [VisionFlow.Engine](https://www.nuget.org/packages/VisionFlow.Engine) | 1.0.0 | VisualStudio | VisionFlow 工作流运行引擎：检查点、断点续跑与节点执行。 |
| 2026-11-23 16:08:45 | [VisionFlow.Sdk](https://www.nuget.org/packages/VisionFlow.Sdk) | 1.0.0 | VisualStudio | VisionFlow 视觉工作流 SDK：加载工作流 JSON、运行整条流程或单个节点，并以 VisionResultData 形式返回单个或多个结构化视觉结… |
| 2026-11-23 16:10:13 | [Metano.Build.TypeScript](https://www.nuget.org/packages/Metano.Build.TypeScript) | 3.0.0 | Daniel Ferreira Monteiro Alves | MSBuild integration for the Metano TypeScript target — automatically transpiles… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

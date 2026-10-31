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

## Latest list — 2026-10-31 15:20 UTC

New packages created between 2026-10-31 14:20 UTC and 2026-10-31 15:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-31T15-20-49-260646Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-31 14:25:41 | [VisionAnnotation](https://www.nuget.org/packages/VisionAnnotation) | 1.0.0 | VisionFlow | 视觉标注显示库：检测框/引线文字自动避让布局（LabelLayout）、繁忙度栅格（BusyMap）、 离屏渲染（VisionRenderer）、交互控件（V… |
| 2026-10-31 14:35:54 | [Bazicalculator.UrlTools](https://www.nuget.org/packages/Bazicalculator.UrlTools) | 0.1.0 | wangneo276-lgtm | Free BaZi calculator: Four Pillars, Day Master, Ten Gods, Five Elements and Luc… |
| 2026-10-31 14:52:17 | [JYPPX.ROCm.MIGraphX.CSharp.API](https://www.nuget.org/packages/JYPPX.ROCm.MIGraphX.CSharp.API) | 0.0.1 | Guojin Yan | Managed bindings and resource wrappers for the AMD MIGraphX C API. Native MIGra… |
| 2026-10-31 14:52:18 | [JYPPX.ROCm.MIGraphX.CSharp.API.HIP.Interop](https://www.nuget.org/packages/JYPPX.ROCm.MIGraphX.CSharp.API.HIP.Interop) | 0.0.1 | Guojin Yan | Optional resource-safe native async adapter between the MIGraphX and HIP manage… |
| 2026-10-31 14:55:08 | [AgentSessions](https://www.nuget.org/packages/AgentSessions) | 0.1.0 | James Burton | List, resume, clean up, label and transfer coding-agent sessions across Claude,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-15 09:21 UTC

New packages created between 2026-11-15 08:19 UTC and 2026-11-15 09:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-15T09-21-58-181371Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-15 08:35:30 | [Laranet.Admin](https://www.nuget.org/packages/Laranet.Admin) | 0.4.0 | TheJavaZ | Provider-neutral contracts for an optional Laranet administrative surface. |
| 2026-11-15 08:35:31 | [Laranet.Admin.AspNetCore](https://www.nuget.org/packages/Laranet.Admin.AspNetCore) | 0.4.0 | TheJavaZ | Experimental Razor Pages integration for Laranet administrative resources. |
| 2026-11-15 08:35:32 | [Laranet.Admin.EntityFrameworkCore](https://www.nuget.org/packages/Laranet.Admin.EntityFrameworkCore) | 0.4.0 | TheJavaZ | Experimental EF Core adapter for Laranet administrative resources. |
| 2026-11-15 08:43:41 | [Tubatools.MacSkin](https://www.nuget.org/packages/Tubatools.MacSkin) | 1.1.0 | 机械 | 全新 macOS 风格应用外壳：玻璃侧栏、胶囊工具栏、工具图标资料库、搜索、收藏及可恢复的宿主页面挂载。 |
| 2026-11-15 08:45:51 | [KvNode.Client](https://www.nuget.org/packages/KvNode.Client) | 0.2.0 | Eli Belash | .NET client for KvNode, the gRPC key-value server written in x86-64 assembly: G… |
| 2026-11-15 09:03:45 | [TranscriptDock](https://www.nuget.org/packages/TranscriptDock) | 0.1.0 | Transcript Dock | Client for the Transcript Dock video transcription API. |
| 2026-11-15 09:08:49 | [EasyImageSharp.Avif](https://www.nuget.org/packages/EasyImageSharp.Avif) | 1.3.0 | Farhan Lodi | Optional native AVIF decoder and encoder for EasyImageSharp, powered by libavif… |
| 2026-11-15 09:17:11 | [ReactiveUI.Binding.Maui.Reactive](https://www.nuget.org/packages/ReactiveUI.Binding.Maui.Reactive) | 10.0.0 | Glenn Watson | MAUI platform support for ReactiveUI.Binding.Reactive, for consumers on System.… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

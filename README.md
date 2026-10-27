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

## Latest list — 2026-10-27 06:21 UTC

New packages created between 2026-10-27 05:20 UTC and 2026-10-27 06:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-27T06-21-14-867755Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-27 05:20:39 | [DemoViewer.NET.Extensions.Sdk](https://www.nuget.org/packages/DemoViewer.NET.Extensions.Sdk) | 2.0.2 | sid2934 | Build extensions for DemoViewer.NET: tabs, demo passes and jobs, 2D Playback co… |
| 2026-10-27 05:20:40 | [DemoViewer.NET.Extensions.Sdk.Ui](https://www.nuget.org/packages/DemoViewer.NET.Extensions.Sdk.Ui) | 2.0.2 | sid2934 | Controls, theme token names and style class names for DemoViewer.NET extension… |
| 2026-10-27 05:23:07 | [Acplite.Pty](https://www.nuget.org/packages/Acplite.Pty) | 0.2.0 | Cristi Pufu | Cross-platform pseudo-terminal (POSIX PTY and Windows ConPTY) wrapper, TUI prom… |
| 2026-10-27 05:52:31 | [DemoViewer.NET.Modules.Abstractions](https://www.nuget.org/packages/DemoViewer.NET.Modules.Abstractions) | 2.0.2 | sid2934 | The read-only playback contract DemoViewer.NET extensions and modules see. Inst… |
| 2026-10-27 05:52:32 | [DemoViewer.NET.Playback2D.Scene](https://www.nuget.org/packages/DemoViewer.NET.Playback2D.Scene) | 2.0.2 | sid2934 | The 2D map scene of DemoViewer.NET: the frame, the layer contract, floors and p… |
| 2026-10-27 06:12:32 | [alanxinn.DenglinOnnxBuilder](https://www.nuget.org/packages/alanxinn.DenglinOnnxBuilder) | 0.1.4 | alanxinn | Managed C# API that invokes Denglin nnexec to convert ONNX models to serialized… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-23 01:22 UTC

New packages created between 2026-10-23 00:18 UTC and 2026-10-23 01:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-23T01-22-00-276611Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-23 00:35:58 | [Pitwall.AspNetCore](https://www.nuget.org/packages/Pitwall.AspNetCore) | 0.1.0 | Ivo Braatz | Connects an ASP.NET Core product to Pitwall: the support bridge, server error r… |
| 2026-10-23 00:51:15 | [Xcellerator.Forge](https://www.nuget.org/packages/Xcellerator.Forge) | 1.0.132 | KyaMedia | Forge capture and content-seed tool for Xcellerator. |
| 2026-10-23 00:51:17 | [Xcellerator.Forge.Engine](https://www.nuget.org/packages/Xcellerator.Forge.Engine) | 1.0.132 | KyaMedia | Forge document, compose, and asset services used by Xcellerator.Admin. |
| 2026-10-23 00:51:19 | [Xcellerator.Mcp](https://www.nuget.org/packages/Xcellerator.Mcp) | 1.0.132 | KyaMedia | Repository-local Xcellerator engineering assistant. |
| 2026-10-23 00:52:38 | [DGZ.PhotinoBlazor.App](https://www.nuget.org/packages/DGZ.PhotinoBlazor.App) | 1.0.0 | DGZ | 基于 PhotinoX.Blazor 5.3.5 的跨平台 Blazor 桌面应用模板，支持 Windows / macOS / Linux。 |
| 2026-10-23 00:53:23 | [Microsoft.CognitiveServices.Speech.Extension.MAS.AEC.Model](https://www.nuget.org/packages/Microsoft.CognitiveServices.Speech.Extension.MAS.AEC.Model) | 1.53.0 | Microsoft | This NuGet package provides the Microsoft Audio Stack Acoustic Echo Cancellatio… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

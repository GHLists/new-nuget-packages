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

## Latest list — 2026-11-18 06:20 UTC

New packages created between 2026-11-18 05:20 UTC and 2026-11-18 06:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-18T06-20-11-22318Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-18 05:30:08 | [Syncfusion.AspNetCore.PptxEditor](https://www.nuget.org/packages/Syncfusion.AspNetCore.PptxEditor) | 35.2.12 | Syncfusion Inc. | Syncfusion® ASP.NET Core PPTX Editor wraps the EJ2 PowerPoint Editor for viewin… |
| 2026-11-18 05:42:56 | [Exchange56.VideoPlaylist.Components.Server](https://www.nuget.org/packages/Exchange56.VideoPlaylist.Components.Server) | 1.0.0 | T.J. McNaboe | Server endpoints and methods for integrating with Exchange56 Video Playlist cli… |
| 2026-11-18 05:50:34 | [NeoUII.Blazor](https://www.nuget.org/packages/NeoUII.Blazor) | 1.0.67 | NeoAdmin | NeoUII.Blazor 的基础框架骨架。 |
| 2026-11-18 05:50:35 | [NeoUII.Templates](https://www.nuget.org/packages/NeoUII.Templates) | 1.0.67 | NeoAdmin | NeoUII 的 dotnet new 项目模板，用于快速创建基于 Blazor Server、NeoUI 与 FreeSql 的后台管理项目。 |
| 2026-11-18 06:12:07 | [CutsceneML.Compiler](https://www.nuget.org/packages/CutsceneML.Compiler) | 0.0.1 | CutsceneML.Compiler | Package Description |
| 2026-11-18 06:12:07 | [CutsceneML.Parser](https://www.nuget.org/packages/CutsceneML.Parser) | 0.0.1 | CutsceneML.Parser | Package Description |
| 2026-11-18 06:12:08 | [CutsceneML.Model](https://www.nuget.org/packages/CutsceneML.Model) | 0.0.1 | CutsceneML.Model | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

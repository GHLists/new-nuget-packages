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

## Latest list — 2026-10-23 11:20 UTC

New packages created between 2026-10-23 10:20 UTC and 2026-10-23 11:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-23T11-20-19-200623Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-23 10:24:52 | [Frontmatec.Net.SqlServer.SqlClient](https://www.nuget.org/packages/Frontmatec.Net.SqlServer.SqlClient) | 2.0.7 | Frontmatec | Forwards the changes of a Frontmatec.Net.SqlServer endpoint to a SQL Server, th… |
| 2026-10-23 10:46:54 | [EluciusFTW.Tui48](https://www.nuget.org/packages/EluciusFTW.Tui48) | 0.1.4 | Guy Buss | A 2048-style sliding tile game as an Elmish component: host it in any SpectreTu… |
| 2026-10-23 10:57:59 | [ZYC.Framework.Modules.TilePyramid](https://www.nuget.org/packages/ZYC.Framework.Modules.TilePyramid) | 1.0.0 | ZYC.Framework.Modules.TilePyr… | Package Description |
| 2026-10-23 10:58:12 | [ZYC.Framework.Modules.TilePyramid.Abstractions](https://www.nuget.org/packages/ZYC.Framework.Modules.TilePyramid.Abstractions) | 1.0.0 | ZYC.Framework.Modules.TilePyr… | Package Description |
| 2026-10-23 11:01:45 | [NArchitecture.Core.Mediator](https://www.nuget.org/packages/NArchitecture.Core.Mediator) | 2.0.0 | Kodlama.io, Contributors | Lightweight, dependency-free mediator (request/response, streaming and pipeline… |
| 2026-10-23 11:04:03 | [Plagx.Preflight](https://www.nuget.org/packages/Plagx.Preflight) | 0.1.2 | Plagiarism Checker X | Free draft checker for .NET: word count, citation and reference list checks, pu… |
| 2026-10-23 11:12:54 | [Byta.Bindings](https://www.nuget.org/packages/Byta.Bindings) | 0.1.0 | Hub-Game-develop | 由 Khronos gl.xml 生成的 OpenGL 绑定：2651 条命令编译成 delegate* unmanaged 函数指针字段（无 DllImpo… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-27 02:20 UTC

New packages created between 2026-10-27 01:21 UTC and 2026-10-27 02:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-27T02-20-43-249924Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-27 01:31:21 | [ParkSquare.BotProtection](https://www.nuget.org/packages/ParkSquare.BotProtection) | 1.0.0 | Jon Meesam | ASP.NET Core middleware that tarpits known bots and temporarily blocks IP addre… |
| 2026-10-27 01:37:00 | [TianWeiToolsPro.Vision](https://www.nuget.org/packages/TianWeiToolsPro.Vision) | 3.2.3 | LaiTianWei | Windows x64 视觉算法与 WPF 窗口显示库，含配套原生依赖。 |
| 2026-10-27 01:46:32 | [Boutquin.Storage.SourceGenerator](https://www.nuget.org/packages/Boutquin.Storage.SourceGenerator) | 2.0.0 | Pierre G. Boutquin | Roslyn source generator that emits ISerializable<T> and IColumnarSegmentFormat<… |
| 2026-10-27 02:01:46 | [PyConductor](https://www.nuget.org/packages/PyConductor) | 0.1.0 | honey the codewitch | A library for automating a python3 environment |
| 2026-10-27 02:02:26 | [Spoolbit](https://www.nuget.org/packages/Spoolbit) | 0.0.1 | Spoolbit | Official .NET SDK for the Spoolbit cloud printing API (coming soon). |
| 2026-10-27 02:09:31 | [Witcher3StringEditor.MCP](https://www.nuget.org/packages/Witcher3StringEditor.MCP) | 0.1.0-beta | Witcher3StringEditor.MCP | MCP server for reading and editing The Witcher 3 .w3strings localization files. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

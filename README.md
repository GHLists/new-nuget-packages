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

## Latest list — 2026-10-17 04:18 UTC

New packages created between 2026-10-17 03:18 UTC and 2026-10-17 04:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-17T04-18-44-43808Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-17 03:19:05 | [NTDLS.Localization](https://www.nuget.org/packages/NTDLS.Localization) | 1.0.1 | NetworkDLS | Localization from a SQLite translation database: one row per phrase, one column… |
| 2026-10-17 03:29:18 | [Opsiva.Arabulucu](https://www.nuget.org/packages/Opsiva.Arabulucu) | 1.0.2 | Opsiva | Uygulama içi istek/bildirim arabulucusu (mediator): istekler ve işleyicileri, b… |
| 2026-10-17 03:47:42 | [Annotype](https://www.nuget.org/packages/Annotype) | 0.1.0 | Sebastien Ros | Move invariants from instances to types. Compile-time enforced, reflection-free… |
| 2026-10-17 04:13:40 | [Meteion.WpfTesting.Mcp](https://www.nuget.org/packages/Meteion.WpfTesting.Mcp) | 0.1.0 | Meteion | An MCP server that lets AI agents drive a WPF application through UI Automation… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

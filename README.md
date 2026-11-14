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

## Latest list — 2026-11-14 03:20 UTC

New packages created between 2026-11-14 02:19 UTC and 2026-11-14 03:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-14T03-20-59-879131Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-14 03:03:25 | [WitchC.Logging.Serilog](https://www.nuget.org/packages/WitchC.Logging.Serilog) | 1.6.1 | ingkele-鳄鳄🐊 | WitchC 框架 Serilog 集成模块，提供操作日志的 Serilog 持久化实现 |
| 2026-11-14 03:11:11 | [PureGate.WebSocket](https://www.nuget.org/packages/PureGate.WebSocket) | 1.0.0 | Ahmed Yasin Koculu | Typed messaging between ASP.NET Core and browsers over WebSockets, with the dep… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

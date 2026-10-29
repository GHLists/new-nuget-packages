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

## Latest list — 2026-10-29 11:21 UTC

New packages created between 2026-10-29 10:21 UTC and 2026-10-29 11:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-29T11-21-24-277904Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-29 10:28:09 | [DepthAI.Net.Runtime.win-x64](https://www.nuget.org/packages/DepthAI.Net.Runtime.win-x64) | 0.3.0 | Gravicode Studios | Runtime native DepthAI.Net untuk Windows x64: shim depthai-c di atas depthai-co… |
| 2026-10-29 10:35:00 | [Tapline.Grid.ChalkQL](https://www.nuget.org/packages/Tapline.Grid.ChalkQL) | 0.2.0 | Mark Hammond | LiveGrid bolted onto a database and its stream through ChalkQL: the store's pag… |
| 2026-10-29 10:37:35 | [BattleMetrics.Net.DependencyInjection](https://www.nuget.org/packages/BattleMetrics.Net.DependencyInjection) | 1.0.0 | collect_vood | Registers the BattleMetrics.Net client with Microsoft.Extensions.DependencyInje… |
| 2026-10-29 10:37:35 | [BattleMetrics.Net](https://www.nuget.org/packages/BattleMetrics.Net) | 1.0.0 | collect_vood | High throughput BattleMetrics API client with built-in rate limiting and reques… |
| 2026-10-29 10:40:55 | [VehicleVision.PleasanterTools.DotNetClient](https://www.nuget.org/packages/VehicleVision.PleasanterTools.DotNetClient) | 0.1.0 | PMC Co., Ltd. IT Solution Div. | Pleasanter の標準 Web API を呼ぶ .NET 向けクライアントライブラリ。 |
| 2026-10-29 10:53:51 | [AppWeaver.QRGenerator](https://www.nuget.org/packages/AppWeaver.QRGenerator) | 1.0.0 | Team AppWeaver | Abstract QR code generation component for AppWeaver. |
| 2026-10-29 10:58:15 | [DotnetAgentKit](https://www.nuget.org/packages/DotnetAgentKit) | 0.1.0 | Dimitri Mamulashvili | dotnet new template that adds Claude Code config (CLAUDE.md, rules, skills, age… |
| 2026-10-29 10:58:24 | [AppWeaver.QRGenerator.QRCoder](https://www.nuget.org/packages/AppWeaver.QRGenerator.QRCoder) | 1.0.0 | Team AppWeaver | QR code generation component for AppWeaver using QRCoder library. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

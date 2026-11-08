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

## Latest list — 2026-11-08 08:20 UTC

New packages created between 2026-11-08 07:18 UTC and 2026-11-08 08:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-08T08-20-15-702418Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-08 07:27:13 | [IraqAdminDivisions](https://www.nuget.org/packages/IraqAdminDivisions) | 1.0.1 | Ammar Kamil | Iraq's governorates, districts and sub-districts in Arabic, English and Kurdish… |
| 2026-11-08 07:27:13 | [IraqAdminDivisions.Boundaries](https://www.nuget.org/packages/IraqAdminDivisions.Boundaries) | 1.0.1 | Ammar Kamil | Offline GPS point to Iraqi sub-district, district and governorate lookup for Ir… |
| 2026-11-08 07:27:14 | [IraqAdminDivisions.AspNetCore](https://www.nuget.org/packages/IraqAdminDivisions.AspNetCore) | 1.0.1 | Ammar Kamil | ASP.NET Core Minimal API endpoints for IraqAdminDivisions: one call to MapIraqD… |
| 2026-11-08 07:45:43 | [Findx.Extensions.Scheduler](https://www.nuget.org/packages/Findx.Extensions.Scheduler) | 11.1.2026.1111 | Findx.Extensions.Scheduler | Findx分布式任务调度扩展组件（Master选举 + Worker能力注册 + HTTP分发） |
| 2026-11-08 08:01:50 | [EncompassApiRest](https://www.nuget.org/packages/EncompassApiRest) | 1.0.1 | EncompassApiRest | A .NET client for the ICE Encompass REST API, including loan contracts, standar… |
| 2026-11-08 08:04:40 | [M0LTE.S5066.Client](https://www.nuget.org/packages/M0LTE.S5066.Client) | 0.1.0 | Tom Fanning M0LTE | A .NET client for the STANAG 5066 Edition 4 Subnetwork Interface Sublayer over… |
| 2026-11-08 08:04:41 | [M0LTE.S5066.Host](https://www.nuget.org/packages/M0LTE.S5066.Host) | 0.1.0 | Tom Fanning M0LTE | Hosts one STANAG 5066 Edition 4 node in real time: the SIS server on TCP 5066 (… |
| 2026-11-08 08:04:42 | [M0LTE.S5066.Core](https://www.nuget.org/packages/M0LTE.S5066.Core) | 0.1.0 | Tom Fanning M0LTE | The sans-IO core of a STANAG 5066 Edition 4 implementation: deterministic proto… |
| 2026-11-08 08:13:20 | [Mafesoft.PlainTextReport](https://www.nuget.org/packages/Mafesoft.PlainTextReport) | 1.0.0 | Federico Mazzanti | PlainTextReport is a .NET library to generate a plain text report from a collec… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

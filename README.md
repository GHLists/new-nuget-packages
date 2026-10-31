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

## Latest list — 2026-10-31 10:20 UTC

New packages created between 2026-10-31 09:21 UTC and 2026-10-31 10:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-31T10-20-40-007086Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-31 09:26:02 | [FlowOrchestrator.OpenTelemetry](https://www.nuget.org/packages/FlowOrchestrator.OpenTelemetry) | 1.34.1 | FlowOrchestrator Contributors | One-call OpenTelemetry wiring for FlowOrchestrator: traces, metrics and logs (w… |
| 2026-10-31 09:29:19 | [DubUrl.Provider.DuckDb.Native](https://www.nuget.org/packages/DubUrl.Provider.DuckDb.Native) | 0.54.0 | Cédric L. Charlier | Native DuckDB encrypted connection initialization for DubUrl. |
| 2026-10-31 09:30:00 | [Rulealize.RuleSet.Calculator](https://www.nuget.org/packages/Rulealize.RuleSet.Calculator) | 1.0.0 | Reny | A scientific calculator: brackets, powers, sin, cos and tan in degrees or radia… |
| 2026-10-31 09:30:13 | [Mnemosyne.NET.Sentinel](https://www.nuget.org/packages/Mnemosyne.NET.Sentinel) | 0.5.0 | Marcel Roozekrans | A capture guard that runs AI.Sentinel's detectors before a Reasonlet is stored. |
| 2026-10-31 09:33:10 | [Promptuarium.Serializer](https://www.nuget.org/packages/Promptuarium.Serializer) | 8.1.0 | Fuszenecker Róbert | A general serializer between .NET objects and Promptuarium trees in the PRMT:CF… |
| 2026-10-31 09:34:00 | [Cratis.Showrunner.Marquee.Contracts](https://www.nuget.org/packages/Cratis.Showrunner.Marquee.Contracts) | 1.3.0 | Cratis | The event contracts for Marquee — the Showrunner announcements part: the public… |
| 2026-10-31 09:35:53 | [Cratis.Showrunner.BoxOffice.Catalog](https://www.nuget.org/packages/Cratis.Showrunner.BoxOffice.Catalog) | 1.3.0 | Cratis | The Box Office catalog — the offers a managed product sells (seat plans, module… |
| 2026-10-31 09:52:10 | [NETQBOT.Contracts](https://www.nuget.org/packages/NETQBOT.Contracts) | 1.0.0 | HUI | 一个基于C#构建的QQ机器人框架，可以使用WebSocket和WebHook进行连接 |
| 2026-10-31 09:53:03 | [VietQR.Deeplink.Client](https://www.nuget.org/packages/VietQR.Deeplink.Client) | 1.0.1 | Hien Dev | Thư viện client C# (.NET) kết nối dịch vụ VietQR Deeplink để lấy link mở ứng dụ… |
| 2026-10-31 09:53:16 | [EssaLab.Zid](https://www.nuget.org/packages/EssaLab.Zid) | 1.0.0 | Reda Essa | Enterprise-Grade Distributed ID Generator (High-Performance, Zero-Allocation, T… |
| 2026-10-31 09:54:10 | [EssaLab.Zid.EntityFramework](https://www.nuget.org/packages/EssaLab.Zid.EntityFramework) | 1.0.0 | Reda Essa | Entity Framework Core value converters and conventions for EssaLab.Zid. |
| 2026-10-31 09:54:36 | [EssaLab.Zid.Extensions.DependencyInjection](https://www.nuget.org/packages/EssaLab.Zid.Extensions.DependencyInjection) | 1.0.0 | Reda Essa | Dependency Injection extensions for EssaLab.Zid ID generator. |
| 2026-10-31 10:01:42 | [BlindVault.SDK.Generated](https://www.nuget.org/packages/BlindVault.SDK.Generated) | 0.1.0 | BlindVault | Generated BlindVault REST API client |
| 2026-10-31 10:01:43 | [BlindVault.SDK](https://www.nuget.org/packages/BlindVault.SDK) | 0.1.0 | BlindVault | BlindVault local encryption, RSA key sharing and encrypted Library API operatio… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

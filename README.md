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

## Latest list — 2026-10-23 02:21 UTC

New packages created between 2026-10-23 01:22 UTC and 2026-10-23 02:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-23T02-21-39-198495Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-23 01:26:30 | [Acme.LabHub.Contracts](https://www.nuget.org/packages/Acme.LabHub.Contracts) | 0.0.1 | Tran Khac Tuan | LabHub multi-lab and team management framework: Contracts. |
| 2026-10-23 01:26:31 | [Acme.LabHub.Infrastructure](https://www.nuget.org/packages/Acme.LabHub.Infrastructure) | 0.0.1 | Tran Khac Tuan | LabHub multi-lab and team management framework: Infrastructure. |
| 2026-10-23 01:26:32 | [Acme.LabHub.Web](https://www.nuget.org/packages/Acme.LabHub.Web) | 0.0.1 | Tran Khac Tuan | LabHub multi-lab and team management framework: Web. |
| 2026-10-23 01:26:32 | [Acme.LabHub.Core](https://www.nuget.org/packages/Acme.LabHub.Core) | 0.0.1 | Tran Khac Tuan | LabHub multi-lab and team management framework: Core. |
| 2026-10-23 01:26:33 | [Acme.LabHub.Hosting](https://www.nuget.org/packages/Acme.LabHub.Hosting) | 0.0.1 | Tran Khac Tuan | LabHub multi-lab and team management framework: Hosting. |
| 2026-10-23 01:26:34 | [Acme.LabHub.UseCases](https://www.nuget.org/packages/Acme.LabHub.UseCases) | 0.0.1 | Tran Khac Tuan | LabHub multi-lab and team management framework: UseCases. |
| 2026-10-23 01:35:15 | [Base.Extensions](https://www.nuget.org/packages/Base.Extensions) | 1.0.3 | Can | Base 项目扩展库 |
| 2026-10-23 01:40:51 | [M0LTE.HfChannel](https://www.nuget.org/packages/M0LTE.HfChannel) | 0.1.0 | Tom Fanning M0LTE | An HF channel simulator for measuring modems: the Watterson tapped-delay-line m… |
| 2026-10-23 01:48:50 | [Dispattchr](https://www.nuget.org/packages/Dispattchr) | 1.0.5 | Dispattchr | lightweight dispatcher library for handling dispatchables and events in .NET ap… |
| 2026-10-23 01:56:17 | [A1Force.MauiObfuscate](https://www.nuget.org/packages/A1Force.MauiObfuscate) | 0.0.1 | A1Force | Rename obfuscator for .NET MAUI projects. Chooses types and members by source-f… |
| 2026-10-23 01:58:48 | [XT.S7netplus](https://www.nuget.org/packages/XT.S7netplus) | 1.0.0 | Derek Heiser,Michele Cattafes… | A continuation of Juergen1969's Siemens communication library. |
| 2026-10-23 02:13:16 | [Our.Umbraco.ConditionalDisplayers.Deploy](https://www.nuget.org/packages/Our.Umbraco.ConditionalDisplayers.Deploy) | 17.0.0-beta1 | Mario Lopez | Umbraco Deploy connector that transfers Conditional Displayers visibility rules… |
| 2026-10-23 02:13:16 | [Our.Umbraco.ConditionalDisplayers.uSync](https://www.nuget.org/packages/Our.Umbraco.ConditionalDisplayers.uSync) | 17.0.0-beta1 | Mario Lopez | uSync handler that exports and imports Conditional Displayers visibility rules. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

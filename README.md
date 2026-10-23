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

## Latest list — 2026-10-23 14:21 UTC

New packages created between 2026-10-23 13:23 UTC and 2026-10-23 14:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-23T14-21-24-667523Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-23 13:32:43 | [LM-Kit.NET.Backend.Cuda13.Windows.Part0](https://www.nuget.org/packages/LM-Kit.NET.Backend.Cuda13.Windows.Part0) | 2026.10.7 | LM-Kit Authors | Part of LM-Kit.NET.Backend.Cuda13.Windows, which references it: install LM-Kit.… |
| 2026-10-23 13:32:47 | [LM-Kit.NET.Backend.Cuda13.Windows.Part1](https://www.nuget.org/packages/LM-Kit.NET.Backend.Cuda13.Windows.Part1) | 2026.10.7 | LM-Kit Authors | Part of LM-Kit.NET.Backend.Cuda13.Windows, which references it: install LM-Kit.… |
| 2026-10-23 13:33:01 | [LM-Kit.NET.Backend.Cuda13.Linux.Part0](https://www.nuget.org/packages/LM-Kit.NET.Backend.Cuda13.Linux.Part0) | 2026.10.7 | LM-Kit Authors | Part of LM-Kit.NET.Backend.Cuda13.Linux, which references it: install LM-Kit.NE… |
| 2026-10-23 13:33:05 | [LM-Kit.NET.Backend.Cuda13.Linux.Part1](https://www.nuget.org/packages/LM-Kit.NET.Backend.Cuda13.Linux.Part1) | 2026.10.7 | LM-Kit Authors | Part of LM-Kit.NET.Backend.Cuda13.Linux, which references it: install LM-Kit.NE… |
| 2026-10-23 13:33:06 | [Soenneker.Twilio.Deactivations](https://www.nuget.org/packages/Soenneker.Twilio.Deactivations) | 4.0.2 | Jake Soenneker | A utility for working with Twilio phone number deactivations. |
| 2026-10-23 13:33:42 | [Engobe.Plugin.EmailProtect](https://www.nuget.org/packages/Engobe.Plugin.EmailProtect) | 2.0.0 | PepperPix | JS-obfuscated email protection Content-Plugin for Engobe static sites. |
| 2026-10-23 13:37:59 | [Kanject.Core.Events.Abstractions](https://www.nuget.org/packages/Kanject.Core.Events.Abstractions) | 0.1.0 | Akinsanya Omogbolahan | Kanject Core events abstractions — the transport-neutral contract a Library pub… |
| 2026-10-23 13:38:01 | [Kanject.Core.Events](https://www.nuget.org/packages/Kanject.Core.Events) | 0.1.0 | Akinsanya Omogbolahan | Kanject Core events — the in-process default IEventPublisher: handlers run befo… |
| 2026-10-23 13:38:03 | [Kanject.Core.Events.Annotations](https://www.nuget.org/packages/Kanject.Core.Events.Annotations) | 0.1.0 | Akinsanya Omogbolahan | Roslyn source generator for Kanject Core events — for each [EventTopic] type it… |
| 2026-10-23 13:38:05 | [Kanject.Core.Events.TestKit](https://www.nuget.org/packages/Kanject.Core.Events.TestKit) | 0.1.0 | Akinsanya Omogbolahan | Kanject Core events contract suite (xUnit): EventPublisherContractTests, the te… |
| 2026-10-23 13:38:46 | [Zhomfr.Validation.Rules.Files](https://www.nuget.org/packages/Zhomfr.Validation.Rules.Files) | 0.5.0 | zhuolyan (Oleg Zhuravskiy) | A powerful, intuitive collection of custom validation attributes built directly… |
| 2026-10-23 13:44:41 | [DotCelery.Abstractions](https://www.nuget.org/packages/DotCelery.Abstractions) | 1.1.0 | Aleksandr Pavlov | Abstractions, models, and configuration contracts for DotCelery |
| 2026-10-23 13:45:24 | [FeetCode](https://www.nuget.org/packages/FeetCode) | 0.1.0 | Ella Gyurkovská | Fetch public LeetCode user stats from F#. |
| 2026-10-23 13:58:25 | [TopCharge.Sdk](https://www.nuget.org/packages/TopCharge.Sdk) | 1.0.0 | TopCharge | Official .NET SDK for the TopCharge merchant API. |
| 2026-10-23 14:07:11 | [Tessera.WpfStyles](https://www.nuget.org/packages/Tessera.WpfStyles) | 0.1.0 | Timbuhtuk | Reusable Tessera themes, controls, typography and motion for .NET 8 WPF applica… |
| 2026-10-23 14:09:03 | [Bluehands.EventSourcing.Commands](https://www.nuget.org/packages/Bluehands.EventSourcing.Commands) | 1.1.0 | Implemented with 💙 by bluehan… | Functional command pattern for Bluehands.EventSourcing |
| 2026-10-23 14:10:39 | [Bluehands.EventSourcing.Persistence.Postgres](https://www.nuget.org/packages/Bluehands.EventSourcing.Persistence.Postgres) | 1.1.0 | Implemented with 💙 by bluehan… | PostgreSQL persistence for EventSourcing |
| 2026-10-23 14:15:23 | [Switchyard](https://www.nuget.org/packages/Switchyard) | 0.1.0 | Pekka Ylenius | Run the services you work on locally and route the rest to dev, staging or prod… |
| 2026-10-23 14:15:29 | [Stellaegis.Issuer.SqlServer](https://www.nuget.org/packages/Stellaegis.Issuer.SqlServer) | 5.1.0 | FRi | The SQL Server stores of Stellaegis.Issuer: the OpenIddict applications, author… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

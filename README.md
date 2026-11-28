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

## Latest list — 2026-11-28 12:21 UTC

New packages created between 2026-11-28 11:19 UTC and 2026-11-28 12:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-28T12-21-04-136266Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-28 11:38:24 | [SmartCore.IO](https://www.nuget.org/packages/SmartCore.IO) | 1.0.0 | SmartCore Contributors | Lightweight .NET I/O utilities for file, text, JSON, XML, and stream operations. |
| 2026-11-28 11:53:24 | [LongCatNetRuntime](https://www.nuget.org/packages/LongCatNetRuntime) | 0.0.2 | dongfangzhizhu | Python-free .NET 8 P/Invoke runtime for the LongCat 1.6 Video Avatar pipeline (… |
| 2026-11-28 11:55:23 | [Libo11y.Spec](https://www.nuget.org/packages/Libo11y.Spec) | 0.1.0 | James Ainslie | The libo11y telemetry specification for .NET: generated attribute, event and me… |
| 2026-11-28 11:55:25 | [Libo11y](https://www.nuget.org/packages/Libo11y) | 0.1.0 | James Ainslie | Opinionated observability for .NET built on OpenTelemetry: one-call setup of tr… |
| 2026-11-28 11:55:26 | [Libo11y.AspNetCore](https://www.nuget.org/packages/Libo11y.AspNetCore) | 0.1.0 | James Ainslie | libo11y instrumentation for ASP.NET Core and HttpClient: server middleware and… |
| 2026-11-28 11:55:27 | [Libo11y.Db](https://www.nuget.org/packages/Libo11y.Db) | 0.1.0 | James Ainslie | libo11y database client instrumentation for .NET: parent-gated client spans, sa… |
| 2026-11-28 11:55:28 | [Libo11y.Testing](https://www.nuget.org/packages/Libo11y.Testing) | 0.1.0 | James Ainslie | Hermetic test harness for libo11y on .NET: an in-memory recorder with conforman… |
| 2026-11-28 11:55:30 | [Libo11y.Cli](https://www.nuget.org/packages/Libo11y.Cli) | 0.1.0 | James Ainslie | The libo11y command line tool for .NET: `libo11y registry check FILE...` valida… |
| 2026-11-28 11:57:24 | [ToucanHub.EventStore.Outbox.ChannelBus](https://www.nuget.org/packages/ToucanHub.EventStore.Outbox.ChannelBus) | 1.0.0 | junglistkirss | Channel-based Outbox bus |
| 2026-11-28 11:57:25 | [ToucanHub.EventStore.Outbox.Client.Abstractions](https://www.nuget.org/packages/ToucanHub.EventStore.Outbox.Client.Abstractions) | 1.0.0 | junglistkirss | Outbox store client abstractions |
| 2026-11-28 11:57:26 | [ToucanHub.EventStore.Outbox.ReactiveBus](https://www.nuget.org/packages/ToucanHub.EventStore.Outbox.ReactiveBus) | 1.0.0 | junglistkirss | Reactive Outbox bus |
| 2026-11-28 11:57:28 | [ToucanHub.EventStore.Subscriptions.ChannelBus](https://www.nuget.org/packages/ToucanHub.EventStore.Subscriptions.ChannelBus) | 1.0.0 | junglistkirss | Channel-based subscription store observer bus |
| 2026-11-28 11:57:29 | [ToucanHub.EventStore.Subscriptions.ReactiveBus](https://www.nuget.org/packages/ToucanHub.EventStore.Subscriptions.ReactiveBus) | 1.0.0 | junglistkirss | Reactive subscription store observer bus |
| 2026-11-28 12:04:04 | [Surly.Surl.Console](https://www.nuget.org/packages/Surly.Surl.Console) | 0.1.13 | Stewart Scott Rogers | surl, the server-side mate of curl: for each request upstream curl makes, surl… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

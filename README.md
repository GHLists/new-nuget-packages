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

## Latest list — 2026-11-19 17:20 UTC

New packages created between 2026-11-19 16:20 UTC and 2026-11-19 17:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-19T17-20-08-066573Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-19 16:22:41 | [Papa.Test](https://www.nuget.org/packages/Papa.Test) | 1.0.0 | PAPA | Basic test package for account/ownership testing. |
| 2026-11-19 16:25:58 | [ElBruno.AI.Decisions.Foundry.Local](https://www.nuget.org/packages/ElBruno.AI.Decisions.Foundry.Local) | 0.9.0 | Bruno Capuano (ElBruno) | Provider-neutral typed decisions using cached decision models through the Micro… |
| 2026-11-19 16:27:17 | [miloRpc.Channels.Quic](https://www.nuget.org/packages/miloRpc.Channels.Quic) | 1.1.1-beta | Sergio Luis Para | QUIC-based channel for the miloRpc framework |
| 2026-11-19 16:31:42 | [SinkSharp.Sinks.Dashboard.Redis](https://www.nuget.org/packages/SinkSharp.Sinks.Dashboard.Redis) | 1.0.0 | SinkSharp | Redis Streams history for the SinkSharp dashboard. Every pod appends to one str… |
| 2026-11-19 16:45:52 | [DigiTFactory.Libraries.CrossCutting](https://www.nuget.org/packages/DigiTFactory.Libraries.CrossCutting) | 0.1.0 | DigiTFactory.Libraries.CrossC… | Cross-cutting resilience and health-check helpers for DigiTFactory EDM microser… |
| 2026-11-19 16:45:58 | [DigiTFactory.Libraries.Testing](https://www.nuget.org/packages/DigiTFactory.Libraries.Testing) | 0.1.0 | DigiTFactory.Libraries.Testing | Coverage-assertion helpers for DigiTFactory EDM microservices: verify every agg… |
| 2026-11-19 17:00:59 | [ForEach.Vat.Abstractions](https://www.nuget.org/packages/ForEach.Vat.Abstractions) | 0.1.0 | For-Each Smederevo | IVatNumberValidator: the vendor-neutral contract for checking a VAT number, wit… |
| 2026-11-19 17:01:00 | [ForEach.Vat.Vies](https://www.nuget.org/packages/ForEach.Vat.Vies) | 0.1.0 | For-Each Smederevo | VIES implementation of IVatNumberValidator: checks an EU VAT number against the… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-23 08:21 UTC

New packages created between 2026-10-23 07:20 UTC and 2026-10-23 08:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-23T08-21-14-989096Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-23 07:27:22 | [NuKnip](https://www.nuget.org/packages/NuKnip) | 0.1.0 | Harris Foster | A CI-friendly .NET tool that detects potentially unused top-level NuGet package… |
| 2026-10-23 07:38:12 | [BigSurCorp.Propus](https://www.nuget.org/packages/BigSurCorp.Propus) | 0.1.0 | BigSur Corp. | Official .NET client for Propus (BigSur Corp.) — SQL, cache, streams, objects a… |
| 2026-10-23 07:40:32 | [Bsft.Hosting.BackgroundWork](https://www.nuget.org/packages/Bsft.Hosting.BackgroundWork) | 2.2.0 | Bochmann Software GmbH | BSFT Framework background work without the web stack: run-once startup operatio… |
| 2026-10-23 07:42:50 | [XtremeIdiots.Redirect.Api.Client.Testing](https://www.nuget.org/packages/XtremeIdiots.Redirect.Api.Client.Testing) | 1.0.1 | XtremeIdiots | Thread-safe fake and DTO factory for XI Redirect Manager consumers. |
| 2026-10-23 07:42:51 | [XtremeIdiots.Redirect.Api.Abstractions.V1](https://www.nuget.org/packages/XtremeIdiots.Redirect.Api.Abstractions.V1) | 1.0.1 | XtremeIdiots | Version one contracts for XI Redirect Manager. |
| 2026-10-23 07:42:52 | [XtremeIdiots.Redirect.Api.Client.V1](https://www.nuget.org/packages/XtremeIdiots.Redirect.Api.Client.V1) | 1.0.1 | XtremeIdiots | Typed MX API client for XI Redirect Manager. |
| 2026-10-23 07:49:30 | [BeneficialStrategies.Iso20022.Messages.Records](https://www.nuget.org/packages/BeneficialStrategies.Iso20022.Messages.Records) | 1.0.0-alpha | Jeff Ward,Beneficial Strategi… | The records of every ISO 20022 message, component and choice, written at compil… |
| 2026-10-23 08:03:01 | [Glubus.MinaCalc](https://www.nuget.org/packages/Glubus.MinaCalc) | 1.0.0 | MinaCalc | .NET bindings for MinaCalc's stable Rust C ABI |
| 2026-10-23 08:10:23 | [Ansight.Pencil](https://www.nuget.org/packages/Ansight.Pencil) | 1.9.0 | Ansight AI | Optional, explicitly enabled Pencil input simulation for Ansight on iOS Simulat… |
| 2026-10-23 08:11:55 | [Yzl.Extensions.Cache.Redis](https://www.nuget.org/packages/Yzl.Extensions.Cache.Redis) | 0.2.0 | YZL | Redis backend for Yzl.Extensions.Cache |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

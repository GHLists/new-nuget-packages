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

## Latest list — 2026-11-19 12:19 UTC

New packages created between 2026-11-19 11:22 UTC and 2026-11-19 12:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-19T12-19-47-862153Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-19 11:25:06 | [Webority.Security.AzureMonitor](https://www.nuget.org/packages/Webority.Security.AzureMonitor) | 0.72.0 | Webority Technologies | Azure Monitor history store for Webority.Security audit events: one row per eve… |
| 2026-11-19 11:25:52 | [Webority.Retention.Abstractions](https://www.nuget.org/packages/Webority.Retention.Abstractions) | 0.5.0 | Webority Technologies | The contract a package implements to join a product's Webority.Retention run: I… |
| 2026-11-19 11:26:31 | [Moltaro.Signals.Hosting](https://www.nuget.org/packages/Moltaro.Signals.Hosting) | 0.1.0 | Bijou Solutions | Registers the Moltaro.Signals host, or a client of a host elsewhere, in a .NET… |
| 2026-11-19 11:26:32 | [Moltaro.Signals](https://www.nuget.org/packages/Moltaro.Signals) | 0.1.0 | Bijou Solutions | Remote signals with consumer groups for .NET: an in-memory host embedded in one… |
| 2026-11-19 11:51:01 | [Univedo.Data.Net48](https://www.nuget.org/packages/Univedo.Data.Net48) | 2.8.2.5 | Stefan Becker | Univedo.Data Class Library for .NET Framework 4.8 (streams, remote objects and… |
| 2026-11-19 12:03:13 | [PrintSharp.Html](https://www.nuget.org/packages/PrintSharp.Html) | 0.5.0 | ogisyouryuu | Standalone HTML export extensions for PrintSharp grid documents. |
| 2026-11-19 12:03:15 | [PrintSharp.Image](https://www.nuget.org/packages/PrintSharp.Image) | 0.5.0 | ogisyouryuu | PNG and lossless WebP page export for PrintSharp. |
| 2026-11-19 12:03:22 | [PrintSharp.Word](https://www.nuget.org/packages/PrintSharp.Word) | 0.5.0 | ogisyouryuu | Editable Word document export for PrintSharp. |
| 2026-11-19 12:06:14 | [PidginHost.Sdk](https://www.nuget.org/packages/PidginHost.Sdk) | 0.18.0 | PidginHost | Official .NET client for the PidginHost API |
| 2026-11-19 12:06:58 | [LSurac.Earwig.Client](https://www.nuget.org/packages/LSurac.Earwig.Client) | 0.1.0 | Leonard Surac | Client for the Earwig transcription service, plus ready-made proxy endpoints fo… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

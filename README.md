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

## Latest list — 2026-10-16 11:21 UTC

New packages created between 2026-10-16 10:20 UTC and 2026-10-16 11:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-16T11-21-25-436469Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-16 10:28:10 | [Arc56.Generated.sambhavverma2004.aircargo-provenance](https://www.nuget.org/packages/Arc56.Generated.sambhavverma2004.aircargo-provenance) | 1.0.1.2026101610 | sambhavverma2004 | Generated ARC-56 Algorand smart-contract clients for sambhavverma2004/aircargo-… |
| 2026-10-16 10:28:25 | [Arc56.Generated.joe-p.algosdk-future-ts](https://www.nuget.org/packages/Arc56.Generated.joe-p.algosdk-future-ts) | 1.0.1.2026101610 | joe-p | Generated ARC-56 Algorand smart-contract clients for joe-p/algosdk-future-ts. |
| 2026-10-16 10:36:18 | [AiDotNet.Evolution.Ptx](https://www.nuget.org/packages/AiDotNet.Evolution.Ptx) | 0.4.0 | AiDotNet.Evolution.Ptx | Optional PTX kernel evolution for AiDotNet.Evolution: contract-driven JIT check… |
| 2026-10-16 10:44:44 | [AlienFruit.Otml.Configuration.Keyraft](https://www.nuget.org/packages/AlienFruit.Otml.Configuration.Keyraft) | 1.3.0 | Alexander Prokopovich | Keyraft secrets storage adapter for AlienFruit.Otml.Configuration: resolves {{s… |
| 2026-10-16 10:48:05 | [StandardTrace](https://www.nuget.org/packages/StandardTrace) | 1.0.0 | Mario Kx | Records HTTP traces, logs, and metrics for .NET 10 applications. |
| 2026-10-16 10:52:20 | [AppWeaver.Helpers](https://www.nuget.org/packages/AppWeaver.Helpers) | 1.0.0 | Team AppWeaver | Helper utilities and common functions for the AppWeaver framework. Includes env… |
| 2026-10-16 11:00:48 | [UnicoreSoftwareSolutions.Base.Business.Interface](https://www.nuget.org/packages/UnicoreSoftwareSolutions.Base.Business.Interface) | 1.0.0 | Unicore Software Solutions | Package Description |
| 2026-10-16 11:01:00 | [Casper.Network.SDK.CES](https://www.nuget.org/packages/Casper.Network.SDK.CES) | 3.3.0 | make-software | Casper Event Standard (CES) schema and event parsing for the Casper .NET SDK. |
| 2026-10-16 11:02:39 | [Pdfxport.Net](https://www.nuget.org/packages/Pdfxport.Net) | 7.0.0 | Gaspard Petit | An MIT-licensed fork of PDFsharp for creating and processing PDF files. Indepen… |
| 2026-10-16 11:02:40 | [Pdfxport.Net.MigraDoc](https://www.nuget.org/packages/Pdfxport.Net.MigraDoc) | 7.0.0 | Gaspard Petit | MigraDoc document layout for the Pdfxport.Net PDFsharp fork. Independent MIT-li… |
| 2026-10-16 11:09:20 | [MinimalKafka.Dashboard](https://www.nuget.org/packages/MinimalKafka.Dashboard) | 0.18.0-alpha002 | Patrick Evers | MinimalKafka is a simple and efficient Kafka consumer library designed to work… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

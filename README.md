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

## Latest list — 2026-10-08 18:23 UTC

New packages created between 2026-10-08 17:20 UTC and 2026-10-08 18:23 UTC.

[Full CSV](data/new-nuget-packages-2026-10-08T18-23-36-129978Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-08 17:22:40 | [CognitiveForge.AgentSkills.Catalog](https://www.nuget.org/packages/CognitiveForge.AgentSkills.Catalog) | 0.1.0 | Cognitive Forge | Catalog views, package manifests, path safety, and validation for Agent Skills… |
| 2026-10-08 17:29:36 | [TapPayments.Net](https://www.nuget.org/packages/TapPayments.Net) | 1.0.1 | Eslam Ashraf,Github Contribut… | The missing .NET SDK for Tap Payments — the MENA payment gateway. Charges, auth… |
| 2026-10-08 17:29:48 | [Bosta.Net](https://www.nuget.org/packages/Bosta.Net) | 1.0.1 | SENESO | .NET SDK for the Bosta shipping API — create and track deliveries, manage picku… |
| 2026-10-08 17:30:02 | [TelnetNegotiationCore.Gmcp](https://www.nuget.org/packages/TelnetNegotiationCore.Gmcp) | 4.5.0 | harrycordewener | The standard GMCP packages for MUD clients and servers, starting with Core: Cor… |
| 2026-10-08 17:32:09 | [Splunk.Api](https://www.nuget.org/packages/Splunk.Api) | 10.6.32 | Panoramic Data Limited | A typed, modern .NET client for the Splunk Enterprise REST API (10.6): searches… |
| 2026-10-08 17:34:23 | [SENESO.Geidea.Net](https://www.nuget.org/packages/SENESO.Geidea.Net) | 1.0.0 | Eslam Ashraf,Github Contribut… | The missing .NET SDK for Geidea — the MENA payment gateway (Saudi, Egypt, UAE).… |
| 2026-10-08 17:34:53 | [GroveGames.Serialization](https://www.nuget.org/packages/GroveGames.Serialization) | 0.1.0 | Grove Games | High-performance JSON, MessagePack and CSV serialization with format conversion… |
| 2026-10-08 18:09:29 | [TraumaStation.ImageSharp](https://www.nuget.org/packages/TraumaStation.ImageSharp) | 5.0.0 | Six Labors and contributors | A new, fully featured, fully managed, cross-platform, 2D graphics API for .NET,… |
| 2026-10-08 18:18:17 | [PdfiumWrapper.runtime.linux-x64](https://www.nuget.org/packages/PdfiumWrapper.runtime.linux-x64) | 2.0.0 | Emmanuel Hameyie | Native PDFium runtime binaries for linux-x64. Internal runtime package for Pdfi… |
| 2026-10-08 18:18:20 | [PdfiumWrapper.runtime.osx-arm64](https://www.nuget.org/packages/PdfiumWrapper.runtime.osx-arm64) | 2.0.0 | Emmanuel Hameyie | Native PDFium runtime binaries for osx-arm64. Internal runtime package for Pdfi… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

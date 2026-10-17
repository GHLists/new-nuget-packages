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

## Latest list — 2026-10-17 20:18 UTC

New packages created between 2026-10-17 19:18 UTC and 2026-10-17 20:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-17T20-18-35-105093Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-17 19:43:04 | [Pinqponq.Billing.RevenueCat](https://www.nuget.org/packages/Pinqponq.Billing.RevenueCat) | 1.0.0 | Pinqponq | RevenueCat webhook handling: payload model, Authorization header verification a… |
| 2026-10-17 19:45:20 | [DataverseRecordRecovery](https://www.nuget.org/packages/DataverseRecordRecovery) | 1.0.0 | AmraouiH | Dataverse Record Recovery brings back Dynamics 365 / Dataverse records that wer… |
| 2026-10-17 19:50:12 | [PanoramicData.SoundPrint](https://www.nuget.org/packages/PanoramicData.SoundPrint) | 1.0.1 | Panoramic Data Limited | Landmark-based audio fingerprinting for .NET: streaming spectral-peak hashing,… |
| 2026-10-17 19:50:13 | [PanoramicData.SoundPrint.Postgres](https://www.nuget.org/packages/PanoramicData.SoundPrint.Postgres) | 1.0.1 | Panoramic Data Limited | PostgreSQL fingerprint store for PanoramicData.SoundPrint, built on EF Core. |
| 2026-10-17 20:03:19 | [MusicTheory.Guitar](https://www.nuget.org/packages/MusicTheory.Guitar) | 1.6.0 | phmatray | Guitar companion to MusicTheory: tunings, chord voicings and framework-agnostic… |
| 2026-10-17 20:06:12 | [PulseTrade.Comm.ResourceNode.Dynamic](https://www.nuget.org/packages/PulseTrade.Comm.ResourceNode.Dynamic) | 0.1.0-alpha4 | PulseTrade.Comm.ResourceNode.… | Package Description |
| 2026-10-17 20:07:14 | [Neomoth.IoC](https://www.nuget.org/packages/Neomoth.IoC) | 1.0.0 | neomoth | A small static IoC container with [Dependency] field injection, plus Roslyn ana… |
| 2026-10-17 20:13:23 | [Jove.Tooling.CMakeSDK](https://www.nuget.org/packages/Jove.Tooling.CMakeSDK) | 1.0.0 | Jove.Tooling.CMakeSDK | MSBuild SDK for CMake projects on macOS, with Nix-provisioned build tools. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

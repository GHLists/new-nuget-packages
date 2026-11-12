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

## Latest list — 2026-11-12 05:20 UTC

New packages created between 2026-11-12 04:19 UTC and 2026-11-12 05:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-12T05-20-41-73523Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-12 04:22:02 | [Skail.Cli](https://www.nuget.org/packages/Skail.Cli) | 0.1.0 | Skail | The Skail CLI: create, run and inspect durable Skail workloads. `skail init --t… |
| 2026-11-12 04:22:10 | [Universal.Apache.Parquet](https://www.nuget.org/packages/Universal.Apache.Parquet) | 1.0.0 | Andrew Ong | Managed Apache Parquet file reading and writing. |
| 2026-11-12 04:25:36 | [SuperSemantics.Vsl](https://www.nuget.org/packages/SuperSemantics.Vsl) | 0.1.1 | Super Semantics | Framework-agnostic VSL governance primitives (PreNode, Invariant, TerminalState… |
| 2026-11-12 04:32:58 | [OhAuthCat](https://www.nuget.org/packages/OhAuthCat) | 0.0.2 | OhAuthCat | OhAuthCat server SDK: enterprise SSO and SCIM directory sync. |
| 2026-11-12 04:52:27 | [VeliraPay](https://www.nuget.org/packages/VeliraPay) | 0.1.0 | VeliraPay | The official .NET library for VeliraPay crypto payments (https://velirapay.com)… |
| 2026-11-12 04:54:53 | [AquaCulture.AI.Torch](https://www.nuget.org/packages/AquaCulture.AI.Torch) | 1.2.0 | Gravicode Studios (Kang Fadhi… | LSTM dissolved-oxygen forecaster for AquaCulture.Net on TorchSharp (libtorch).… |
| 2026-11-12 04:54:54 | [AquaCulture.ComputerVision.MediaPipe](https://www.nuget.org/packages/AquaCulture.ComputerVision.MediaPipe) | 1.2.0 | Gravicode Studios (Kang Fadhi… | Fish and shrimp length and weight from photos and video with MediaPipe's MagicT… |
| 2026-11-12 05:04:03 | [NTComponents.Analyzers](https://www.nuget.org/packages/NTComponents.Analyzers) | 2.0.0 | NT Technologies | Roslyn analyzers that validate NTComponents usage and accessibility at build ti… |
| 2026-11-12 05:13:44 | [Arbitrator](https://www.nuget.org/packages/Arbitrator) | 0.7.0 | Dylan de Beer | A small, opinionated, in-process mediator: typed request dispatch to exactly on… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

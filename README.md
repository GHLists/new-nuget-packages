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

## Latest list — 2026-11-08 00:18 UTC

New packages created between 2026-11-07 23:19 UTC and 2026-11-08 00:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-08T00-18-53-032016Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-07 23:36:27 | [sfiruch.OpenHomeRadio](https://www.nuget.org/packages/sfiruch.OpenHomeRadio) | 0.1.0 | Simon Felix | Send and receive 868 MHz home-automation radio protocols (the Domino and IoHome… |
| 2026-11-07 23:36:28 | [sfiruch.OpenHomeRadio.Cli](https://www.nuget.org/packages/sfiruch.OpenHomeRadio.Cli) | 0.1.0 | Simon Felix | Command-line tool for OpenHomeRadio: send, receive, capture and decode 868 MHz… |
| 2026-11-08 00:10:42 | [Kerf.Kernel.Foundation](https://www.nuget.org/packages/Kerf.Kernel.Foundation) | 0.3.0 | Kerf contributors | Kerf.Kernel foundation, derived from Open CASCADE Technology 8.0.1 (Open Cascad… |
| 2026-11-08 00:11:06 | [Kerf.Kernel.ModelingData](https://www.nuget.org/packages/Kerf.Kernel.ModelingData) | 0.3.0 | Kerf contributors | Kerf.Kernel modelling data, derived from Open CASCADE Technology 8.0.1 (Open Ca… |
| 2026-11-08 00:11:16 | [Kerf.Kernel.ModelingAlgorithms](https://www.nuget.org/packages/Kerf.Kernel.ModelingAlgorithms) | 0.3.0 | Kerf contributors | Kerf.Kernel modelling algorithms, derived from Open CASCADE Technology 8.0.1 (O… |
| 2026-11-08 00:11:37 | [Kerf.Kernel.DataExchange](https://www.nuget.org/packages/Kerf.Kernel.DataExchange) | 0.3.0 | Kerf contributors | Kerf.Kernel data exchange, derived from Open CASCADE Technology 8.0.1 (Open Cas… |
| 2026-11-08 00:11:46 | [Kerf.Modeling](https://www.nuget.org/packages/Kerf.Modeling) | 0.3.0 | Kerf contributors | Kerf.Modeling: a code-first CAD modelling library for .NET, derived from build1… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

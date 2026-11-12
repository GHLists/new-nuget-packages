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

## Latest list — 2026-11-12 01:21 UTC

New packages created between 2026-11-12 00:21 UTC and 2026-11-12 01:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-12T01-21-03-499725Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-12 00:24:09 | [Aleator.Torch](https://www.nuget.org/packages/Aleator.Torch) | 0.4.1 | Aleator contributors | TorchSharp bridge for Aleator — wraps a TorchSharp tensor program inside an IDi… |
| 2026-11-12 00:24:09 | [Aleator.MLNet](https://www.nuget.org/packages/Aleator.MLNet) | 0.4.1 | Aleator contributors | ML.NET adapter for Aleator — exposes probabilistic-model inference as an ML.NET… |
| 2026-11-12 00:24:10 | [Aleator.Algorithms](https://www.nuget.org/packages/Aleator.Algorithms) | 0.4.1 | Aleator contributors | Inference algorithms (VE, BP, Importance, Metropolis-Hastings, Gibbs, EM, parti… |
| 2026-11-12 00:24:10 | [Aleator.Library](https://www.nuget.org/packages/Aleator.Library) | 0.4.1 | Aleator contributors | Standard library of probabilistic elements (atomic continuous/discrete, collect… |
| 2026-11-12 00:24:10 | [Aleator.Core](https://www.nuget.org/packages/Aleator.Core) | 0.4.1 | Aleator contributors | Core probabilistic programming primitives (Element, Universe, language) for Ale… |
| 2026-11-12 00:24:11 | [Aleator.DependencyInjection](https://www.nuget.org/packages/Aleator.DependencyInjection) | 0.4.1 | Aleator contributors | Microsoft.Extensions.DependencyInjection integration for Aleator (per-request U… |
| 2026-11-12 00:24:11 | [Aleator.AutoDiff](https://www.nuget.org/packages/Aleator.AutoDiff) | 0.4.1 | Aleator contributors | Reverse-mode automatic differentiation, unconstraining transforms, and a differ… |
| 2026-11-12 00:25:26 | [WASU.Plugin.RPC](https://www.nuget.org/packages/WASU.Plugin.RPC) | 26.1112.9 | WASU.Plugin.RPC | Package Description |
| 2026-11-12 00:34:30 | [Sentry.Quartz3](https://www.nuget.org/packages/Sentry.Quartz3) | 6.13.0 | Sentry Team and Contributors | Official Quartz.NET 3.x integration for Sentry - Open-source error tracking tha… |
| 2026-11-12 00:34:38 | [Sentry.Quartz](https://www.nuget.org/packages/Sentry.Quartz) | 6.13.0 | Sentry Team and Contributors | Official Quartz.NET 4.x integration for Sentry - Open-source error tracking tha… |
| 2026-11-12 00:36:43 | [Soenneker.Vtracer.Util](https://www.nuget.org/packages/Soenneker.Vtracer.Util) | 11.0.10 | Jake Soenneker | A cross-platform .NET API for raster to SVG conversion using bundled VTracer ex… |
| 2026-11-12 01:03:39 | [SharpRTCP](https://www.nuget.org/packages/SharpRTCP) | 0.8.1 | Lukas Volf | RTCP sender and receiver reports, reception statistics, source descriptions and… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

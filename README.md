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

## Latest list — 2026-11-16 20:18 UTC

New packages created between 2026-11-16 19:19 UTC and 2026-11-16 20:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-16T20-18-43-587465Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-16 19:23:00 | [Fetchling](https://www.nuget.org/packages/Fetchling) | 3.0.0 | Patrick Sachmann | Fetchling — TanStack Query-inspired async data fetching and caching for .NET. M… |
| 2026-11-16 19:23:00 | [Fetchling.Blazor](https://www.nuget.org/packages/Fetchling.Blazor) | 3.0.0 | Patrick Sachmann | Blazor components (Suspense, Transition, QueryRefreshMonitor) for Fetchling |
| 2026-11-16 19:23:00 | [Fetchling.Blazor.DevTools](https://www.nuget.org/packages/Fetchling.Blazor.DevTools) | 3.0.0 | Patrick Sachmann | DevTools Blazor component for inspecting the Fetchling cache at runtime |
| 2026-11-16 19:23:01 | [Fetchling.Core](https://www.nuget.org/packages/Fetchling.Core) | 3.0.0 | Patrick Sachmann | TanStack Query-inspired async data fetching and state management for .NET |
| 2026-11-16 19:23:02 | [Fetchling.Mvvm](https://www.nuget.org/packages/Fetchling.Mvvm) | 3.0.0 | Patrick Sachmann | MVVM view models (INotifyPropertyChanged bindings) for Fetchling — MAUI, WPF, W… |
| 2026-11-16 19:23:02 | [Fetchling.Extensions.DependencyInjection](https://www.nuget.org/packages/Fetchling.Extensions.DependencyInjection) | 3.0.0 | Patrick Sachmann | Dependency injection extensions for Fetchling |
| 2026-11-16 19:24:11 | [MessageValidation.OnnxRuntime](https://www.nuget.org/packages/MessageValidation.OnnxRuntime) | 2.2.0 | Romain-OD | ONNX Runtime adapter for the MessageValidation pipeline — run an on-device ONNX… |
| 2026-11-16 19:24:12 | [MessageValidation.SparkplugB](https://www.nuget.org/packages/MessageValidation.SparkplugB) | 2.2.0 | Romain-OD | Eclipse Sparkplug B validator for the MessageValidation pipeline — parses spBv1… |
| 2026-11-16 19:24:18 | [Canducci.DataMasker](https://www.nuget.org/packages/Canducci.DataMasker) | 0.0.5 | Canducci.DataMasker | Package Description |
| 2026-11-16 19:27:06 | [AzureRetriever](https://www.nuget.org/packages/AzureRetriever) | 1.0.0 | Outled | Gets a list of all Git repositories in an Azure DevOps organization. |
| 2026-11-16 19:35:01 | [FastKMeans](https://www.nuget.org/packages/FastKMeans) | 1.0.0 | Nikolai Voronin | Fast K-Means++ clustering for N-dimensional numerical data, with SIMD, parallel… |
| 2026-11-16 19:55:01 | [CardProbability.Engine](https://www.nuget.org/packages/CardProbability.Engine) | 1.0.0 | SeyTi01 | A synchronous, domain-neutral probability engine for finite decks, overlapping… |
| 2026-11-16 19:57:07 | [Flap](https://www.nuget.org/packages/Flap) | 0.0.1-beta1 | Devon Burriss | A clap-inspired, pipe-friendly command line parser for F#. Native AOT and Fable… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

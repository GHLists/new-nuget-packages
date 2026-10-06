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

## Latest list — 2026-10-06 17:19 UTC

New packages created between 2026-10-06 16:22 UTC and 2026-10-06 17:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-06T17-19-27-647876Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-06 16:28:16 | [Trama.UI](https://www.nuget.org/packages/Trama.UI) | 1.0.0 | Daniele Lopreiato | Framework-independent Trama UI Web Components packaged as ASP.NET Core static w… |
| 2026-10-06 16:31:31 | [Tessel.NET](https://www.nuget.org/packages/Tessel.NET) | 1.1.0 | EXLIRIX Software,Jurca Alexan… | A modern, themeable WPF UI framework for .NET 10: light/dark/system themes, acc… |
| 2026-10-06 16:34:26 | [TypeSafeSharp](https://www.nuget.org/packages/TypeSafeSharp) | 0.1.0 | TypeSafeSharp contributors | Unofficial .NET client for TypeSafe AI's System One API and the Jev model. Type… |
| 2026-10-06 16:34:27 | [TypeSafeSharp.Extensions.DependencyInjection](https://www.nuget.org/packages/TypeSafeSharp.Extensions.DependencyInjection) | 0.1.0 | TypeSafeSharp contributors | IServiceCollection registration for TypeSafeSharp, the unofficial .NET client f… |
| 2026-10-06 16:45:34 | [SolutionComponentCloner](https://www.nuget.org/packages/SolutionComponentCloner) | 1.0.0 | abdel | Copies components from one Dataverse / Dynamics 365 solution into another, with… |
| 2026-10-06 16:49:47 | [Flyleaf.FFmpeg.ABI](https://www.nuget.org/packages/Flyleaf.FFmpeg.ABI) | 9.0.0-alpha | SuRGeoNix | Low-level, ABI-focused .NET bindings for FFmpeg, providing direct access to nat… |
| 2026-10-06 16:50:43 | [DeepSharp.Pipelines.Binance](https://www.nuget.org/packages/DeepSharp.Pipelines.Binance) | 0.8.0 | H.P. Gansevoort | Lands the candles an exchange answers with as a file that a DeepSharp pipeline… |
| 2026-10-06 17:00:05 | [ITBees.Wp](https://www.nuget.org/packages/ITBees.Wp) | 8.0.1 | ITBees.Wp | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

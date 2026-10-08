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

## Latest list — 2026-10-08 19:18 UTC

New packages created between 2026-10-08 18:23 UTC and 2026-10-08 19:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-08T19-18-50-29706Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-08 18:24:11 | [Gondwana.Video.Widgets](https://www.nuget.org/packages/Gondwana.Video.Widgets) | 2.6.1 | Mike Adkins | Optional interactive and draggable video widgets composing Gondwana Video and W… |
| 2026-10-08 18:32:45 | [NBTerminal](https://www.nuget.org/packages/NBTerminal) | 0.1.0 | postmium | A lightweight, event-driven .NET terminal library with non-blocking input, inde… |
| 2026-10-08 18:35:31 | [FluxLector.Client](https://www.nuget.org/packages/FluxLector.Client) | 0.1.1 | IntegralByte | Wrapper .NET oficial para la API de Flux Lector (lectura automatica de medidore… |
| 2026-10-08 18:46:46 | [Lait.Umbraco.Awesome.SEO](https://www.nuget.org/packages/Lait.Umbraco.Awesome.SEO) | 1.0.0 | LAIT, Anders Bootsmann Overvad | SEO report and action plan inside the Umbraco 17 backoffice. Crawls your site a… |
| 2026-10-08 18:57:52 | [SinkSharp.Core](https://www.nuget.org/packages/SinkSharp.Core) | 1.0.0 | SinkSharp | High-performance structured logging for .NET 9. Striped async channel queue, Me… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-24 20:21 UTC

New packages created between 2026-11-24 19:20 UTC and 2026-11-24 20:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-24T20-21-25-44417Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-24 19:31:21 | [Umbraco.Community.PropertyJsonViewer](https://www.nuget.org/packages/Umbraco.Community.PropertyJsonViewer) | 18.0.0 | Jack Stunell | See and fix the raw value Umbraco stores for any document property, right from… |
| 2026-11-24 19:33:00 | [ElRoso.Commons.OpenApi](https://www.nuget.org/packages/ElRoso.Commons.OpenApi) | 1.0.0 | Di Rosolini Ezequiel | OpenAPI nativo de ASP.NET Core, un documento por versión de API, con esquemas J… |
| 2026-11-24 19:39:01 | [Esatto.Umbraco.Backoffice.SeoReport](https://www.nuget.org/packages/Esatto.Umbraco.Backoffice.SeoReport) | 1.0.0 | Carl Schéle | SEO Report for Umbraco: a Content-section dashboard that turns Google Analytics… |
| 2026-11-24 19:46:11 | [GroundWerk.Telemetry](https://www.nuget.org/packages/GroundWerk.Telemetry) | 2.0.1 | The GroundWerk authors | Sets up OpenTelemetry traces, metrics and structured logs for an ASP.NET Core s… |
| 2026-11-24 20:00:15 | [Kebechet.Maui.WebView.VersionGate](https://www.nuget.org/packages/Kebechet.Maui.WebView.VersionGate) | 1.0.0 | Kebechet | Holds a .NET MAUI app behind an update dialog while the Android System WebView… |
| 2026-11-24 20:03:40 | [Bequadro](https://www.nuget.org/packages/Bequadro) | 0.1.0 | James Duley | An incremental source generator and runtime for FlatBuffers schemas (.fbs). |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

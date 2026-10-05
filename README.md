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

## Latest list — 2026-10-05 18:21 UTC

New packages created between 2026-10-05 17:19 UTC and 2026-10-05 18:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-05T18-21-45-186171Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-05 17:22:13 | [Scowalt.NoCommentsAnalyzer](https://www.nuget.org/packages/Scowalt.NoCommentsAnalyzer) | 0.1.0 | Scott Walters | FSharp.Analyzers.SDK analyzer that reports every comment token (//, ///, (* *))… |
| 2026-10-05 17:41:21 | [ResilienceLab](https://www.nuget.org/packages/ResilienceLab) | 0.5.0 | ResilienceLab contributors | Educational .NET resilience: result and exception retry, fallback, rate limitin… |
| 2026-10-05 17:41:25 | [ResilienceLab.Http](https://www.nuget.org/packages/ResilienceLab.Http) | 0.5.0 | ResilienceLab contributors | Reintentos HTTP con backoff, jitter, Retry-After, cancelación y registro tipado… |
| 2026-10-05 17:42:53 | [BetaCalendars.CalendarFixtureKit](https://www.nuget.org/packages/BetaCalendars.CalendarFixtureKit) | 0.1.0 | Beta Calendars | Deterministic .NET calendar fixtures, month-grid validation, regression diffs,… |
| 2026-10-05 17:59:30 | [Axelerate.Revit.ExtensibleStorage](https://www.nuget.org/packages/Axelerate.Revit.ExtensibleStorage) | 2026.0.0 | Axelerate | Attribute-based mapping of classes to Revit Extensible Storage schemas and enti… |
| 2026-10-05 18:05:08 | [Meshmakers.Common.Observability](https://www.nuget.org/packages/Meshmakers.Common.Observability) | 4.3.0 | meshmakers GmbH and Contribut… | NLog layout renderers that expose OpenTelemetry trace context, for correlating… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

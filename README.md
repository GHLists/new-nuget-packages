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

## Latest list — 2026-11-07 08:20 UTC

New packages created between 2026-11-07 07:19 UTC and 2026-11-07 08:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-07T08-20-46-7417Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-07 07:39:49 | [Prdb.Observability](https://www.nuget.org/packages/Prdb.Observability) | 0.1.0 | prdb | OpenTelemetry logs and metrics over OTLP for ASP.NET Core applications, configu… |
| 2026-11-07 07:44:07 | [Runax.Http](https://www.nuget.org/packages/Runax.Http) | 1.0.0 | Runax Software | Declarative HTTP clients for .NET: annotate an interface, get an implementation… |
| 2026-11-07 07:44:08 | [Runax.Http.Transports.RestSharp](https://www.nuget.org/packages/Runax.Http.Transports.RestSharp) | 1.0.0 | Runax Software | RestSharp transport for Runax.Http. Lets a Runax.Http client interface run over… |
| 2026-11-07 07:44:09 | [Runax.Http.TestKit](https://www.nuget.org/packages/Runax.Http.TestKit) | 1.0.0 | Runax Software | Test support for Runax.Http: a recording transport and a harness that stands up… |
| 2026-11-07 07:44:14 | [Runax.Http.Abstractions](https://www.nuget.org/packages/Runax.Http.Abstractions) | 1.0.0 | Runax Software | Attributes and transport-neutral contracts for Runax.Http. Reference this from… |
| 2026-11-07 08:05:29 | [FsiMcp](https://www.nuget.org/packages/FsiMcp) | 0.1.0 | Onur Gumus | MCP server that gives AI agents a persistent, project-aware F# Interactive sess… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

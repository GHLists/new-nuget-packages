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

## Latest list — 2026-10-13 04:19 UTC

New packages created between 2026-10-13 03:20 UTC and 2026-10-13 04:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-13T04-19-14-780535Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-13 03:20:42 | [TeaQL.Telemetry.OpenTelemetry](https://www.nuget.org/packages/TeaQL.Telemetry.OpenTelemetry) | 0.3.1 | TeaQL | TeaQL runtime and data services for .NET |
| 2026-10-13 03:54:05 | [DocWeave](https://www.nuget.org/packages/DocWeave) | 0.1.0 | Francois Roux | Fluent API and JSON templates for exporting and importing Excel (.xlsx) and CSV… |
| 2026-10-13 03:55:02 | [DocWeaveNS](https://www.nuget.org/packages/DocWeaveNS) | 0.1.0 | Francois Roux | .NET Standard 2.0 compatible variant of DocWeave for importing and exporting Ex… |
| 2026-10-13 04:04:44 | [AVCoders.Alarm](https://www.nuget.org/packages/AVCoders.Alarm) | 2026.10.2 | AV Coders | Alarm panel, area, zone and relay base classes for the AV Coders device library. |
| 2026-10-13 04:09:28 | [Pmmux.Extensions.Management.Models](https://www.nuget.org/packages/Pmmux.Extensions.Management.Models) | 0.0.2 | Lenny Kean | PMMux management API models. |
| 2026-10-13 04:09:29 | [Pmmux.Extensions.Management.Abstractions](https://www.nuget.org/packages/Pmmux.Extensions.Management.Abstractions) | 0.0.2 | Lenny Kean | PMMux management API extension contracts. |
| 2026-10-13 04:09:30 | [Pmmux.Extensions.Acme.Abstractions](https://www.nuget.org/packages/Pmmux.Extensions.Acme.Abstractions) | 0.0.2 | Lenny Kean | PMMux ACME challenge contracts. |
| 2026-10-13 04:09:30 | [Pmmux.Abstractions](https://www.nuget.org/packages/Pmmux.Abstractions) | 0.0.2 | Lenny Kean | PMMux extension contracts. |
| 2026-10-13 04:09:31 | [Pmmux.Extensions.Tls.Abstractions](https://www.nuget.org/packages/Pmmux.Extensions.Tls.Abstractions) | 0.0.2 | Lenny Kean | PMMux TLS certificate contracts. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-27 23:19 UTC

New packages created between 2026-10-27 22:20 UTC and 2026-10-27 23:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-27T23-19-10-439896Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-27 22:48:21 | [DteChile](https://www.nuget.org/packages/DteChile) | 0.3.0 | Jorge Luis Saraiva Ruas | Biblioteca .NET sin dependencias para generar, timbrar, firmar y enviar Documen… |
| 2026-10-27 23:01:11 | [Splunk.OpenTelemetry.SecureApp](https://www.nuget.org/packages/Splunk.OpenTelemetry.SecureApp) | 26.9.0 | AppDynamics LLC | This package contains the Splunk OpenTelemetry SecureApp auto-instrumentation p… |
| 2026-10-27 23:04:35 | [Gravicode.PollenRobotics.Net.AmazingHand](https://www.nuget.org/packages/Gravicode.PollenRobotics.Net.AmazingHand) | 0.3.0 | Gravicode Studios | .NET client for the Pollen Robotics Amazing Hand: four parallel-linkage fingers… |
| 2026-10-27 23:09:26 | [RainnWorks.Porkbun](https://www.nuget.org/packages/RainnWorks.Porkbun) | 0.1.2 | RainnWorks | A Pulumi provider for Porkbun: DNS records and domain nameservers. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

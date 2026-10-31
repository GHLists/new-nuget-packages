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

## Latest list — 2026-10-31 01:19 UTC

New packages created between 2026-10-31 00:20 UTC and 2026-10-31 01:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-31T01-19-44-782204Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-31 00:30:06 | [Raven.Gui](https://www.nuget.org/packages/Raven.Gui) | 0.2.0 | Oscar Soirey | C# bindings for Raven, a lightweight, multithreaded GUI library in C for editor… |
| 2026-10-31 00:36:06 | [Kokoabim.OnionHttpClient](https://www.nuget.org/packages/Kokoabim.OnionHttpClient) | 0.1.1 | Spencer James | Onion HTTP client library for .NET |
| 2026-10-31 00:38:33 | [Shiny.Controls.Gauge.Shared](https://www.nuget.org/packages/Shiny.Controls.Gauge.Shared) | 2.3.0-beta-0001 | Allan Ritchie | Host-neutral engine behind the Shiny gauge controls — value-to-angle scale mapp… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

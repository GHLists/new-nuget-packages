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

## Latest list — 2026-10-11 13:20 UTC

New packages created between 2026-10-11 12:21 UTC and 2026-10-11 13:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-11T13-20-34-99008Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-11 12:33:49 | [XmltvDigital3d.Mcp](https://www.nuget.org/packages/XmltvDigital3d.Mcp) | 1.0.9 | Digital3D | MCP server for the French TV guide of xmltv.digital3d.com: channels, schedules… |
| 2026-10-11 12:56:15 | [Filemaster.Domain](https://www.nuget.org/packages/Filemaster.Domain) | 2.0.0 | Gabriele Vianello | Filemaster.Domain: ID tipizzati, entita' ed eccezioni del client per l'API HTTP… |
| 2026-10-11 12:56:16 | [Filemaster.Application](https://www.nuget.org/packages/Filemaster.Application) | 2.0.0 | Gabriele Vianello | Filemaster.Application: porte (interfacce), modelli di richiesta ed estensioni… |
| 2026-10-11 12:56:17 | [Filemaster.Infrastructure](https://www.nuget.org/packages/Filemaster.Infrastructure) | 2.0.0 | Gabriele Vianello | Filemaster.Infrastructure: adapter HTTP, trasporto (timeout e retry) e serializ… |
| 2026-10-11 12:56:18 | [Filemaster](https://www.nuget.org/packages/Filemaster) | 2.0.0 | Gabriele Vianello | Filemaster: client .NET per l'API HTTP di Sharp-a-File (registrazione DI e fact… |
| 2026-10-11 13:02:23 | [Meshmakers.Octo.ConstructionKit.Models.System.Files](https://www.nuget.org/packages/Meshmakers.Octo.ConstructionKit.Models.System.Files) | 3.5.12 | meshmakers GmbH and Contribut… | OctoMesh System.Files construction kit model (platform file system) |
| 2026-10-11 13:06:15 | [Gravicode.Finance.LLM.Local](https://www.nuget.org/packages/Gravicode.Finance.LLM.Local) | 0.2.0 | Gravicode Studios | Finance.Net local model inference: FinBERT financial sentiment run in-process t… |
| 2026-10-11 13:08:40 | [Shiny.AppStore](https://www.nuget.org/packages/Shiny.AppStore) | 6.0.0-beta-0002 | Allan Ritchie | Shiny App Store - check the store for a newer version of the running app, deep-… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

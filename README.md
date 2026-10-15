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

## Latest list — 2026-10-15 09:22 UTC

New packages created between 2026-10-15 08:19 UTC and 2026-10-15 09:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-15T09-22-04-679039Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-15 08:20:02 | [Esatto.Umbraco.Backoffice.BlockPreview](https://www.nuget.org/packages/Esatto.Umbraco.Backoffice.BlockPreview) | 1.0.1 | Carl Schéle | Live frontend previews for Umbraco 17/18 Block List blocks in the backoffice: e… |
| 2026-10-15 08:25:50 | [Dynamicweb.ServiceApi](https://www.nuget.org/packages/Dynamicweb.ServiceApi) | 10.25.1-BETA001 | Dynamicweb Software A/S | RESTful Service API for Dynamicweb 10 administration: CRUD endpoints for produc… |
| 2026-10-15 08:34:56 | [PulseSharp.Sync.Server](https://www.nuget.org/packages/PulseSharp.Sync.Server) | 0.5.0-alpha | Waqas Ahmad | The server side of PulseSharp sync: an ASP.NET Core endpoint that receives even… |
| 2026-10-15 08:34:58 | [PulseSharp.Sync](https://www.nuget.org/packages/PulseSharp.Sync) | 0.5.0-alpha | Waqas Ahmad | Device to cloud sync for PulseSharp: the device keeps working offline and sends… |
| 2026-10-15 08:36:06 | [HeroKit](https://www.nuget.org/packages/HeroKit) | 1.0.0 | Emre Akdemir | Extension methods for everyday .NET types: validation, conversion and manipulat… |
| 2026-10-15 09:00:46 | [Blueprint.Hangfire](https://www.nuget.org/packages/Blueprint.Hangfire) | 1.0.8 | Symprex | Hangfire integration for Blueprint background and recurring tasks. |
| 2026-10-15 09:01:16 | [Blueprint.HttpClient](https://www.nuget.org/packages/Blueprint.HttpClient) | 1.0.8 | Symprex | A typed HTTP client for calling Blueprint APIs using their operation types. |
| 2026-10-15 09:01:45 | [Parlem.Crm.Drivers](https://www.nuget.org/packages/Parlem.Crm.Drivers) | 10.0.1 | Parlem.Crm.Drivers | Package Description |
| 2026-10-15 09:02:47 | [Blueprint.Marten](https://www.nuget.org/packages/Blueprint.Marten) | 1.0.8 | Symprex | Marten integration for Blueprint: a unit of work for generated pipelines and do… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

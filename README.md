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

## Latest list — 2026-10-27 09:20 UTC

New packages created between 2026-10-27 08:20 UTC and 2026-10-27 09:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-27T09-20-20-990628Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-27 08:34:48 | [Zucchetti.SDH.DCA.Client](https://www.nuget.org/packages/Zucchetti.SDH.DCA.Client) | 1.0.2 | Zucchetti Software Spain S.L.… | Cliente .NET Standard 2.0 para la SDH DCA API (Documento de Control Administrat… |
| 2026-10-27 08:40:20 | [Pycom.Agent.Platform](https://www.nuget.org/packages/Pycom.Agent.Platform) | 0.1.0 | Pycom | Strongly typed client for the Pycom Agent Platform runtime API. |
| 2026-10-27 08:48:08 | [Transformations.Sql](https://www.nuget.org/packages/Transformations.Sql) | 3.0.0 | opentail.net, Dmitri Rechetil… | SQL Server transient fault classification shared by the Transformations data pa… |
| 2026-10-27 08:50:18 | [Fable.NodaTime.Thoth](https://www.nuget.org/packages/Fable.NodaTime.Thoth) | 0.1.0 | Oliver Coad | Backend-independent Thoth.Json.Core codecs for Fable.NodaTime. |
| 2026-10-27 08:50:18 | [Fable.NodaTime](https://www.nuget.org/packages/Fable.NodaTime) | 0.1.0 | Oliver Coad | Shared ISO datetime API for .NET and Fable, backed by NodaTime and Temporal. |
| 2026-10-27 08:50:19 | [Fable.NodaTime.TypedJson](https://www.nuget.org/packages/Fable.NodaTime.TypedJson) | 0.1.0 | Oliver Coad | Backend-independent Fable.TypedJson codecs for Fable.NodaTime. |
| 2026-10-27 08:54:56 | [UnifiedBlazor.Extensions.FastReport.OpenSource](https://www.nuget.org/packages/UnifiedBlazor.Extensions.FastReport.OpenSource) | 0.1.0 | TW1225 | UnifiedBlazor框架的FastReport开源版扩展库 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

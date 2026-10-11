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

## Latest list — 2026-10-11 20:20 UTC

New packages created between 2026-10-11 19:19 UTC and 2026-10-11 20:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-11T20-20-17-841759Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-11 19:20:36 | [KaizenIO.Jev](https://www.nuget.org/packages/KaizenIO.Jev) | 0.1.0 | Kaizenio, Inc. | .NET client for the Jev API (POST /v1/systemone): ask noul (yes/no), choice and… |
| 2026-10-11 19:23:00 | [NextcloudNotesClient](https://www.nuget.org/packages/NextcloudNotesClient) | 1.0.0 | NextcloudNotesClient | Package Description |
| 2026-10-11 19:29:08 | [NatureRemo](https://www.nuget.org/packages/NatureRemo) | 0.1.0 | C | C# client for Nature Remo API (port of morinokami/nature-remo) |
| 2026-10-11 19:32:57 | [MIG.Audio](https://www.nuget.org/packages/MIG.Audio) | 1.0.0 | G-Labs | Local speech recognition and synthesis for MIG and HomeGenie, powered by Whispe… |
| 2026-10-11 19:38:30 | [clbfc](https://www.nuget.org/packages/clbfc) | 1.100.0 | clbfc | Package Description |
| 2026-10-11 20:03:09 | [Hateoas.AspNetCore](https://www.nuget.org/packages/Hateoas.AspNetCore) | 2.1.1 | Yahya Erdogan | ASP.NET Core integration for Hateoas: one LinkProvider per resource type applie… |
| 2026-10-11 20:03:09 | [Hateoas.Hal](https://www.nuget.org/packages/Hateoas.Hal) | 2.1.1 | Yahya Erdogan | Framework-agnostic building blocks for HAL hypermedia (HATEOAS): Link, a LinkCo… |
| 2026-10-11 20:05:43 | [LibrusApixNet](https://www.nuget.org/packages/LibrusApixNet) | 1.6.0-beta1 | LibrusApixNet contributors | Unofficial cross-platform .NET 10 port of RustySnek/librus-apix for Librus Syne… |
| 2026-10-11 20:07:02 | [KlabTranslations.Generator.Blazor](https://www.nuget.org/packages/KlabTranslations.Generator.Blazor) | 1.1.0 | Burak Kizilkaya | Package Description |
| 2026-10-11 20:07:02 | [KlabTranslations.Cli](https://www.nuget.org/packages/KlabTranslations.Cli) | 1.1.0 | Burak Kizilkaya | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

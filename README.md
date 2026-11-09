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

## Latest list — 2026-11-09 22:21 UTC

New packages created between 2026-11-09 21:20 UTC and 2026-11-09 22:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-09T22-21-41-392541Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-09 21:22:00 | [DBUDoctor](https://www.nuget.org/packages/DBUDoctor) | 0.2.0 | Nemanja Markovic | Estimates what a Databricks bundle change will cost, per resource, from the pul… |
| 2026-11-09 21:29:48 | [Nobirds.OldenEra.Modding.Catalog](https://www.nuget.org/packages/Nobirds.OldenEra.Modding.Catalog) | 0.1.0 | fogone | Writes a mod catalog for the Olden Era mod manager (Heroes of Might and Magic:… |
| 2026-11-09 21:30:18 | [Runic.Translations.Hosting](https://www.nuget.org/packages/Runic.Translations.Hosting) | 0.9.1 | RunicArtifex | Registers a shared Runic Translations context, its catalogs and overlays with M… |
| 2026-11-09 21:33:21 | [Plugin.Maui.AiChat](https://www.nuget.org/packages/Plugin.Maui.AiChat) | 1.0.0 | Mykhailo Davydenko | A drop-in AI chat view for .NET MAUI on any Microsoft.Extensions.AI IChatClient… |
| 2026-11-09 21:50:56 | [Eleris.FitsNet](https://www.nuget.org/packages/Eleris.FitsNet) | 0.1.0 | Sébastien Putier | Pure managed .NET library to read, write and manipulate FITS (Flexible Image Tr… |
| 2026-11-09 21:58:40 | [Bit.BevTools.Belemetry](https://www.nuget.org/packages/Bit.BevTools.Belemetry) | 11.0.0-pre-17 | bit platform | bit Belemetry integration for bit BevTools: a Support panel with Belemetry's di… |
| 2026-11-09 21:59:54 | [Cosmos.Types.Empresas](https://www.nuget.org/packages/Cosmos.Types.Empresas) | 1.0.0 | Cosmos | Value Objects de la empresa del tenant para el ERP Cosmos: FichaEmpresa (la fic… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

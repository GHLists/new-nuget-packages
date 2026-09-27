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

## Latest list — 2026-09-27 18:20 UTC

New packages created between 2026-09-27 17:21 UTC and 2026-09-27 18:20 UTC.

[Full CSV](data/new-nuget-packages-2026-09-27T18-20-13-478643Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-27 17:32:36 | [TrailerClipper.Tool](https://www.nuget.org/packages/TrailerClipper.Tool) | 2.0.0 | Mark Rogers | The tclipper command: batch removal of intros and trailers from video and audio… |
| 2026-09-27 17:50:14 | [Experimently.SDK](https://www.nuget.org/packages/Experimently.SDK) | 0.0.0 | Experimently | Placeholder that holds the package ID. The Experimently .NET SDK is not publish… |
| 2026-09-27 17:53:21 | [GlpiNg.Modules.Abstractions](https://www.nuget.org/packages/GlpiNg.Modules.Abstractions) | 0.1.0 | AnthoDingo | Contrats partagés entre l'hôte GlpiNg, ses modules et les plugins. |
| 2026-09-27 17:54:13 | [GlpiNg.Plugins.Sdk](https://www.nuget.org/packages/GlpiNg.Plugins.Sdk) | 0.1.0 | AnthoDingo | Contrats pour écrire un plugin GlpiNg : point d'entrée IGlpiNgPlugin et contrat… |
| 2026-09-27 18:08:44 | [Meshline.Sdk](https://www.nuget.org/packages/Meshline.Sdk) | 1.0.0 | Meshline | Client SDK for the Meshline protocol, with self-sovereign accounts, encrypted m… |
| 2026-09-27 18:13:05 | [Offramp.Analyzers](https://www.nuget.org/packages/Offramp.Analyzers) | 0.15.0 | Andrew Benz and contributors | Roslyn analyzers and code fixes for migrating .NET Framework code to modern .NE… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

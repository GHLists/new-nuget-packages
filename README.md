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

## Latest list — 2026-10-20 04:21 UTC

New packages created between 2026-10-20 03:20 UTC and 2026-10-20 04:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-20T04-21-23-182004Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-20 03:53:51 | [DeepSharp.Pipelines.Images](https://www.nuget.org/packages/DeepSharp.Pipelines.Images) | 0.13.0 | H.P. Gansevoort | Reads a DeepSharp pipeline's rows out of a folder of pictures, a folder to each… |
| 2026-10-20 03:53:54 | [DeepSharp.Pipelines.Sound](https://www.nuget.org/packages/DeepSharp.Pipelines.Sound) | 0.13.0 | H.P. Gansevoort | Reads a DeepSharp pipeline's rows out of a folder of recordings, a folder to ea… |
| 2026-10-20 03:56:46 | [Hosihikari.Plugin.Template](https://www.nuget.org/packages/Hosihikari.Plugin.Template) | 0.1.0 | 星光 | dotnet new template for a precompiled Hosihikari plugin. |
| 2026-10-20 04:16:10 | [DeidSharp.Fhir](https://www.nuget.org/packages/DeidSharp.Fhir) | 1.0.0 | Valentin Burkin | FHIR R4 de-identification for DeidSharp: Safe Harbor or pseudonymized resources… |
| 2026-10-20 04:16:11 | [DeidSharp](https://www.nuget.org/packages/DeidSharp) | 1.0.0 | Valentin Burkin | De-identification of health data: HIPAA Safe Harbor transforms, pseudonymizatio… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

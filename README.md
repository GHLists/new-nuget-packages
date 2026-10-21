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

## Latest list — 2026-10-21 08:19 UTC

New packages created between 2026-10-21 07:22 UTC and 2026-10-21 08:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-21T08-19-59-952098Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-21 07:27:16 | [MyStackBlazor.Calendar](https://www.nuget.org/packages/MyStackBlazor.Calendar) | 1.4.0 | Vilas Sagar | Full-featured calendar and scheduler component for MyStackBlazor. Supports Day,… |
| 2026-10-21 07:43:50 | [CSEPDI.Update](https://www.nuget.org/packages/CSEPDI.Update) | 1.0.26.1021 | CSEPDI | 系统更新 |
| 2026-10-21 07:48:45 | [Sallyport](https://www.nuget.org/packages/Sallyport) | 0.1.0 | Jiarong Gu | An OpenVPN-compatible client in pure .NET: one profile's tunnel inside your pro… |
| 2026-10-21 08:00:46 | [TheBuilder.AIImageDisclosure](https://www.nuget.org/packages/TheBuilder.AIImageDisclosure) | 0.1.0 | Daniel Schmidt | Classify fully AI-generated and partially AI-modified Umbraco images from C2PA… |
| 2026-10-21 08:00:48 | [TheBuilder.AIImageDisclosure.OpenAI](https://www.nuget.org/packages/TheBuilder.AIImageDisclosure.OpenAI) | 0.1.0 | Daniel Schmidt | Optional OpenAI SynthID verification fallback for AI Image Disclosure. |
| 2026-10-21 08:00:51 | [TheBuilder.AIImageDisclosure.OpenAI.UmbracoAI](https://www.nuget.org/packages/TheBuilder.AIImageDisclosure.OpenAI.UmbracoAI) | 0.1.0 | Daniel Schmidt | Optional Umbraco.AI connection adapter for AI Image Disclosure OpenAI provenanc… |
| 2026-10-21 08:11:38 | [seedunk.net](https://www.nuget.org/packages/seedunk.net) | 0.9.0.2610 | seedunk | 暂无 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

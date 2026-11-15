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

## Latest list — 2026-11-15 08:19 UTC

New packages created between 2026-11-15 07:19 UTC and 2026-11-15 08:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-15T08-19-40-639797Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-15 07:39:25 | [wwosik.DocLibs.DocumentGeneration.Docx](https://www.nuget.org/packages/wwosik.DocLibs.DocumentGeneration.Docx) | 2611.15.8 | Wojciech Wosik | Generates Word documents (.docx) from Markdown, on a built-in template in a bra… |
| 2026-11-15 07:43:44 | [OrbitLang.Sdk](https://www.nuget.org/packages/OrbitLang.Sdk) | 0.1.0 | ORBIT contributors | Worker SDK for the ORBIT workflow orchestration runtime: long-polls for tasks,… |
| 2026-11-15 07:49:22 | [BunnyTail.XamlProperty.WinUI](https://www.nuget.org/packages/BunnyTail.XamlProperty.WinUI) | 2.0.0 | machi_pon | DependencyProperty source generator for WinUI. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

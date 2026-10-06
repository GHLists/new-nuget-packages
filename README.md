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

## Latest list — 2026-10-06 04:21 UTC

New packages created between 2026-10-06 03:21 UTC and 2026-10-06 04:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-06T04-21-04-027404Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-06 03:37:39 | [CodeWF.Markdown.Export](https://www.nuget.org/packages/CodeWF.Markdown.Export) | 13.0.0 | 沙漠尽头的狼 | Export capability package for CodeWF.Markdown: PNG / PDF / Word export and soci… |
| 2026-10-06 03:37:41 | [CodeWF.Markdown.Highlighting](https://www.nuget.org/packages/CodeWF.Markdown.Highlighting) | 13.0.0 | 沙漠尽头的狼 | TextMate-based code syntax highlighting capability package for CodeWF.Markdown. |
| 2026-10-06 03:37:42 | [CodeWF.Markdown.Images](https://www.nuget.org/packages/CodeWF.Markdown.Images) | 13.0.0 | 沙漠尽头的狼 | Image rendering capability package for CodeWF.Markdown (SVG/GIF preview, async… |
| 2026-10-06 03:37:43 | [CodeWF.Markdown.Math](https://www.nuget.org/packages/CodeWF.Markdown.Math) | 13.0.0 | 沙漠尽头的狼 | Math formula rendering capability package for CodeWF.Markdown (CSharpMath based… |
| 2026-10-06 03:37:45 | [CodeWF.Markdown.Mermaid](https://www.nuget.org/packages/CodeWF.Markdown.Mermaid) | 13.0.0 | 沙漠尽头的狼 | Mermaid diagram rendering capability package for CodeWF.Markdown (pure .NET via… |
| 2026-10-06 03:46:23 | [FragmentDonor.Sdk](https://www.nuget.org/packages/FragmentDonor.Sdk) | 0.1.0 | Fragment Donor | Independent .NET client for the public Fragment Donor Stars and Premium API. |
| 2026-10-06 03:48:43 | [DragoAnt.Roslyn.Shared.Sources](https://www.nuget.org/packages/DragoAnt.Roslyn.Shared.Sources) | 1.0.0 | DragoAnt | Source-only helpers for Roslyn analyzers, source generators and code fixes: eac… |
| 2026-10-06 03:55:30 | [CollectionGenerator](https://www.nuget.org/packages/CollectionGenerator) | 1.1.0 | CollectionGenerator | Generates collections from members in C#. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

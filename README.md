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

## Latest list — 2026-11-16 23:20 UTC

New packages created between 2026-11-16 22:20 UTC and 2026-11-16 23:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-16T23-20-11-532322Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-16 22:49:16 | [TemplateDsl.AspNetCore](https://www.nuget.org/packages/TemplateDsl.AspNetCore) | 0.1.0 | Alexander Oliver Mader | Return TemplateDsl templates from ASP.NET Core minimal APIs and controllers, re… |
| 2026-11-16 22:49:17 | [TemplateDsl.Html](https://www.nuget.org/packages/TemplateDsl.Html) | 0.1.0 | Alexander Oliver Mader | The HTML format for TemplateDsl: write HTML templates as plain C#, rendered as… |
| 2026-11-16 22:49:17 | [TemplateDsl](https://www.nuget.org/packages/TemplateDsl) | 0.1.0 | Alexander Oliver Mader | Write templates for any nested text format as plain C#, compiled by a source ge… |
| 2026-11-16 22:51:08 | [BorrowedTorch.Collisions](https://www.nuget.org/packages/BorrowedTorch.Collisions) | 1.0.0 | Vladyslav Pysarenko | Collision volumes on MonoGame's types: spheres, boxes, capsules and cylinders i… |
| 2026-11-16 22:51:33 | [Iciclecreek.Azure.Storage.Lucene](https://www.nuget.org/packages/Iciclecreek.Azure.Storage.Lucene) | 2.1.0-rc001 | Tom Laird-McConnell | Drop-in replacements for the Azure.Data.Tables, Azure.Storage.Blobs and Azure.S… |
| 2026-11-16 22:52:02 | [ManagedCodecs.Avalonia](https://www.nuget.org/packages/ManagedCodecs.Avalonia) | 0.18.0 | Jakob Boman | Live cameras in Avalonia: LiveView shows a LivePlayer's newest frame (MJPEG ove… |
| 2026-11-16 22:52:04 | [ManagedCodecs.Wpf](https://www.nuget.org/packages/ManagedCodecs.Wpf) | 0.18.0 | Jakob Boman | Live cameras in WPF: LiveView shows a LivePlayer's newest frame (MJPEG over HTT… |
| 2026-11-16 23:03:13 | [BorrowedTorch.Culling](https://www.nuget.org/packages/BorrowedTorch.Culling) | 1.0.0 | Vladyslav Pysarenko | Frustum culling on MonoGame's types: a frustum from any view-projection matrix… |
| 2026-11-16 23:06:51 | [CloakAPI.Sdk](https://www.nuget.org/packages/CloakAPI.Sdk) | 1.3.1 | Klokk Nettablering | CloakAPI SDK for .NET. Replaces personal data in a prompt with stand-ins on you… |
| 2026-11-16 23:12:37 | [DtPipe.PipelineNode.Hosting](https://www.nuget.org/packages/DtPipe.PipelineNode.Hosting) | 1.17.0 | NicoPon | AddDtPipeNode: makes any .NET host a dtpipe pipeline node, and offers its own d… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-14 09:20 UTC

New packages created between 2026-10-14 08:20 UTC and 2026-10-14 09:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-14T09-20-10-051266Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-14 08:24:02 | [SUI](https://www.nuget.org/packages/SUI) | 0.0.3 | RobertCXC | SUI - Small UI. Sharp Experience. A lightweight, native, composable WPF UI comp… |
| 2026-10-14 08:33:29 | [Opinionated.DotNet.CodingStandards](https://www.nuget.org/packages/Opinionated.DotNet.CodingStandards) | 0.0.17 | Lee Sanderson | Strongly opinionated coding standards recommendations for .NET. |
| 2026-10-14 08:35:25 | [iPaas.Controls](https://www.nuget.org/packages/iPaas.Controls) | 1.0.7 | accntech | Avalonia design system and component library with shadcn/ui semantics, ported f… |
| 2026-10-14 08:41:13 | [Valitor.DistributedCache](https://www.nuget.org/packages/Valitor.DistributedCache) | 1.11.0 | tabaahi | Valitor.DistributedCache |
| 2026-10-14 08:41:18 | [Valitor.Security.ApiKeyAuthenticator](https://www.nuget.org/packages/Valitor.Security.ApiKeyAuthenticator) | 1.0.6 | tabaahi | Valitor.Security.ApiKeyAuthenticator |
| 2026-10-14 08:41:33 | [Webority.Social](https://www.nuget.org/packages/Webority.Social) | 0.3.1 | Webority Technologies | Social media posting and social analytics a product runs on its own database: a… |
| 2026-10-14 08:41:36 | [Webority.Social.Admin](https://www.nuget.org/packages/Webority.Social.Admin) | 0.3.1 | Webority Technologies | Social pages for Webority admin portals: the publication queue, connected accou… |
| 2026-10-14 08:41:39 | [Webority.Social.Content](https://www.nuget.org/packages/Webority.Social.Content) | 0.3.1 | Webority Technologies | Draft review for social posts a product runs on Webority.Social: drafts with va… |
| 2026-10-14 08:41:45 | [Webority.Social.Content.Ai](https://www.nuget.org/packages/Webority.Social.Content.Ai) | 0.3.1 | Webority Technologies | The AI drafter and grader for Webority.Social.Content drafts: writes each targe… |
| 2026-10-14 08:45:36 | [OfficeAgent.Excel.Calculation](https://www.nuget.org/packages/OfficeAgent.Excel.Calculation) | 1.2.0 | Ilia Sokolov | Optional Excel formula calculation for OfficeAgent.NET: after an edit, calculat… |
| 2026-10-14 08:46:50 | [Intel.ShaderCompiler.D3D12](https://www.nuget.org/packages/Intel.ShaderCompiler.D3D12) | 1.1.0.1019150 | Intel Corporation | Intel D3D12 Advanced Shader Delivery (ASD) Compiler DDI Plugin. Drives ahead-of… |
| 2026-10-14 09:04:34 | [Devlead.Testing.MockHttp.Tool](https://www.nuget.org/packages/Devlead.Testing.MockHttp.Tool) | 2026.10.14.1023 | devlead | .NET global tool that hosts Routes.json as a local mock HTTP API |
| 2026-10-14 09:13:33 | [ONEO.Manta](https://www.nuget.org/packages/ONEO.Manta) | 1.2026.1 | ONEO | Themeable Avalonia controls and an explicit MVVM runtime for cross-platform des… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

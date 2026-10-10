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

## Latest list — 2026-10-10 12:19 UTC

New packages created between 2026-10-10 11:21 UTC and 2026-10-10 12:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-10T12-19-55-50278Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-10 11:24:07 | [ETLBox.AI.Html](https://www.nuget.org/packages/ETLBox.AI.Html) | 3.11.1 | ETLBoxperts GmbH | This is the HTML connector for ETLBox.AI. It converts HTML resources to Markdow… |
| 2026-10-10 11:24:20 | [ETLBox.AI.Pdf](https://www.nuget.org/packages/ETLBox.AI.Pdf) | 3.11.1 | ETLBoxperts GmbH | This is the PDF connector for ETLBox.AI. It reads PDF resources and converts ea… |
| 2026-10-10 11:29:06 | [Mapping_Tools.Core](https://www.nuget.org/packages/Mapping_Tools.Core) | 2.0.0 | Mapping_Tools.Core | Package Description |
| 2026-10-10 11:29:07 | [Mapping_Tools.Application](https://www.nuget.org/packages/Mapping_Tools.Application) | 2.0.0 | Mapping_Tools.Application | Package Description |
| 2026-10-10 11:29:08 | [Mapping_Tools.Infrastructure](https://www.nuget.org/packages/Mapping_Tools.Infrastructure) | 2.0.0 | Mapping_Tools.Infrastructure | Package Description |
| 2026-10-10 11:29:10 | [Mapping_Tools.Desktop](https://www.nuget.org/packages/Mapping_Tools.Desktop) | 2.0.0 | Mapping_Tools.Desktop | Package Description |
| 2026-10-10 11:29:50 | [NetAI.ResxTranslator.Tasks](https://www.nuget.org/packages/NetAI.ResxTranslator.Tasks) | 1.0.1 | Stephan Emmermann | MSBuild-Task zur KI-gestÃ¼tzten Ãœbersetzung von .resx-Ressourcendateien (emine… |
| 2026-10-10 11:41:39 | [Kusachius.Fakedata](https://www.nuget.org/packages/Kusachius.Fakedata) | 1.4.2 | Aldis Arust | Random Lithuanian person, company, and address data for tests and development. |
| 2026-10-10 11:44:44 | [Sezzlee.AspNetCore](https://www.nuget.org/packages/Sezzlee.AspNetCore) | 0.1.0 | Sezzlee.AspNetCore | Embeds an MCP layer into an existing ASP.NET Core backend: search-first tool di… |
| 2026-10-10 11:46:47 | [PageCurl.Core](https://www.nuget.org/packages/PageCurl.Core) | 0.1.0 | Marius Muntean | Platform-independent page-turn interaction, navigation and developable page geo… |
| 2026-10-10 11:47:25 | [PageCurl.Maui](https://www.nuget.org/packages/PageCurl.Maui) | 0.1.0 | Marius Muntean | Interactive stiff-paper page turns for images, live .NET MAUI views and two-pag… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

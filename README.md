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

## Latest list — 2026-10-19 17:22 UTC

New packages created between 2026-10-19 16:20 UTC and 2026-10-19 17:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-19T17-22-24-282289Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-19 16:20:47 | [Moonwell.Objects](https://www.nuget.org/packages/Moonwell.Objects) | 0.1.1 | mdlsvensson | Warcraft III's standard units, abilities, items, buffs and other objects as C#… |
| 2026-10-19 16:20:47 | [Moonwell.Templates](https://www.nuget.org/packages/Moonwell.Templates) | 0.1.1 | mdlsvensson | The Moonwell map project template: dotnet new moonwell. |
| 2026-10-19 16:20:48 | [Moonwell](https://www.nuget.org/packages/Moonwell) | 0.1.1 | mdlsvensson | The Moonwell runtime for Warcraft III maps in C#: units, components, reactions,… |
| 2026-10-19 16:20:48 | [Moonwell.Natives](https://www.nuget.org/packages/Moonwell.Natives) | 0.1.1 | mdlsvensson | Warcraft III's natives as C#, for Moonwell. |
| 2026-10-19 16:20:49 | [Moonwell.Cli](https://www.nuget.org/packages/Moonwell.Cli) | 0.1.1 | mdlsvensson | The moonwell command: builds a Moonwell map project into a Warcraft III map and… |
| 2026-10-19 16:23:49 | [Phoney.WireMock](https://www.nuget.org/packages/Phoney.WireMock) | 1.2.0 | Mattias Sundström | Phoney fake data for WireMock.Net mocks: Response.Create().WithFakeJson(Fake.Fo… |
| 2026-10-19 16:28:00 | [HtmlForgeX.AspNetCore](https://www.nuget.org/packages/HtmlForgeX.AspNetCore) | 2.0.0 | HtmlForgeX.AspNetCore | Package Description |
| 2026-10-19 16:28:02 | [HtmlForgeX.CanopyX](https://www.nuget.org/packages/HtmlForgeX.CanopyX) | 2.0.0 | Przemyslaw Klys | Optional CanopyX integration for HtmlForgeX. Hosts tree grids, flat data grids… |
| 2026-10-19 16:28:05 | [HtmlForgeX.ChartForgeX.Stories](https://www.nuget.org/packages/HtmlForgeX.ChartForgeX.Stories) | 3.0.0 | Przemyslaw Klys | Optional typed story, transcript and completed-image components over ChartForge… |
| 2026-10-19 16:28:07 | [HtmlForgeX.ChartForgeX.Visuals](https://www.nuget.org/packages/HtmlForgeX.ChartForgeX.Visuals) | 3.0.0 | Przemyslaw Klys | Optional static grid and canvas components over ChartForgeX.Visuals for HtmlFor… |
| 2026-10-19 16:28:08 | [HtmlForgeX.CodeGlyphX](https://www.nuget.org/packages/HtmlForgeX.CodeGlyphX) | 2.0.0 | Przemyslaw Klys | Optional CodeGlyphX integration for HtmlForgeX. Renders accessible, theme-aware… |
| 2026-10-19 16:28:10 | [HtmlForgeX.DbaClientX](https://www.nuget.org/packages/HtmlForgeX.DbaClientX) | 2.0.0 | Przemyslaw Klys | Optional DbaClientX integration for HtmlForgeX. Answers report queries (ReportQ… |
| 2026-10-19 16:28:13 | [HtmlForgeX.Pdf](https://www.nuget.org/packages/HtmlForgeX.Pdf) | 2.0.0 | Przemyslaw Klys | Optional PDF export for HtmlForgeX reports: renders the report's print version… |
| 2026-10-19 16:31:16 | [Egami.Barcodes](https://www.nuget.org/packages/Egami.Barcodes) | 1.0.0 | Lars Dytterud | Barcodes for Egami: writes and reads 1D and 2D barcodes, drawn onto Egami.Drawi… |
| 2026-10-19 17:02:51 | [Relevox.Contracts](https://www.nuget.org/packages/Relevox.Contracts) | 1.0.0 | Tunahan Ali Ozturk | Request, notification and handler interfaces for Relevox. No dependencies, so d… |
| 2026-10-19 17:02:52 | [Relevox](https://www.nuget.org/packages/Relevox) | 1.0.0 | Tunahan Ali Ozturk | A mediator for .NET whose dispatch is written by a source generator at build ti… |
| 2026-10-19 17:05:26 | [Xsl3](https://www.nuget.org/packages/Xsl3) | 0.2.0-alpha | Xsl3 contributors | XSLT 3.0, XSLT 2.0 and XPath 3.1 processor for .NET, compiled to IL. Built on t… |
| 2026-10-19 17:08:37 | [rhym](https://www.nuget.org/packages/rhym) | 2026.1019.0 | flustix | An extensible file format for music-based software. |
| 2026-10-19 17:11:28 | [Neph.GenericLibs.Net.CopilotLib](https://www.nuget.org/packages/Neph.GenericLibs.Net.CopilotLib) | 0.1.0 | Neph | GitHub Copilot SDK wrapper with a service, DI registration and a reusable ASP.N… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

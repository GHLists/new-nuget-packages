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

## Latest list — 2026-10-22 20:18 UTC

New packages created between 2026-10-22 19:21 UTC and 2026-10-22 20:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-22T20-18-58-357842Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-22 19:27:46 | [Verstappen](https://www.nuget.org/packages/Verstappen) | 0.1.1 | Diogo Martins | A synchronous HTTP/1.1 server for Linux: one pinned epoll reactor per core, han… |
| 2026-10-22 19:29:37 | [Ninjasoft.ReportCreator](https://www.nuget.org/packages/Ninjasoft.ReportCreator) | 0.0.1-alpha | Ninjasoft | Create labels |
| 2026-10-22 19:31:17 | [RecursiveAI.OneImage.Web](https://www.nuget.org/packages/RecursiveAI.OneImage.Web) | 1.1.0 | Recursive AI, LLC | ASP.NET Core middleware for on-the-fly image processing and caching: resize, cr… |
| 2026-10-22 19:31:43 | [Dapr.Vector](https://www.nuget.org/packages/Dapr.Vector) | 1.19.0 | dapr.io | Dapr Vector SDK for .NET (alpha API). |
| 2026-10-22 19:31:44 | [Dapr.Search](https://www.nuget.org/packages/Dapr.Search) | 1.19.0 | dapr.io | Dapr Search SDK for .NET (alpha API). |
| 2026-10-22 19:31:48 | [Dapr.BinaryStore](https://www.nuget.org/packages/Dapr.BinaryStore) | 1.19.0 | dapr.io | Dapr Binary Store SDK for .NET |
| 2026-10-22 19:37:52 | [Pmad.Markitdown](https://www.nuget.org/packages/Pmad.Markitdown) | 0.0.1 | Julien Etelain | Pure managed .NET library to convert HTML, PDF, and DOCX documents into clean M… |
| 2026-10-22 19:37:52 | [Pmad.MarkdownFetch](https://www.nuget.org/packages/Pmad.MarkdownFetch) | 0.0.1 | Julien Etelain | Small CLI to download any web resource as a markdown (with markitdown-api). |
| 2026-10-22 19:45:51 | [Javxp.MFAAuthenticator](https://www.nuget.org/packages/Javxp.MFAAuthenticator) | 1.0.0 | Javxp.MFAAuthenticator | Package Description |
| 2026-10-22 20:09:55 | [Meteion.Toolkit.Templates](https://www.nuget.org/packages/Meteion.Toolkit.Templates) | 1.8.0 | frogcrush | dotnet new templates for Meteion.Toolkit: a RESX item template, a WPF applicati… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-21 21:21 UTC

New packages created between 2026-10-21 20:19 UTC and 2026-10-21 21:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-21T21-21-46-807334Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-21 20:25:41 | [BorrowedTorch.UI](https://www.nuget.org/packages/BorrowedTorch.UI) | 1.0.0 | Vladyslav Pysarenko | UI framework for MonoGame games on Windows (DesktopGL and WindowsDX): WPF-style… |
| 2026-10-21 20:31:25 | [RifVenezuela](https://www.nuget.org/packages/RifVenezuela) | 0.0.1 | Wilmer Ferreira | Validation, parsing, and formatting for Venezuelan tax identification numbers (… |
| 2026-10-21 20:32:02 | [Umbraco.Community.AI.Pinecone](https://www.nuget.org/packages/Umbraco.Community.AI.Pinecone) | 0.9.0 | Lee Mills | An Umbraco AI embeddings provider that generates vectors with Pinecone's hosted… |
| 2026-10-21 20:39:26 | [Carbon.MicroData](https://www.nuget.org/packages/Carbon.MicroData) | 0.1.0 | Carbon.MicroData | Reads HTML microdata (itemscope, itemprop) into a tree of nodes |
| 2026-10-21 20:41:07 | [AmoosedWeb.Native](https://www.nuget.org/packages/AmoosedWeb.Native) | 0.23.0 | Juhapekka Piiroinen | Native AmoosedWeb reader runtime for Windows x64 .NET applications. |
| 2026-10-21 20:41:15 | [Blazor.AI.MediaPipe](https://www.nuget.org/packages/Blazor.AI.MediaPipe) | 1.2.0 | Gravicode Studios | Real-time computer-vision components for Blazor on MediaPipe.NET (native .NET M… |
| 2026-10-21 20:55:17 | [VpnHood.Manager.Api](https://www.nuget.org/packages/VpnHood.Manager.Api) | 4.0.417 | VpnHood.Manager.Api | VpnHood! MANAGER API |
| 2026-10-21 21:01:58 | [XtudioPdf.Core](https://www.nuget.org/packages/XtudioPdf.Core) | 1.1.0 | TELCOMDEV S.A.C.S. | XtudioPdf engine: JSON template contract and its own layout and PDF engine on S… |
| 2026-10-21 21:02:02 | [XtudioPdf.AspNetCore](https://www.nuget.org/packages/XtudioPdf.AspNetCore) | 1.1.0 | TELCOMDEV S.A.C.S. | XtudioPdf visual designer for ASP.NET Core: drag-and-drop template editor insid… |
| 2026-10-21 21:02:04 | [XtudioPdf.Templates](https://www.nuget.org/packages/XtudioPdf.Templates) | 1.1.0 | TELCOMDEV S.A.C.S. | XtudioPdf document template (dotnet new xtudiopdf): creates the .pdfx template,… |
| 2026-10-21 21:03:23 | [XtudioPdf.Tool](https://www.nuget.org/packages/XtudioPdf.Tool) | 1.1.0 | TELCOMDEV S.A.C.S. | XtudioPdf tool: opens a .pdfx template in the designer (double click from Visua… |
| 2026-10-21 21:05:26 | [Wkp](https://www.nuget.org/packages/Wkp) | 0.6.0 | kodonnell | Well Known Polylines - fast and compact encoding of geometries to strings using… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

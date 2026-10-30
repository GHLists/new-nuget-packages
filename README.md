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

## Latest list — 2026-10-30 18:21 UTC

New packages created between 2026-10-30 17:21 UTC and 2026-10-30 18:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-30T18-21-47-060474Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-30 17:23:40 | [Trexon.Web.Testing](https://www.nuget.org/packages/Trexon.Web.Testing) | 1.1.0 | Trexoncorp | In-process async HTTP and WebSocket testing for Trexon.Web with isolated depend… |
| 2026-10-30 17:31:46 | [Async.Prism.Events.Extensions](https://www.nuget.org/packages/Async.Prism.Events.Extensions) | 1.0.0 | Azat Tazayan | High-performance synchronous and ValueTask-based asynchronous event types for P… |
| 2026-10-30 17:33:10 | [SI.Money](https://www.nuget.org/packages/SI.Money) | 1.3.0 | SI.Informational.Systems | Package Description |
| 2026-10-30 17:43:11 | [Pdfik](https://www.nuget.org/packages/Pdfik) | 0.1.0 | PDFik | Official C# SDK for the PDFik API: URL/HTML/Markdown to PDF, PNG/JPEG screensho… |
| 2026-10-30 18:12:59 | [Fayakun.Security.Cryptography](https://www.nuget.org/packages/Fayakun.Security.Cryptography) | 1.0.0 | Fayakun Services | A lightweight, secure, and zero-dependency .NET cryptography package providing… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

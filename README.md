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

## Latest list — 2026-10-01 23:21 UTC

New packages created between 2026-10-01 22:21 UTC and 2026-10-01 23:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-01T23-21-04-638679Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-01 22:24:01 | [OpenMaui.Controls.Linux.Pdf](https://www.nuget.org/packages/OpenMaui.Controls.Linux.Pdf) | 10.0.110.6 | MarketAlly Pte Ltd, David H.… | PDF page rendering and text extraction for OpenMaui apps on Linux, on Google's… |
| 2026-10-01 22:39:18 | [DotNetSseClient](https://www.nuget.org/packages/DotNetSseClient) | 1.0.0 | Paul Karam | A lightweight, HttpClient-based Server-Sent Events (SSE) client with keyed DI r… |
| 2026-10-01 22:47:35 | [HappyHakunaMatata.Common](https://www.nuget.org/packages/HappyHakunaMatata.Common) | 1.0.0 | Common | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

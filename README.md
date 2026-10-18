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

## Latest list — 2026-10-18 01:19 UTC

New packages created between 2026-10-18 00:18 UTC and 2026-10-18 01:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-18T01-19-11-698584Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-18 00:56:46 | [Webority.Documents](https://www.nuget.org/packages/Webority.Documents) | 0.1.0 | Webority Technologies | Document text extraction (PDF, Word, PowerPoint, HTML, plain text), PDF page la… |
| 2026-10-18 00:56:46 | [Webority.Books](https://www.nuget.org/packages/Webority.Books) | 0.1.0 | Webority Technologies | Books (accounting ledger) contracts for Webority products: reader, writer, e-in… |
| 2026-10-18 00:56:48 | [Webority.Books.Zoho](https://www.nuget.org/packages/Webority.Books.Zoho) | 0.1.0 | Webority Technologies | Zoho Books adapter for Webority.Books: OAuth grants, pacing, resilience and the… |
| 2026-10-18 01:00:43 | [VeriSec](https://www.nuget.org/packages/VeriSec) | 1.0.0 | VeriSec Labs | The official .NET library for the VeriSec API: identity (KYC) and Financial che… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

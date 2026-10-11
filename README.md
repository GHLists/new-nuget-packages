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

## Latest list — 2026-10-11 01:21 UTC

New packages created between 2026-10-11 00:21 UTC and 2026-10-11 01:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-11T01-21-30-693435Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-11 00:22:20 | [CodeBrix.VideoProcessing.Core.MitLicenseForever](https://www.nuget.org/packages/CodeBrix.VideoProcessing.Core.MitLicenseForever) | 1.0.284.20 | Jeremy Ellis | The engine-neutral contract for video processing in .NET: analyse media files,… |
| 2026-10-11 00:54:46 | [Rayscale.Foundation](https://www.nuget.org/packages/Rayscale.Foundation) | 0.1.0 | Rayscale | Foundational abstractions, primitives, and shared utilities |
| 2026-10-11 00:59:52 | [EgyptianToolkit](https://www.nuget.org/packages/EgyptianToolkit) | 1.0.0 | Mahmoud Yusuf | Egypt-focused .NET library for Egyptian national ID parsing and validation, age… |
| 2026-10-11 01:08:41 | [Nur.Store2026.Access](https://www.nuget.org/packages/Nur.Store2026.Access) | 1.0.0 | joseco | Package Description |
| 2026-10-11 01:09:01 | [Nur.Store2026.Access.Catalog](https://www.nuget.org/packages/Nur.Store2026.Access.Catalog) | 1.0.0 | joseco | Package Description |
| 2026-10-11 01:09:14 | [Nur.Store2026.Access.Contracts](https://www.nuget.org/packages/Nur.Store2026.Access.Contracts) | 1.0.0 | joseco | Package Description |
| 2026-10-11 01:09:54 | [Nur.Store2026.Access.Identity](https://www.nuget.org/packages/Nur.Store2026.Access.Identity) | 1.0.0 | joseco | Package Description |
| 2026-10-11 01:10:08 | [Nur.Store2026.Access.Inventory](https://www.nuget.org/packages/Nur.Store2026.Access.Inventory) | 1.0.0 | joseco | Package Description |
| 2026-10-11 01:10:24 | [Nur.Store2026.Access.Orders](https://www.nuget.org/packages/Nur.Store2026.Access.Orders) | 1.0.0 | joseco | Package Description |
| 2026-10-11 01:10:39 | [Nur.Store2026.Access.Payments](https://www.nuget.org/packages/Nur.Store2026.Access.Payments) | 1.0.0 | joseco | Package Description |
| 2026-10-11 01:10:53 | [Nur.Store2026.Security](https://www.nuget.org/packages/Nur.Store2026.Security) | 1.0.0 | joseco | Package Description |
| 2026-10-11 01:11:19 | [Nur.Store2026.Integration](https://www.nuget.org/packages/Nur.Store2026.Integration) | 1.0.0 | joseco | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

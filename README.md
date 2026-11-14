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

## Latest list — 2026-11-14 02:19 UTC

New packages created between 2026-11-14 01:20 UTC and 2026-11-14 02:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-14T02-19-59-996337Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-14 01:26:10 | [MCUnderground.IES.NET](https://www.nuget.org/packages/MCUnderground.IES.NET) | 1.0.0 | MCUnderground | Parse IES LM-63 photometric files and render them to WPF bitmaps. |
| 2026-11-14 01:28:03 | [MxUtilities.AssetManagement](https://www.nuget.org/packages/MxUtilities.AssetManagement) | 1.0.0 | Daniel | Reads and rewrites the external asset list stored in Autodesk 3ds Max (.max) fi… |
| 2026-11-14 01:28:31 | [MxUtilities.Scripting](https://www.nuget.org/packages/MxUtilities.Scripting) | 1.0.0 | Daniel | Discovers running Autodesk 3ds Max instances and sends MAXScript commands to th… |
| 2026-11-14 01:29:01 | [TdbIO](https://www.nuget.org/packages/TdbIO) | 0.1.0 | mahach666 | Reads Tekla Structures model files (.db1, .db2, DBV@ files, id range and GUID m… |
| 2026-11-14 01:29:02 | [TdbIO.Cli](https://www.nuget.org/packages/TdbIO.Cli) | 0.1.0 | mahach666 | Command line tool that reports the structure of Tekla Structures model files, D… |
| 2026-11-14 01:34:00 | [EasyShm](https://www.nuget.org/packages/EasyShm) | 0.0.2 | EasyShm | Package Description |
| 2026-11-14 01:40:47 | [Umbraco.Community.AIProvenance.UmbracoAI](https://www.nuget.org/packages/Umbraco.Community.AIProvenance.UmbracoAI) | 17.0.0 | Liam Goldfinch | Marks content as AI generated or AI modified automatically when Umbraco.AI agen… |
| 2026-11-14 01:40:48 | [Umbraco.Community.AIProvenance](https://www.nuget.org/packages/Umbraco.Community.AIProvenance) | 17.0.0 | Liam Goldfinch | Records where AI was involved in Umbraco content, property by property. Editors… |
| 2026-11-14 01:47:49 | [OpenBarcode](https://www.nuget.org/packages/OpenBarcode) | 2.0.0 | Yoel Nunez | Barcode generation for Code 39, EAN-13 and UPC-A. Returns the bar and space mod… |
| 2026-11-14 01:58:16 | [Sondor.AspNetCore.FluentValidation](https://www.nuget.org/packages/Sondor.AspNetCore.FluentValidation) | 0.1.0 | Sondor Dev | FluentValidation for Sondor.AspNetCore: a ValidationException is answered with… |
| 2026-11-14 02:07:18 | [Usa.Smart.WinUI.Extensions](https://www.nuget.org/packages/Usa.Smart.WinUI.Extensions) | 1.0.0 | machi_pon | Smart WinUI support library |
| 2026-11-14 02:07:19 | [Usa.Smart.WinUI](https://www.nuget.org/packages/Usa.Smart.WinUI) | 1.0.0 | machi_pon | Smart WinUI support library |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

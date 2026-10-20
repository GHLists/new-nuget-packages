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

## Latest list — 2026-10-20 03:20 UTC

New packages created between 2026-10-20 02:21 UTC and 2026-10-20 03:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-20T03-20-03-566712Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-20 02:38:19 | [SiameseCat.Communication](https://www.nuget.org/packages/SiameseCat.Communication) | 0.9.0 | RabitLogic | Industrial communication library for .NET: Modbus RTU/TCP, Siemens S7, pluggabl… |
| 2026-10-20 02:46:38 | [TX.Stdf4Net](https://www.nuget.org/packages/TX.Stdf4Net) | 1.0.0 | TX.Stdf4Net | Package Description |
| 2026-10-20 02:49:56 | [Parlot.SourceGenerator](https://www.nuget.org/packages/Parlot.SourceGenerator) | 2.0.0 | Sebastien Ros | Roslyn source generator for compiling Parlot parser combinators into optimized… |
| 2026-10-20 02:52:59 | [OfficePDF.Sdk](https://www.nuget.org/packages/OfficePDF.Sdk) | 1.0.0 | OfficePDF | OfficePDF — high-fidelity Word to PDF conversion (cloud API and on-premise serv… |
| 2026-10-20 03:02:15 | [YH_SDK_RM_PRINTER](https://www.nuget.org/packages/YH_SDK_RM_PRINTER) | 1.0.0 | YH_SDK_RM_PRINTER | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-01 16:20 UTC

New packages created between 2026-10-01 15:21 UTC and 2026-10-01 16:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-01T16-20-54-34655Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-01 15:26:31 | [Euonia.Security](https://www.nuget.org/packages/Euonia.Security) | 2026.4.3 | damon | Authorization primitives: operation permission requirements and data-scope (row… |
| 2026-10-01 15:43:22 | [TerminalMatrixNetFramework](https://www.nuget.org/packages/TerminalMatrixNetFramework) | 1.0.0 | Anders Hesselbom | A .NET Framework version of Terminal Pixel Matrix Library |
| 2026-10-01 15:58:14 | [Beryllium.Camera](https://www.nuget.org/packages/Beryllium.Camera) | 1.5.1 | Vladyslav Pysarenko | Camera functionality. |
| 2026-10-01 16:04:39 | [ApricotFramework.Agentic.Tools.ErrorDefinitions](https://www.nuget.org/packages/ApricotFramework.Agentic.Tools.ErrorDefinitions) | 0.1.2 | Project Apricot | Describes ApricotFramework.ErrorDefinitions errors thrown by agent tools as Apr… |
| 2026-10-01 16:07:37 | [deniszykov.VCDiff](https://www.nuget.org/packages/deniszykov.VCDiff) | 6.0.0 | Metric,chyyran,Snowflake Auth… | A fast, pure C# implementation of the VCDIFF algorithm. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

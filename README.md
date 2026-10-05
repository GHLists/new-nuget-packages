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

## Latest list — 2026-10-05 20:20 UTC

New packages created between 2026-10-05 19:21 UTC and 2026-10-05 20:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-05T20-20-21-748185Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-05 19:29:56 | [Eternet.Banks.Movements.Firebird.Contracts](https://www.nuget.org/packages/Eternet.Banks.Movements.Firebird.Contracts) | 1.0.0 | Eternet | Gateway contracts for legacy bank movement operations. |
| 2026-10-05 19:51:38 | [DataStar.Tools](https://www.nuget.org/packages/DataStar.Tools) | 3.1.0 | Absolute Technology Limited | DataStar command line interface: builds deployment packages from source control… |
| 2026-10-05 19:52:27 | [Canducci.FileUpload.FluentValidation](https://www.nuget.org/packages/Canducci.FileUpload.FluentValidation) | 1.0.0.3 | Canducci.FileUpload.FluentVal… | Package Description |
| 2026-10-05 19:54:44 | [Serilog.Ui.Domain](https://www.nuget.org/packages/Serilog.Ui.Domain) | 4.0.0 | Mohsen Esmailpour | Simple web UI for several Serilog sinks. |
| 2026-10-05 20:02:12 | [DataStar.Tools.win-x64](https://www.nuget.org/packages/DataStar.Tools.win-x64) | 3.1.0 | Absolute Technology Limited | DataStar command line interface: builds deployment packages from source control… |
| 2026-10-05 20:02:44 | [DataStar.Tools.osx-x64](https://www.nuget.org/packages/DataStar.Tools.osx-x64) | 3.1.0 | Absolute Technology Limited | DataStar command line interface: builds deployment packages from source control… |
| 2026-10-05 20:02:59 | [Brows.Win32.Interop](https://www.nuget.org/packages/Brows.Win32.Interop) | 1.0.0 | Ken Yourek | Package Description |
| 2026-10-05 20:03:00 | [Brows.Win32.Interop.Composition](https://www.nuget.org/packages/Brows.Win32.Interop.Composition) | 1.0.0 | Ken Yourek | Package Description |
| 2026-10-05 20:03:05 | [Brows.Win32.Interop.Operations](https://www.nuget.org/packages/Brows.Win32.Interop.Operations) | 1.0.0 | Ken Yourek | Package Description |
| 2026-10-05 20:03:13 | [DataStar.Tools.osx-arm64](https://www.nuget.org/packages/DataStar.Tools.osx-arm64) | 3.1.0 | Absolute Technology Limited | DataStar command line interface: builds deployment packages from source control… |
| 2026-10-05 20:03:42 | [DataStar.Tools.linux-x64](https://www.nuget.org/packages/DataStar.Tools.linux-x64) | 3.1.0 | Absolute Technology Limited | DataStar command line interface: builds deployment packages from source control… |
| 2026-10-05 20:04:03 | [DataStar.Tools.linux-arm64](https://www.nuget.org/packages/DataStar.Tools.linux-arm64) | 3.1.0 | Absolute Technology Limited | DataStar command line interface: builds deployment packages from source control… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

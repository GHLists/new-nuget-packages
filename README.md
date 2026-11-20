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

## Latest list — 2026-11-20 13:20 UTC

New packages created between 2026-11-20 12:22 UTC and 2026-11-20 13:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-20T13-20-04-729896Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-20 12:28:05 | [csff](https://www.nuget.org/packages/csff) | 0.1.0 | Takumi Kuroda | A fast C# formatter CLI written in F#. |
| 2026-11-20 12:29:31 | [KKDB.Lib.PrinterAbstract](https://www.nuget.org/packages/KKDB.Lib.PrinterAbstract) | 1.0.0 | kkdb | 一个用来把zpl语句发送到打印机的nuget包 抽象 |
| 2026-11-20 12:31:04 | [AIBirthdayVideoGenerator](https://www.nuget.org/packages/AIBirthdayVideoGenerator) | 0.1.0 | AI Birthday Video Generator | AI birthday video generator from a single photo: they pop champagne on a park b… |
| 2026-11-20 12:31:10 | [KKDB.Lib.Printer.Tcp](https://www.nuget.org/packages/KKDB.Lib.Printer.Tcp) | 1.0.0 | kkdb | 一个用来把zpl语句发送到打印机的nuget包 tcp打印机模块 |
| 2026-11-20 12:32:14 | [KKDB.Lib.Printer.Raw](https://www.nuget.org/packages/KKDB.Lib.Printer.Raw) | 1.0.0 | kkdb | 一个用来把zpl语句发送到打印机的nuget包 windown api打印机模块 |
| 2026-11-20 12:32:49 | [KKDB.Lib.Printer.Port](https://www.nuget.org/packages/KKDB.Lib.Printer.Port) | 1.0.0 | kkdb | 一个用来把zpl语句发送到打印机的nuget包 串口打印机模块 |
| 2026-11-20 12:33:13 | [KKDB.Lib.Printer](https://www.nuget.org/packages/KKDB.Lib.Printer) | 1.0.0 | kkdb | 一个用来把zpl语句发送到打印机的nuget包 |
| 2026-11-20 12:40:24 | [SimplePocketBase](https://www.nuget.org/packages/SimplePocketBase) | 0.1.0 | aiinty | Simple asynchronous REST client for PocketBase |
| 2026-11-20 13:00:38 | [XrmMockup.PermissionAnalyzer](https://www.nuget.org/packages/XrmMockup.PermissionAnalyzer) | 1.0.0 | Context& | CLI tool that works out which Dataverse privileges your code needs, by static a… |
| 2026-11-20 13:07:13 | [BindOpen.Messages.Dtos.Models](https://www.nuget.org/packages/BindOpen.Messages.Dtos.Models) | 1.3.1 | Sumer Team | A package to easily deal with feeds. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-10 10:19 UTC

New packages created between 2026-10-10 09:21 UTC and 2026-10-10 10:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-10T10-19-41-576577Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-10 09:22:14 | [potluckdb.runtime.osx](https://www.nuget.org/packages/potluckdb.runtime.osx) | 0.1.0 | potluckdb | potluckdb native runtime assets for macOS and Mac Catalyst |
| 2026-10-10 09:22:24 | [potluckdb.runtime.win](https://www.nuget.org/packages/potluckdb.runtime.win) | 0.1.0 | potluckdb | potluckdb native runtime assets for Windows |
| 2026-10-10 09:22:26 | [potluckdb](https://www.nuget.org/packages/potluckdb) | 0.1.0 | potluckdb | potluckdb application SDK with native runtime assets |
| 2026-10-10 09:35:53 | [NetAI.TestGenerator.Tasks](https://www.nuget.org/packages/NetAI.TestGenerator.Tasks) | 1.0.0 | Stephan Emmermann | MSBuild-Task zum Generieren von KI-gestützten Unit-Tests für .NET-Projekte (emi… |
| 2026-10-10 09:43:17 | [Webority.Insights.Ai](https://www.nuget.org/packages/Webority.Insights.Ai) | 0.2.0 | Webority Technologies | The weekly AI review over a product's Webority Insights rollups: a 28-day pack… |
| 2026-10-10 09:49:40 | [KinTN.CTUWCS.ModbusLib](https://www.nuget.org/packages/KinTN.CTUWCS.ModbusLib) | 1.0.1 | ZhangGuoWei | Modbus TCP / 串口通信库，封装堆垛机(巷道)PLC协议：任务下发(D100-D209)、任务完成信号(D260-D264)、监控/报警/统计数据读… |
| 2026-10-10 09:49:47 | [Balsoft.Hive.Installer.Windows](https://www.nuget.org/packages/Balsoft.Hive.Installer.Windows) | 1.0.0 | Ertugrul Balveren | A Windows installer for .NET products, built in WPF: a per-machine Setup.exe wi… |
| 2026-10-10 09:52:18 | [MaksIT.Core.Desktop](https://www.nuget.org/packages/MaksIT.Core.Desktop) | 0.1.0 | Maksym Sadovnychyy | Shared desktop helpers for MaksIT apps: crash-report text and log files, What's… |
| 2026-10-10 09:52:33 | [MaksIT.Core.UI](https://www.nuget.org/packages/MaksIT.Core.UI) | 0.1.0 | Maksym Sadovnychyy | Avalonia windows shared by MaksIT desktop apps: About, What's New, logs, the cr… |
| 2026-10-10 10:00:27 | [InvoiceXml.Zugferd.XRechnung](https://www.nuget.org/packages/InvoiceXml.Zugferd.XRechnung) | 1.0.0 | InvoiceXML | Create, validate, embed, render and read ZUGFeRD and XRechnung e-invoices from… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

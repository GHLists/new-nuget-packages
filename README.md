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

## Latest list — 2026-10-09 06:20 UTC

New packages created between 2026-10-09 05:18 UTC and 2026-10-09 06:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-09T06-20-20-352766Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-09 05:24:53 | [XAvalonia.Bootstrap](https://www.nuget.org/packages/XAvalonia.Bootstrap) | 0.1.0 | Karen Liliou | XAvalonia shell bootstrap — plugin loader, lifecycle manager, DI wiring, and co… |
| 2026-10-09 05:24:54 | [XAvalonia.IconProviders](https://www.nuget.org/packages/XAvalonia.IconProviders) | 0.1.0 | Karen Liliou | XAvalonia icon providers — Material icon set implementation for IIconProvider. |
| 2026-10-09 05:24:56 | [XAvalonia.LogViewer](https://www.nuget.org/packages/XAvalonia.LogViewer) | 0.1.0 | Karen Liliou | XAvalonia log viewer plugin — Output panel that displays log messages at Debug/… |
| 2026-10-09 05:24:59 | [XAvalonia.MainWindow](https://www.nuget.org/packages/XAvalonia.MainWindow) | 0.1.0 | Karen Liliou | XAvalonia default docking layout plugin — Explorer, Documents, Properties, and… |
| 2026-10-09 05:25:01 | [XAvalonia.PluginBrowser](https://www.nuget.org/packages/XAvalonia.PluginBrowser) | 0.1.0 | Karen Liliou | XAvalonia plugin browser — lists installed plugins, versions, and checks NuGet… |
| 2026-10-09 05:25:07 | [XAvalonia.Shell.Abstractions](https://www.nuget.org/packages/XAvalonia.Shell.Abstractions) | 0.1.0 | Karen Liliou | Plugin contract library for XAvalonia — interfaces and contribution models that… |
| 2026-10-09 05:44:08 | [Kayisoft.Abp.DicomRecycle.Consumer](https://www.nuget.org/packages/Kayisoft.Abp.DicomRecycle.Consumer) | 5.3.7 | virtual | Kayisoft DicomRecycle file deletion consumers |
| 2026-10-09 05:44:12 | [Kayisoft.Abp.DicomRecycle.Consumer.ActiveMQ](https://www.nuget.org/packages/Kayisoft.Abp.DicomRecycle.Consumer.ActiveMQ) | 5.3.7 | virtual | Kayisoft DicomRecycle Module |
| 2026-10-09 05:44:17 | [Kayisoft.Abp.DicomRecycle.Consumer.Kafka](https://www.nuget.org/packages/Kayisoft.Abp.DicomRecycle.Consumer.Kafka) | 5.3.7 | virtual | Kayisoft DicomRecycle Module |
| 2026-10-09 05:44:20 | [Kayisoft.Abp.DicomRecycle.Consumer.PostgreSql](https://www.nuget.org/packages/Kayisoft.Abp.DicomRecycle.Consumer.PostgreSql) | 5.3.7 | virtual | Kayisoft DicomRecycle Module |
| 2026-10-09 05:44:24 | [Kayisoft.Abp.DicomRecycle.Consumer.RabbitMQ](https://www.nuget.org/packages/Kayisoft.Abp.DicomRecycle.Consumer.RabbitMQ) | 5.3.7 | virtual | Kayisoft DicomRecycle Module |
| 2026-10-09 05:44:42 | [Kayisoft.Abp.DicomRecycle.Producer.ActiveMQ](https://www.nuget.org/packages/Kayisoft.Abp.DicomRecycle.Producer.ActiveMQ) | 5.3.7 | virtual | Kayisoft DicomRecycle Module |
| 2026-10-09 05:44:45 | [Kayisoft.Abp.DicomRecycle.Producer.Kafka](https://www.nuget.org/packages/Kayisoft.Abp.DicomRecycle.Producer.Kafka) | 5.3.7 | virtual | Kayisoft DicomRecycle Module |
| 2026-10-09 05:44:50 | [Kayisoft.Abp.DicomRecycle.Producer.PostgreSql](https://www.nuget.org/packages/Kayisoft.Abp.DicomRecycle.Producer.PostgreSql) | 5.3.7 | virtual | Kayisoft DicomRecycle Module |
| 2026-10-09 05:44:57 | [Kayisoft.Abp.DicomRecycle.Producer.RabbitMQ](https://www.nuget.org/packages/Kayisoft.Abp.DicomRecycle.Producer.RabbitMQ) | 5.3.7 | virtual | Kayisoft DicomRecycle Module |
| 2026-10-09 05:45:01 | [Kayisoft.Abp.DicomRecycle.Protocols](https://www.nuget.org/packages/Kayisoft.Abp.DicomRecycle.Protocols) | 5.3.7 | virtual | Kayisoft DicomRecycle Module |
| 2026-10-09 05:49:46 | [Fluence.Wpf](https://www.nuget.org/packages/Fluence.Wpf) | 0.9.2-pre | Dan Cunningham | Windows 11 Fluent Design controls and theming for WPF (.NET Framework 4.7.2, .N… |
| 2026-10-09 06:12:27 | [KillerScan.Engine](https://www.nuget.org/packages/KillerScan.Engine) | 1.8.0 | Steve the Killer | The network scanning engine behind KillerScan: local network detection, ARP and… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

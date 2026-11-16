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

## Latest list — 2026-11-16 06:19 UTC

New packages created between 2026-11-16 05:20 UTC and 2026-11-16 06:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-16T06-19-52-861007Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-16 05:21:19 | [DAABLike](https://www.nuget.org/packages/DAABLike) | 1.0.0 | ysmgthntt | A DAAB-style data access library for .NET and .NET Framework, providing a famil… |
| 2026-11-16 05:24:25 | [IndustrialControls.Avalonia](https://www.nuget.org/packages/IndustrialControls.Avalonia) | 1.0.0 | daipeng0809 | 面向 Avalonia 12 的工业控件库：仪表盘、扇形进度条、竖向进度条、电池电量、指南针、状态灯等，支持高度自定义、AOT 与高帧率数据刷新。 |
| 2026-11-16 05:27:15 | [Bilyk.QwibeeSport.Generic](https://www.nuget.org/packages/Bilyk.QwibeeSport.Generic) | 1.0.0 | Anastasiia Bilyk | Generic entity and repository classes for QWIBEE SPORT |
| 2026-11-16 05:28:47 | [Jakar.Logging.Serilog](https://www.nuget.org/packages/Jakar.Logging.Serilog) | 10.1.0 | Tyler Stegmaier | Jakar.Extensions integration for Jakar.Logging: Serilog properties for AppInfor… |
| 2026-11-16 05:33:23 | [Epsitec.MuGet](https://www.nuget.org/packages/Epsitec.MuGet) | 0.1.3.2647 | Pierre ARNAUD | Develop NuGet packages from their source code inside the solution that consumes… |
| 2026-11-16 05:33:23 | [Epsitec.Muget](https://www.nuget.org/packages/Epsitec.Muget) | 0.1.3.2647 | Pierre ARNAUD | Develop NuGet packages from their source code inside the solution that consumes… |
| 2026-11-16 05:37:13 | [LogMark.Shroud.Cli](https://www.nuget.org/packages/LogMark.Shroud.Cli) | 0.4.0 | LogMark | CLI tool for detecting and masking sensitive data in markdown files. |
| 2026-11-16 05:37:13 | [LogMark.Shroud](https://www.nuget.org/packages/LogMark.Shroud) | 0.4.0 | LogMark | Sensitive data detection and tokenization for text files. Zero dependencies. Au… |
| 2026-11-16 05:41:21 | [NugetVerify](https://www.nuget.org/packages/NugetVerify) | 1.0.0 | NugetVerify | Package Description |
| 2026-11-16 05:44:04 | [ProtocolConversion](https://www.nuget.org/packages/ProtocolConversion) | 0.1.1 | ProtocolConversion Contributo… | 协议转换库（元包）：将一种协议的消息翻译转换为另一种协议的消息。安装本包即包含全部功能：SECS/GEM（Secs4Net）、HTTP、Rpc（gRPC）协议… |
| 2026-11-16 05:44:42 | [WinForms.ExtendedControls](https://www.nuget.org/packages/WinForms.ExtendedControls) | 1.0.0 | DotNet Community | Extended Windows Forms Controls and UI components for modern desktop applicatio… |
| 2026-11-16 05:44:58 | [WinForms.Components.Extensions](https://www.nuget.org/packages/WinForms.Components.Extensions) | 1.0.0 | DotNet Community | Windows Forms reusable component extensions and reactive controls. |
| 2026-11-16 05:52:48 | [ProngsFaints.JsxCore](https://www.nuget.org/packages/ProngsFaints.JsxCore) | 1.0.4.1 | David Whitney | A TSX/JSX view engine for ASP.NET Core. Write views as .tsx or .jsx files and r… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

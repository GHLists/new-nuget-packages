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

## Latest list — 2026-11-07 10:19 UTC

New packages created between 2026-11-07 09:20 UTC and 2026-11-07 10:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-07T10-19-48-966101Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-07 09:29:30 | [ZL.IotDriver](https://www.nuget.org/packages/ZL.IotDriver) | 2.2.18 | UseThink | 【读法B】ZL.IotHub 自研驱动的独立程序集（58 个协议描述符）。只依赖 ZL.IotEngine 的契约面，不依赖任何编排实现。 |
| 2026-11-07 09:29:55 | [ZL.IotEngine](https://www.nuget.org/packages/ZL.IotEngine) | 2.2.18 | UseThink | 工业 PLC 数据采集运行时内核（.NET：netstandard2.0 / net48 / net8.0 / net10.0）——编排、地址合并、批量采集、… |
| 2026-11-07 09:30:14 | [ZL.IotHub.Ipc](https://www.nuget.org/packages/ZL.IotHub.Ipc) | 2.2.18 | UseThink | 工业 IPC 传输抽象（命名管道行协议）：提供行客户端/服务端/发布订阅接口与 NamedPipe 实现，供跨进程采集与工具链复用。零第三方依赖（仅 Syst… |
| 2026-11-07 09:31:06 | [ZL.IotOss](https://www.nuget.org/packages/ZL.IotOss) | 2.2.18 | UseThink | ZL.IotEngine 的开源驱动适配包：S7.Net Plus（西门子）/ NModbus 3.x（Modbus TCP/RTU/ASCII）/ LibP… |
| 2026-11-07 09:31:21 | [Doppelganger.Isolation](https://www.nuget.org/packages/Doppelganger.Isolation) | 0.13.0 | Niklas Wendel | Doppelganger.Isolation - mock non-virtual members and sealed classes with Doppe… |
| 2026-11-07 09:33:33 | [SQMD.Reports](https://www.nuget.org/packages/SQMD.Reports) | 0.3.4 | SQUAREMILED S.A. | SQMD Reports report engine: YAML definitions to HTML, PDF (Chromium), Word, Exc… |
| 2026-11-07 09:33:33 | [SQMD.Reports.Server](https://www.nuget.org/packages/SQMD.Reports.Server) | 0.3.4 | SQUAREMILED S.A. | SQMD Reports for ASP.NET Core: IReportRenderer, REST API, embedded web viewer a… |
| 2026-11-07 09:41:19 | [Ryn.Plugins.Sidecar](https://www.nuget.org/packages/Ryn.Plugins.Sidecar) | 0.39.0 | Moh | Identity-safe managed sidecar lifecycle services with crash-owned native proces… |
| 2026-11-07 09:47:17 | [Fp.SharePoint](https://www.nuget.org/packages/Fp.SharePoint) | 0.2.0 | Financial Partners | Upload, download, delete and list files in a SharePoint document library via Mi… |
| 2026-11-07 09:47:23 | [Maplibre.NativeFfi.Runtime.OpenGL.MinGW](https://www.nuget.org/packages/Maplibre.NativeFfi.Runtime.OpenGL.MinGW) | 0.202611.0 | MapLibre | OpenGL.MinGW native runtime assets for MapLibre Native .NET. |
| 2026-11-07 09:47:29 | [Maplibre.NativeFfi.Runtime.Vulkan.MinGW](https://www.nuget.org/packages/Maplibre.NativeFfi.Runtime.Vulkan.MinGW) | 0.202611.0 | MapLibre | Vulkan.MinGW native runtime assets for MapLibre Native .NET. |
| 2026-11-07 09:47:44 | [tomware.Cyclo](https://www.nuget.org/packages/tomware.Cyclo) | 0.1.0 | Thomas Duft | A command-line tool for calculating the cyclomatic complexity of code. |
| 2026-11-07 09:49:20 | [Glacier.Cluster](https://www.nuget.org/packages/Glacier.Cluster) | 1.1.0 | Ian Cowley | Pure C# .NET 10 distributed computing fabric, dynamic DAG scheduler, zero-alloc… |
| 2026-11-07 09:52:35 | [Glacier.Cli](https://www.nuget.org/packages/Glacier.Cli) | 1.1.0 | Ian Cowley | Unified pure C# .NET 10 LLM command-line application (glacier). High-performanc… |
| 2026-11-07 09:54:52 | [NotRemoting](https://www.nuget.org/packages/NotRemoting) | 0.0.6 | osexpert, Hagen Siegel | Grpc (Not)Remoting library for migration from .NET Remoting |
| 2026-11-07 09:54:54 | [NotRemoting.Compression.Lz4](https://www.nuget.org/packages/NotRemoting.Compression.Lz4) | 0.0.6 | osexpert | Grpc (Not)Remoting library for migration from .NET Remoting |
| 2026-11-07 09:54:56 | [NotRemoting.Serialization.BinaryFormatter](https://www.nuget.org/packages/NotRemoting.Serialization.BinaryFormatter) | 0.0.6 | osexpert, Hagen Siegel | Grpc (Not)Remoting library for migration from .NET Remoting |
| 2026-11-07 09:54:58 | [NotRemoting.Serialization.Json](https://www.nuget.org/packages/NotRemoting.Serialization.Json) | 0.0.6 | osexpert | Grpc (Not)Remoting library for migration from .NET Remoting |
| 2026-11-07 09:55:00 | [NotRemoting.Serialization.MemoryPack](https://www.nuget.org/packages/NotRemoting.Serialization.MemoryPack) | 0.0.6 | osexpert | Grpc (Not)Remoting library for migration from .NET Remoting |
| 2026-11-07 09:55:02 | [NotRemoting.Serialization.MessagePack](https://www.nuget.org/packages/NotRemoting.Serialization.MessagePack) | 0.0.6 | osexpert | Grpc (Not)Remoting library for migration from .NET Remoting |
| 2026-11-07 09:55:04 | [NotRemoting.Serialization.Protobuf](https://www.nuget.org/packages/NotRemoting.Serialization.Protobuf) | 0.0.6 | osexpert | Grpc (Not)Remoting library for migration from .NET Remoting |
| 2026-11-07 09:55:44 | [Coworkee.Client.Blazor.ClientEntities.Sqlite](https://www.nuget.org/packages/Coworkee.Client.Blazor.ClientEntities.Sqlite) | 0.0.1.65 | fgilde | Client entities in SQLite inside the browser: the server sends the copy as a SQ… |
| 2026-11-07 10:02:50 | [Dav](https://www.nuget.org/packages/Dav) | 3.0.1 | Aizaz Zaheen | Checks a .NET assembly without running it: risky API calls, known vulnerabiliti… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-12 09:19 UTC

New packages created between 2026-11-12 08:20 UTC and 2026-11-12 09:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-12T09-19-08-295194Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-12 08:24:55 | [Cratis.Templates.Extensions](https://www.nuget.org/packages/Cratis.Templates.Extensions) | 1.9.0 | Cratis | Templates for Cratis extension packages: a full extension (an OCI package with… |
| 2026-11-12 08:29:58 | [Box2D.NET.Fork](https://www.nuget.org/packages/Box2D.NET.Fork) | 0.1.0 | ice1000 | Box2D.NET - Box2D.NET - a port of Box2D, is a 2D physics engine for games, .NET… |
| 2026-11-12 08:33:04 | [Fickl.Sdk](https://www.nuget.org/packages/Fickl.Sdk) | 0.10.0 | Alfonso García-Caro Núñez,Fab… | Fickl.Sdk: compile F# to JavaScript and the other Fickl targets as part of dotn… |
| 2026-11-12 08:34:17 | [DubUrl.Provider.Hive](https://www.nuget.org/packages/DubUrl.Provider.Hive) | 0.66.0 | Cédric L. Charlier | Apache Hive database metadata for DubUrl. |
| 2026-11-12 08:34:24 | [DubUrl.Provider.Spark](https://www.nuget.org/packages/DubUrl.Provider.Spark) | 0.66.0 | Cédric L. Charlier | Apache Spark and Databricks database metadata for DubUrl. |
| 2026-11-12 08:34:51 | [Vot.Update.Client](https://www.nuget.org/packages/Vot.Update.Client) | 1.0.0 | VOT | VOT 自动更新客户端库。支持 .NET Framework 4.5~4.8.1 与 .NET 6/7/8/9/10，WinForms 与 WPF 通用（更新… |
| 2026-11-12 08:51:06 | [CvSharp.DL](https://www.nuget.org/packages/CvSharp.DL) | 1.0.0 | GreatBear | SharpDL — 纯卷积深度学习框架（C#）：语义分割 / 目标检测 / 多分类训练与推理，支持 Vulkan GPU 加速与 ONNX 导出。提供 Tra… |
| 2026-11-12 08:53:57 | [Devart.Data.BigQuery](https://www.nuget.org/packages/Devart.Data.BigQuery) | 1.0.248 | Devart | dotConnect for Google BigQuery is an ADO.NET provider for working with Google B… |
| 2026-11-12 08:54:00 | [Devart.Data.BigQuery.EFCore](https://www.nuget.org/packages/Devart.Data.BigQuery.EFCore) | 1.0.248.11 | Devart | dotConnect for Google BigQuery is an ADO.NET provider for working with Google B… |
| 2026-11-12 08:56:08 | [Devart.Data.MongoDB](https://www.nuget.org/packages/Devart.Data.MongoDB) | 1.0.248 | Devart | dotConnect for MongoDB is an ADO.NET data provider for MongoDB. Its built-in SQ… |
| 2026-11-12 08:56:11 | [Devart.Data.MongoDB.EFCore](https://www.nuget.org/packages/Devart.Data.MongoDB.EFCore) | 1.0.248.11 | Devart | dotConnect for MongoDB is an ADO.NET data provider for MongoDB. Its built-in SQ… |
| 2026-11-12 08:59:35 | [Crosswalk.Core](https://www.nuget.org/packages/Crosswalk.Core) | 0.1.0 | James Mann | Runs Crosswalk maps in .NET: JSON-to-JSON mappings drawn in the Crosswalk edito… |
| 2026-11-12 09:00:09 | [QwenZImage.NET](https://www.nuget.org/packages/QwenZImage.NET) | 0.1.0 | dongfangzhizhu | High-performance .NET 10 P/Invoke wrapper over the stable qzi C ABI for Qwen-Im… |
| 2026-11-12 09:00:46 | [MyConsoleApp_symas](https://www.nuget.org/packages/MyConsoleApp_symas) | 1.0.0 | MyConsoleApp | Package Description |
| 2026-11-12 09:04:48 | [MapFlux.DependencyInjection](https://www.nuget.org/packages/MapFlux.DependencyInjection) | 1.0.0 | Kadir Demirkaya | Service collection registration for MapFlux: one AddMapFlux call registers a si… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

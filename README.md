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

## Latest list — 2026-11-19 08:20 UTC

New packages created between 2026-11-19 07:22 UTC and 2026-11-19 08:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-19T08-20-15-07961Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-19 07:24:27 | [dotnet-crap](https://www.nuget.org/packages/dotnet-crap) | 0.2.0 | dotnet-crap contributors | Code quality analysis for .NET projects. |
| 2026-11-19 07:31:58 | [Webority.Email.Abstractions](https://www.nuget.org/packages/Webority.Email.Abstractions) | 0.93.0 | Webority Technologies | The email records a product's domain layer may link to, with no EF Core and no… |
| 2026-11-19 07:32:58 | [BlobStorage.Client](https://www.nuget.org/packages/BlobStorage.Client) | 1.0.3 | Ankit Chodavadiya | Client SDK for the BlobStorage service. Provides BlobServiceClient (project-sco… |
| 2026-11-19 07:34:02 | [x86cc.KVBind.Schema](https://www.nuget.org/packages/x86cc.KVBind.Schema) | 0.2.2 | Stefan Szakal | A serializer-neutral POCO description of a KVBind model definition (fields, gro… |
| 2026-11-19 07:41:25 | [ApeFree.ApeLog](https://www.nuget.org/packages/ApeFree.ApeLog) | 0.1.0 | Guijie Lee | 轻量级、解耦且高性能的 .NET 日志记录框架。基于观察者模式提供极简的 API，自动捕获调用方行号与源码元数据，内置控制台与缓冲文件写入，无缝协同 STTe… |
| 2026-11-19 07:41:37 | [ApeFree.ApeLog.Controls](https://www.nuget.org/packages/ApeFree.ApeLog.Controls) | 0.1.0 | Guijie Lee | ApeFree.ApeLog 的 Windows Forms UI 界面日志扩展库，提供无闪烁、支持富文本着色与同色合并批处理的 LogTextBox 控件与… |
| 2026-11-19 07:42:15 | [M.Simple.Services.Interception](https://www.nuget.org/packages/M.Simple.Services.Interception) | 1.0.0.1 | Mr.Sunny | Interface method interception with synchronous and asynchronous hooks for .NET… |
| 2026-11-19 07:46:57 | [IGzip.Bindings](https://www.nuget.org/packages/IGzip.Bindings) | 1.0.0 | Kamron Batman | Intel ISA-L igzip bindings for .NET 10+: one-shot zlib, raw deflate and gzip ov… |
| 2026-11-19 07:48:56 | [EntityJson.DevToys](https://www.nuget.org/packages/EntityJson.DevToys) | 1.0.0 | EntityJson | Convert entity classes (C# first) into JSON request bodies. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-17 14:19 UTC

New packages created between 2026-11-17 13:20 UTC and 2026-11-17 14:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-17T14-19-46-783777Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-17 13:25:32 | [SpeartonCS.ExtendedGenerics](https://www.nuget.org/packages/SpeartonCS.ExtendedGenerics) | 1.0.0 | SpeartonCS | Modern .NET 10 crossplatform library, compatible with NativeAOT, and containing… |
| 2026-11-17 13:27:54 | [VirtuaMesh.WireGuard.NET](https://www.nuget.org/packages/VirtuaMesh.WireGuard.NET) | 1.0.0 | VirtuaMesh | Pure .NET WireGuard implementation: Noise_IKpsk2 handshake, ChaCha20-Poly1305 t… |
| 2026-11-17 13:30:12 | [RuleKit.Analyzer](https://www.nuget.org/packages/RuleKit.Analyzer) | 0.1.0 | samueldias21 | RuleKit.Analyzer: Roslyn Analyzer configurável que valida padrões arquiteturais… |
| 2026-11-17 13:30:12 | [RuleKit.Cli](https://www.nuget.org/packages/RuleKit.Cli) | 0.1.0 | samueldias21 | RuleKit.Cli (arch-rules): ferramenta de linha de comando que valida o arch-rule… |
| 2026-11-17 13:36:06 | [Dloizides.SignInPage.AspNetCore](https://www.nuget.org/packages/Dloizides.SignInPage.AspNetCore) | 1.0.0 | DLoizides | Brand-neutral server-rendered sign-in page for ASP.NET Core: email + password f… |
| 2026-11-17 13:39:13 | [OpenDCP.Framework.Connections.Core](https://www.nuget.org/packages/OpenDCP.Framework.Connections.Core) | 0.5.1 | OpenDCP.Framework.Connections… | Package Description |
| 2026-11-17 13:39:51 | [RDCore.Forms](https://www.nuget.org/packages/RDCore.Forms) | 0.1.0-alpha | 9562-7303 Québec inc. | RDForms' form model, with no UI dependency: component classes, their properties… |
| 2026-11-17 13:45:23 | [MrSquirrely.Flags](https://www.nuget.org/packages/MrSquirrely.Flags) | 1.0.0 | MrSquirrely | A Blazor component that renders CSS-animated waving flags: LGBTQ+ pride, countr… |
| 2026-11-17 13:46:44 | [Kazo.Os.AppSdk.Testing](https://www.nuget.org/packages/Kazo.Os.AppSdk.Testing) | 3.5.0 | Benoit Robin | Kazo OS App SDK test kit: the public conformance suite of a network drive provi… |
| 2026-11-17 13:47:02 | [Kazo.Os.Platform.CloudDrives](https://www.nuget.org/packages/Kazo.Os.Platform.CloudDrives) | 3.5.0 | Benoit Robin | The cloud drive connectors shipped with Kazo OS (Dropbox, OneDrive, S3), mounte… |
| 2026-11-17 13:57:09 | [SoftwareMadeSimple.spgen](https://www.nuget.org/packages/SoftwareMadeSimple.spgen) | 1.0.0 | spgen | Package Description |
| 2026-11-17 14:00:09 | [Orsak.Remoting.AspNetCore](https://www.nuget.org/packages/Orsak.Remoting.AspNetCore) | 0.9.0 | Johannes Sandgren | Serves the members of an interface to Orsak.Remoting's clients, from ASP.NET Co… |
| 2026-11-17 14:00:10 | [Orsak.Remoting](https://www.nuget.org/packages/Orsak.Remoting) | 0.9.0 | Johannes Sandgren | Calls the members of an interface on a server, from .NET or Fable: the wire for… |
| 2026-11-17 14:05:06 | [Gadamaxi.BackendWork](https://www.nuget.org/packages/Gadamaxi.BackendWork) | 0.1.0 | pughua | 自研后台任务框架核心库：即时/延时/连续任务、Cron 周期任务、批量任务、Saga 分布式事务编排；存储层可插拔（关系库 / MongoDB）。 |
| 2026-11-17 14:06:13 | [Gadamaxi.BackendWork.Mongodb](https://www.nuget.org/packages/Gadamaxi.BackendWork.Mongodb) | 0.1.0 | pughua | Gadamaxi.BackendWork 的 MongoDB 存储实现（MongoDB.Driver）。多文档事务需副本集或分片集群，单机 standalon… |
| 2026-11-17 14:06:36 | [Gadamaxi.BackendWork.Dashboard](https://www.nuget.org/packages/Gadamaxi.BackendWork.Dashboard) | 0.1.0 | pughua | Gadamaxi.BackendWork 监控控制面板：内嵌 DLL 的 Web 面板 + 共享宿主鉴权的 HTTP API |
| 2026-11-17 14:07:27 | [Bashka.Plugins.Market](https://www.nuget.org/packages/Bashka.Plugins.Market) | 1.0.4 | Evgeny Gorbovoy | Bashka plugin package catalog. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-27 07:20 UTC

New packages created between 2026-11-27 06:19 UTC and 2026-11-27 07:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-27T07-20-47-190817Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-27 06:27:34 | [VisioForge.CrossPlatform.ElevenLabs.Windows.arm64](https://www.nuget.org/packages/VisioForge.CrossPlatform.ElevenLabs.Windows.arm64) | 2026.11.26 | VisioForge | ElevenLabs integration package for VisioForge .NET SDKs. |
| 2026-11-27 06:41:42 | [CogniChain.Agents](https://www.nuget.org/packages/CogniChain.Agents) | 0.4.0 | Wouter Nijenhuis (DevDad.net) | Bridges CogniChain chains to the Microsoft Agent Framework: run a chain as an A… |
| 2026-11-27 06:50:46 | [TCIS.SharedKernel](https://www.nuget.org/packages/TCIS.SharedKernel) | 1.4.1 | TCIS Core Community and Contr… | TCIS Core Framework is an application framework for building modular, multi-ten… |
| 2026-11-27 06:51:34 | [TlsWebSocket](https://www.nuget.org/packages/TlsWebSocket) | 1.0.1 | Wujindong | 精简的 WebSocket 客户端类库，结构仿照 websocket-sharp。传输层使用 TcpClient + BouncyCastle TLS 并显式… |
| 2026-11-27 06:59:32 | [LockrAuth](https://www.nuget.org/packages/LockrAuth) | 1.0.0 | LockrAuth Team | Official LockrAuth C# (.NET) SDK with automated hardware ID (HWID) locking and… |
| 2026-11-27 07:04:10 | [MyName.SourceG1](https://www.nuget.org/packages/MyName.SourceG1) | 1.0.1 | MyName | 为 partial 类的常量生成 GetConstXxx() 静态方法的 C# 源生成器。 |
| 2026-11-27 07:06:00 | [Soluling.AspNet](https://www.nuget.org/packages/Soluling.AspNet) | 1.0.84 | Soluling | Soluling's ASP.NET Core library: over-the-air translation updates from Soluling… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

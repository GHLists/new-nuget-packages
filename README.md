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

## Latest list — 2026-10-16 18:19 UTC

New packages created between 2026-10-16 17:19 UTC and 2026-10-16 18:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-16T18-19-20-306391Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-16 17:27:28 | [NFe.Danfe.PdfSharp](https://www.nuget.org/packages/NFe.Danfe.PdfSharp) | 1.0.0 | Bruno Moreno (bsmoreno2910),A… | Gerador de DANFE NFe modelo 55 em PDF, sem SixLabors.ImageSharp. Fork do Danfe.… |
| 2026-10-16 17:32:36 | [wordnet.Fonts](https://www.nuget.org/packages/wordnet.Fonts) | 1.1.0 | wordnet.Fonts | OFL-licensed Liberation, Carlito and Caladea fallback font resources for wordne… |
| 2026-10-16 17:32:39 | [wordnet.Ocr](https://www.nuget.org/packages/wordnet.Ocr) | 1.1.0 | wordnet.Ocr | Optional native PDF import and local English OCR providers for wordnet. Managed… |
| 2026-10-16 17:36:12 | [NsdRpc](https://www.nuget.org/packages/NsdRpc) | 0.1.0 | Chase Huegel | A zero-dependency nsd based C# RPC framework and library. |
| 2026-10-16 17:36:14 | [NsdRpc.Generators](https://www.nuget.org/packages/NsdRpc.Generators) | 0.1.0 | Chase Huegel | Source generator for NsdRpc: emits typed service clients from [RpcService] inte… |
| 2026-10-16 17:36:15 | [NsdRpc.Tcp](https://www.nuget.org/packages/NsdRpc.Tcp) | 0.1.0 | Chase Huegel | A TCP transport for the nsd-rpc framework. |
| 2026-10-16 17:44:13 | [Hipcall.Sdk.Deneme](https://www.nuget.org/packages/Hipcall.Sdk.Deneme) | 1.0.2 | Abdulvahap Fansa, Hipcall | Hipcall API'leri ile entegrasyon sağlamak için resmi C# .NET 8 SDK'si. OAuth2 d… |
| 2026-10-16 17:54:29 | [Timbn.GraveyardKeeperTwo.Core](https://www.nuget.org/packages/Timbn.GraveyardKeeperTwo.Core) | 2.0.0 | Timbn | Shared framework for Graveyard Keeper 2 (BepInEx 5) mods. A plugin base class w… |
| 2026-10-16 18:02:06 | [Msixpkg.Build](https://www.nuget.org/packages/Msixpkg.Build) | 0.1.0 | Elipese568 | Build-time MSBuild task that packs a signed single-project MSIX into a .msixpkg… |
| 2026-10-16 18:06:22 | [qianshipoi.FlowLauncher.Plugin.S3](https://www.nuget.org/packages/qianshipoi.FlowLauncher.Plugin.S3) | 1.0.4 | qianshipoi | Flow Launcher 插件：S3 兼容对象存储文件上传、下载、浏览与元数据管理。 |
| 2026-10-16 18:08:24 | [EmbedIO-Neo.Jwt](https://www.nuget.org/packages/EmbedIO-Neo.Jwt) | 2.2.0 | William Smith,EmbedIO contrib… | Optional explicit-key JWT bearer validation for EmbedIO-Neo. |
| 2026-10-16 18:11:50 | [BbQ.Outcome.AspNetCore](https://www.nuget.org/packages/BbQ.Outcome.AspNetCore) | 1.2.0 | Jean | Explicit HTTP and Problem Details mapping for BbQ.Outcome. |
| 2026-10-16 18:11:50 | [BbQ.Outcome.Diagnostics](https://www.nuget.org/packages/BbQ.Outcome.Diagnostics) | 1.2.0 | Jean | Opt-in structured logging and Activity instrumentation for BbQ.Outcome. |
| 2026-10-16 18:11:51 | [BbQ.Outcome.SystemTextJson](https://www.nuget.org/packages/BbQ.Outcome.SystemTextJson) | 1.2.0 | Jean | Explicit, Native AOT-compatible System.Text.Json contracts for BbQ.Outcome. |
| 2026-10-16 18:13:12 | [BbQ.Cqrs.Outcome](https://www.nuget.org/packages/BbQ.Cqrs.Outcome) | 1.3.0 | Jean | Optional type-safe validation behaviors and response factories for BbQ.Cqrs and… |
| 2026-10-16 18:13:13 | [BbQ.Cqrs.Outcome.FluentValidation](https://www.nuget.org/packages/BbQ.Cqrs.Outcome.FluentValidation) | 1.3.0 | Jean | Async FluentValidation adapter for BbQ.Cqrs Outcome validation. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

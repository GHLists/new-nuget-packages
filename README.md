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

## Latest list — 2026-10-29 16:19 UTC

New packages created between 2026-10-29 15:22 UTC and 2026-10-29 16:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-29T16-19-49-595709Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-29 15:25:43 | [NSail.Storage.WebApi](https://www.nuget.org/packages/NSail.Storage.WebApi) | 0.1.400 | Leonardo Porro,Emmanuel Arias | NSail.Storage.WebApi, part of NSail Stack: a .NET modular-monolith framework (m… |
| 2026-10-29 15:25:45 | [NSail.Storage.Shared](https://www.nuget.org/packages/NSail.Storage.Shared) | 0.1.400 | Leonardo Porro,Emmanuel Arias | NSail.Storage.Shared, part of NSail Stack: a .NET modular-monolith framework (m… |
| 2026-10-29 15:25:46 | [NSail.Storage.Sdk](https://www.nuget.org/packages/NSail.Storage.Sdk) | 0.1.400 | Leonardo Porro,Emmanuel Arias | NSail.Storage.Sdk, part of NSail Stack: a .NET modular-monolith framework (mess… |
| 2026-10-29 15:25:48 | [NSail.Storage.FileSystem](https://www.nuget.org/packages/NSail.Storage.FileSystem) | 0.1.400 | Leonardo Porro,Emmanuel Arias | NSail.Storage.FileSystem, part of NSail Stack: a .NET modular-monolith framewor… |
| 2026-10-29 15:25:51 | [NSail.Storage.S3](https://www.nuget.org/packages/NSail.Storage.S3) | 0.1.400 | Leonardo Porro,Emmanuel Arias | NSail.Storage.S3, part of NSail Stack: a .NET modular-monolith framework (messa… |
| 2026-10-29 15:29:39 | [Superroute.SApp](https://www.nuget.org/packages/Superroute.SApp) | 0.1.1 | Goodneo Solutions | sApp for .NET: sign-in, the platform app API and Open Platform capabilities, fo… |
| 2026-10-29 15:36:23 | [Ybd.AbpLite.AI](https://www.nuget.org/packages/Ybd.AbpLite.AI) | 1.0.0 | ybd | ABP 模块：用 Ai 配置节注册 OpenAI 兼容的默认工作区，并从该工作区创建 Microsoft.Agents.AI 的 Agent。不含聊天接口，也… |
| 2026-10-29 15:38:07 | [ReiA](https://www.nuget.org/packages/ReiA) | 0.0.0.1 | Shiranai | ReliableUdp transport |
| 2026-10-29 15:40:29 | [Lombiq.MSBuild.OrchardCore.Tests.UI.Library.Sdk](https://www.nuget.org/packages/Lombiq.MSBuild.OrchardCore.Tests.UI.Library.Sdk) | 2.1.1 | Lombiq Technologies | MSBuild SDK for reusable UI test libraries using Lombiq.Tests.UI. |
| 2026-10-29 15:46:41 | [InventiveRhythm.fluXis](https://www.nuget.org/packages/InventiveRhythm.fluXis) | 2026.1029.0 | fluXis.Shared | A community-driven rhythm game with a focus on creativity and expression. |
| 2026-10-29 15:47:59 | [MohsinArif.XrmToolBox.FormWiringValidator](https://www.nuget.org/packages/MohsinArif.XrmToolBox.FormWiringValidator) | 1.0.0 | Mohsin Arif | Finds form script problems that nothing else reports: a handler calling a funct… |
| 2026-10-29 15:55:52 | [E2eStarter.Playwright](https://www.nuget.org/packages/E2eStarter.Playwright) | 1.3.0 | Nikola Perisic | Playwright for .NET + xUnit v3 test infrastructure: one browser per run, an iso… |
| 2026-10-29 15:55:53 | [E2eStarter.Reporters](https://www.nuget.org/packages/E2eStarter.Reporters) | 1.3.0 | Nikola Perisic | dotnet tool that turns a TRX test result plus Playwright failure evidence into… |
| 2026-10-29 15:55:54 | [E2eStarter.AspNetCore](https://www.nuget.org/packages/E2eStarter.AspNetCore) | 1.3.0 | Nikola Perisic | Add a Playwright test dashboard to your ASP.NET Core API: endpoints to start UI… |
| 2026-10-29 15:57:48 | [Dwain.RibbonLib](https://www.nuget.org/packages/Dwain.RibbonLib) | 1.0.0-net10 | DwainSnickles,Jose Menendez P… | Office-style ribbon control for Windows Forms on .NET 8 or 10, with working out… |
| 2026-10-29 15:59:13 | [NetEvolve.HealthChecks.Milvus](https://www.nuget.org/packages/NetEvolve.HealthChecks.Milvus) | 5.17.351 | NetEvolve, samtrion | Contains HealthChecks for Milvus, based on the nuget package `Milvus.Client`. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

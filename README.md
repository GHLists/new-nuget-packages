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

## Latest list — 2026-10-17 16:19 UTC

New packages created between 2026-10-17 15:19 UTC and 2026-10-17 16:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-17T16-19-50-314493Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-17 15:30:19 | [Ybd.AbpLite.Jwt](https://www.nuget.org/packages/Ybd.AbpLite.Jwt) | 1.0.0 | ybd | ABP 模块：开箱即用的 JWT 签发与校验。过期时间可按秒/分/时/天/月/年配置，可通过继承 JwtModel 把自己的对象存进 token，不带任何用户… |
| 2026-10-17 15:30:22 | [Ybd.AbpLite.Configuration](https://www.nuget.org/packages/Ybd.AbpLite.Configuration) | 1.0.0 | ybd | 把配置拆成多个 JSON 文件（例如 Configs/oss.json、Configs/pay.json）并自动加载：目录、文件、环境后缀都可配置，优先级正确… |
| 2026-10-17 15:31:01 | [LithoSharp.CodeFixes](https://www.nuget.org/packages/LithoSharp.CodeFixes) | 2.0.0 | LithoSharp.CodeFixes | Conservative IDE fixes for generated LithoSharp page references. Requires the m… |
| 2026-10-17 15:31:02 | [LithoSharp.Analyzers](https://www.nuget.org/packages/LithoSharp.Analyzers) | 2.0.0 | Htkym | Compiler-safe LithoSharp static API and HTML interpolation context diagnostics. |
| 2026-10-17 15:32:15 | [fksegundo.Hangfire.Dashboard.JobSearch](https://www.nuget.org/packages/fksegundo.Hangfire.Dashboard.JobSearch) | 1.1.0 | fksegundo | Hangfire Dashboard extension: searchable, filterable, sortable job indexing wit… |
| 2026-10-17 15:35:41 | [Hexalith.Works.Contracts](https://www.nuget.org/packages/Hexalith.Works.Contracts) | 1.0.1 | Hexalith Contributors | Stable Hexalith Works contract types for work item commands, events, query mode… |
| 2026-10-17 15:35:43 | [Hexalith.Works.Server](https://www.nuget.org/packages/Hexalith.Works.Server) | 1.0.1 | Hexalith Contributors | Hexalith work item domain module for .NET |
| 2026-10-17 15:35:45 | [Hexalith.Works.Projections](https://www.nuget.org/packages/Hexalith.Works.Projections) | 1.0.1 | Hexalith Contributors | Hexalith work item domain module for .NET |
| 2026-10-17 15:35:46 | [Hexalith.Works.Reactor](https://www.nuget.org/packages/Hexalith.Works.Reactor) | 1.0.1 | Hexalith Contributors | Hexalith work item domain module for .NET |
| 2026-10-17 15:35:48 | [Hexalith.Works.Testing](https://www.nuget.org/packages/Hexalith.Works.Testing) | 1.0.1 | Hexalith Contributors | Hexalith work item domain module for .NET |
| 2026-10-17 15:42:44 | [Ybd.AbpLite.Template](https://www.nuget.org/packages/Ybd.AbpLite.Template) | 1.3.0 | ybd | ABP 8.3.4 分层后端脚手架（干净起步，不含用户 / 登录业务）：MySQL / SQL Server 可选，JWT（独立包 Ybd.AbpLite.J… |
| 2026-10-17 15:57:41 | [Brows.Win32.STAThreadPool.Composition](https://www.nuget.org/packages/Brows.Win32.STAThreadPool.Composition) | 1.4.0 | Ken Yourek | Composition factory contract for a reusable single-threaded apartment thread po… |
| 2026-10-17 15:57:42 | [Brows.Win32.STAThreadPool.Composition.Exports](https://www.nuget.org/packages/Brows.Win32.STAThreadPool.Composition.Exports) | 1.4.0 | Ken Yourek | The Windows factory for a reusable single-threaded apartment thread pool. The i… |
| 2026-10-17 16:06:37 | [GameBanking](https://www.nuget.org/packages/GameBanking) | 0.5.0 | GameBanking | Server-side SDK for the Game Banking Engine API. |
| 2026-10-17 16:10:08 | [reeutils](https://www.nuget.org/packages/reeutils) | 1.6.0 | reeutils | RE Engine pak and resource tooling, including an MCP server for AI coding assis… |
| 2026-10-17 16:11:45 | [CodeBrix.LibGit2.MitLicenseForever](https://www.nuget.org/packages/CodeBrix.LibGit2.MitLicenseForever) | 1.0.290.970 | Jeremy Ellis | A managed .NET wrapper around the libgit2 native Git library, with the native l… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

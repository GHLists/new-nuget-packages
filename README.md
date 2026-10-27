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

## Latest list — 2026-10-27 07:18 UTC

New packages created between 2026-10-27 06:21 UTC and 2026-10-27 07:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-27T07-18-58-613173Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-27 06:28:39 | [ilspycmd.win-x64](https://www.nuget.org/packages/ilspycmd.win-x64) | 11.2.0.10050 | ILSpy Team | Command-line decompiler using the ILSpy decompilation engine |
| 2026-10-27 06:29:05 | [ilspycmd.linux-x64](https://www.nuget.org/packages/ilspycmd.linux-x64) | 11.2.0.10050 | ILSpy Team | Command-line decompiler using the ILSpy decompilation engine |
| 2026-10-27 06:29:23 | [ilspycmd.any](https://www.nuget.org/packages/ilspycmd.any) | 11.2.0.10050 | ILSpy Team | Command-line decompiler using the ILSpy decompilation engine |
| 2026-10-27 06:41:02 | [RecursiveAI.OneGame.Particles](https://www.nuget.org/packages/RecursiveAI.OneGame.Particles) | 1.4.0 | Recursive AI, LLC | Particle emitters: a seedable, allocation-free simulation for sparks, smoke, du… |
| 2026-10-27 06:42:22 | [DicomKit](https://www.nuget.org/packages/DicomKit) | 1.0.0 | PrologicSign Technology | High-throughput, low-allocation, fuzz-resistant DICOM toolkit for .NET: Part 10… |
| 2026-10-27 06:42:25 | [DicomKit.Imaging](https://www.nuget.org/packages/DicomKit.Imaging) | 1.0.0 | PrologicSign Technology | Decode and render DICOM images with DicomKit: native and compressed pixel data… |
| 2026-10-27 06:42:28 | [DicomKit.Web](https://www.nuget.org/packages/DicomKit.Web) | 1.0.0 | PrologicSign Technology | DICOMweb for DicomKit: DICOM JSON Model and Native DICOM Model (XML) serializer… |
| 2026-10-27 06:42:31 | [DicomKit.Web.AspNetCore](https://www.nuget.org/packages/DicomKit.Web.AspNetCore) | 1.0.0 | PrologicSign Technology | DICOMweb (PS3.18) server building blocks for ASP.NET Core on DicomKit: app.MapD… |
| 2026-10-27 06:42:35 | [DicomKit.Cli](https://www.nuget.org/packages/DicomKit.Cli) | 1.0.0 | PrologicSign Technology | Free command-line tool built on DicomKit: C-ECHO, C-STORE, C-FIND (Patient / St… |
| 2026-10-27 06:42:38 | [DicomKit.Activator](https://www.nuget.org/packages/DicomKit.Activator) | 1.0.1 | PrologicSign Technology | Activates DicomKit licenses on the machine that runs your application: shows th… |
| 2026-10-27 07:05:02 | [WoW2.Sdk.Beta.Be.Identity.Auth](https://www.nuget.org/packages/WoW2.Sdk.Beta.Be.Identity.Auth) | 10.0.0-beta | WoW 2.0 | Identity edge: cookie and API-key authentication, allowlist authorization, gues… |
| 2026-10-27 07:05:02 | [WoW2.Sdk.Beta.Be.Identity.Providers](https://www.nuget.org/packages/WoW2.Sdk.Beta.Be.Identity.Providers) | 10.0.0-beta | WoW 2.0 | Identity providers: OAuth sign-in with 17 upstream providers, the Google ID-tok… |
| 2026-10-27 07:05:03 | [WoW2.Sdk.Beta.Be.Identity.Testing](https://www.nuget.org/packages/WoW2.Sdk.Beta.Be.Identity.Testing) | 10.0.0-beta | WoW 2.0 | Identity test kit: fakes over the Identity contract and the conformance bases e… |
| 2026-10-27 07:05:03 | [WoW2.Sdk.Beta.Be.Identity.Server](https://www.nuget.org/packages/WoW2.Sdk.Beta.Be.Identity.Server) | 10.0.0-beta | WoW 2.0 | Identity server: the OIDC provider role the Identity service runs over the Form… |
| 2026-10-27 07:05:03 | [WoW2.Sdk.Beta.Be.Identity.Module](https://www.nuget.org/packages/WoW2.Sdk.Beta.Be.Identity.Module) | 10.0.0-beta | WoW 2.0 | Identity Form 1: user accounts and their slices, OTP over email, SMS, Telegram… |
| 2026-10-27 07:05:04 | [WoW2.Sdk.Beta.Be.Identity.Client](https://www.nuget.org/packages/WoW2.Sdk.Beta.Be.Identity.Client) | 10.0.0-beta | WoW 2.0 | Identity Forms 2 and 3: the OIDC client (Authorization Code + PKCE) a product s… |
| 2026-10-27 07:05:04 | [WoW2.Sdk.Beta.Be.Identity.Abstractions](https://www.nuget.org/packages/WoW2.Sdk.Beta.Be.Identity.Abstractions) | 10.0.0-beta | WoW 2.0 | Identity contract: the error codes and their ru/uz texts, and the organization… |
| 2026-10-27 07:08:58 | [Easy.WorkFlow.Abstractions](https://www.nuget.org/packages/Easy.WorkFlow.Abstractions) | 1.0.0 | Easy.WorkFlow contributors | 工作流核心抽象：上下文、步骤、执行结果、回调与存储接口，供其他项目引用。 |
| 2026-10-27 07:09:08 | [Easy.WorkFlow.Definitions](https://www.nuget.org/packages/Easy.WorkFlow.Definitions) | 1.0.0 | Easy.WorkFlow contributors | 声明式工作流定义加载：把 JSON/YAML 文档编译成可执行的流程模型，并校验步骤和条件名称。 |
| 2026-10-27 07:09:11 | [Easy.WorkFlow.Runtime](https://www.nuget.org/packages/Easy.WorkFlow.Runtime) | 1.0.0 | Easy.WorkFlow contributors | 工作流运行时：执行引擎、检查点持久化、断点恢复、审批、取消、补偿、跨进程租约、动态跳转、循环、子流程、扇出、原生步骤、自动恢复、终态清理和内置遥测。 |
| 2026-10-27 07:09:16 | [Easy.WorkFlow.Storage.EntityFrameworkCore](https://www.nuget.org/packages/Easy.WorkFlow.Storage.EntityFrameworkCore) | 1.0.0 | Easy.WorkFlow contributors | 基于 Entity Framework Core 的工作流存储：提供与数据库提供程序无关的 DbContext、实例存储、跨进程租约、远程取消和终态清理，迁移… |
| 2026-10-27 07:09:19 | [Easy.WorkFlow.Storage.Sqlite](https://www.nuget.org/packages/Easy.WorkFlow.Storage.Sqlite) | 1.0.0 | Easy.WorkFlow contributors | SQLite 工作流存储：原子创建实例、持久化检查点，通过数据库租约支持多进程安全执行，并支持跨节点远程取消请求。 |
| 2026-10-27 07:09:47 | [Tawfir.Tafqit](https://www.nuget.org/packages/Tawfir.Tafqit) | 1.0.2 | wael EL azizy | Spell plain numbers, currency amounts, and ages in Arabic, English, Persian, an… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

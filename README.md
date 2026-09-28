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

## Latest list — 2026-09-28 08:22 UTC

New packages created between 2026-09-28 07:22 UTC and 2026-09-28 08:22 UTC.

[Full CSV](data/new-nuget-packages-2026-09-28T08-22-04-196326Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-28 07:42:56 | [Tansr.Sdk](https://www.nuget.org/packages/Tansr.Sdk) | 0.1.0.2 | Tansr | Tansr Serve 原生 .NET 协议、会话与终端能力 SDK。 |
| 2026-09-28 07:43:51 | [Tansr.Sdk.Windows](https://www.nuget.org/packages/Tansr.Sdk.Windows) | 0.1.0.2 | Tansr | Tansr .NET SDK 的 Windows 文件、进程与本地安全存储适配。 |
| 2026-09-28 07:44:05 | [TIEG.SystemOne.LLamaSharp](https://www.nuget.org/packages/TIEG.SystemOne.LLamaSharp) | 1.0.0 | The Intelligent Enterprise Gr… | Sub-100ms deterministic decision routing and VRAM management for LLamaSharp. De… |
| 2026-09-28 07:44:56 | [AustinHarris.JsonRpc.Newtonsoft](https://www.nuget.org/packages/AustinHarris.JsonRpc.Newtonsoft) | 2.0.0 | Austin Harris | Json.NET serializer for AustinHarris.JsonRpc. Uses JsonSerializerSettings for c… |
| 2026-09-28 07:44:57 | [AustinHarris.JsonRpc.SystemTextJson](https://www.nuget.org/packages/AustinHarris.JsonRpc.SystemTextJson) | 2.0.0 | Austin Harris | System.Text.Json serializer for AustinHarris.JsonRpc. Reads UTF-8 parameters an… |
| 2026-09-28 07:44:58 | [AustinHarris.JsonRpc.AspNetCore](https://www.nuget.org/packages/AustinHarris.JsonRpc.AspNetCore) | 2.0.0 | Austin Harris | ASP.NET Core hosting for AustinHarris.JsonRpc. Adds HTTP endpoints and raw Kest… |
| 2026-09-28 07:46:49 | [OrielWeb](https://www.nuget.org/packages/OrielWeb) | 0.1.0 | OrielWeb Contributors | OrielWeb — 类 Tauri 的 C# 跨平台系统 webview 核心库。无 C++ 中间层、无 GUI 框架依赖、Native AOT 友好、零反… |
| 2026-09-28 07:54:29 | [Zaya.PluginManager.Impl](https://www.nuget.org/packages/Zaya.PluginManager.Impl) | 1.0.0 | SHTrassEr | Host plugin pipeline for Zaya: zip extract, catalog, GitHub updates. Not an App… |
| 2026-09-28 07:58:39 | [Polhem.Api.AspNetCore](https://www.nuget.org/packages/Polhem.Api.AspNetCore) | 1.0.0 | Polhem contributors | Provides a JSON-RPC 2.0 API controller for ASP.NET Core, serving as a unified e… |
| 2026-09-28 07:58:40 | [Polhem.Api.Client](https://www.nuget.org/packages/Polhem.Api.Client) | 1.0.0 | Polhem contributors | Connector for local or remote invocation of backend logic. |
| 2026-09-28 07:58:41 | [Polhem.Api.Contracts](https://www.nuget.org/packages/Polhem.Api.Contracts) | 1.0.0 | Polhem contributors | Defines the interface contracts for the API layer, serving as the boundary betw… |
| 2026-09-28 07:58:42 | [Polhem.Api.Core](https://www.nuget.org/packages/Polhem.Api.Core) | 1.0.0 | Polhem contributors | The JSON-RPC 2.0 layer of the Polhem framework: request and response messages,… |
| 2026-09-28 07:58:44 | [Polhem.Base](https://www.nuget.org/packages/Polhem.Base) | 1.0.0 | Polhem contributors | Base infrastructure for the Polhem framework, including collections, serializat… |
| 2026-09-28 07:58:45 | [Polhem.Business](https://www.nuget.org/packages/Polhem.Business) | 1.0.0 | Polhem contributors | Implements core business logic and application-level workflows. |
| 2026-09-28 07:58:47 | [Polhem.Cli](https://www.nuget.org/packages/Polhem.Cli) | 1.0.0 | Polhem contributors | Polhem framework CLI, a dotnet tool invoked as `dotnet polhem`. Writes out and… |
| 2026-09-28 07:58:48 | [Polhem.Db](https://www.nuget.org/packages/Polhem.Db) | 1.0.0 | Polhem contributors | Database abstraction with dynamic command generation and connection binding. |
| 2026-09-28 07:58:50 | [Polhem.Definition](https://www.nuget.org/packages/Polhem.Definition) | 1.0.0 | Polhem contributors | The definition types of the Polhem framework (settings, form and table schemas,… |
| 2026-09-28 07:58:51 | [Polhem.Expressions](https://www.nuget.org/packages/Polhem.Expressions) | 1.0.0 | Polhem contributors | Portable expression evaluation engine (DynamicExpresso-backed) shared by the bu… |
| 2026-09-28 07:58:52 | [Polhem.Hosting](https://www.nuget.org/packages/Polhem.Hosting) | 1.0.0 | Polhem contributors | Composition root for the Polhem framework. Registers backend services into any… |
| 2026-09-28 07:58:53 | [Polhem.ObjectCaching](https://www.nuget.org/packages/Polhem.ObjectCaching) | 1.0.0 | Polhem contributors | Runtime caching of definitions and related system data to improve performance. |
| 2026-09-28 07:58:54 | [Polhem.Repository](https://www.nuget.org/packages/Polhem.Repository) | 1.0.0 | Polhem contributors | Provides common repository base classes and data access mechanisms. |
| 2026-09-28 07:58:56 | [Polhem.Repository.Abstractions](https://www.nuget.org/packages/Polhem.Repository.Abstractions) | 1.0.0 | Polhem contributors | Defines the interface contracts for the business layer to access the data layer… |
| 2026-09-28 07:58:57 | [Polhem.UI.Avalonia](https://www.nuget.org/packages/Polhem.UI.Avalonia) | 1.0.0 | Polhem contributors | Avalonia control library for Polhem: FormSchema-driven UI for desktop, browser… |
| 2026-09-28 07:58:59 | [Polhem.UI.Core](https://www.nuget.org/packages/Polhem.UI.Core) | 1.0.0 | Polhem contributors | Manages client-server connection settings and states. |
| 2026-09-28 07:59:00 | [Polhem.Web.Blazor.Server](https://www.nuget.org/packages/Polhem.Web.Blazor.Server) | 1.0.0 | Polhem contributors | Blazor Server component library for Polhem: FormSchema-driven UI that calls the… |
| 2026-09-28 08:05:59 | [DocWright.Reporting.Export](https://www.nuget.org/packages/DocWright.Reporting.Export) | 1.1.3 | DocWright contributors | File exports for DocWright reports, lowered from the paginated page model: DOCX… |
| 2026-09-28 08:06:05 | [DocWright.Reporting.Rdl](https://www.nuget.org/packages/DocWright.Reporting.Rdl) | 1.1.3 | DocWright contributors | Reads and writes SSRS / Power BI paginated report definitions (.rdl, .rdlc) for… |
| 2026-09-28 08:06:07 | [DocWright.Formats.Xlsx](https://www.nuget.org/packages/DocWright.Formats.Xlsx) | 1.1.3 | DocWright contributors | SpreadsheetML (.xlsx) writing for DocWright: a dependency-free, byte-determinis… |
| 2026-09-28 08:06:18 | [DocWright.Reporting](https://www.nuget.org/packages/DocWright.Reporting) | 1.1.3 | DocWright contributors | Report definitions for DocWright: a mutable, lossless object model for SSRS / P… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

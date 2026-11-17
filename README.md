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

## Latest list — 2026-11-17 20:20 UTC

New packages created between 2026-11-17 19:20 UTC and 2026-11-17 20:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-17T20-20-43-689816Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-17 19:21:16 | [LinqPadCosmosDB](https://www.nuget.org/packages/LinqPadCosmosDB) | 0.0.1 | LinqPadCosmosDB | Azure Cosmos DB for NoSQL driver for LINQPad 7 and 9. |
| 2026-11-17 19:22:05 | [MinApiLib.Oidc.JwtBearer](https://www.nuget.org/packages/MinApiLib.Oidc.JwtBearer) | 1.0.0 | MinApiLib.Oidc.JwtBearer | DPoP (RFC 9449) for ASP.NET Core JWT bearer authentication: accepts Authorizati… |
| 2026-11-17 19:22:06 | [MinApiLib.Oidc.Http](https://www.nuget.org/packages/MinApiLib.Oidc.Http) | 1.0.0 | MinApiLib.Oidc.Http | Access tokens for HttpClient without ASP.NET Core: client credentials tokens se… |
| 2026-11-17 19:22:07 | [MinApiLib.Oidc.Authentication](https://www.nuget.org/packages/MinApiLib.Oidc.Authentication) | 1.0.0 | MinApiLib.Oidc.Authentication | The signed-in user's access tokens for HttpClient in ASP.NET Core: keeps the to… |
| 2026-11-17 19:22:08 | [MinApiLib.Oidc.DPoP](https://www.nuget.org/packages/MinApiLib.Oidc.DPoP) | 1.0.0 | MinApiLib.Oidc.DPoP | DPoP (RFC 9449) building blocks shared by clients, resource servers and MinApiL… |
| 2026-11-17 19:22:09 | [MinApiLib.Oidc.Server](https://www.nuget.org/packages/MinApiLib.Oidc.Server) | 1.0.0 | MinApiLib.Oidc.Server | OpenID Connect and OAuth 2.0 server for ASP.NET Core built on MinApiLib endpoin… |
| 2026-11-17 19:22:10 | [MinApiLib.Oidc.Server.MongoDB](https://www.nuget.org/packages/MinApiLib.Oidc.Server.MongoDB) | 1.0.0 | MinApiLib.Oidc.Server.MongoDB | MongoDB stores for MinApiLib.Oidc.Server: clients, resources, CORS origins, per… |
| 2026-11-17 19:28:38 | [AsmFoundation.Toolchain.win-x64](https://www.nuget.org/packages/AsmFoundation.Toolchain.win-x64) | 0.1.0 | Eli Belash | The assembler and linker AsmFoundation.Sdk runs on win-x64 build machines: NASM… |
| 2026-11-17 19:28:41 | [AsmFoundation.Toolchain.linux-x64](https://www.nuget.org/packages/AsmFoundation.Toolchain.linux-x64) | 0.1.0 | Eli Belash | The assembler and linker AsmFoundation.Sdk runs on linux-x64 build machines: NA… |
| 2026-11-17 19:28:43 | [AsmFoundation.Toolchain.osx-arm64](https://www.nuget.org/packages/AsmFoundation.Toolchain.osx-arm64) | 0.1.0 | Eli Belash | The assembler and linker AsmFoundation.Sdk runs on osx-arm64 build machines: NA… |
| 2026-11-17 19:28:44 | [AsmFoundation.Sdk](https://www.nuget.org/packages/AsmFoundation.Sdk) | 0.1.0 | Eli Belash | Enterprise-grade project, dependency and build management for x86-64 assembly,… |
| 2026-11-17 19:33:48 | [Mapsui.Avalonia12](https://www.nuget.org/packages/Mapsui.Avalonia12) | 5.2.0 | Mapsui Developers | Avalonia 12 map components based on the Mapsui library |
| 2026-11-17 19:35:02 | [OSK.Petra.Godot.Experiences](https://www.nuget.org/packages/OSK.Petra.Godot.Experiences) | 0.1.0 | BlankDev117 | Provides an implementation for an game experience (quest, objective) tracking,… |
| 2026-11-17 19:36:46 | [AStarDev.LoggingExtensions](https://www.nuget.org/packages/AStarDev.LoggingExtensions) | 0.7.2 | Jason Barden | This package contains extension methods designed to add OpenTelemetry logging,… |
| 2026-11-17 19:48:25 | [PulseAnalytics.DataProcessor.Contracts](https://www.nuget.org/packages/PulseAnalytics.DataProcessor.Contracts) | 1.0.0 | Ilya Ovsyannikov | Message contracts of the events published by the Pulse Analytics Data Processor. |
| 2026-11-17 19:52:16 | [OmniEurope.Diagnostics.Core](https://www.nuget.org/packages/OmniEurope.Diagnostics.Core) | 1.2.0 | OmniEurope contributors | The host-agnostic part of OmniEurope.Diagnostics, without the ASP.NET Core shar… |
| 2026-11-17 19:52:19 | [OmniEurope.Diagnostics.Maui](https://www.nuget.org/packages/OmniEurope.Diagnostics.Maui) | 1.2.0 | OmniEurope contributors | The .NET MAUI Blazor Hybrid integration of OmniEurope.Diagnostics (Windows): on… |
| 2026-11-17 19:54:42 | [TencentCloudSDK.Makers](https://www.nuget.org/packages/TencentCloudSDK.Makers) | 3.0.1536 | Tencent Cloud API Team | Tencent Cloud API 3.0 SDK for .NET |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-20 15:20 UTC

New packages created between 2026-10-20 14:20 UTC and 2026-10-20 15:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-20T15-20-15-324723Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-20 14:21:50 | [UniOne](https://www.nuget.org/packages/UniOne) | 2.1.3 | UniOne | UniOne Web API client library for .NET |
| 2026-10-20 14:21:55 | [AllAgent.NET.Terminal](https://www.nuget.org/packages/AllAgent.NET.Terminal) | 1.0.8 | AllAgent.NET | AllAgent.NET terminal AI agent with Hyperlight microVM CodeAct execution for Wi… |
| 2026-10-20 14:21:58 | [AllAgent.NET.Terminal.arm64](https://www.nuget.org/packages/AllAgent.NET.Terminal.arm64) | 1.0.8 | AllAgent.NET | AllAgent.NET terminal AI agent with CodeAct execution for Windows ARM64. |
| 2026-10-20 14:23:02 | [Transitio.Logging](https://www.nuget.org/packages/Transitio.Logging) | 1.4.0 | Transitio | Structured, correlation-aware logging context on top of Microsoft.Extensions.Lo… |
| 2026-10-20 14:25:33 | [CoinSelection](https://www.nuget.org/packages/CoinSelection) | 0.1.0 | Dávid Molnár,CoinSelection co… | Dependency-free, deterministic coin selection for integer-valued candidates, wi… |
| 2026-10-20 14:27:55 | [CoinSelection.NBitcoin](https://www.nuget.org/packages/CoinSelection.NBitcoin) | 0.1.0 | Dávid Molnár,CoinSelection co… | NBitcoin adapter for changeless payment coin selection, with fee rates, caller-… |
| 2026-10-20 14:33:32 | [UniOne.AspNetCore](https://www.nuget.org/packages/UniOne.AspNetCore) | 2.1.3 | UniOne | UniOne Web API for ASP.NET Core: API client in DI, webhook endpoint |
| 2026-10-20 14:33:53 | [Wirtschaftsspionage](https://www.nuget.org/packages/Wirtschaftsspionage) | 1.0.0 | AscendantWare e.K. | Ihre Anwendung weiß mehr, als sie zugibt. |
| 2026-10-20 14:37:40 | [Theneo.AspNetCore](https://www.nuget.org/packages/Theneo.AspNetCore) | 0.1.0 | Theneo | ASP.NET Core integration for the Theneo API Reference viewer. Serve a beautiful… |
| 2026-10-20 14:37:51 | [CohoCms.Codegen](https://www.nuget.org/packages/CohoCms.Codegen) | 2026.1.0 | Coho CMS | Generates a typed content library from your Coho CMS content types. |
| 2026-10-20 14:37:52 | [CohoCms.Templates](https://www.nuget.org/packages/CohoCms.Templates) | 2026.1.0 | Coho CMS | dotnet new coho-library: creates your Coho CMS content library, a .NET library… |
| 2026-10-20 14:37:52 | [CohoCms.Delivery](https://www.nuget.org/packages/CohoCms.Delivery) | 2026.1.0 | Coho CMS | The Coho CMS delivery client, and the runtime that generated content libraries… |
| 2026-10-20 14:44:10 | [CohoCms.Razor](https://www.nuget.org/packages/CohoCms.Razor) | 2026.1.0 | Coho CMS | Razor components and tag helpers for Coho CMS content: images resized at the ed… |
| 2026-10-20 14:48:21 | [Musictopia2.CommonBasicLibraries](https://www.nuget.org/packages/Musictopia2.CommonBasicLibraries) | 10.0.1 | musictopia | This has lots of common standard libraries New Collection Classes, Extensions,… |
| 2026-10-20 14:55:09 | [NuVersions](https://www.nuget.org/packages/NuVersions) | 0.3.0 | Alastair Lundy | Unlist NuGet package versions programmatically with ease. |
| 2026-10-20 15:07:54 | [Tooq.Tech.MD.BinaryProtocol](https://www.nuget.org/packages/Tooq.Tech.MD.BinaryProtocol) | 3.5.4 | Tooq Technology S.A. | Tooq Technology Market Data Binary Protocol |
| 2026-10-20 15:08:44 | [Tooq.Tech.FH.ClientLib](https://www.nuget.org/packages/Tooq.Tech.FH.ClientLib) | 8.0.1 | Tooq Technology S.A. | Tooq FH C# Client Library |
| 2026-10-20 15:10:58 | [Umbraco.Community.UmbraDesktop.Services.Arcade](https://www.nuget.org/packages/Umbraco.Community.UmbraDesktop.Services.Arcade) | 17.4.0 | Luuk Peters | High scores and leaderboards for UmbraDesktop games. A service package: you get… |
| 2026-10-20 15:10:59 | [Umbraco.Community.UmbraDesktop.Services.Media](https://www.nuget.org/packages/Umbraco.Community.UmbraDesktop.Services.Media) | 17.4.0 | Luuk Peters | Opening and saving media library files for UmbraDesktop apps. A service package… |
| 2026-10-20 15:13:04 | [Delta3.ByteSize](https://www.nuget.org/packages/Delta3.ByteSize) | 1.0.0 | Lucas Teles - me@lucasteles.d… | Represents a byte size value |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

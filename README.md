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

## Latest list — 2026-11-15 00:19 UTC

New packages created between 2026-11-14 23:21 UTC and 2026-11-15 00:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-15T00-19-24-566174Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-14 23:23:56 | [LlmsInk](https://www.nuget.org/packages/LlmsInk) | 0.1.0 | Lucas Espindola | Client for llms.ink: turn any public link (a site, docs page, GitHub repo, PDF… |
| 2026-11-14 23:27:01 | [StorageC](https://www.nuget.org/packages/StorageC) | 0.1.0 | StorageC | High-performance .NET SMB2/3 client backed by libsmb2. |
| 2026-11-14 23:28:55 | [AotServiceProvider](https://www.nuget.org/packages/AotServiceProvider) | 1.0.0 | cherepets | Automatically discover and register services at compile time. |
| 2026-11-14 23:48:24 | [EggMapper.Analyzers](https://www.nuget.org/packages/EggMapper.Analyzers) | 2.2.0 | Eggspot | Roslyn analyzers for EggMapper runtime API. Catches missing AssertConfiguration… |
| 2026-11-14 23:48:32 | [Ritten.Npm](https://www.nuget.org/packages/Ritten.Npm) | 0.30.0 | Tom Wolfe | npm projects for Ritten workflows: install, lint, build and test. |
| 2026-11-15 00:03:03 | [Mcp.Client.Net](https://www.nuget.org/packages/Mcp.Client.Net) | 1.0.0 | Keerthi RB | A lightweight, zero-dependency .NET 10 Model Context Protocol (MCP) Client libr… |
| 2026-11-15 00:03:11 | [OmniBuf.ProtocGen](https://www.nuget.org/packages/OmniBuf.ProtocGen) | 0.1.0 | OmniBuf Contributors | Protobuf compiler plugin generating OmniBuf C# codecs and Opaque header-hop vie… |
| 2026-11-15 00:03:12 | [OmniBuf](https://www.nuget.org/packages/OmniBuf) | 0.1.0 | OmniBuf Contributors | Self-delimiting, SIMD-friendly binary serialization format for .NET 8. |
| 2026-11-15 00:08:57 | [Mtsc.Functional.Analyzers](https://www.nuget.org/packages/Mtsc.Functional.Analyzers) | 0.1.0 | Matheus Leal | Roslyn analyzers for Mtsc.Functional: discarded Result/Option values, async lam… |
| 2026-11-15 00:08:58 | [Mtsc.Functional.AspNetCore](https://www.nuget.org/packages/Mtsc.Functional.AspNetCore) | 0.1.0 | Matheus Leal | Turns Mtsc.Functional Results into ASP.NET Core Minimal API results (IResult /… |
| 2026-11-15 00:08:59 | [Mtsc.Functional.Testing](https://www.nuget.org/packages/Mtsc.Functional.Testing) | 0.1.0 | Matheus Leal | Test-framework-neutral assertions (ShouldSucceed, ShouldFailWith, ShouldBeSome.… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

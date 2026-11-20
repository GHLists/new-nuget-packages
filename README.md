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

## Latest list — 2026-11-20 12:22 UTC

New packages created between 2026-11-20 11:22 UTC and 2026-11-20 12:22 UTC.

[Full CSV](data/new-nuget-packages-2026-11-20T12-22-12-866132Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-20 11:32:09 | [Digizuite.Sdk.Attributes](https://www.nuget.org/packages/Digizuite.Sdk.Attributes) | 6.7.0 | Digizuite.Sdk.Attributes | Package Description |
| 2026-11-20 11:33:08 | [bora399.CacheShield.Application](https://www.nuget.org/packages/bora399.CacheShield.Application) | 1.0.0 | Bora Saltık | Hybrid L1/L2 caching orchestration with fail-open Redis handling and origin-awa… |
| 2026-11-20 11:33:09 | [bora399.CacheShield.Core](https://www.nuget.org/packages/bora399.CacheShield.Core) | 1.0.0 | Bora Saltık | Core contracts, O(1) thread-safe LRU cache, and singleflight stampede lock for… |
| 2026-11-20 11:33:10 | [bora399.CacheShield.Extensions.DependencyInjection](https://www.nuget.org/packages/bora399.CacheShield.Extensions.DependencyInjection) | 1.0.0 | Bora Saltık | Dependency injection extensions (AddCacheShield) and option validation for Cach… |
| 2026-11-20 11:33:11 | [bora399.CacheShield.Infrastructure.Redis](https://www.nuget.org/packages/bora399.CacheShield.Infrastructure.Redis) | 1.0.0 | Bora Saltık | StackExchange.Redis L2 cache, Pub/Sub backplane, and UTF-8 JSON serializer for… |
| 2026-11-20 11:35:06 | [EasyTypeFactory.HyperbeeExpressionCompiler](https://www.nuget.org/packages/EasyTypeFactory.HyperbeeExpressionCompiler) | 1.0.1 | banator99 | EasyTypeFactory helps you with creating types fluently in .NET. |
| 2026-11-20 11:35:07 | [EasyTypeFactory](https://www.nuget.org/packages/EasyTypeFactory) | 1.0.1 | banator99 | EasyTypeFactory helps you with creating types fluently in .NET. |
| 2026-11-20 11:35:21 | [TecalisSoftware.Identity.SDK](https://www.nuget.org/packages/TecalisSoftware.Identity.SDK) | 1.1.0 | Tecalis Software | Tecalis Identity SDK |
| 2026-11-20 11:48:10 | [Molib](https://www.nuget.org/packages/Molib) | 0.1.0 | Molib | Extensions for Gum UI on MonoGame: motion, layers, scrolling, scaling. |
| 2026-11-20 11:52:06 | [Mittena](https://www.nuget.org/packages/Mittena) | 0.1.0 | Mittena | Official .NET SDK for the Mittena email API. |
| 2026-11-20 11:56:57 | [FlameFox666.FSMGodot](https://www.nuget.org/packages/FlameFox666.FSMGodot) | 1.0.1 | FlameFox666 | Finite State Machine for Godot Engine 4.x |
| 2026-11-20 12:00:15 | [Sentivium.Trellis.SDK](https://www.nuget.org/packages/Sentivium.Trellis.SDK) | 0.2.0 | Sentivium Team | Unified .NET SDK for Trellis: The Governed Business Operating System for Agenti… |
| 2026-11-20 12:02:37 | [SpeakerForge](https://www.nuget.org/packages/SpeakerForge) | 1.0.0 | Stephen White | SpeakerForge - standalone .NET engine for discovering and streaming audio to ne… |
| 2026-11-20 12:05:58 | [csff.any](https://www.nuget.org/packages/csff.any) | 0.1.0 | Takumi Kuroda | A fast C# formatter CLI written in F#. |
| 2026-11-20 12:06:00 | [csff.linux-arm64](https://www.nuget.org/packages/csff.linux-arm64) | 0.1.0 | Takumi Kuroda | A fast C# formatter CLI written in F#. |
| 2026-11-20 12:06:01 | [csff.linux-musl-arm64](https://www.nuget.org/packages/csff.linux-musl-arm64) | 0.1.0 | Takumi Kuroda | A fast C# formatter CLI written in F#. |
| 2026-11-20 12:06:03 | [csff.linux-musl-x64](https://www.nuget.org/packages/csff.linux-musl-x64) | 0.1.0 | Takumi Kuroda | A fast C# formatter CLI written in F#. |
| 2026-11-20 12:06:04 | [csff.linux-x64](https://www.nuget.org/packages/csff.linux-x64) | 0.1.0 | Takumi Kuroda | A fast C# formatter CLI written in F#. |
| 2026-11-20 12:06:05 | [csff.osx-arm64](https://www.nuget.org/packages/csff.osx-arm64) | 0.1.0 | Takumi Kuroda | A fast C# formatter CLI written in F#. |
| 2026-11-20 12:06:07 | [csff.win-arm64](https://www.nuget.org/packages/csff.win-arm64) | 0.1.0 | Takumi Kuroda | A fast C# formatter CLI written in F#. |
| 2026-11-20 12:08:15 | [D4S.Mcp.Server](https://www.nuget.org/packages/D4S.Mcp.Server) | 1.0.0 | Dev4Side | Entra-secured stateless MCP hosting with validated per-request D4S user context. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

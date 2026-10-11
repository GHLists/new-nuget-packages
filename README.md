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

## Latest list — 2026-10-11 14:21 UTC

New packages created between 2026-10-11 13:20 UTC and 2026-10-11 14:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-11T14-21-26-210459Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-11 13:21:51 | [Altruist.Gaming.Lobbies](https://www.nuget.org/packages/Altruist.Gaming.Lobbies) | 0.9.9-beta | Lobbies | Package Description |
| 2026-10-11 13:21:52 | [Altruist.Gaming.Matchmaking](https://www.nuget.org/packages/Altruist.Gaming.Matchmaking) | 0.9.9-beta | Matchmaking | Package Description |
| 2026-10-11 13:21:52 | [Altruist.Gaming.Rooms](https://www.nuget.org/packages/Altruist.Gaming.Rooms) | 0.9.9-beta | Rooms | Package Description |
| 2026-10-11 13:22:12 | [Gravicode.HFNet.GraviTransformers.Vision](https://www.nuget.org/packages/Gravicode.HFNet.GraviTransformers.Vision) | 0.9.0 | Gravicode Studios | GraviTransformers.Vision - ViT image classification and CLIP zero-shot classifi… |
| 2026-10-11 13:26:51 | [miniClockLibrary](https://www.nuget.org/packages/miniClockLibrary) | 1.0.0 | Tracy Software | Live analog clock for any country or time zone, in one line of code. Show it as… |
| 2026-10-11 13:30:15 | [Kebechet.Api.ToMcp](https://www.nuget.org/packages/Kebechet.Api.ToMcp) | 2.0.0 | Kebechet | A C# source generator that transforms ASP.NET Core API endpoints into MCP (Mode… |
| 2026-10-11 13:44:01 | [Labcoat](https://www.nuget.org/packages/Labcoat) | 1.0.0 | Erik Lieben | A web UI for Microsoft.Testing.Platform: browse, run and watch your MSTest, NUn… |
| 2026-10-11 13:44:02 | [Labcoat.Aspire.Hosting](https://www.nuget.org/packages/Labcoat.Aspire.Hosting) | 1.0.0 | Erik Lieben | Aspire hosting integration for Labcoat, a web UI for Microsoft.Testing.Platform… |
| 2026-10-11 13:44:03 | [Labcoat.Testing](https://www.nuget.org/packages/Labcoat.Testing) | 1.0.0 | Erik Lieben | Test-side core for Labcoat, framework neutral: per-test OpenTelemetry traces fo… |
| 2026-10-11 13:44:04 | [Labcoat.Testing.MSTest](https://www.nuget.org/packages/Labcoat.Testing.MSTest) | 1.0.0 | Erik Lieben | MSTest adapter for Labcoat.Testing: per-test OpenTelemetry traces for MSTest +… |
| 2026-10-11 13:44:05 | [Labcoat.Testing.TUnit](https://www.nuget.org/packages/Labcoat.Testing.TUnit) | 1.0.0 | Erik Lieben | TUnit adapter for Labcoat.Testing: per-test OpenTelemetry traces for TUnit + As… |
| 2026-10-11 13:44:06 | [Labcoat.Testing.NUnit](https://www.nuget.org/packages/Labcoat.Testing.NUnit) | 1.0.0 | Erik Lieben | NUnit adapter for Labcoat.Testing: per-test OpenTelemetry traces for NUnit + As… |
| 2026-10-11 13:44:07 | [Labcoat.Testing.XUnit](https://www.nuget.org/packages/Labcoat.Testing.XUnit) | 1.0.0 | Erik Lieben | xUnit v3 adapter for Labcoat.Testing: per-test OpenTelemetry traces for xUnit v… |
| 2026-10-11 13:44:08 | [Labcoat.TestingPlatform](https://www.nuget.org/packages/Labcoat.TestingPlatform) | 1.0.0 | Erik Lieben | Microsoft.Testing.Platform extension for Labcoat: 'dotnet run -- --labcoat' ope… |
| 2026-10-11 13:50:06 | [ClamGauge](https://www.nuget.org/packages/ClamGauge) | 0.9.0 | machi_pon | MAUI circular gauge rendered with SkiaSharp |
| 2026-10-11 13:50:30 | [lucaslgt.WorkflowContext](https://www.nuget.org/packages/lucaslgt.WorkflowContext) | 0.1.0 | Lucas Lenglet | Lightweight helpers for building workflow contexts and execution pipelines. |
| 2026-10-11 13:53:32 | [MacOSX.SDK](https://www.nuget.org/packages/MacOSX.SDK) | 26.1.12 | Apple Inc.,DotNet-AGPL | Filtered macOS SDK 26.1 (from joseluisq/macosx-sdks) for cross-compiling Native… |
| 2026-10-11 13:58:54 | [SharpAbp.Abp.AspNetCore.IpAccessControl](https://www.nuget.org/packages/SharpAbp.Abp.AspNetCore.IpAccessControl) | 6.0.1 | virtual | SharpAbp ASP.NET Core IP access control module |
| 2026-10-11 13:59:04 | [SharpAbp.Abp.ConcurrencyLimiting](https://www.nuget.org/packages/SharpAbp.Abp.ConcurrencyLimiting) | 6.0.1 | virtual | ABP process-local execution concurrency limiting |
| 2026-10-11 14:00:49 | [SharpAbp.Abp.OperationRateLimiting](https://www.nuget.org/packages/SharpAbp.Abp.OperationRateLimiting) | 6.0.1 | virtual | ABP operation count limiting with replaceable atomic storage |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-15 21:21 UTC

New packages created between 2026-11-15 20:21 UTC and 2026-11-15 21:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-15T21-21-32-568755Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-15 20:23:23 | [AuthCallout.Client](https://www.nuget.org/packages/AuthCallout.Client) | 0.1.30 | Ryan Anthony | Consumer-side integration library for nats-auth-callout-service (ADR 0020): tok… |
| 2026-11-15 20:23:24 | [AuthCallout.Client.Wolverine](https://www.nuget.org/packages/AuthCallout.Client.Wolverine) | 0.1.30 | Ryan Anthony | Wolverine integration for nats-auth-callout-service (ADR 0022): a thin adapter… |
| 2026-11-15 20:27:14 | [Akinly](https://www.nuget.org/packages/Akinly) | 1.0.1 | Valentin Burkin | Incremental clustering of short texts by embedding similarity, with lasting clu… |
| 2026-11-15 20:27:14 | [Akinly.VectorData](https://www.nuget.org/packages/Akinly.VectorData) | 1.0.1 | Valentin Burkin | An Akinly cluster store over a vector database with a Microsoft.Extensions.Vect… |
| 2026-11-15 20:27:15 | [Akinly.AI](https://www.nuget.org/packages/Akinly.AI) | 1.0.1 | Valentin Burkin | Akinly with any language model through Microsoft.Extensions.AI: a judge that de… |
| 2026-11-15 20:31:06 | [SseClientLib](https://www.nuget.org/packages/SseClientLib) | 0.3.1 | Macha Celeste | A simple SSE listener client |
| 2026-11-15 20:31:54 | [Agentics.Extensions.Aspire.TeamsBot](https://www.nuget.org/packages/Agentics.Extensions.Aspire.TeamsBot) | 0.2.7 | Poul Kjeldager Sørensen | Aspire hosting integration for a notification bot in Microsoft Teams: provision… |
| 2026-11-15 20:34:49 | [GoomeSharp](https://www.nuget.org/packages/GoomeSharp) | 0.4.0 | sevvy-wevvy | C# bindings for goome: see-through always on top overlays, normal app windows a… |
| 2026-11-15 20:35:17 | [Jeninnet.Assertions.TUnit](https://www.nuget.org/packages/Jeninnet.Assertions.TUnit) | 1.1.0 | Jeninnet | Optional TUnit integration for Jeninnet.Assertions: surfaces fluent assertion f… |
| 2026-11-15 20:35:18 | [Jeninnet.Assertions.NUnit](https://www.nuget.org/packages/Jeninnet.Assertions.NUnit) | 1.1.0 | Jeninnet | Optional NUnit integration for Jeninnet.Assertions: surfaces fluent assertion f… |
| 2026-11-15 20:35:19 | [Jeninnet.Assertions.xUnit.v3](https://www.nuget.org/packages/Jeninnet.Assertions.xUnit.v3) | 1.1.0 | Jeninnet | Optional xUnit v3 integration for Jeninnet.Assertions: surfaces fluent assertio… |
| 2026-11-15 20:35:19 | [Jeninnet.Assertions.xUnit](https://www.nuget.org/packages/Jeninnet.Assertions.xUnit) | 1.1.0 | Jeninnet | Optional xUnit v2 integration for Jeninnet.Assertions: surfaces fluent assertio… |
| 2026-11-15 20:38:26 | [DotnetRsync](https://www.nuget.org/packages/DotnetRsync) | 0.0.1 | Linus Berg | A managed .NET reimplementation of the rsync client protocol. Pull files from a… |
| 2026-11-15 20:38:26 | [DotnetRsync.S3](https://www.nuget.org/packages/DotnetRsync.S3) | 0.0.1 | Linus Berg | Amazon S3 (and S3-compatible storage) target for DotnetRsync: rsync files from… |
| 2026-11-15 20:43:16 | [Elyspio.Utils.Results.AspNetCore](https://www.nuget.org/packages/Elyspio.Utils.Results.AspNetCore) | 1.0.0 | Elyspio.Utils.Results.AspNetC… | Maps Elyspio.Utils.Results to ASP.NET Core results and ProblemDetails |
| 2026-11-15 20:43:17 | [Elyspio.Utils.Results](https://www.nuget.org/packages/Elyspio.Utils.Results) | 1.0.0 | Elyspio.Utils.Results | Result type built on C# 15 unions, with a closed hierarchy of HTTP-mappable err… |
| 2026-11-15 20:43:18 | [Elyspio.Utils.Telemetry](https://www.nuget.org/packages/Elyspio.Utils.Telemetry) | 3.0.0 | Elyspio.Utils.Telemetry | OpenTelemetry bootstrap configured by the standard OTEL_* settings, Serilog log… |
| 2026-11-15 20:43:33 | [GoalNET.Calculator](https://www.nuget.org/packages/GoalNET.Calculator) | 1.0.0 | GoalNET.Calculator | Package Description |
| 2026-11-15 20:48:56 | [EFCore.MaterializR.PostgreSql](https://www.nuget.org/packages/EFCore.MaterializR.PostgreSql) | 1.1.61 | Adam O'Neil | EF Core-based incremental cache updates for PostgreSql |
| 2026-11-15 20:56:04 | [CosmicChimps.Aspire.Hosting.Umbral](https://www.nuget.org/packages/CosmicChimps.Aspire.Hosting.Umbral) | 0.12.0 | Cosmic Chimps | Aspire hosting integration for Umbral, a self-hosted OpenID Connect provider. A… |
| 2026-11-15 20:58:55 | [Tanuki.Parsing](https://www.nuget.org/packages/Tanuki.Parsing) | 0.1.0 | Caprine Logic | A small command-line parser with explicit commands, options, and arguments. |
| 2026-11-15 20:58:56 | [Tanuki](https://www.nuget.org/packages/Tanuki) | 0.1.0 | Caprine Logic | An intentionally boring, attribute-based CLI framework. |
| 2026-11-15 21:07:42 | [ChromaDotNet.Client.Backup](https://www.nuget.org/packages/ChromaDotNet.Client.Backup) | 2.22.0 | ChromaDotNet contributors | Backup and restore of Chroma collections through the API, for ChromaDotNet.Clie… |
| 2026-11-15 21:07:42 | [ChromaDotNet.Client.Cli](https://www.nuget.org/packages/ChromaDotNet.Client.Cli) | 2.22.0 | ChromaDotNet contributors | The command chromadotnet: backup, restore and verify of Chroma collections thro… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

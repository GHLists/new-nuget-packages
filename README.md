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

## Latest list — 2026-10-22 01:20 UTC

New packages created between 2026-10-22 00:19 UTC and 2026-10-22 01:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-22T01-20-29-913241Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-22 00:19:41 | [Zhomfr.Validation.Rules.Database](https://www.nuget.org/packages/Zhomfr.Validation.Rules.Database) | 0.3.0 | zhuolyan (Oleg Zhuravskiy) | Package Description |
| 2026-10-22 00:23:46 | [Asteroid.AgentTools.CompilerTools](https://www.nuget.org/packages/Asteroid.AgentTools.CompilerTools) | 0.1.0 | Asteroid.AgentTools.CompilerT… | Source generator and analyzer for [AgentPlayFace] typed play tool projection. |
| 2026-10-22 00:47:13 | [Tracescribe.Query](https://www.nuget.org/packages/Tracescribe.Query) | 0.3.0-alpha | Senthil Sekar | Read traces from Jaeger, Grafana Tempo or OTLP/JSON files and turn them into Tr… |
| 2026-10-22 00:47:14 | [Tracescribe](https://www.nuget.org/packages/Tracescribe) | 0.3.0-alpha | Senthil Sekar | Triage-ready instrumentation for .NET on top of System.Diagnostics.Activity: in… |
| 2026-10-22 00:47:15 | [Tracescribe.Mcp](https://www.nuget.org/packages/Tracescribe.Mcp) | 0.3.0-alpha | Senthil Sekar | MCP server and CLI that give AI agents triage digests of traces and intent-keye… |
| 2026-10-22 00:47:16 | [Tracescribe.OpenTelemetry](https://www.nuget.org/packages/Tracescribe.OpenTelemetry) | 0.3.0-alpha | Senthil Sekar | OpenTelemetry .NET integration for Tracescribe: a span processor that infers fa… |
| 2026-10-22 00:47:17 | [Tracescribe.Extensions.AI](https://www.nuget.org/packages/Tracescribe.Extensions.AI) | 0.3.0-alpha | Senthil Sekar | Microsoft.Extensions.AI middleware that wraps chat calls in Tracescribe operati… |
| 2026-10-22 00:47:17 | [Tracescribe.SemanticConventions](https://www.nuget.org/packages/Tracescribe.SemanticConventions) | 0.3.0-alpha | Senthil Sekar | Attribute, event and enum constants for the Tracescribe semantic conventions. |
| 2026-10-22 00:47:18 | [Tracescribe.Generators](https://www.nuget.org/packages/Tracescribe.Generators) | 0.3.0-alpha | Senthil Sekar | Source generator for Tracescribe: writes the body of [Scribe] partial methods s… |
| 2026-10-22 01:07:06 | [TemporaryDiagnostics.AspNetCore](https://www.nuget.org/packages/TemporaryDiagnostics.AspNetCore) | 1.0.2 | csvkse | ASP.NET Core integration for TemporaryDiagnostics: Middleware, Minimal APIs, em… |
| 2026-10-22 01:07:07 | [TemporaryDiagnostics.Core](https://www.nuget.org/packages/TemporaryDiagnostics.Core) | 1.0.2 | csvkse | Core contracts, models, state machines and options for TemporaryDiagnostics mid… |
| 2026-10-22 01:07:08 | [TemporaryDiagnostics.Infrastructure](https://www.nuget.org/packages/TemporaryDiagnostics.Infrastructure) | 1.0.2 | csvkse | Infrastructure implementation for TemporaryDiagnostics: PTY engines, IL Emit fa… |
| 2026-10-22 01:08:49 | [BYFoundation.ZWCAD.2026](https://www.nuget.org/packages/BYFoundation.ZWCAD.2026) | 1.1.2 | Dawsen | Helper classes and functions for ZWCAD 2026 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-01 12:18 UTC

New packages created between 2026-11-01 11:19 UTC and 2026-11-01 12:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-01T12-18-42-883759Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-01 11:34:38 | [Cratis.Showrunner.Herald.Contracts](https://www.nuget.org/packages/Cratis.Showrunner.Herald.Contracts) | 1.10.0 | Cratis | The event contracts for Herald — the Showrunner email part: the facts recorded… |
| 2026-11-01 11:34:39 | [Cratis.Showrunner.Herald](https://www.nuget.org/packages/Cratis.Showrunner.Herald) | 1.10.0 | Cratis | Herald — the Showrunner email part for applications: templated, email-safe mess… |
| 2026-11-01 11:42:07 | [Glacier.Tune](https://www.nuget.org/packages/Glacier.Tune) | 1.0.7 | Ian Cowley | Pure C# .NET 10 LLM fine-tuning, PEFT (LoRA / QLoRA), and model alignment engin… |
| 2026-11-01 11:43:36 | [Glacier.Codec](https://www.nuget.org/packages/Glacier.Codec) | 1.0.1 | Ian Cowley | Enterprise ultra-high-throughput cryptographic and compression library in pure… |
| 2026-11-01 11:47:58 | [AlliedBits.Parlot.SourceGenerator](https://www.nuget.org/packages/AlliedBits.Parlot.SourceGenerator) | 2.1.0.1 | Sebastien Ros | Roslyn source generator for compiling Parlot parser combinators into optimized… |
| 2026-11-01 11:49:57 | [Spreadox](https://www.nuget.org/packages/Spreadox) | 1.0.0 | Conq.Noble | Spreadox is a high-performance, dependency-isolated C# library for native Excel… |
| 2026-11-01 11:50:27 | [Cratis.Environments](https://www.nuget.org/packages/Cratis.Environments) | 3.114.0 | Cratis | Reads Cratis environments from .cratis/environments: configuration values and s… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

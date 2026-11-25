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

## Latest list — 2026-11-25 19:20 UTC

New packages created between 2026-11-25 18:18 UTC and 2026-11-25 19:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-25T19-20-33-617644Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-25 18:22:20 | [ScipSharp](https://www.nuget.org/packages/ScipSharp) | 26.11.8531 | SCIP Maintainers | .NET library for the SCIP Code Intelligence Protocol: protobuf types, symbol pa… |
| 2026-11-25 18:22:26 | [ScipSharp.Cli](https://www.nuget.org/packages/ScipSharp.Cli) | 26.11.8531 | SCIP Maintainers | The scip command-line tool (print, lint, stats, snapshot, test, expt-convert, i… |
| 2026-11-25 18:22:29 | [ScipSharp.Indexer.Clang](https://www.nuget.org/packages/ScipSharp.Indexer.Clang) | 26.11.8531 | SCIP Maintainers | SCIP indexer for C, C++ (port of scip-clang). |
| 2026-11-25 18:22:31 | [ScipSharp.Indexer.Dart](https://www.nuget.org/packages/ScipSharp.Indexer.Dart) | 26.11.8531 | SCIP Maintainers | SCIP indexer for Dart (port of scip-dart). |
| 2026-11-25 18:22:33 | [ScipSharp.Indexer.DotNet](https://www.nuget.org/packages/ScipSharp.Indexer.DotNet) | 26.11.8531 | SCIP Maintainers | SCIP indexer for C#, Visual Basic (port of scip-dotnet). |
| 2026-11-25 18:22:36 | [ScipSharp.Indexer.Java](https://www.nuget.org/packages/ScipSharp.Indexer.Java) | 26.11.8531 | SCIP Maintainers | SCIP indexer for Java (native C# port of scip-java; needs no javac, plugin jar… |
| 2026-11-25 18:22:39 | [ScipSharp.Indexer.Php](https://www.nuget.org/packages/ScipSharp.Indexer.Php) | 26.11.8531 | SCIP Maintainers | SCIP indexer for PHP (port of scip-php). |
| 2026-11-25 18:22:41 | [ScipSharp.Indexer.Python](https://www.nuget.org/packages/ScipSharp.Indexer.Python) | 26.11.8531 | SCIP Maintainers | SCIP indexer for Python (native C# port of scip-python). |
| 2026-11-25 18:22:44 | [ScipSharp.Indexer.Ruby](https://www.nuget.org/packages/ScipSharp.Indexer.Ruby) | 26.11.8531 | SCIP Maintainers | SCIP indexer for Ruby (port of scip-ruby). |
| 2026-11-25 18:22:46 | [ScipSharp.Indexer.Rust](https://www.nuget.org/packages/ScipSharp.Indexer.Rust) | 26.11.8531 | SCIP Maintainers | SCIP indexer for Rust (port of rust-analyzer). |
| 2026-11-25 18:22:49 | [ScipSharp.Indexer.TypeScript](https://www.nuget.org/packages/ScipSharp.Indexer.TypeScript) | 26.11.8531 | SCIP Maintainers | SCIP indexer for TypeScript, JavaScript (native C# port of scip-typescript: par… |
| 2026-11-25 18:22:52 | [ScipSharp.Indexing](https://www.nuget.org/packages/ScipSharp.Indexing) | 26.11.8531 | SCIP Maintainers | Shared abstractions for SCIP indexers (per-language packages). |
| 2026-11-25 18:36:36 | [Ivetech.ORM.OpenTelemetry](https://www.nuget.org/packages/Ivetech.ORM.OpenTelemetry) | 4.1.1 | Lucas Santos | Instrumentação OpenTelemetry do Ivetech.ORM: registra a fonte de atividades Ive… |
| 2026-11-25 18:40:44 | [slnsync](https://www.nuget.org/packages/slnsync) | 0.1.1 | slnsync | Keeps an aggregate solution in sync with source .sln/.slnx solutions. |
| 2026-11-25 18:44:12 | [Sidub.Platform.Search.Testing](https://www.nuget.org/packages/Sidub.Platform.Search.Testing) | 1.24.1 | Sidub Inc. | Package Description |
| 2026-11-25 18:53:46 | [NCode.Randomness.Nist](https://www.nuget.org/packages/NCode.Randomness.Nist) | 0.3.0 | NCode Group | The NIST Randomness Beacon 2.0 adapter for NCode.Randomness: fetches pulses of… |
| 2026-11-25 18:53:46 | [NCode.Randomness.Drand](https://www.nuget.org/packages/NCode.Randomness.Drand) | 0.3.0 | NCode Group | The drand adapter for NCode.Randomness: fetches rounds of the League of Entropy… |
| 2026-11-25 18:56:33 | [Sobis.UI](https://www.nuget.org/packages/Sobis.UI) | 1.0.0 | Sobis | Standalone Blazor UI Component Library with Layout, Form, Input, DataGrid and O… |
| 2026-11-25 18:56:43 | [SoilData_WindowsGraphics](https://www.nuget.org/packages/SoilData_WindowsGraphics) | 1.0.1 | Adam Pinkowski | SoilData Windows graphics helper for SoilData library |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

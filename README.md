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

## Latest list — 2026-10-23 20:22 UTC

New packages created between 2026-10-23 19:20 UTC and 2026-10-23 20:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-23T20-22-24-499444Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-23 19:21:12 | [Octeka.CodeAnalysis.CommandLine](https://www.nuget.org/packages/Octeka.CodeAnalysis.CommandLine) | 2.0.0 | Patrick Robichaud (operating… | Hierarchical command-line parser engine with infinite subparser chaining and dy… |
| 2026-10-23 19:21:13 | [Octeka.CodeAnalysis.CommandLine.Abstractions](https://www.nuget.org/packages/Octeka.CodeAnalysis.CommandLine.Abstractions) | 2.0.0 | Patrick Robichaud (operating… | Core abstractions, contracts, and extension interfaces for Octeka.CodeAnalysis.… |
| 2026-10-23 19:21:14 | [Octeka.CodeAnalysis.CommandLine.Extensions.Help](https://www.nuget.org/packages/Octeka.CodeAnalysis.CommandLine.Extensions.Help) | 2.0.0 | Patrick Robichaud (operating… | Rich, beautifully formatted help screens and contextual error diagnostics for O… |
| 2026-10-23 19:21:14 | [Octeka.CodeAnalysis.CommandLine.Extensions.Logo](https://www.nuget.org/packages/Octeka.CodeAnalysis.CommandLine.Extensions.Logo) | 2.0.0 | Patrick Robichaud (operating… | Terminal logo, application header, and banner rendering extension with --nologo… |
| 2026-10-23 19:21:15 | [Octeka.CodeAnalysis.CommandLine.Mapping](https://www.nuget.org/packages/Octeka.CodeAnalysis.CommandLine.Mapping) | 2.0.0 | Patrick Robichaud (operating… | Declarative object mapping and execution pipeline for Octeka.CodeAnalysis.Comma… |
| 2026-10-23 19:29:07 | [FromToken](https://www.nuget.org/packages/FromToken) | 1.0.0 | s.t.a.r.t.s.e.v. | A library for working with tokens in ASP.NET Core. |
| 2026-10-23 19:33:12 | [Mecesoft.Mediator](https://www.nuget.org/packages/Mecesoft.Mediator) | 1.0.0 | Mecesoft | A lightweight, dependency-injection-friendly mediator library for .NET. |
| 2026-10-23 19:33:54 | [ConnPool](https://www.nuget.org/packages/ConnPool) | 1.0.4 | Mikhail Ilyushin | Generic connection pool for .NET (sync + async), dependency-free (netstandard2.… |
| 2026-10-23 19:36:05 | [Playtest](https://www.nuget.org/packages/Playtest) | 0.0.0 | Archont561 | Reserved placeholder for playtest polyglot testing framework |
| 2026-10-23 19:45:11 | [Goo.SpellCheck](https://www.nuget.org/packages/Goo.SpellCheck) | 0.10.0 | Xaz | Optional system spell checking and editor suggestions for Goo. |
| 2026-10-23 19:45:13 | [Goo.SpellCheck.Hunspell](https://www.nuget.org/packages/Goo.SpellCheck.Hunspell) | 0.10.0 | Xaz | Opt-in system Hunspell backend for Goo.SpellCheck. No bundled libraries or dict… |
| 2026-10-23 19:45:14 | [Goo.SpellCheck.Android](https://www.nuget.org/packages/Goo.SpellCheck.Android) | 0.10.0 | Xaz | Optional Android SpellCheckerSession backend for Goo.SpellCheck. |
| 2026-10-23 19:45:15 | [Goo.Printing](https://www.nuget.org/packages/Goo.Printing) | 0.10.0 | Xaz | Optional paginated raster PDF export and native printing for Goo. |
| 2026-10-23 19:45:16 | [Goo.Printing.Android](https://www.nuget.org/packages/Goo.Printing.Android) | 0.10.0 | Xaz | Optional Android PrintManager adapter for Goo.Printing. |
| 2026-10-23 20:00:29 | [BeneficialStrategies.Iso20022.Validation.Xml](https://www.nuget.org/packages/BeneficialStrategies.Iso20022.Validation.Xml) | 1.0.0-alpha | Jeff Ward,Beneficial Strategi… | Validate ISO 20022 XML straight from text, a document or an element: every prob… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

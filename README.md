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

## Latest list — 2026-10-04 20:18 UTC

New packages created between 2026-10-04 19:19 UTC and 2026-10-04 20:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-04T20-18-55-586848Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-04 19:31:32 | [NetWasm.System.Formats.Cbor](https://www.nuget.org/packages/NetWasm.System.Formats.Cbor) | 0.6.0 | Zion Sati | NetWasm netwasm0.1 implementation of System.Formats.Cbor. |
| 2026-10-04 19:43:13 | [Localisation.Avalonia](https://www.nuget.org/packages/Localisation.Avalonia) | 2.0.0 | Chris Pulman | Localisation libraries for WPF and Avalonia |
| 2026-10-04 19:55:15 | [Structly.AI](https://www.nuget.org/packages/Structly.AI) | 0.2.0 | menk-dev | Typed, structured LLM output for automated .NET workflows. |
| 2026-10-04 19:55:16 | [Structly.AI.Hosting](https://www.nuget.org/packages/Structly.AI.Hosting) | 0.2.0 | menk-dev | Dependency injection and configuration integration for Structly.AI. |
| 2026-10-04 19:58:07 | [Cave.Logging.Database](https://www.nuget.org/packages/Cave.Logging.Database) | 4.0.9 | Andreas Rohleder | This package contains classes for using the database logging. |
| 2026-10-04 20:02:39 | [Mics.CodeAnalysis](https://www.nuget.org/packages/Mics.CodeAnalysis) | 1.0.0 | Eduardo Zitinho | Turn C# source code into music. Roslyn-based parser and mapper for the Mics eco… |
| 2026-10-04 20:07:21 | [Localisation.Avalonia.Reactive](https://www.nuget.org/packages/Localisation.Avalonia.Reactive) | 2.0.0 | Chris Pulman | Localisation libraries for WPF and Avalonia |
| 2026-10-04 20:07:23 | [Localisation.WPF.Reactive](https://www.nuget.org/packages/Localisation.WPF.Reactive) | 2.0.0 | Chris Pulman | Localisation libraries for WPF and Avalonia |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

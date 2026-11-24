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

## Latest list — 2026-11-24 21:22 UTC

New packages created between 2026-11-24 20:21 UTC and 2026-11-24 21:22 UTC.

[Full CSV](data/new-nuget-packages-2026-11-24T21-22-39-142286Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-24 20:33:18 | [Arthur.Genesis](https://www.nuget.org/packages/Arthur.Genesis) | 0.1.17 | AuthurOne | Source and Visual Studio build project for the Arthur AXAML Editor extension. |
| 2026-11-24 20:38:17 | [FonsecaFramework.Ai.Knowledge](https://www.nuget.org/packages/FonsecaFramework.Ai.Knowledge) | 2026.11.24.2 | FonsecaFramework.Ai.Knowledge | Partitioned hybrid knowledge indexing with VectorData 11 and in-memory, SQLite,… |
| 2026-11-24 20:46:44 | [EmailKitchen](https://www.nuget.org/packages/EmailKitchen) | 1.0.0 | Mateusz Mardosz | Preview, test, and send Razor email templates in ASP.NET Core. Edit sample data… |
| 2026-11-24 20:46:49 | [ManagedCompressions.Brotli](https://www.nuget.org/packages/ManagedCompressions.Brotli) | 0.4.0 | Evariops | A Brotli (RFC 7932) decompressor and compressor in fully managed C#: no native… |
| 2026-11-24 20:47:55 | [BitBindle.ClosedXML](https://www.nuget.org/packages/BitBindle.ClosedXML) | 0.107.3 | Jan Havlíček, Francois Botha,… | See release notes https://github.com/BitBindle/ClosedXML/releases/tag/0.107.3 C… |
| 2026-11-24 20:48:27 | [BitBindle.ClosedXML.IO](https://www.nuget.org/packages/BitBindle.ClosedXML.IO) | 0.107.3 | Jan Havlíček, Francois Botha,… | See release notes https://github.com/BitBindle/ClosedXML/releases/tag/0.107.3 C… |
| 2026-11-24 20:49:27 | [CHDSharp.Cli](https://www.nuget.org/packages/CHDSharp.Cli) | 1.7.2 | Peterson Fernandes | Pure C# CHD (Compressed Hunks of Data) command-line tool, compatible with MAME'… |
| 2026-11-24 20:56:32 | [Racka](https://www.nuget.org/packages/Racka) | 26.11.2 | David Kozma | Multi-agent framework on .NET: agents on Claude Code, Codex, the Claude API or… |
| 2026-11-24 21:10:24 | [MyGeocode](https://www.nuget.org/packages/MyGeocode) | 1.1.1 | My Geocode | Official .NET client for the My Geocode API: forward and reverse geocoding, add… |
| 2026-11-24 21:15:21 | [Duxel.Linux.App](https://www.nuget.org/packages/Duxel.Linux.App) | 0.4.0 | dimohy | Linux X11 host for Duxel, a Vulkan-rendered .NET desktop UI library. |
| 2026-11-24 21:15:59 | [Zzdats.Lgp.Common.Caching.Oracle](https://www.nuget.org/packages/Zzdats.Lgp.Common.Caching.Oracle) | 10.0.0 | Zzdats.Lgp.Common.Caching.Ora… | Distributed cache implementation using Oracle database for NetStandard 2.0 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

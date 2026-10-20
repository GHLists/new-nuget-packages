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

## Latest list — 2026-10-20 00:20 UTC

New packages created between 2026-10-19 23:20 UTC and 2026-10-20 00:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-20T00-20-29-385477Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-19 23:26:50 | [QimErp.Shared.DataIntegrity](https://www.nuget.org/packages/QimErp.Shared.DataIntegrity) | 1.0.0 | IAmQwame | DATA-06 nightly loose-link integrity checks for QimErp services. Discovers refe… |
| 2026-10-19 23:35:51 | [Smartstore.EmbeddedSass.Net](https://www.nuget.org/packages/Smartstore.EmbeddedSass.Net) | 1.2.1 | gumbarros and EmbeddedSass.Ne… | Asynchronous .NET host for the Embedded Sass Protocol. |
| 2026-10-19 23:35:53 | [Smartstore.EmbeddedSass.Net.Compiler](https://www.nuget.org/packages/Smartstore.EmbeddedSass.Net.Compiler) | 1.2.1 | gumbarros and EmbeddedSass.Ne… | Bundled Dart Sass compilers for EmbeddedSass.Net on Windows, macOS, and Linux. |
| 2026-10-19 23:40:55 | [Rorix.Registry.GaFixture](https://www.nuget.org/packages/Rorix.Registry.GaFixture) | 0.1.0 | Authaz | Harmless fixture for Rorix Registry admission and recovery tests. |
| 2026-10-19 23:48:12 | [Novolis.Transports.Torrent.Trackers](https://www.nuget.org/packages/Novolis.Transports.Torrent.Trackers) | 2026.1.11.83 | Novolis | HTTP clients and aggregation for maintained public BitTorrent tracker lists. |
| 2026-10-19 23:48:14 | [TALXIS.DevKit.AgentBox.CLI](https://www.nuget.org/packages/TALXIS.DevKit.AgentBox.CLI) | 1.4.0 | NETWORG | Makes any machine or container ready for coding agents working on Power Platfor… |
| 2026-10-20 00:08:16 | [Kiji.Templates](https://www.nuget.org/packages/Kiji.Templates) | 0.1.0 | zzzkan | Project templates for Kiji, a static site generator for .NET. |
| 2026-10-20 00:09:36 | [NuExt.Tools.ProjectMerger](https://www.nuget.org/packages/NuExt.Tools.ProjectMerger) | 1.0.0 | ivanvoyager | Merges project files into one or more text files suitable for AI analysis. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

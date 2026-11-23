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

## Latest list — 2026-11-23 22:20 UTC

New packages created between 2026-11-23 21:19 UTC and 2026-11-23 22:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-23T22-20-26-700351Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-23 21:20:28 | [Nazor.Themes.WindowsXP](https://www.nuget.org/packages/Nazor.Themes.WindowsXP) | 0.1.1-alpha | Nazor | Windows XP Luna-inspired light control styles for Nazor. |
| 2026-11-23 21:21:35 | [Nazor.Themes.Adwaita](https://www.nuget.org/packages/Nazor.Themes.Adwaita) | 0.1.1-alpha | Nazor | Light and dark control styles based on Libadwaita 1.10, with private Adwaita fo… |
| 2026-11-23 21:34:06 | [GroveGames.Audio](https://www.nuget.org/packages/GroveGames.Audio) | 0.1.0 | Grove Games | Music and sound effect playback with playlists and fades |
| 2026-11-23 21:34:17 | [Epsilon.Solving](https://www.nuget.org/packages/Epsilon.Solving) | 1.0.0 | Max Zakharov | Equation solving for the Epsilon symbolic math library. Exact solutions of equa… |
| 2026-11-23 21:44:02 | [SparkplugNet.nanoFramework](https://www.nuget.org/packages/SparkplugNet.nanoFramework) | 1.5.0 | SeppPenner | Sparkplug B Edge Node for .NET nanoFramework over MQTT 3.1.1, supporting the Sp… |
| 2026-11-23 21:55:24 | [BccCode.Privacy.Postgres](https://www.nuget.org/packages/BccCode.Privacy.Postgres) | 0.17.0 | BCC | The PostgreSQL layer of BCC Privacy: the privacy columns, column comments, cons… |
| 2026-11-23 22:08:12 | [Gleanvolt.Providers.Contracts](https://www.nuget.org/packages/Gleanvolt.Providers.Contracts) | 1.3.1 | Martin Pospisil | The wire contract between Gleanvolt and an external data provider (#386): the h… |
| 2026-11-23 22:08:14 | [Gleanvolt.Providers.Client](https://www.nuget.org/packages/Gleanvolt.Providers.Client) | 1.3.1 | Martin Pospisil | Write an external data provider for Gleanvolt (#386): connects to Gleanvolt ove… |
| 2026-11-23 22:08:15 | [Gleanvolt.Providers.Testing](https://www.nuget.org/packages/Gleanvolt.Providers.Testing) | 1.3.1 | Martin Pospisil | Test a Gleanvolt charger plugin without Gleanvolt (#439): a charger hub on a lo… |
| 2026-11-23 22:08:16 | [Gleanvolt.Chargers.Hosting](https://www.nuget.org/packages/Gleanvolt.Chargers.Hosting) | 1.3.1 | Martin Pospisil | Write a Gleanvolt charger plugin in a few files: the host, the page Gleanvolt f… |
| 2026-11-23 22:08:17 | [Gleanvolt.Modbus](https://www.nuget.org/packages/Gleanvolt.Modbus) | 1.3.1 | Martin Pospisil | A Modbus TCP client that keeps its connection healthy (#439): one request at a… |
| 2026-11-23 22:08:54 | [Packata.ExtendedTypes](https://www.nuget.org/packages/Packata.ExtendedTypes) | 1.39.0 | Cédric L. Charlier | Optional NetTopologySuite and Chrononuensis CLR representations and reader bind… |
| 2026-11-23 22:08:57 | [IdeaBlade.Validation](https://www.nuget.org/packages/IdeaBlade.Validation) | 0.1.0 | IdeaBlade | Data-store agnostic, metadata-driven validation framework. Server-side (.NET) c… |
| 2026-11-23 22:10:07 | [PinguApps.Playbook](https://www.nuget.org/packages/PinguApps.Playbook) | 1.0.0 | PinguApps | Original, offline .NET implementation recipes for coding agents over stdio MCP. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-09-27 20:20 UTC

New packages created between 2026-09-27 19:20 UTC and 2026-09-27 20:20 UTC.

[Full CSV](data/new-nuget-packages-2026-09-27T20-20-20-76623Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-27 19:20:43 | [Brigade.Net.Mise.Engines.MySQL](https://www.nuget.org/packages/Brigade.Net.Mise.Engines.MySQL) | 1.0.0 | Steffen Blake | Brigade.NET typed application, validation, and database components: Brigade.Net… |
| 2026-09-27 19:24:15 | [SharpNinja.McpServer.Repl](https://www.nuget.org/packages/SharpNinja.McpServer.Repl) | 1.4.39 | SharpNinja | MCP Server REPL Host - Interactive and STDIO modes for Model Context Protocol i… |
| 2026-09-27 19:24:27 | [Brigade.Net.Mise.Engines.MariaDb](https://www.nuget.org/packages/Brigade.Net.Mise.Engines.MariaDb) | 1.0.0 | Steffen Blake | Brigade.NET typed application, validation, and database components: Brigade.Net… |
| 2026-09-27 19:28:48 | [Brigade.Net.Partie.Extensions.Mise](https://www.nuget.org/packages/Brigade.Net.Partie.Extensions.Mise) | 1.0.0 | Steffen Blake | Brigade.NET typed application, validation, and database components: Brigade.Net… |
| 2026-09-27 19:32:11 | [Brigade.Net.Partie.Extensions.Expo](https://www.nuget.org/packages/Brigade.Net.Partie.Extensions.Expo) | 1.0.0 | Steffen Blake | Brigade.NET typed application, validation, and database components: Brigade.Net… |
| 2026-09-27 19:33:08 | [Memtly.Localization.Fork](https://www.nuget.org/packages/Memtly.Localization.Fork) | 1.0.0 | Memtly | Language pack used by Memtly for display, this is a fork version. |
| 2026-09-27 19:35:44 | [Brigade.Net.Partie.Extensions.Expo.Engines.AspNetCore](https://www.nuget.org/packages/Brigade.Net.Partie.Extensions.Expo.Engines.AspNetCore) | 1.0.0 | Steffen Blake | Brigade.NET typed application, validation, and database components: Brigade.Net… |
| 2026-09-27 19:41:34 | [RatelKey.Burrow.Sdk](https://www.nuget.org/packages/RatelKey.Burrow.Sdk) | 1.0.0 | RatelKey | Read secrets from a self-hosted RatelKey Burrow with a machine identity. |
| 2026-09-27 19:47:37 | [Encore](https://www.nuget.org/packages/Encore) | 1.0.0 | SirusDoma | TCP sessions, command dispatch, framing, and attribute-based binary serializati… |
| 2026-09-27 20:04:26 | [RibbitMassQ](https://www.nuget.org/packages/RibbitMassQ) | 0.1.0 | oceanic_tree | Thin RabbitMQ consumer/RPC library built on RabbitMQ.Client v7, with declarativ… |
| 2026-09-27 20:11:44 | [Niddy.Avalonia](https://www.nuget.org/packages/Niddy.Avalonia) | 1.0.1 | Christian Webber | Niddy: my personal .NET utilities. Avalonia UI helpers: app hosting, dialogs (w… |
| 2026-09-27 20:11:45 | [Niddy.Avalonia.Generators](https://www.nuget.org/packages/Niddy.Avalonia.Generators) | 1.0.1 | Christian Webber | Niddy: my personal .NET utilities. Registers Niddy.Avalonia pages tagged with [… |
| 2026-09-27 20:11:45 | [Niddy.Core](https://www.nuget.org/packages/Niddy.Core) | 1.0.1 | Christian Webber | Niddy: my personal .NET utilities. Core helpers (IO, atomic file writes, deboun… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

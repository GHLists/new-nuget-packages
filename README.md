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

## Latest list — 2026-10-03 13:18 UTC

New packages created between 2026-10-03 12:20 UTC and 2026-10-03 13:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-03T13-18-41-455394Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-03 12:28:15 | [JdkFind.Cli](https://www.nuget.org/packages/JdkFind.Cli) | 0.1.0 | ghostflyby | Locate installed JDKs across Windows, macOS and Linux. |
| 2026-10-03 12:33:21 | [Shiny.BluetoothLE.Hubs.Client](https://www.nuget.org/packages/Shiny.BluetoothLE.Hubs.Client) | 1.0.0-alpha-0004-gb… | Allan Ritchie | Shiny.BluetoothLE.Hubs client - discovers BLE hub hosts and calls them through… |
| 2026-10-03 12:33:21 | [Shiny.BluetoothLE.Hubs.Host](https://www.nuget.org/packages/Shiny.BluetoothLE.Hubs.Host) | 1.0.0-alpha-0004-gb… | Allan Ritchie | Shiny.BluetoothLE.Hubs host - SignalR style hubs served over a BLE GATT server,… |
| 2026-10-03 12:33:22 | [Shiny.BluetoothLE.Hubs](https://www.nuget.org/packages/Shiny.BluetoothLE.Hubs) | 1.0.0-alpha-0004-gb… | Allan Ritchie | SignalR style hubs over Bluetooth LE - shared protocol and the hub source gener… |
| 2026-10-03 12:38:36 | [SchemaArchitects.AspNetCore.Slo](https://www.nuget.org/packages/SchemaArchitects.AspNetCore.Slo) | 1.0.0 | SchemaArchitects | ASP.NET Core middleware that standardizes per-endpoint latency SLO targets via… |
| 2026-10-03 12:39:44 | [Mikita.Godot](https://www.nuget.org/packages/Mikita.Godot) | 0.1.0-alpha | Markushonok | Godot-specific extensions and integrations for Mikita. |
| 2026-10-03 12:40:16 | [Mikita](https://www.nuget.org/packages/Mikita) | 0.1.0-alpha | Markushonok | General-purpose library used by Inkraft. |
| 2026-10-03 12:52:52 | [danisss9.Lite.QuickJs](https://www.nuget.org/packages/danisss9.Lite.QuickJs) | 0.0.17 | danisss9 | QuickJS native bridge and managed runtime for Lite on Windows x64. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

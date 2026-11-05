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

## Latest list — 2026-11-05 14:21 UTC

New packages created between 2026-11-05 13:21 UTC and 2026-11-05 14:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-05T14-21-18-53949Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-05 13:21:59 | [MambaMQ.Client.NET](https://www.nuget.org/packages/MambaMQ.Client.NET) | 0.1.0 | MambaMQ.Client.NET | Package Description |
| 2026-11-05 13:22:26 | [Unicorn.EntityFrameworkCore.MongoDB](https://www.nuget.org/packages/Unicorn.EntityFrameworkCore.MongoDB) | 10.0.5 | MongoDB Inc. | Unofficial community build of the MongoDB provider for Entity Framework Core th… |
| 2026-11-05 13:26:10 | [TidyClassRoom](https://www.nuget.org/packages/TidyClassRoom) | 1.0.2 | Devseesharp | A Roslyn analyzer and code fix that keeps class members in a configurable order… |
| 2026-11-05 13:31:15 | [PDFjet.Fonts.World](https://www.nuget.org/packages/PDFjet.Fonts.World) | 9.1.7 | PDFjet Software | The fonts of PDFjet for Chinese, Japanese, Korean, Arabic, Hebrew and Thai: IBM… |
| 2026-11-05 13:39:30 | [BaryoDev.Umbraco.MediumImport](https://www.nuget.org/packages/BaryoDev.Umbraco.MediumImport) | 0.1.0 | BaryoDev | Import your Medium export into Umbraco 17: code blocks kept exact, gists inline… |
| 2026-11-05 13:44:52 | [GroundControl](https://www.nuget.org/packages/GroundControl) | 0.2.0 | Uladzislau Trayan | Runs xUnit.net v3 tests within a container of a Docker Compose project wherever… |
| 2026-11-05 14:00:13 | [Shiny.Obd.Ble.Linux](https://www.nuget.org/packages/Shiny.Obd.Ble.Linux) | 1.5.1-beta-0002 | aritchie,ShinyLib | Linux (BlueZ) BLE transport registration for Shiny.Obd using Shiny.BluetoothLE.… |
| 2026-11-05 14:00:42 | [LoomTerminal.Core](https://www.nuget.org/packages/LoomTerminal.Core) | 0.2.0 | LoomTerminal contributors | Platform-independent terminal emulator of LoomTerminal (VT parser and buffers,… |
| 2026-11-05 14:00:43 | [LoomTerminal.Pty](https://www.nuget.org/packages/LoomTerminal.Pty) | 0.2.0 | LoomTerminal contributors | Pseudo terminal for LoomTerminal: Windows ConPTY and a native forkpty shim for… |
| 2026-11-05 14:00:44 | [LoomTerminal.Presentation](https://www.nuget.org/packages/LoomTerminal.Presentation) | 0.2.0 | LoomTerminal contributors | UI-independent presentation layer of LoomTerminal: render model, input encoding… |
| 2026-11-05 14:00:44 | [LoomTerminal.WinUI](https://www.nuget.org/packages/LoomTerminal.WinUI) | 0.2.0 | LoomTerminal contributors | LoomTerminal: a native, Native AOT-compatible terminal control for WinUI 3 (no… |
| 2026-11-05 14:00:45 | [LoomTerminal.Avalonia](https://www.nuget.org/packages/LoomTerminal.Avalonia) | 0.2.0 | LoomTerminal contributors | LoomTerminal: a native, Native AOT-compatible terminal control for Avalonia (Sk… |
| 2026-11-05 14:05:46 | [RZeroF1.Minecraft.Projection](https://www.nuget.org/packages/RZeroF1.Minecraft.Projection) | 0.1.0 | RZeroF1 | Windows x64 SDK for parsing Minecraft projections, loading game resources, buil… |
| 2026-11-05 14:08:27 | [Alastack.Extensions.Configuration.Consul](https://www.nuget.org/packages/Alastack.Extensions.Configuration.Consul) | 1.0.0 | kyzala | Alastack.Extensions.Configuration.Consul loads Hashicorp Consul KV values as co… |
| 2026-11-05 14:08:56 | [JsonSchemaObjectModel](https://www.nuget.org/packages/JsonSchemaObjectModel) | 0.1.0 | Will Fuqua | An AOT-compatible JSON Schema (draft 2020-12) object model, builder and seriali… |
| 2026-11-05 14:12:09 | [FortyOne.Fody](https://www.nuget.org/packages/FortyOne.Fody) | 1.0.0 | FortyOne | FortyOne Godot C# Framework: Fody |
| 2026-11-05 14:13:14 | [StokerHQ.PluginRegistry](https://www.nuget.org/packages/StokerHQ.PluginRegistry) | 1.0.1 | StokerHQ | Stoker plugin registries: publisher and registry signatures, version statements… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

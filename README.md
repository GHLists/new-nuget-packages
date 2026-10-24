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

## Latest list — 2026-10-24 23:20 UTC

New packages created between 2026-10-24 22:22 UTC and 2026-10-24 23:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-24T23-20-05-155758Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-24 22:52:35 | [BrizUI](https://www.nuget.org/packages/BrizUI) | 1.0.0 | Allan Prieto Badilla | Componentes reutilizables para Blazor. |
| 2026-10-24 22:57:17 | [SlusserLabs.AnglePlates](https://www.nuget.org/packages/SlusserLabs.AnglePlates) | 1.1.0 | Jacob Slusser | Text templates that compile into plain C# classes at build time. There's no run… |
| 2026-10-24 22:57:53 | [WinToAws](https://www.nuget.org/packages/WinToAws) | 1.0.0 | VENKATESHWAR REDDY VURUMALLA | Move a Windows / .NET application to AWS by adding one library: analyse blocker… |
| 2026-10-24 22:59:17 | [RequestBatcher.OpenTelemetry](https://www.nuget.org/packages/RequestBatcher.OpenTelemetry) | 0.3.4 | EventHorizon CLI | Optional OpenTelemetry registration and linked-batch sampling for RequestBatche… |
| 2026-10-24 23:01:48 | [LANCommander.Plugins.Steam](https://www.nuget.org/packages/LANCommander.Plugins.Steam) | 1.0.0 | LANCommander | Adds SteamCMD to a LANCommander server: Steam sign-in profiles, an admin page,… |
| 2026-10-24 23:02:16 | [LabSync.Driver.Sdk](https://www.nuget.org/packages/LabSync.Driver.Sdk) | 0.4.0 | Lab Sync | Write a Lab Sync Device Hub driver in .NET: driver protocol v0 over stdio, the… |
| 2026-10-24 23:02:17 | [LabSync.Driver.Sdk.Testing](https://www.nuget.org/packages/LabSync.Driver.Sdk.Testing) | 0.4.0 | Lab Sync | Test a LabSync.Driver.Sdk driver: an in-process protocol harness, the driver as… |
| 2026-10-24 23:07:09 | [Workes.ConsoleSystem.DotNet.Logging](https://www.nuget.org/packages/Workes.ConsoleSystem.DotNet.Logging) | 1.0.0 | Workes | Opt-in adapter that mirrors .NET console output into Workes.ConsoleSystem while… |
| 2026-10-24 23:13:52 | [LANCommander.Plugins.Relay](https://www.nuget.org/packages/LANCommander.Plugins.Relay) | 1.0.0 | LANCommander | Hosts the LANCommander Interposer's network relay on a LANCommander server, so… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

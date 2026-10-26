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

## Latest list — 2026-10-26 19:21 UTC

New packages created between 2026-10-26 18:21 UTC and 2026-10-26 19:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-26T19-21-58-946914Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-26 18:27:29 | [Senseble.Maui.BottomSheet](https://www.nuget.org/packages/Senseble.Maui.BottomSheet) | 0.1.1 | Senseble B.V. | Lightweight modal bottom sheet for .NET MAUI (Android and iOS). The sheet is sh… |
| 2026-10-26 18:34:06 | [ConventionMapper.Testing](https://www.nuget.org/packages/ConventionMapper.Testing) | 1.8.0 | Katragadda | Test helpers for ConventionMapper and ConventionMapper.SourceGenerator mappings… |
| 2026-10-26 18:44:44 | [SparkStudio.RoomRelay.Api.Client](https://www.nuget.org/packages/SparkStudio.RoomRelay.Api.Client) | 0.1.1857 | SparkStudio | C# clients for SparkStudio RoomRelay. |
| 2026-10-26 18:44:46 | [SparkStudio.RoomRelay.Client](https://www.nuget.org/packages/SparkStudio.RoomRelay.Client) | 0.1.1857 | SparkStudio | One RoomRelay client for room management, WebSocket broadcasts, and UDP room me… |
| 2026-10-26 18:44:47 | [SparkStudio.RoomRelay.Udp.Client](https://www.nuget.org/packages/SparkStudio.RoomRelay.Udp.Client) | 0.1.1857 | SparkStudio | C# clients for SparkStudio RoomRelay. |
| 2026-10-26 18:44:48 | [SparkStudio.RoomRelay.WebSocket.Client](https://www.nuget.org/packages/SparkStudio.RoomRelay.WebSocket.Client) | 0.1.1857 | SparkStudio | C# clients for SparkStudio RoomRelay. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

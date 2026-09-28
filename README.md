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

## Latest list — 2026-09-28 03:21 UTC

New packages created between 2026-09-28 02:22 UTC and 2026-09-28 03:21 UTC.

[Full CSV](data/new-nuget-packages-2026-09-28T03-21-08-567072Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-28 02:51:29 | [ContentCalendar.V17](https://www.nuget.org/packages/ContentCalendar.V17) | 1.0.0 | ZAAKS! | A content calendar for the Umbraco 17 backoffice. A Content section dashboard a… |
| 2026-09-28 02:57:20 | [VDriver](https://www.nuget.org/packages/VDriver) | 1.4.1 | Goes Team | vdriver — Driver management CLI for Goes projects. Browse and download driver p… |
| 2026-09-28 03:04:38 | [Universal.Operative.Sdk.Google](https://www.nuget.org/packages/Universal.Operative.Sdk.Google) | 1.0.0 | Andrew Ong | Google Maps, Places, Routes, Drive, Sheets, and Calendar tools for Universal.Op… |
| 2026-09-28 03:06:29 | [Universal.Operative.Sdk.Discrete.Xiaomi.MiMo](https://www.nuget.org/packages/Universal.Operative.Sdk.Discrete.Xiaomi.MiMo) | 1.0.0 | Andrew Ong | MiMo model adapters for Universal.Operative.Sdk. |
| 2026-09-28 03:07:52 | [Paradise.ImGui.Plot](https://www.nuget.org/packages/Paradise.ImGui.Plot) | 3.1.2 | ParadiseEngine | Not an official Hexa.NET package: ParadiseEngine's fork of Hexa.NET.ImPlot by J… |
| 2026-09-28 03:07:53 | [Paradise.ImGui.Nodes](https://www.nuget.org/packages/Paradise.ImGui.Nodes) | 3.1.2 | ParadiseEngine | Not an official Hexa.NET package: ParadiseEngine's fork of Hexa.NET.ImNodes by… |
| 2026-09-28 03:07:55 | [Paradise.ImGui.Plot3D](https://www.nuget.org/packages/Paradise.ImGui.Plot3D) | 3.1.2 | ParadiseEngine | Not an official Hexa.NET package: ParadiseEngine's fork of Hexa.NET.ImPlot3D by… |
| 2026-09-28 03:07:55 | [Paradise.ImGui.Guizmo](https://www.nuget.org/packages/Paradise.ImGui.Guizmo) | 3.1.2 | ParadiseEngine | Not an official Hexa.NET package: ParadiseEngine's fork of Hexa.NET.ImGuizmo by… |
| 2026-09-28 03:11:13 | [Transfocus.TMS.Sdk](https://www.nuget.org/packages/Transfocus.TMS.Sdk) | 1.0.0 | Transfocus | Official .NET client for the Transfocus TMS public API (v1 and v2): typed resou… |
| 2026-09-28 03:15:06 | [SendPing](https://www.nuget.org/packages/SendPing) | 1.0.0 | SendPing | Official SendPing .NET SDK — send transactional and marketing email from your o… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

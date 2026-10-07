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

## Latest list — 2026-10-07 03:22 UTC

New packages created between 2026-10-07 02:19 UTC and 2026-10-07 03:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-07T03-22-13-562667Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-07 02:44:23 | [AvaloniaUIKit](https://www.nuget.org/packages/AvaloniaUIKit) | 0.1.0 | supermomonga | Avalonia themes that reproduce the look and motion of GPUI Kit components. |
| 2026-10-07 02:44:24 | [AvaloniaUIKit.ColorPicker](https://www.nuget.org/packages/AvaloniaUIKit.ColorPicker) | 0.1.0 | supermomonga | GPUI Kit's ColorPicker and ColorSelect looks for Avalonia.Controls.ColorPicker,… |
| 2026-10-07 02:44:24 | [AvaloniaUIKit.Dock](https://www.nuget.org/packages/AvaloniaUIKit.Dock) | 0.1.0 | supermomonga | GPUI Kit's Dock look for Dock.Avalonia, on top of AvaloniaUIKit's UIKitTheme. |
| 2026-10-07 02:44:25 | [AvaloniaUIKit.DataGrid](https://www.nuget.org/packages/AvaloniaUIKit.DataGrid) | 0.1.0 | supermomonga | GPUI Kit's DataTable look for Avalonia.Controls.DataGrid, on top of AvaloniaUIK… |
| 2026-10-07 02:45:31 | [lucnd.icloud.maui.Realm.Refurbished](https://www.nuget.org/packages/lucnd.icloud.maui.Realm.Refurbished) | 6.10.70 | Lucy | Tiện ích hỗ trợ truy cập Realm Database |
| 2026-10-07 02:47:43 | [Eternet.Inbox.Contracts](https://www.nuget.org/packages/Eternet.Inbox.Contracts) | 1.0.0 | Eternet.Inbox.Contracts | Package Description |
| 2026-10-07 02:48:09 | [Eternet.Sec.TsAs.Public.Contracts](https://www.nuget.org/packages/Eternet.Sec.TsAs.Public.Contracts) | 1.0.0 | Sec.TsAs.Public.Contracts | Package Description |
| 2026-10-07 02:51:48 | [Vard](https://www.nuget.org/packages/Vard) | 1.0.0 | Junior Schröder | Toolkit de resiliência sem atrito, type-safe, com zero dependências externas pa… |
| 2026-10-07 03:08:53 | [CoreSystem.Correlation](https://www.nuget.org/packages/CoreSystem.Correlation) | 1.0.0 | Federin Pastor Gutierrez Ortiz | Correlation-id propagation middleware for ASP.NET Core, usable standalone or al… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

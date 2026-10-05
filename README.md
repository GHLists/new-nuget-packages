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

## Latest list — 2026-10-05 01:19 UTC

New packages created between 2026-10-05 00:21 UTC and 2026-10-05 01:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-05T01-19-21-263129Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-05 00:26:52 | [Mopups.JimmyPun610](https://www.nuget.org/packages/Mopups.JimmyPun610) | 1.3.5 | Tyson Hooker,Maksym Koshovyi,… | Popups for MAUI, Temperary build for fixing iOS 27 crash |
| 2026-10-05 00:45:35 | [VpnHood.AppUi.Hosting.Abstractions](https://www.nuget.org/packages/VpnHood.AppUi.Hosting.Abstractions) | 8.2.853.11-prerelea… | VpnHood.AppUi.Hosting.Abstrac… | What a desktop host and a desktop UI agree on - IDesktopUi and what the host ha… |
| 2026-10-05 00:45:40 | [VpnHood.AppUi.Hosting.Avalonia.Ios](https://www.nuget.org/packages/VpnHood.AppUi.Hosting.Avalonia.Ios) | 8.2.853.11-prerelea… | VpnHood.AppUi.Hosting.Avaloni… | Hosts the VpnHood Avalonia UI in an iOS app: the application delegate a head's… |
| 2026-10-05 00:45:43 | [VpnHood.AppUi.Hosting.Cli.Windows](https://www.nuget.org/packages/VpnHood.AppUi.Hosting.Cli.Windows) | 8.2.853.11-prerelea… | VpnHood.AppUi.Hosting.Cli.Win… | The VpnHood command line on Windows: a LocalSystem service is the app, ProgramD… |
| 2026-10-05 00:56:03 | [StdUnit.Tags.Templates](https://www.nuget.org/packages/StdUnit.Tags.Templates) | 0.5.0 | itminus | Templates for StdUnit.Tags project |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

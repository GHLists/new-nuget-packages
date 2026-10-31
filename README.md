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

## Latest list — 2026-10-31 18:20 UTC

New packages created between 2026-10-31 17:21 UTC and 2026-10-31 18:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-31T18-20-52-741872Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-31 17:23:39 | [Fibril](https://www.nuget.org/packages/Fibril) | 0.0.1 | Axmouth | Name reserved for the .NET client of the Fibril message broker. Not usable yet. |
| 2026-10-31 17:30:56 | [Chronicler.Diagnostics](https://www.nuget.org/packages/Chronicler.Diagnostics) | 1.0.0 | mrdav30 | Dependency-free diagnostic channels, lazy logging, and allocation-conscious exc… |
| 2026-10-31 17:34:40 | [NetReporter.Viewer](https://www.nuget.org/packages/NetReporter.Viewer) | 1.4.0 | Marvin Chinchilla | Report viewer for ASP.NET Core apps: app.MapNetReporterViewer("/reports", ...)… |
| 2026-10-31 17:36:11 | [MASS4.Localization.Abstractions](https://www.nuget.org/packages/MASS4.Localization.Abstractions) | 3.8.0 | Bruno Massa | The locale contract that interface and host code resolve text through, independ… |
| 2026-10-31 17:36:14 | [MASS4.Localization](https://www.nuget.org/packages/MASS4.Localization) | 3.8.0 | Bruno Massa | Shared string tables, localization and translation interchange. |
| 2026-10-31 17:42:21 | [MASS4.Guinevere.Graphs](https://www.nuget.org/packages/MASS4.Guinevere.Graphs) | 6.5.0 | Bruno Massa | Virtualized graph canvas and accessible graph navigation for Guinevere. |
| 2026-10-31 17:46:14 | [VpnHood.Net.Http3](https://www.nuget.org/packages/VpnHood.Net.Http3) | 9.0.860 | VpnHood.Net.Http3 | VpnHood HTTP/3. A server-side HTTP/3 engine over the VpnHood QUIC abstractions:… |
| 2026-10-31 18:09:54 | [Mokaterm.Plugin.TestHost](https://www.nuget.org/packages/Mokaterm.Plugin.TestHost) | 0.2.5 | Moka | Test harness for Mokaterm plugins: renders a plugin's views to HTML with Blazor… |
| 2026-10-31 18:13:16 | [Lunixi.Sdk](https://www.nuget.org/packages/Lunixi.Sdk) | 0.1.1 | Lunixi | Lunixi server-side .NET SDK: signed requests, hosted payment intents, payment o… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

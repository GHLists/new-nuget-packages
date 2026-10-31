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

## Latest list — 2026-10-31 16:21 UTC

New packages created between 2026-10-31 15:20 UTC and 2026-10-31 16:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-31T16-21-00-604242Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-31 15:24:43 | [Wiretap](https://www.nuget.org/packages/Wiretap) | 13.0.0 | HeDev | Logging extensions to produce logs that are easier to organize. |
| 2026-10-31 15:32:03 | [Quire](https://www.nuget.org/packages/Quire) | 1.0.1 | Quire | Immutable asset packages with directory loading, typed metadata and concurrent… |
| 2026-10-31 15:44:42 | [Fomoxa.Backend.Templates](https://www.nuget.org/packages/Fomoxa.Backend.Templates) | 0.1.0 | Fomoxa | dotnet new template for a game backend of a Fomoxa cluster: fRPC server, player… |
| 2026-10-31 15:48:24 | [Vestigium.Helpers.Network.RawSocket](https://www.nuget.org/packages/Vestigium.Helpers.Network.RawSocket) | 1.0.0 | Vestigium | Elevated raw-socket probes for diagnostic hosts. SYN scan first. Requires admin… |
| 2026-10-31 15:49:59 | [Conq.Noble.Spreadox](https://www.nuget.org/packages/Conq.Noble.Spreadox) | 0.9.0 | Conq.Noble | Spreadox is a high-level C# library for Excel (.xlsx) workbooks and A4 PDF char… |
| 2026-10-31 15:50:19 | [NetTaskList](https://www.nuget.org/packages/NetTaskList) | 1.0.0 | NetTaskList Team | CLI tool to parse, list and execute tasks declared in nxtl.json |
| 2026-10-31 15:54:10 | [Wayfinder.Umbraco.Templates](https://www.nuget.org/packages/Wayfinder.Umbraco.Templates) | 6.4.0 | Jonny Muir | dotnet new templates for Wayfinder for Umbraco sites. `dotnet new wayfinder-age… |
| 2026-10-31 16:04:11 | [NecessarySdk](https://www.nuget.org/packages/NecessarySdk) | 0.1.7 | Meraj Hasan | Device trust for .NET apps on Android and iOS: a key the app never exports, sig… |
| 2026-10-31 16:10:50 | [Renouveau.Caffeine](https://www.nuget.org/packages/Renouveau.Caffeine) | 0.1.0 | Ji Luo | For requesting the system not go idle so that long-running tasks continue unint… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-18 04:20 UTC

New packages created between 2026-10-18 03:21 UTC and 2026-10-18 04:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-18T04-20-42-999832Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-18 03:50:46 | [CodeGenNew.Cli](https://www.nuget.org/packages/CodeGenNew.Cli) | 0.1.0 | ericwood8 | Generates stored procedures, entities, APIs and WinUI3 / React / Angular screen… |
| 2026-10-18 04:01:03 | [NetPowerON.UI.FileModel](https://www.nuget.org/packages/NetPowerON.UI.FileModel) | 0.0.0.12 | Darren King | Package Description |
| 2026-10-18 04:01:03 | [NetPowerON.UI.Session](https://www.nuget.org/packages/NetPowerON.UI.Session) | 0.0.0.12 | Darren King | Package Description |
| 2026-10-18 04:01:04 | [NetPowerON.UI.Session.Abstractions](https://www.nuget.org/packages/NetPowerON.UI.Session.Abstractions) | 0.0.0.12 | Darren King | Package Description |
| 2026-10-18 04:01:04 | [NetPowerON.UI](https://www.nuget.org/packages/NetPowerON.UI) | 0.0.0.12 | Darren King | Package Description |
| 2026-10-18 04:01:04 | [NetPowerON.UI.FileModel.Abstractions](https://www.nuget.org/packages/NetPowerON.UI.FileModel.Abstractions) | 0.0.0.12 | Darren King | Package Description |
| 2026-10-18 04:01:04 | [NetPowerON.UI.Abstractions](https://www.nuget.org/packages/NetPowerON.UI.Abstractions) | 0.0.0.12 | Darren King | Package Description |
| 2026-10-18 04:08:33 | [PrintedJs.HeadlessWebView](https://www.nuget.org/packages/PrintedJs.HeadlessWebView) | 0.2.0 | PrintedJS Contributors | Cross-platform headless webview and vector PDF rendering library for .NET power… |
| 2026-10-18 04:12:07 | [Navs.CSharp](https://www.nuget.org/packages/Navs.CSharp) | 2.0.0 | Angel Munoz and contributors | Package Description |
| 2026-10-18 04:12:08 | [UrlTemplates.CSharp](https://www.nuget.org/packages/UrlTemplates.CSharp) | 2.0.0 | Angel Munoz and contributors | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

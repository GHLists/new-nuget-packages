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

## Latest list — 2026-11-03 09:18 UTC

New packages created between 2026-11-03 08:20 UTC and 2026-11-03 09:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-03T09-18-41-824338Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-03 08:44:30 | [Jony.TextTools](https://www.nuget.org/packages/Jony.TextTools) | 1.0.0 | dev-jony | A small library of text helper methods. |
| 2026-11-03 08:44:46 | [NockMon.ServiceStatus](https://www.nuget.org/packages/NockMon.ServiceStatus) | 0.1.0 | nockawa | NockMon widget: the status of the online services you follow (Claude, OpenAI, G… |
| 2026-11-03 08:47:09 | [Webority.Pdf](https://www.nuget.org/packages/Webority.Pdf) | 1.0.0 | Webority.Pdf | Webority's PDF library: generate documents, and open, inspect, unlock, protect,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

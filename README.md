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

## Latest list — 2026-10-12 05:20 UTC

New packages created between 2026-10-12 04:19 UTC and 2026-10-12 05:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-12T05-20-21-932078Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-12 04:23:33 | [BusyMeter.Plugins](https://www.nuget.org/packages/BusyMeter.Plugins) | 0.2.1 | The Busy Meter authors | Client for the Busy Meter status light's local plugin API (127.0.0.1 only). No… |
| 2026-10-12 04:27:48 | [FastReport.Plugins.Transport.Demo](https://www.nuget.org/packages/FastReport.Plugins.Transport.Demo) | 2027.1.0 | Fast Reports Inc. | Provides a plugin that integrates cloud transports with FastReport .NET, FastRe… |
| 2026-10-12 04:27:49 | [FastReport.Transport.Demo](https://www.nuget.org/packages/FastReport.Transport.Demo) | 2027.1.0 | Fast Reports Inc. | Provides transports for saving and loading reports in cloud storage services. |
| 2026-10-12 04:55:43 | [AioFrameworkWps](https://www.nuget.org/packages/AioFrameworkWps) | 1.0.0 | zhangchuncheng | All in one Framework |
| 2026-10-12 04:56:41 | [sdo-launcher](https://www.nuget.org/packages/sdo-launcher) | 1.21.0 | naz-hage | sdo-launcher has migrated to sdo-launcher. Install the sdo-launcher package for… |
| 2026-10-12 05:02:56 | [Activities.YiHaiJiaLi.ComLib](https://www.nuget.org/packages/Activities.YiHaiJiaLi.ComLib) | 1.0.5 | zhangchuncheng | My package description. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

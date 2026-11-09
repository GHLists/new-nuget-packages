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

## Latest list — 2026-11-09 01:21 UTC

New packages created between 2026-11-09 00:19 UTC and 2026-11-09 01:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-09T01-21-24-824624Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-09 00:36:46 | [BaryoDev.Umbraco.PostAlerts](https://www.nuget.org/packages/BaryoDev.Umbraco.PostAlerts) | 0.1.0 | BaryoDev | New-post alerts for Umbraco 17. Readers get a weekly email digest after double… |
| 2026-11-09 00:57:42 | [HikService](https://www.nuget.org/packages/HikService) | 1.0.8 | TheOne | Hikrobot MVS industrial camera wrapper for .NET with OpenCvSharp frame output o… |
| 2026-11-09 00:58:01 | [ilm1218.Avalonia.Semi.Core](https://www.nuget.org/packages/ilm1218.Avalonia.Semi.Core) | 1.0.7 | TheOne | Shared styles, controls, and UI helpers for Avalonia applications using Semi.Av… |
| 2026-11-09 01:04:40 | [MusselCalendar](https://www.nuget.org/packages/MusselCalendar) | 0.0.1 | machi_pon | Calendar views for Blazor with day, week and month layouts and drag operations |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

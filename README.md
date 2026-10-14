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

## Latest list — 2026-10-14 02:20 UTC

New packages created between 2026-10-14 01:21 UTC and 2026-10-14 02:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-14T02-20-23-830536Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-14 01:30:15 | [CompanyHQ.Services.Sales.Contracts](https://www.nuget.org/packages/CompanyHQ.Services.Sales.Contracts) | 2.1.0 | CompanyHQ | Package Description |
| 2026-10-14 01:38:42 | [CloudySkySoftware.Pulumi.Render](https://www.nuget.org/packages/CloudySkySoftware.Pulumi.Render) | 0.6.0 | Cloudy Sky Software | A Pulumi package for creating and managing Render resources. |
| 2026-10-14 01:52:06 | [TinyMCE.Premium](https://www.nuget.org/packages/TinyMCE.Premium) | 8.10.0 | Ephox Corporation DBA Tiny Te… | Premium plugins for the TinyMCE rich text editor |
| 2026-10-14 02:02:06 | [Swipewalk.any](https://www.nuget.org/packages/Swipewalk.any) | 0.6.0 | Swipewalk | Accessibility scanner for running Android and iOS apps, tried on native Android… |
| 2026-10-14 02:02:36 | [Swipewalk.osx-arm64](https://www.nuget.org/packages/Swipewalk.osx-arm64) | 0.6.0 | Swipewalk | Accessibility scanner for running Android and iOS apps, tried on native Android… |
| 2026-10-14 02:02:41 | [Swipewalk.osx-x64](https://www.nuget.org/packages/Swipewalk.osx-x64) | 0.6.0 | Swipewalk | Accessibility scanner for running Android and iOS apps, tried on native Android… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

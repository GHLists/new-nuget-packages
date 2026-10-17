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

## Latest list — 2026-10-17 15:19 UTC

New packages created between 2026-10-17 14:21 UTC and 2026-10-17 15:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-17T15-19-27-761784Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-17 14:51:42 | [GPAL](https://www.nuget.org/packages/GPAL) | 1.0.0 | Software Decisions, Inc. | GPAL (Generally Positive Automation Library) is a fluent C# library for automat… |
| 2026-10-17 14:52:09 | [GPAL.Image](https://www.nuget.org/packages/GPAL.Image) | 1.0.0 | Software Decisions, Inc. | Image matching for GPAL (Generally Positive Automation Library). Finds a pictur… |
| 2026-10-17 14:53:18 | [SafeSign](https://www.nuget.org/packages/SafeSign) | 1.0.0 | Glenn Watson and Contributors | Cross-platform code signing command line for Windows executables, installers, p… |
| 2026-10-17 14:55:27 | [Unshackle](https://www.nuget.org/packages/Unshackle) | 0.1.0 | Timme Kingma | Migrates .NET code away from libraries that went commercial: FluentAssertions →… |
| 2026-10-17 15:06:20 | [ES.Framework.AspNetCore](https://www.nuget.org/packages/ES.Framework.AspNetCore) | 1.0.0 | Framework CO Team. | Core framework AspNetCore utilities for ASP.NET Core applications |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

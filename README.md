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

## Latest list — 2026-10-01 11:20 UTC

New packages created between 2026-10-01 10:19 UTC and 2026-10-01 11:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-01T11-20-38-086942Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-01 10:44:17 | [LocalOrigin](https://www.nuget.org/packages/LocalOrigin) | 0.1.0 | iyulab | Gives a local web page its own origin: origin allocation and persistence, a dur… |
| 2026-10-01 10:44:17 | [LocalOrigin.AspNetCore](https://www.nuget.org/packages/LocalOrigin.AspNetCore) | 0.1.0 | iyulab | Hosting for local-origin on ASP.NET Core: serving a scope's pages with a fixed… |
| 2026-10-01 10:44:57 | [LineTrace](https://www.nuget.org/packages/LineTrace) | 0.1.1 | Akshay Dhola | Line-level .NET profiler: patches IL after build and writes an HTML report of t… |
| 2026-10-01 11:02:31 | [Ironbrain.Calendar](https://www.nuget.org/packages/Ironbrain.Calendar) | 0.1.0 | kern-services | CalDAV / iCalendar client for arbitrary self-hosted calendar servers (e.g. Mail… |
| 2026-10-01 11:02:32 | [Ironbrain.Email](https://www.nuget.org/packages/Ironbrain.Email) | 0.1.0 | kern-services | IMAP/SMTP client (MailKit) for self-hosted mail servers. Shared by Ironbrain Ma… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

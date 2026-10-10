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

## Latest list — 2026-10-10 04:18 UTC

New packages created between 2026-10-10 03:20 UTC and 2026-10-10 04:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-10T04-18-51-829331Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-10 03:51:02 | [Loathesoft.Equatables](https://www.nuget.org/packages/Loathesoft.Equatables) | 0.0.1-alpha | Scott Sanderson | Package Description |
| 2026-10-10 03:56:08 | [WebHop.Gateway](https://www.nuget.org/packages/WebHop.Gateway) | 2.0.0 | elebree | The WebHop gateway as ASP.NET Core middleware: accept public HTTP traffic and f… |
| 2026-10-10 03:56:09 | [webhop](https://www.nuget.org/packages/webhop) | 2.0.0 | elebree | Package Description |
| 2026-10-10 03:56:10 | [WebHop.Origin](https://www.nuget.org/packages/WebHop.Origin) | 2.0.0 | elebree | Serve an ASP.NET Core app through a WebHop gateway from behind NAT or a firewal… |
| 2026-10-10 03:59:13 | [NickStrupat.Atomic](https://www.nuget.org/packages/NickStrupat.Atomic) | 0.1.0 | Nick Strupat | A generic atomic cell for .NET. Read, Write and Exchange allocate nothing, for… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

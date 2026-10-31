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

## Latest list — 2026-10-31 13:20 UTC

New packages created between 2026-10-31 12:20 UTC and 2026-10-31 13:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-31T13-20-20-508555Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-31 12:42:06 | [Cratis.Showrunner.BoxOffice.Offering](https://www.nuget.org/packages/Cratis.Showrunner.BoxOffice.Offering) | 1.6.0 | Cratis | Box Office for a product - declare what the product sells (modules, meters, sea… |
| 2026-10-31 12:45:30 | [Surprenant.Grunt.Gateway.Client](https://www.nuget.org/packages/Surprenant.Grunt.Gateway.Client) | 0.1.0 | Noah Surprenant | IHaloInfiniteClient implementation that calls a Grunt Halo gateway over HTTP in… |
| 2026-10-31 13:06:43 | [Cratis.Showrunner.Marquee.Authoring](https://www.nuget.org/packages/Cratis.Showrunner.Marquee.Authoring) | 1.6.0 | Cratis | Marquee authoring — the commands, events and outbox for writing announcements t… |
| 2026-10-31 13:06:44 | [Cratis.Showrunner.Marquee](https://www.nuget.org/packages/Cratis.Showrunner.Marquee) | 1.6.0 | Cratis | Marquee — the Showrunner announcements part for products: receive announcements… |
| 2026-10-31 13:12:12 | [Spoleto.TrueApi.Edo](https://www.nuget.org/packages/Spoleto.TrueApi.Edo) | 1.2.0 | OlegNadymov,Spoleto-Software | TrueApi EDO Lite provider for CRPT |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

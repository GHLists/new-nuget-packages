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

## Latest list — 2026-11-07 02:21 UTC

New packages created between 2026-11-07 01:20 UTC and 2026-11-07 02:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-07T02-21-57-372691Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-07 01:29:03 | [Thrivea.Sdk](https://www.nuget.org/packages/Thrivea.Sdk) | 0.1.0 | Thrivea d.o.o. | Official .NET client for the Thrivea public REST API (/v1): job openings, candi… |
| 2026-11-07 01:37:12 | [StdUnit.DingTalk](https://www.nuget.org/packages/StdUnit.DingTalk) | 0.2.0 | StdUnit.DingTalk | Package Description |
| 2026-11-07 01:37:14 | [StdUnit.DingTalk.OneAuth](https://www.nuget.org/packages/StdUnit.DingTalk.OneAuth) | 0.2.0 | StdUnit.DingTalk.OneAuth | Package Description |
| 2026-11-07 01:39:05 | [redb.Route.DataFormats.XmlJson](https://www.nuget.org/packages/redb.Route.DataFormats.XmlJson) | 4.7.0 | redbase | XML to JSON and back without a class for redb.Route: the Json.NET notation (@at… |
| 2026-11-07 01:39:27 | [EasyReasy.Auth.Microsoft](https://www.nuget.org/packages/EasyReasy.Auth.Microsoft) | 1.0.0 | Adam Tovatt | Sign in with Microsoft work and school accounts for EasyReasy.Auth, through the… |
| 2026-11-07 01:48:34 | [Stomme.Cartographer](https://www.nuget.org/packages/Stomme.Cartographer) | 10.82.0 | Nova Globen AB | Surveys a software repository of any shape and writes what a tracker and a wiki… |
| 2026-11-07 01:48:37 | [Stomme.Conductor](https://www.nuget.org/packages/Stomme.Conductor) | 10.82.0 | Nova Globen AB | A general engine that runs a playbook with context: units of work, a resumable… |
| 2026-11-07 01:51:47 | [BinaryBufferLib](https://www.nuget.org/packages/BinaryBufferLib) | 0.1.0 | Quantam | A collection of lightweight objects for reading and writing binary data with au… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

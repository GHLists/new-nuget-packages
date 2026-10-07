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

## Latest list — 2026-10-07 14:20 UTC

New packages created between 2026-10-07 13:22 UTC and 2026-10-07 14:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-07T14-20-24-08568Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-07 13:25:49 | [DanishFriendlyIds](https://www.nuget.org/packages/DanishFriendlyIds) | 0.1.0 | Kim Lindhard | Human-friendly Danish identifiers: "glade danser" for a person, "blå kasse" for… |
| 2026-10-07 13:31:48 | [Umbraco.Community.DocumentBlueprintsInContent](https://www.nuget.org/packages/Umbraco.Community.DocumentBlueprintsInContent) | 1.0.0 | Gheorghe Efros | Adds Document Blueprints to the Umbraco Content section, behind a dedicated use… |
| 2026-10-07 13:44:22 | [MavLinkSharp.Cli](https://www.nuget.org/packages/MavLinkSharp.Cli) | 1.14.0 | TekLot | MAVLink diagnostic CLI: capture, inspect, replay, and dialect introspection. |
| 2026-10-07 13:47:31 | [Richardbmk.IncidentTracker.Core](https://www.nuget.org/packages/Richardbmk.IncidentTracker.Core) | 1.0.0 | Richardbmk | Shared models and utilities for the Incident Tracker application. |
| 2026-10-07 13:51:05 | [LunaticPanel.Core.Analyzer](https://www.nuget.org/packages/LunaticPanel.Core.Analyzer) | 0.0.9 | LunaticPanel.Core.Analyzer | Package Description |
| 2026-10-07 13:55:31 | [nightmaregaurav.schedulite](https://www.nuget.org/packages/nightmaregaurav.schedulite) | 1.0.1 | Gaurav Nyaupane | A lightweight and flexible scheduling library for .NET applications. |
| 2026-10-07 13:56:10 | [Nesco.Server.Contracts](https://www.nuget.org/packages/Nesco.Server.Contracts) | 0.1.0 | Nesco | The routes, headers and records of the wire between a product installation and… |
| 2026-10-07 13:56:30 | [Balikobot](https://www.nuget.org/packages/Balikobot) | 0.1.0 | M1chlCZ | A C#/.NET client for the Balikobot shipping API v2: packages, labels, tracking,… |
| 2026-10-07 14:05:44 | [CK.AppIdentity.Cris.AuthCenter](https://www.nuget.org/packages/CK.AppIdentity.Cris.AuthCenter) | 2.0.0 | Signature Code | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-18 12:19 UTC

New packages created between 2026-10-18 11:18 UTC and 2026-10-18 12:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-18T12-19-54-882218Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-18 11:29:54 | [Insiyab.Avalonia](https://www.nuget.org/packages/Insiyab.Avalonia) | 0.2.0 | Mohammad Diab | Insiyab for Avalonia: the glass, RTL-first design system as Avalonia themes. |
| 2026-10-18 11:32:44 | [Authway.Native](https://www.nuget.org/packages/Authway.Native) | 0.1.0 | iyulab | Sign a desktop or command-line app's user in with the system browser (OAuth 2.0… |
| 2026-10-18 11:44:15 | [sf-DiscordRPC-NativeAOT](https://www.nuget.org/packages/sf-DiscordRPC-NativeAOT) | 1.6.1 | Lachee,AlphaBs | .NET 10 and NativeAOT compatible Discord Rich Presence client using System.Text… |
| 2026-10-18 11:52:38 | [SlipeServer.Net.Core](https://www.nuget.org/packages/SlipeServer.Net.Core) | 0.1.0-CI-20261018-1… | Slipe | Interfaces and enums for the Slipe Server MTA San Andreas net library wrapper |
| 2026-10-18 11:52:41 | [SlipeServer.Net.MtaBinaries](https://www.nuget.org/packages/SlipeServer.Net.MtaBinaries) | 0.1.0-CI-20261018-1… | Slipe | MTA San Andreas net library binaries and NetWrapper implementation for Slipe Se… |
| 2026-10-18 12:03:31 | [D365KnowledgeBase.Devbox](https://www.nuget.org/packages/D365KnowledgeBase.Devbox) | 1.0.0 | D365KnowledgeBase.Devbox | Where Dynamics 365 Finance and Operations metadata lives on a development box a… |
| 2026-10-18 12:04:03 | [D365KnowledgeBase.Labels](https://www.nuget.org/packages/D365KnowledgeBase.Labels) | 1.0.0 | D365KnowledgeBase.Labels | Dynamics 365 Finance and Operations label files: reading and writing the .label… |
| 2026-10-18 12:04:17 | [D365KnowledgeBase.Metadata](https://www.nuget.org/packages/D365KnowledgeBase.Metadata) | 1.0.0 | D365KnowledgeBase.Metadata | Dynamics 365 Finance and Operations metadata elements read from their XML files… |
| 2026-10-18 12:09:53 | [Vestigium.Helpers.Kql.ActiveSetup](https://www.nuget.org/packages/Vestigium.Helpers.Kql.ActiveSetup) | 1.0.0 | Vestigium | Active Setup field catalog and session for Vestigium.Helpers.Kql. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-14 18:21 UTC

New packages created between 2026-10-14 17:21 UTC and 2026-10-14 18:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-14T18-21-40-516252Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-14 17:23:25 | [CPMForge.Browser.Profiles](https://www.nuget.org/packages/CPMForge.Browser.Profiles) | 0.1.3 | Christian Prior-Mamulyan | Bare Chrome and Edge user data folder templates for deterministic UiPath browse… |
| 2026-10-14 17:32:42 | [Bennewitz.Ninja.XamlQuality.ThemeRuntime](https://www.nuget.org/packages/Bennewitz.Ninja.XamlQuality.ThemeRuntime) | 2026.4.1014 | Brian Bennewitz | The runtime half of the XamlQuality theme audit, as source files an Avalonia te… |
| 2026-10-14 17:33:26 | [XperienceCommunity.UsageApplications](https://www.nuget.org/packages/XperienceCommunity.UsageApplications) | 0.2.0 | BlueModus | Admin applications for Xperience by Kentico that report how many content items… |
| 2026-10-14 17:41:13 | [CodeWF.Avalonia.MindView](https://www.nuget.org/packages/CodeWF.Avalonia.MindView) | 12.1.4.16 | 沙漠尽头的狼 | Avalonia mind map editor, Markdown viewer, import/export and light/dark accent… |
| 2026-10-14 17:43:49 | [budul.ChainFinder](https://www.nuget.org/packages/budul.ChainFinder) | 1.0.0 | budul100 | Generic helper library to build chains (connected paths) from directed elements… |
| 2026-10-14 18:00:08 | [Stellaegis.Messaging.MailKit](https://www.nuget.org/packages/Stellaegis.Messaging.MailKit) | 1.0.0 | FRi | SMTP transport for Stellaegis.Messaging, on MailKit: Basic or client-certificat… |
| 2026-10-14 18:00:08 | [Stellaegis.Messaging.PostgreSQL](https://www.nuget.org/packages/Stellaegis.Messaging.PostgreSQL) | 1.0.0 | FRi | Durable outbox for Stellaegis.Messaging on PostgreSQL: payload encrypted at res… |
| 2026-10-14 18:00:09 | [Stellaegis.Messaging](https://www.nuget.org/packages/Stellaegis.Messaging) | 1.0.0 | FRi | Stellaegis messaging core: EmailMessage/IEmailSender contracts, configuration p… |
| 2026-10-14 18:00:10 | [Stellaegis.Messaging.Secrets](https://www.nuget.org/packages/Stellaegis.Messaging.Secrets) | 1.0.0 | FRi | Messaging configuration per compartment in a Stellaegis.Secrets vault, for Stel… |
| 2026-10-14 18:02:14 | [MyMc.Net](https://www.nuget.org/packages/MyMc.Net) | 0.1.0 | Eric Hill | A .Net port of MyMC, an open-source utility for managing PS2 memory card images… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

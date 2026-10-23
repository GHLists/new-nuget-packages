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

## Latest list — 2026-10-23 16:20 UTC

New packages created between 2026-10-23 15:21 UTC and 2026-10-23 16:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-23T16-20-33-64607Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-23 15:25:21 | [Activout.MemberData](https://www.nuget.org/packages/Activout.MemberData) | 1.0.0 | Activout AB | Client for LinkedIn's Member Data Portability (Member) snapshot and changelog A… |
| 2026-10-23 15:25:23 | [Activout.MemberData.Cli](https://www.nuget.org/packages/Activout.MemberData.Cli) | 1.0.0 | Activout AB | The member command: sync your own LinkedIn Member Data Portability data into a… |
| 2026-10-23 15:29:35 | [Solvano.Sdk](https://www.nuget.org/packages/Solvano.Sdk) | 0.0.1 | Solvano | Reserved for the Solvano SDK — https://solvano.ai |
| 2026-10-23 15:32:02 | [ReactiveDomain.PolicyTool](https://www.nuget.org/packages/ReactiveDomain.PolicyTool) | 0.19.0 | Reactive Domain Group | Command-line tool for administering ReactiveDomain identity and policy streams.… |
| 2026-10-23 15:32:05 | [ReactiveDomain.Policy.Core](https://www.nuget.org/packages/ReactiveDomain.Policy.Core) | 0.19.0 | Reactive Domain Group | Policies, roles and permissions for ReactiveDomain, with the dispatcher that au… |
| 2026-10-23 15:32:05 | [ReactiveDomain.IdentityStorage](https://www.nuget.org/packages/ReactiveDomain.IdentityStorage) | 0.19.0 | Reactive Domain Group | Event-sourced identity storage for ReactiveDomain: users, subjects and clients,… |
| 2026-10-23 15:41:27 | [RecursiveAI.OneImage.Pdf](https://www.nuget.org/packages/RecursiveAI.OneImage.Pdf) | 1.6.0 | Recursive AI, LLC | PDF support for OneImage: renders PDF pages as an image format, drawn on demand… |
| 2026-10-23 15:44:57 | [PowerTraces.Sdk](https://www.nuget.org/packages/PowerTraces.Sdk) | 1.0.1 | PowerTraces | OpenTelemetry for ASP.NET Core, set up for PowerTraces in one line: traces, log… |
| 2026-10-23 15:45:17 | [K9o.Core](https://www.nuget.org/packages/K9o.Core) | 1.0.0 | Kilimanjaro | Kilimanjaro platform SDK — createClient + data DSL + projects + gate + Studio (… |
| 2026-10-23 15:45:22 | [K9o.Kibo](https://www.nuget.org/packages/K9o.Kibo) | 1.0.0 | Kilimanjaro | Kibo Zero-Knowledge BYOK/HYOK vault SDK for .NET — client-side encrypt/decrypt… |
| 2026-10-23 15:46:41 | [MetuCom.Testy.MySecondPackage](https://www.nuget.org/packages/MetuCom.Testy.MySecondPackage) | 1.0.0 | MySecondPackage | Package Description |
| 2026-10-23 15:46:54 | [DubUrl.Adbc](https://www.nuget.org/packages/DubUrl.Adbc) | 0.44.0 | Cédric L. Charlier | ADBC provider integration for DubUrl's ADO.NET connection and querying APIs. |
| 2026-10-23 15:48:55 | [SLVZ.Billing.Myket](https://www.nuget.org/packages/SLVZ.Billing.Myket) | 1.0.0 | Ashkan SLVZ | A lightweight library for Android developers that make you able to purchase in… |
| 2026-10-23 15:49:18 | [SLVZ.Billing.Bazaar](https://www.nuget.org/packages/SLVZ.Billing.Bazaar) | 1.0.0 | Ashkan SLVZ | A lightweight library for Android developers that make you able to purchase in… |
| 2026-10-23 15:50:32 | [ConventionMapper](https://www.nuget.org/packages/ConventionMapper) | 1.0.0 | Katragadda | A convention-based object-object mapper for .NET. Flattening, unflattening (Rev… |
| 2026-10-23 15:51:55 | [FireShop.Net.Hub](https://www.nuget.org/packages/FireShop.Net.Hub) | 1.2026.0 | FIRESOFT ITALIA SRL | Contratti condivisi fra il servizio di FireShop.Net per i dispositivi (hub) e i… |
| 2026-10-23 15:54:04 | [Stellaegis.Identity.SqlServer](https://www.nuget.org/packages/Stellaegis.Identity.SqlServer) | 6.0.0 | FRi | The SQL Server stores of Stellaegis.Identity: the accounts, their second factor… |
| 2026-10-23 16:05:01 | [CodeCrush.Meshtastic.Core](https://www.nuget.org/packages/CodeCrush.Meshtastic.Core) | 0.1.1 | CodeCrush | Transport-agnostic Meshtastic client: streaming API handshake, text messages, n… |
| 2026-10-23 16:05:03 | [CodeCrush.Meshtastic.Protobufs](https://www.nuget.org/packages/CodeCrush.Meshtastic.Protobufs) | 0.1.1 | CodeCrush | Generated C# types for the official Meshtastic protobuf definitions. |
| 2026-10-23 16:05:04 | [CodeCrush.Meshtastic.Serial](https://www.nuget.org/packages/CodeCrush.Meshtastic.Serial) | 0.1.1 | CodeCrush | USB serial transport for CodeCrush.Meshtastic.Core. |
| 2026-10-23 16:13:16 | [DigitalWonderlab.ImageResizer](https://www.nuget.org/packages/DigitalWonderlab.ImageResizer) | 1.0.0 | Digital Wonderlab | Backoffice dashboard that finds oversized images in the media library, resizes… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

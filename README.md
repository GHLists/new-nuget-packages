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

## Latest list — 2026-11-16 10:19 UTC

New packages created between 2026-11-16 09:18 UTC and 2026-11-16 10:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-16T10-19-11-488817Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-16 09:21:21 | [BccCode.Privacy.Hosting](https://www.nuget.org/packages/BccCode.Privacy.Hosting) | 0.5.1 | BCC | One AddPrivacy() for BCC Privacy: the EF Core, ASP.NET Core and Wolverine packa… |
| 2026-11-16 09:38:51 | [BehpardakhtPosPc.Sdk](https://www.nuget.org/packages/BehpardakhtPosPc.Sdk) | 0.0.1 | Alirezar | Behpardakht POS-PC client for .NET. Speaks protocol revision 4.7 over TCP and s… |
| 2026-11-16 09:56:16 | [ArdinLogger.netcore](https://www.nuget.org/packages/ArdinLogger.netcore) | 1.0.42128 | ARDINSYS | ArdinSys logger .NET Core component |
| 2026-11-16 09:59:43 | [io7.FreePDF.Accessibility.Tool](https://www.nuget.org/packages/io7.FreePDF.Accessibility.Tool) | 7.11.0 | io7 | Offline PDF/UA-1 accessibility preflight with explicit partial coverage and hum… |
| 2026-11-16 10:02:21 | [Rustegon.Driver](https://www.nuget.org/packages/Rustegon.Driver) | 0.1.0 | Davide Pegoraro | Official .NET driver for the Rustegon distributed ACID document database. |
| 2026-11-16 10:06:26 | [TestResults.Engine](https://www.nuget.org/packages/TestResults.Engine) | 6.0.0.15 | progile AG | Engine test framework for developing testcases with TestResults |
| 2026-11-16 10:07:17 | [Ranvier.BAREWire.Query.Traced](https://www.nuget.org/packages/Ranvier.BAREWire.Query.Traced) | 0.1.0 | shayanhabibi | Ranvier.Query families and mutations whose remote calls are BAREWire asks, and… |
| 2026-11-16 10:07:18 | [Ranvier.BAREWire.Traced](https://www.nuget.org/packages/Ranvier.BAREWire.Traced) | 0.1.0 | shayanhabibi | BAREWire for Ranvier: BAREWire's encoder, decoder, schema and envelope framing… |
| 2026-11-16 10:07:19 | [Ranvier.BAREWire](https://www.nuget.org/packages/Ranvier.BAREWire) | 0.1.0 | shayanhabibi | BAREWire for Ranvier: BAREWire's encoder, decoder, schema and envelope framing… |
| 2026-11-16 10:07:20 | [Ranvier.BAREWire.Query](https://www.nuget.org/packages/Ranvier.BAREWire.Query) | 0.1.0 | shayanhabibi | Ranvier.Query families and mutations whose remote calls are BAREWire asks, and… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

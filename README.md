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

## Latest list — 2026-10-08 07:19 UTC

New packages created between 2026-10-08 06:19 UTC and 2026-10-08 07:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-08T07-19-06-991052Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-08 06:21:30 | [Database.Oracle](https://www.nuget.org/packages/Database.Oracle) | 1.0.0 | Dio Liew | An Oracle databse package wrapper. |
| 2026-10-08 06:22:56 | [Database.Services](https://www.nuget.org/packages/Database.Services) | 1.0.0 | Dio Liew | A generic databse package wrapper. |
| 2026-10-08 06:28:18 | [Beckhoff.TwinCAT.HMI.Industries.Utils.FaceplateObject](https://www.nuget.org/packages/Beckhoff.TwinCAT.HMI.Industries.Utils.FaceplateObject) | 1.0.3 | Beckhoff Automation GmbH & Co… | TwinCAT HMI is a development environment for web-based HMIs (Human Machine Inte… |
| 2026-10-08 06:31:51 | [Org.Limitless.Seqeron](https://www.nuget.org/packages/Org.Limitless.Seqeron) | 0.11.0 | Fredrik Dahlberg | The seqeron client tier: follow a seqeron cluster's ordered stream and submit t… |
| 2026-10-08 06:36:23 | [Galosys.Foundation.Elastic.Clients.Elasticsearch](https://www.nuget.org/packages/Galosys.Foundation.Elastic.Clients.Elasticsearch) | 26.10.8.1 | Galosys | Galosys.Foundation快速开发库 |
| 2026-10-08 06:41:53 | [ProCode.Engine.Model](https://www.nuget.org/packages/ProCode.Engine.Model) | 7.0.0.1 | ProCode | Package Description |
| 2026-10-08 06:41:55 | [ProCode.Plugin](https://www.nuget.org/packages/ProCode.Plugin) | 7.0.0.1 | ProCode | Package Description |
| 2026-10-08 06:41:57 | [ProCode.License](https://www.nuget.org/packages/ProCode.License) | 7.0.0.1 | ProCode | Package Description |
| 2026-10-08 06:41:59 | [ProCode.Engine.ML.Contracts](https://www.nuget.org/packages/ProCode.Engine.ML.Contracts) | 7.0.0.1 | ProCode | Package Description |
| 2026-10-08 06:42:02 | [ProCode.Core](https://www.nuget.org/packages/ProCode.Core) | 7.0.0.1 | ProCode | Package Description |
| 2026-10-08 06:42:04 | [ProCode.Engine](https://www.nuget.org/packages/ProCode.Engine) | 7.0.0.1 | ProCode | Package Description |
| 2026-10-08 06:42:06 | [ProCode.Engine.ML.Client](https://www.nuget.org/packages/ProCode.Engine.ML.Client) | 7.0.0.1 | ProCode | Package Description |
| 2026-10-08 06:42:08 | [ProCode.Engine.ML.Onnx](https://www.nuget.org/packages/ProCode.Engine.ML.Onnx) | 7.0.0.1 | ProCode | Package Description |
| 2026-10-08 06:42:10 | [ProCode.Engine.Identity](https://www.nuget.org/packages/ProCode.Engine.Identity) | 7.0.0.1 | ProCode | Package Description |
| 2026-10-08 06:42:12 | [ProCode.Mvc](https://www.nuget.org/packages/ProCode.Mvc) | 7.0.0.1 | ProCode | Package Description |
| 2026-10-08 06:46:52 | [IFSBA](https://www.nuget.org/packages/IFSBA) | 2026.10.8.64641 | IFSBA | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

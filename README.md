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

## Latest list — 2026-10-03 06:21 UTC

New packages created between 2026-10-03 05:20 UTC and 2026-10-03 06:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-03T06-21-44-987065Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-03 05:33:59 | [IPMax](https://www.nuget.org/packages/IPMax) | 0.1.0 | IP-Max | .NET client for the IP-Max GeoIP and IP intelligence API. |
| 2026-10-03 05:47:12 | [Webority.Ads.Microsoft](https://www.nuget.org/packages/Webority.Ads.Microsoft) | 0.2.0 | Webority Technologies | Microsoft Advertising for Webority.Ads: offline conversions through the Campaig… |
| 2026-10-03 06:01:20 | [Polhem.JsonRpc.Payload](https://www.nuget.org/packages/Polhem.JsonRpc.Payload) | 1.0.0 | Polhem contributors | Optional payload envelope for Polhem.JsonRpc: codecs, gzip compression, AES-CBC… |
| 2026-10-03 06:01:21 | [Polhem.JsonRpc.Payload.Server](https://www.nuget.org/packages/Polhem.JsonRpc.Payload.Server) | 1.0.0 | Polhem contributors | Server half of Polhem.JsonRpc.Payload: a dispatcher filter that opens the paylo… |
| 2026-10-03 06:05:43 | [Webority.Ai.Judgment.AspNetCore](https://www.nuget.org/packages/Webority.Ai.Judgment.AspNetCore) | 0.6.0 | Webority Technologies | Calibrated judgments over HTTP for Webority.Ai.Judgment: one handler a product… |
| 2026-10-03 06:05:45 | [Webority.Ai.Judgment.Ledger](https://www.nuget.org/packages/Webority.Ai.Judgment.Ledger) | 0.6.0 | Webority Technologies | The judgment ledger for Webority.Ai.Judgment: one row per judgment leg in the p… |
| 2026-10-03 06:15:29 | [Kombine.Flex.Portal.Client](https://www.nuget.org/packages/Kombine.Flex.Portal.Client) | 0.3.3 | Kombine Technology ApS | Official typed HTTPS/JSON client from Kombine Technology ApS for the public Kom… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

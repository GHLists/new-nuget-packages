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

## Latest list — 2026-09-28 00:20 UTC

New packages created between 2026-09-27 23:22 UTC and 2026-09-28 00:20 UTC.

[Full CSV](data/new-nuget-packages-2026-09-28T00-20-40-576752Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-28 00:04:18 | [Wakebox](https://www.nuget.org/packages/Wakebox) | 0.1.1 | Wakebox | On-device wake word. No key. |
| 2026-09-28 00:13:00 | [CloudMAS](https://www.nuget.org/packages/CloudMAS) | 2026.928.0 | CloudMAS | Send sms with CMCC CloudMAS. |
| 2026-09-28 00:13:28 | [VPT.Einkr.Client](https://www.nuget.org/packages/VPT.Einkr.Client) | 2.0.0 | VPT | OpenAI-SDK-shaped .NET client for Einkr's OpenAI-compatible endpoint (EinkrAICl… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

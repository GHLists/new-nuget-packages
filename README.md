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

## Latest list — 2026-11-01 05:20 UTC

New packages created between 2026-11-01 04:19 UTC and 2026-11-01 05:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-01T05-20-26-039358Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-01 04:31:16 | [SuccessMortgagePartners.Encompass.Client](https://www.nuget.org/packages/SuccessMortgagePartners.Encompass.Client) | 0.1.0 | Success Mortgage Partners | A .NET client for the ICE Mortgage Technology Encompass Developer Connect API:… |
| 2026-11-01 04:43:50 | [GaganDeepSingh.PowerAutomateFlowInventory](https://www.nuget.org/packages/GaganDeepSingh.PowerAutomateFlowInventory) | 1.2026.10.12 | Gagan Deep Singh | Inventory selected Power Automate cloud and desktop flows. Summarize flow trigg… |
| 2026-11-01 04:50:34 | [Doppelganger.HttpClient](https://www.nuget.org/packages/Doppelganger.HttpClient) | 0.0.9 | Niklas Wendel | Doppelganger.HttpClient - mocks HttpClient with Doppelganger's setups and verif… |
| 2026-11-01 05:08:15 | [net.codingwell.quiche](https://www.nuget.org/packages/net.codingwell.quiche) | 0.1.0-alpha1 | Quiche.NET contributors | C# wrapper for Cloudflare's quiche (raw QUIC streams) with prebuilt native bina… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-15 19:21 UTC

New packages created between 2026-10-15 18:21 UTC and 2026-10-15 19:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-15T19-21-22-136069Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-15 18:24:09 | [Bynn.DecisionNode](https://www.nuget.org/packages/Bynn.DecisionNode) | 0.3.1 | Bynn Intelligence | The official .NET client for the DecisionNode decision engine API: ask yes-or-n… |
| 2026-10-15 18:35:31 | [E2e4.Chess.Logic](https://www.nuget.org/packages/E2e4.Chess.Logic) | 1.0.0 | th3snark | Chess move generation and rules library: bitboards, legal move generation, FEN… |
| 2026-10-15 18:40:35 | [BillerContracts.Clients](https://www.nuget.org/packages/BillerContracts.Clients) | 1.1.1 | Aldis | Typed HTTP clients for the Biller API |
| 2026-10-15 18:43:58 | [Indiko.StoreInsights.Client](https://www.nuget.org/packages/Indiko.StoreInsights.Client) | 4.1.0 | INDIKO | Client for Indiko Store Insights: subscription entitlements for app backends, w… |
| 2026-10-15 18:44:25 | [HeroKit.FluentValidation](https://www.nuget.org/packages/HeroKit.FluentValidation) | 2.2.0 | Emre Akdemir | FluentValidation rules for HeroKit: Turkish identity and tax numbers, IBAN, Tur… |
| 2026-10-15 18:51:05 | [Keryhe.Telemetry.Parquet](https://www.nuget.org/packages/Keryhe.Telemetry.Parquet) | 2.0.1 | Keith Heard | Parquet and DuckDB implementation for telemetry persistence |
| 2026-10-15 18:55:53 | [Casko.UmbracoTopology.Templates](https://www.nuget.org/packages/Casko.UmbracoTopology.Templates) | 0.0.1-pre | Casko | Local Umbraco 17 CM/CD topology template for dotnet new. |
| 2026-10-15 19:03:55 | [DotCourier.EntityFrameworkCore](https://www.nuget.org/packages/DotCourier.EntityFrameworkCore) | 0.6.0 | Valossa515 | EF Core transactions for DotCourier: every command runs in a transaction that c… |
| 2026-10-15 19:05:02 | [Xingqiao.SDK](https://www.nuget.org/packages/Xingqiao.SDK) | 1.0.0-alpha | CuPhoenix | .NET 10 Xingqiao SDK restricted to manually approved endpoints, with Responses-… |
| 2026-10-15 19:09:19 | [Aardvark.PixImage.PixCodec](https://www.nuget.org/packages/Aardvark.PixImage.PixCodec) | 1.0.0-prerelease0001 | Aardvark Platform Team | Pure managed image loading and saving for Aardvark PixImages and plain images:… |
| 2026-10-15 19:10:56 | [MarbleSoft.FlowModule.MetaDataAdder](https://www.nuget.org/packages/MarbleSoft.FlowModule.MetaDataAdder) | 0.1.0 | Mario Bless (MarbleSoft) | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

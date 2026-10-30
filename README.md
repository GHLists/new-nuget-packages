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

## Latest list — 2026-10-30 12:21 UTC

New packages created between 2026-10-30 11:20 UTC and 2026-10-30 12:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-30T12-21-25-088733Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-30 11:49:26 | [VehicleVision.PleasanterTools.DatabaseConverter](https://www.nuget.org/packages/VehicleVision.PleasanterTools.DatabaseConverter) | 0.2.0 | PMC Co., Ltd. IT Solution Div. | Pleasanter の DB を、SQL Server・PostgreSQL・MySQL の間で相互に変換するコマンドラインツール。 |
| 2026-10-30 11:53:27 | [Centrifugal.Cent](https://www.nuget.org/packages/Centrifugal.Cent) | 0.1.0 | Centrifugal Labs | Centrifugo server API SDK for .NET: the HTTP API client with broadcasts, batche… |
| 2026-10-30 11:53:28 | [Centrifugal.Cent.AspNetCore](https://www.nuget.org/packages/Centrifugal.Cent.AspNetCore) | 0.1.0 | Centrifugal Labs | ASP.NET Core integration of Centrifugal.Cent, the Centrifugo server API SDK: se… |
| 2026-10-30 11:56:34 | [Resultron.FluentAssertions](https://www.nuget.org/packages/Resultron.FluentAssertions) | 1.0.0 | ferdikurnazdm | FluentAssertions integration for Resultron, providing expressive and readable a… |
| 2026-10-30 11:58:01 | [Themia.Storage.Configuration](https://www.nuget.org/packages/Themia.Storage.Configuration) | 0.46.0 | Sarawut Phaekuntod | One configuration shape for Themia.Storage: AddThemiaStorageFromConfiguration r… |
| 2026-10-30 11:59:00 | [Arc56.Generated.algorandfoundation.algokit-ts](https://www.nuget.org/packages/Arc56.Generated.algorandfoundation.algokit-ts) | 1.0.1.2026103011 | algorandfoundation | Generated ARC-56 Algorand smart-contract clients for algorandfoundation/algokit… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

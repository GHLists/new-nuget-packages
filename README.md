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

## Latest list — 2026-11-15 11:21 UTC

New packages created between 2026-11-15 10:21 UTC and 2026-11-15 11:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-15T11-21-48-041634Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-15 10:48:32 | [PrintSharp.Fonts.Noto](https://www.nuget.org/packages/PrintSharp.Fonts.Noto) | 0.4.0 | ogisyouryuu | All supported Noto fonts for PrintSharp. |
| 2026-11-15 10:48:34 | [PrintSharp.Fonts.NotoSans](https://www.nuget.org/packages/PrintSharp.Fonts.NotoSans) | 0.4.0 | ogisyouryuu | Optional Noto font assets for PrintSharp: NotoSans. |
| 2026-11-15 10:48:35 | [PrintSharp.Fonts.NotoSansArabic](https://www.nuget.org/packages/PrintSharp.Fonts.NotoSansArabic) | 0.4.0 | ogisyouryuu | Optional Noto font assets for PrintSharp: NotoSansArabic. |
| 2026-11-15 10:48:37 | [PrintSharp.Fonts.NotoSansCjk](https://www.nuget.org/packages/PrintSharp.Fonts.NotoSansCjk) | 0.4.0 | ogisyouryuu | Optional Noto font assets for PrintSharp: NotoSansCjk. |
| 2026-11-15 10:48:40 | [PrintSharp.Fonts.NotoSerifCjk](https://www.nuget.org/packages/PrintSharp.Fonts.NotoSerifCjk) | 0.4.0 | ogisyouryuu | Optional Noto font assets for PrintSharp: NotoSerifCjk. |
| 2026-11-15 10:58:33 | [BlazorFeatures.Tools.Abstractions](https://www.nuget.org/packages/BlazorFeatures.Tools.Abstractions) | 1.0.0 | Federico Mangini | Transport-neutral contracts for BlazorFeatures events and external SignalR clie… |
| 2026-11-15 10:58:46 | [BlazorFeatures.Tools.Client](https://www.nuget.org/packages/BlazorFeatures.Tools.Client) | 1.0.0 | Federico Mangini | Cross-render-mode event management for BlazorFeatures client applications. |
| 2026-11-15 10:58:59 | [BlazorFeatures.Tools.Server](https://www.nuget.org/packages/BlazorFeatures.Tools.Server) | 1.0.0 | Federico Mangini | Server routing, authorization and SignalR transport for BlazorFeatures events. |
| 2026-11-15 11:00:00 | [DuckDB.EFCoreProvider.EF11.NTS](https://www.nuget.org/packages/DuckDB.EFCoreProvider.EF11.NTS) | 1.1.0 | skuirrels | NetTopologySuite (spatial) support for DuckDB.EFCoreProvider.EF11 on Entity Fra… |
| 2026-11-15 11:00:01 | [DuckDB.EFCoreProvider.EF11](https://www.nuget.org/packages/DuckDB.EFCoreProvider.EF11) | 1.31.0 | skuirrels | DuckDB, DuckLake and Parquet provider for Entity Framework Core 11, for analyti… |
| 2026-11-15 11:05:50 | [Usa.Smart.WinUI.Hosting](https://www.nuget.org/packages/Usa.Smart.WinUI.Hosting) | 2.0.0 | machi_pon | Smart WinUI support library |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

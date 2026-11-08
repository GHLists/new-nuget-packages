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

## Latest list — 2026-11-08 15:21 UTC

New packages created between 2026-11-08 14:21 UTC and 2026-11-08 15:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-08T15-21-25-978697Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-08 14:24:00 | [Solhigson.Templates](https://www.nuget.org/packages/Solhigson.Templates) | 10.0.0 | Solhigson | dotnet new templates for Solhigson projects. solhigson-web: a layered solution… |
| 2026-11-08 14:28:01 | [BlackSharp.UI.Avalonia.Markdown](https://www.nuget.org/packages/BlackSharp.UI.Avalonia.Markdown) | 1.0.0 | BlackSharp.UI.Avalonia.Markdo… | Native Avalonia controls for viewing and editing CommonMark and GitHub Markdown… |
| 2026-11-08 14:33:02 | [TrueDotBin.CosmosUtils](https://www.nuget.org/packages/TrueDotBin.CosmosUtils) | 1.0.1 | Demiomad | A collection of utilities for Cosmos kernels. |
| 2026-11-08 14:36:42 | [BoringSslStream](https://www.nuget.org/packages/BoringSslStream) | 1.0.0 | Vitaly Yakovlev (optinsoft) | .NET TLS stream backed by BoringSSL with Chrome-like JA4 fingerprints and nativ… |
| 2026-11-08 14:39:28 | [KeelMatrix.FeedFence](https://www.nuget.org/packages/KeelMatrix.FeedFence) | 0.1.0 | KeelMatrix | Audits effective NuGet package sources and Package Source Mapping against the r… |
| 2026-11-08 14:39:32 | [Kreisverkehr.DvbMetadataDecoder](https://www.nuget.org/packages/Kreisverkehr.DvbMetadataDecoder) | 0.1.0 | Kreisverkehr | DvbMetadataDecoder is a .NET library for decoding metadata from DVB transport s… |
| 2026-11-08 14:54:00 | [BYFoundation.ProductUpdate](https://www.nuget.org/packages/BYFoundation.ProductUpdate) | 1.2.0 | BYFoundation | Product updater bridge, bilingual Windows host and installer compatibility asse… |
| 2026-11-08 14:54:02 | [BYFoundation.ReleaseTools](https://www.nuget.org/packages/BYFoundation.ReleaseTools) | 1.0.1 | BYFoundation | Build and release scripts for BYFoundation products, with bounded HFS transfers… |
| 2026-11-08 14:56:11 | [Meshmakers.Octo.Services.RestDeprecation](https://www.nuget.org/packages/Meshmakers.Octo.Services.RestDeprecation) | 3.5.68 | meshmakers GmbH and Contribut… | Marks REST actions deprecated with one attribute: RFC 9745/8594 headers, OpenAP… |
| 2026-11-08 14:59:18 | [DeepSeek.Decisions](https://www.nuget.org/packages/DeepSeek.Decisions) | 1.0.6 | Yue Zhishun | 基于 DeepSeek API 的 Jev 和 Decisions 强类型决策客户端。 |
| 2026-11-08 15:00:47 | [Dflat.Edi.ApiTask](https://www.nuget.org/packages/Dflat.Edi.ApiTask) | 1.7.2.90 | Dflat | Plugins EDI qui exécutent les tâches planifiées d'une application par un appel… |
| 2026-11-08 15:01:27 | [Spoleto.Edm](https://www.nuget.org/packages/Spoleto.Edm) | 1.0.0 | OlegNadymov,Spoleto-Software | Electronic document management (EDM, ЭДО) with different EDM operators such as… |
| 2026-11-08 15:01:27 | [Spoleto.Edm.Extensions](https://www.nuget.org/packages/Spoleto.Edm.Extensions) | 1.0.0 | OlegNadymov,Spoleto-Software | Registration of Spoleto.Edm service in Microsoft DependencyInjection |
| 2026-11-08 15:01:28 | [Spoleto.Edm.Extensions.TrueApi](https://www.nuget.org/packages/Spoleto.Edm.Extensions.TrueApi) | 1.0.0 | OlegNadymov,Spoleto-Software | Registration of CRPT EDO Lite provider for Spoleto.Edm in Microsoft DependencyI… |
| 2026-11-08 15:01:29 | [Spoleto.Edm.TrueApi](https://www.nuget.org/packages/Spoleto.Edm.TrueApi) | 1.0.0 | OlegNadymov,Spoleto-Software | CRPT EDO Lite provider (True API section 9) for Spoleto.Edm |
| 2026-11-08 15:02:56 | [OmniEurope.Diagnostics](https://www.nuget.org/packages/OmniEurope.Diagnostics) | 1.0.0 | OmniEurope contributors | Minimal, unstyled ASP.NET Core diagnostics pages for the site they are mounted… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

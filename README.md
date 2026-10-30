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

## Latest list — 2026-10-30 11:20 UTC

New packages created between 2026-10-30 10:21 UTC and 2026-10-30 11:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-30T11-20-11-882977Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-30 10:30:06 | [KirillMaster.QualityGates.Results](https://www.nuget.org/packages/KirillMaster.QualityGates.Results) | 0.3.0 | KirillMaster | Minimal Result, Result of T, Error and ErrorType for early-return error handlin… |
| 2026-10-30 10:30:07 | [KirillMaster.QualityGates.Testing.AspNetCore](https://www.nuget.org/packages/KirillMaster.QualityGates.Testing.AspNetCore) | 0.3.0 | KirillMaster | WebApplicationFactory helpers for quality-gate tests: host-start smoke, route c… |
| 2026-10-30 10:30:08 | [KirillMaster.QualityGates.Results.AspNetCore](https://www.nuget.org/packages/KirillMaster.QualityGates.Results.AspNetCore) | 0.3.0 | KirillMaster | ToHttpResult ProblemDetails mapping for KirillMaster.QualityGates.Results and a… |
| 2026-10-30 10:31:56 | [StdUnit.Tags.WebUi](https://www.nuget.org/packages/StdUnit.Tags.WebUi) | 2.0.0-beta5 | itminus | 测点项目的 Web 界面（自托管、AOT 友好）：监控页（结构树 + SSE 值流）与设计器（通道/测点，导出项目 XML） |
| 2026-10-30 10:32:41 | [RtoGtoR](https://www.nuget.org/packages/RtoGtoR) | 1.0.0 | TuanFaied | RtoGtoR .NET SDK: bidirectional relational ↔ graph migration (PostgreSQL → Neo4… |
| 2026-10-30 10:36:05 | [Aurionpro.PaymentFramework.Core10.0.API](https://www.nuget.org/packages/Aurionpro.PaymentFramework.Core10.0.API) | 10.0.0 | manoj.aurionpro.com | Package Description |
| 2026-10-30 10:41:42 | [Folio.Store.Oqtane.Trial](https://www.nuget.org/packages/Folio.Store.Oqtane.Trial) | 1.7.0 | CISS / dnndefender.com | Independent Folio Commerce installer for Oqtane 10.0.0+. Includes the native 2s… |
| 2026-10-30 10:44:55 | [VehicleVision.PleasanterTools.BinaryMigrator](https://www.nuget.org/packages/VehicleVision.PleasanterTools.BinaryMigrator) | 0.2.0 | PMC Co., Ltd. IT Solution Div. | Pleasanter に添付されたファイル（Binaries）の保管先を、Rds・Local・AzureBlob の間で移すコマンドラインツール。 |
| 2026-10-30 10:53:54 | [TheDotSide.Aspire.Tools](https://www.nuget.org/packages/TheDotSide.Aspire.Tools) | 0.3.0 | The Dot Side | Traçabilité et migrations contrôlées des dépendances des projets The Dot Side A… |
| 2026-10-30 10:58:23 | [CredOS](https://www.nuget.org/packages/CredOS) | 0.1.0 | Cédric L. Charlier | Application-scoped username/password storage using Windows Credential Manager,… |
| 2026-10-30 11:02:36 | [Len.StronglyTypedId.Testing](https://www.nuget.org/packages/Len.StronglyTypedId.Testing) | 1.4.0 | lenfon | Test-time helpers for Len.StronglyTypedId: generate arbitrary but realistic id… |
| 2026-10-30 11:02:37 | [Len.StronglyTypedId.Testing.AutoFixture](https://www.nuget.org/packages/Len.StronglyTypedId.Testing.AutoFixture) | 1.4.0 | lenfon | AutoFixture integration for Len.StronglyTypedId: fills strongly typed ids as co… |
| 2026-10-30 11:02:38 | [Len.StronglyTypedId.Testing.Bogus](https://www.nuget.org/packages/Len.StronglyTypedId.Testing.Bogus) | 1.4.0 | lenfon | Bogus integration for Len.StronglyTypedId: teaches Bogus to fill strongly typed… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

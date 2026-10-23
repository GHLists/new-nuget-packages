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

## Latest list — 2026-10-23 04:19 UTC

New packages created between 2026-10-23 03:20 UTC and 2026-10-23 04:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-23T04-19-50-704646Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-23 03:20:12 | [ArgentSea.Orleans.Pg](https://www.nuget.org/packages/ArgentSea.Orleans.Pg) | 2.1.0 | ArgentSea.Orleans.Pg | Extension to enable ArgentSea to serve as a data provider for Microsoft Orleans… |
| 2026-10-23 03:24:14 | [Cratis.Specifications.TUnit](https://www.nuget.org/packages/Cratis.Specifications.TUnit) | 4.2.0 | Cratis | Specification by Example (BDD) for .NET with TUnit - Given/When/Then specificat… |
| 2026-10-23 03:24:15 | [Cratis.Specifications.XUnit.v3](https://www.nuget.org/packages/Cratis.Specifications.XUnit.v3) | 4.2.0 | Cratis | Specification by Example (BDD) for .NET with xUnit v3 - Given/When/Then specifi… |
| 2026-10-23 03:24:16 | [Cratis.Specifications.NUnit5](https://www.nuget.org/packages/Cratis.Specifications.NUnit5) | 4.2.0 | Cratis | Specification by Example (BDD) for .NET with NUnit 5 - Given/When/Then specific… |
| 2026-10-23 03:25:54 | [dotnet-nsis](https://www.nuget.org/packages/dotnet-nsis) | 0.1.0 | dotnet-nsis contributors | 将已发布的应用目录打包为 Windows NSIS 安装程序。 |
| 2026-10-23 03:32:49 | [BinToss.XmlSourceGenerator](https://www.nuget.org/packages/BinToss.XmlSourceGenerator) | 0.0.1-DUMMY | Saivineeth,Noah Sherwin | High-performance XML serialization via source generation with XmlSerializer fea… |
| 2026-10-23 03:32:51 | [BinToss.XmlSourceGenerator.Abstractions](https://www.nuget.org/packages/BinToss.XmlSourceGenerator.Abstractions) | 0.0.1-DUMMY | Saivineeth,Noah Sherwin | Runtime abstractions for XmlSourceGenerator - attributes, interfaces, and utili… |
| 2026-10-23 03:34:05 | [BeneficialStrategies.Iso20022.Primitives](https://www.nuget.org/packages/BeneficialStrategies.Iso20022.Primitives) | 1.0.0-alpha | Jeff Ward,Beneficial Strategi… | The ISO 20022 primitive data types, code sets and external codes, with their fo… |
| 2026-10-23 03:43:47 | [SafeQuery](https://www.nuget.org/packages/SafeQuery) | 0.0.1 | Llewellyn Falco | Read-only SQL Server query CLI that rejects anything but SELECT, plus a schema-… |
| 2026-10-23 03:52:21 | [A1Force.MauiObfuscate.Build](https://www.nuget.org/packages/A1Force.MauiObfuscate.Build) | 1.0.1 | A1Force | MSBuild targets that run maui-obfuscate after a Release build. Install the A1Fo… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

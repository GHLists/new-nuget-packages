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

## Latest list — 2026-11-24 16:19 UTC

New packages created between 2026-11-24 15:21 UTC and 2026-11-24 16:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-24T16-19-31-663616Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-24 15:24:21 | [Eagle.Mes.Infrastructure](https://www.nuget.org/packages/Eagle.Mes.Infrastructure) | 1.0.0 | MES Team | MES 基础设施层：缓存（Redis / 内存）、ClickHouse 查询与批量写入、MongoDB GridFS 文件与头像、SMTP 邮件、请求签名认证… |
| 2026-11-24 15:33:15 | [MIA.Padezh.Neural](https://www.nuget.org/packages/MIA.Padezh.Neural) | 0.5.0 | MIA | Нейро-fallback для MIA.Padezh: склонение фамилий, не покрытых правилами (ONNX,… |
| 2026-11-24 15:40:28 | [AgentCircuit](https://www.nuget.org/packages/AgentCircuit) | 1.0.0 | James Hrabchak | Token budget and runaway-loop circuit breaker middleware for Microsoft.Extensio… |
| 2026-11-24 15:50:19 | [SourceCrafter.LiteSpeedLink.Hosting](https://www.nuget.org/packages/SourceCrafter.LiteSpeedLink.Hosting) | 2.26.328.309 | Pedro Gil Mora | LiteSpeedLink on any .NET host (IHost): a generated host runs as a hosted servi… |
| 2026-11-24 15:57:56 | [Devolutions.Psign.Core](https://www.nuget.org/packages/Devolutions.Psign.Core) | 0.9.0 | Devolutions | Pure C# psign core: Authenticode digest recomputation and portable signature ve… |
| 2026-11-24 15:57:58 | [Devolutions.Psign.Signing](https://www.nuget.org/packages/Devolutions.Psign.Signing) | 0.9.0 | Devolutions | Pure C# portable Authenticode and package signing compatible with psign: CMS /… |
| 2026-11-24 16:07:49 | [ExpressionBinding.Avalonia](https://www.nuget.org/packages/ExpressionBinding.Avalonia) | 1.0.0 | Sylinko | Runtime-bound expressions for Avalonia bindings. |
| 2026-11-24 16:07:58 | [Trax.Analyzers](https://www.nuget.org/packages/Trax.Analyzers) | 1.72.0 | Theauxm,mark-keaton | Opt-in Roslyn rules for code that builds on Trax .NET, and for any other .NET c… |
| 2026-11-24 16:08:01 | [Trax.Analyzers.Annotations](https://www.nuget.org/packages/Trax.Analyzers.Annotations) | 1.72.0 | Theauxm,mark-keaton | Attributes that tune the Trax.Analyzers rules from your own code: mark a parame… |
| 2026-11-24 16:08:05 | [Trax.Effect.Configuration.Aws](https://www.nuget.org/packages/Trax.Effect.Configuration.Aws) | 1.72.0 | Theauxm,mark-keaton | Reads a Trax .NET host's secrets from AWS Secrets Manager into its configuratio… |
| 2026-11-24 16:08:16 | [CompuMaster.Excel.OpenXml](https://www.nuget.org/packages/CompuMaster.Excel.OpenXml) | 2026.11.24 | CompuMaster GmbH | Edits XLSX templates with the Open XML SDK through the ExcelOps API. |
| 2026-11-24 16:12:10 | [Alchiweb.Yousign](https://www.nuget.org/packages/Alchiweb.Yousign) | 0.7.0 | Alchiweb | Alchiweb.Yousign |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

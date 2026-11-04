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

## Latest list — 2026-11-04 01:21 UTC

New packages created between 2026-11-04 00:21 UTC and 2026-11-04 01:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-04T01-21-08-363943Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-04 00:56:15 | [Khamsin](https://www.nuget.org/packages/Khamsin) | 0.1.0 | lllggghhhaaa | Khamsin: build-time utility CSS for Blazor with a closed, literal class set. |
| 2026-11-04 00:57:40 | [cecloud.archive.netframework.referenceassemblies](https://www.nuget.org/packages/cecloud.archive.netframework.referenceassemblies) | 1.0.0 | zsc | .NET Framework 4.0 4.5.2 4.6.1 vs2022 运行以上环境。使用方法 下载解压，打开如下目录 .NETFramework 解压后… |
| 2026-11-04 01:08:26 | [FerreiraCodecraft.Commons.Ofx](https://www.nuget.org/packages/FerreiraCodecraft.Commons.Ofx) | 5.2.1 | Lipe1994 | Tolerant reader for OFX bank and credit card statements (OFX 1.x SGML and 2.x X… |
| 2026-11-04 01:14:53 | [WASU.Plugin.RPC.Client](https://www.nuget.org/packages/WASU.Plugin.RPC.Client) | 26.1104.9 | WASU.Plugin.RPC.Client | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

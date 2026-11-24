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

## Latest list — 2026-11-24 06:18 UTC

New packages created between 2026-11-24 05:21 UTC and 2026-11-24 06:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-24T06-18-52-923462Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-24 05:33:42 | [Nextorm.Extensions.Orca](https://www.nuget.org/packages/Nextorm.Extensions.Orca) | 1.0.0 | Nextorm.Extensions.Orca | Nextorm repository contexts for the Orca 1.4.272 SQLite schemas. |
| 2026-11-24 05:37:11 | [Nextorm.Extensions.N8n](https://www.nuget.org/packages/Nextorm.Extensions.N8n) | 1.0.0 | Nextorm.Extensions.N8n | Nextorm repository context for the n8n 2.48.8 SQLite schema. |
| 2026-11-24 05:38:02 | [Shan.ImageCompressor](https://www.nuget.org/packages/Shan.ImageCompressor) | 1.0.0 | Hasibul Islam Shanto | Compress JPEG and PNG images toward a target file size with zero dependencies (… |
| 2026-11-24 05:54:02 | [Jtext103.CFET2.Things.DdaqThing](https://www.nuget.org/packages/Jtext103.CFET2.Things.DdaqThing) | 1.0.0 | Jtext103 | DDAQ acquisition control for CFET2. |
| 2026-11-24 05:57:09 | [Jtext103.CFET2.Things.NewMDSplusThing](https://www.nuget.org/packages/Jtext103.CFET2.Things.NewMDSplusThing) | 1.0.0 | Jtext103 | MDSplus archiving of DDAQ acquisition data for CFET2. |
| 2026-11-24 06:11:39 | [ConfigInfo](https://www.nuget.org/packages/ConfigInfo) | 1.2.0 | daipeng0809 | 面向 AOT 的轻量文本配置库（.cif 格式）：核心零反射、单遍解析、宽松类型转换，支持注释读写、自动注释与可选自动对象映射。 |
| 2026-11-24 06:12:47 | [Tacsa](https://www.nuget.org/packages/Tacsa) | 1.0.0 | TACSA — Compañía de Transport… | TACSA cafe Guayaquil, Ecuador constants. Official: https://tacsa.com.ec/expreso… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

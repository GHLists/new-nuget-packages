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

## Latest list — 2026-10-22 15:20 UTC

New packages created between 2026-10-22 14:19 UTC and 2026-10-22 15:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-22T15-20-48-457543Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-22 14:20:23 | [org.anosys.in.DevOps](https://www.nuget.org/packages/org.anosys.in.DevOps) | 1.0.0 | Anosys | Shared PowerShell commands for planning, validating and publishing NuGet releas… |
| 2026-10-22 14:33:04 | [Transmitly.ContentTemplate.Contentful](https://www.nuget.org/packages/Transmitly.ContentTemplate.Contentful) | 0.4.5 | Code Impressions | A extension to enable content from Contentful to be used as channel content tem… |
| 2026-10-22 14:34:10 | [Tesserae.Themes.Stratus](https://www.nuget.org/packages/Tesserae.Themes.Stratus) | 26.10.72651 | Curiosity GmbH | An aerospace-grade design language as a Tesserae custom theme: deep navy accent… |
| 2026-10-22 14:34:21 | [Tesserae.Themes.RetroOS](https://www.nuget.org/packages/Tesserae.Themes.RetroOS) | 26.10.72651 | Curiosity GmbH | A Tesserae custom theme inspired by the original 1984 Macintosh System Software… |
| 2026-10-22 14:34:59 | [Bitzsoft.Integrations.SyntheticData.Enterprise](https://www.nuget.org/packages/Bitzsoft.Integrations.SyntheticData.Enterprise) | 1.0.4 | Bitzsoft | Bitzsoft 智能合成数据企业与协同垂直扩展包 — 包含层级部门树、职级职能、审批流任务单与公文流转语料 |
| 2026-10-22 14:35:28 | [Bitzsoft.Integrations.SyntheticData.Web](https://www.nuget.org/packages/Bitzsoft.Integrations.SyntheticData.Web) | 1.0.4 | Bitzsoft | Bitzsoft 智能合成数据门户与媒体垂直扩展包 — 包含栏目分类树、深度资讯文章、轮播Banner与免版税视觉资产语料 |
| 2026-10-22 14:36:04 | [Bitzsoft.Integrations.SyntheticData.Legal](https://www.nuget.org/packages/Bitzsoft.Integrations.SyntheticData.Legal) | 1.0.4 | Bitzsoft | Bitzsoft 智能合成数据司法垂直扩展包 — 包含审级法院、司法案号、案由事实、裁判文书、法条与律师执业资质语料 |
| 2026-10-22 14:38:40 | [EsOptionGamma.Core](https://www.nuget.org/packages/EsOptionGamma.Core) | 0.2.8 | PulseTrade M:/YT Team | Core Domain, CME Trading Calendar, and IEs1kOhlcvProvider contract |
| 2026-10-22 14:41:00 | [Umbraco.Community.AI.Search.Pinecone](https://www.nuget.org/packages/Umbraco.Community.AI.Search.Pinecone) | 18.0.0 | Lee Mills | A vector store for Umbraco AI Search that keeps its embeddings in a Pinecone se… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

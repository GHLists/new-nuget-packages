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

## Latest list — 2026-11-12 04:19 UTC

New packages created between 2026-11-12 03:20 UTC and 2026-11-12 04:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-12T04-19-37-150082Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-12 03:25:30 | [SourceGenerators.Shared](https://www.nuget.org/packages/SourceGenerators.Shared) | 1.0.0 | 何镇汐 | 源生成器共享源码包 |
| 2026-11-12 03:33:51 | [AquaCulture.GIS.Gdal](https://www.nuget.org/packages/AquaCulture.GIS.Gdal) | 1.1.0 | Gravicode Studios (Kang Fadhi… | GDAL raster I/O for AquaCulture.Net (GeoTIFF and 200+ formats via Gravicode.GDA… |
| 2026-11-12 03:33:54 | [AquaCulture.IoT.OpcUa](https://www.nuget.org/packages/AquaCulture.IoT.OpcUa) | 1.1.0 | Gravicode Studios (Kang Fadhi… | OPC UA for AquaCulture.Net over the OPC Foundation .NET Standard stack: an IOpc… |
| 2026-11-12 03:33:56 | [AquaCulture.Data](https://www.nuget.org/packages/AquaCulture.Data) | 1.1.0 | Gravicode Studios (Kang Fadhi… | Persistence for AquaCulture.Net: EF Core / SQLite store for farms, culture cycl… |
| 2026-11-12 03:38:00 | [Patware.PingTrace.Adapter.RedisCache](https://www.nuget.org/packages/Patware.PingTrace.Adapter.RedisCache) | 0.3.1 | Patware | Redis ping diagnostics through a registered IConnectionMultiplexer. |
| 2026-11-12 03:42:45 | [Juice.Observability.Slos](https://www.nuget.org/packages/Juice.Observability.Slos) | 1.2.0 | Creatorflow.io | Juice Observability: discovery, health, rules and alerts over OpenTelemetry for… |
| 2026-11-12 03:42:46 | [Juice.Observability.Agents](https://www.nuget.org/packages/Juice.Observability.Agents) | 1.2.0 | Creatorflow.io | Juice Observability agent control plane: enrollment, mTLS agent identity, revoc… |
| 2026-11-12 03:42:46 | [Juice.Observability.Agent](https://www.nuget.org/packages/Juice.Observability.Agent) | 1.2.0 | Creatorflow.io | Juice Agent: a host's outbound, mTLS agent for Juice Observability. Reference i… |
| 2026-11-12 03:42:47 | [Juice.Observability.Agent.Contracts](https://www.nuget.org/packages/Juice.Observability.Agent.Contracts) | 1.2.0 | Creatorflow.io | Juice Observability agent contracts: signed command envelopes, typed read-only… |
| 2026-11-12 03:49:47 | [Atct.Sso](https://www.nuget.org/packages/Atct.Sso) | 1.0.1 | Atct | Shared Casdoor OIDC SSO protocol and flow library for Atct systems. |
| 2026-11-12 04:05:09 | [Cike.Localization](https://www.nuget.org/packages/Cike.Localization) | 1.0.13 | Lemon.Li | Package Description |
| 2026-11-12 04:11:19 | [Zue.PhoneticAnnotator.Cli](https://www.nuget.org/packages/Zue.PhoneticAnnotator.Cli) | 0.2.0 | danzuep | Multi-language phonetic annotation (pinyin, Jyutping, furigana, Arabic tashkeel… |
| 2026-11-12 04:11:22 | [Zue.Unihan](https://www.nuget.org/packages/Zue.Unihan) | 0.2.0 | danzuep | Multi-language phonetic annotation (pinyin, Jyutping, furigana, Arabic tashkeel… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

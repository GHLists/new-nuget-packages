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

## Latest list — 2026-10-12 16:21 UTC

New packages created between 2026-10-12 15:20 UTC and 2026-10-12 16:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-12T16-21-18-512735Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-12 15:36:23 | [SjolystInnovation.AppKit.Auth](https://www.nuget.org/packages/SjolystInnovation.AppKit.Auth) | 0.1.0 | Sjølyst Innovation AS | JWT access tokens, rotating refresh tokens with reuse detection, and password r… |
| 2026-10-12 15:38:52 | [NextGenSoftware.OASIS.API.Providers.HoloOASIS.Edge](https://www.nuget.org/packages/NextGenSoftware.OASIS.API.Providers.HoloOASIS.Edge) | 1.0.0 | David Ellams (NextGen Softwar… | Lightweight Holochain 0.7 domain replication target for OASIS Edge Runtime. |
| 2026-10-12 15:56:00 | [Sdcb.HyMT2Sharp](https://www.nuget.org/packages/Sdcb.HyMT2Sharp) | 2.0.0 | sdcb | Hy-MT2 hunyuan-dense inference: GGUF, tokenize, KV cache, CPU (SIMD), Metal and… |
| 2026-10-12 16:04:26 | [YamlD](https://www.nuget.org/packages/YamlD) | 0.0.1 | Infologique.net | Native, allocation-free YAML 1.2.2 parser for .NET 10 with YAML 1.1 merge keys… |
| 2026-10-12 16:12:46 | [Umbraco.Community.FrontendBlockPreview](https://www.nuget.org/packages/Umbraco.Community.FrontendBlockPreview) | 17.0.0 | Busra Sengul | Preview Block List and Block Grid blocks in the Umbraco backoffice, rendered by… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

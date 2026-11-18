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

## Latest list — 2026-11-18 05:20 UTC

New packages created between 2026-11-18 04:20 UTC and 2026-11-18 05:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-18T05-20-56-379707Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-18 04:27:36 | [WhatArch.win-x64](https://www.nuget.org/packages/WhatArch.win-x64) | 0.3.0 | Craig | A command-line tool to detect the target architecture of Windows PE binaries |
| 2026-11-18 04:27:38 | [WhatArch.win-arm64](https://www.nuget.org/packages/WhatArch.win-arm64) | 0.3.0 | Craig | A command-line tool to detect the target architecture of Windows PE binaries |
| 2026-11-18 04:27:40 | [WhatArch.any](https://www.nuget.org/packages/WhatArch.any) | 0.3.0 | Craig | A command-line tool to detect the target architecture of Windows PE binaries |
| 2026-11-18 04:28:05 | [Ambystech.Relate](https://www.nuget.org/packages/Ambystech.Relate) | 1.0.0 | Ambystech | .NET client for Relate by Neo4j, the embedded Cypher graph database for AI agen… |
| 2026-11-18 04:56:21 | [ZeroMayo.Framework.Android](https://www.nuget.org/packages/ZeroMayo.Framework.Android) | 2026.1118.0 | ppy Pty Ltd | A 2D application/game framework written with rhythm games in mind. A community… |
| 2026-11-18 05:02:21 | [Exchange56.GithubProfile.Components.Server](https://www.nuget.org/packages/Exchange56.GithubProfile.Components.Server) | 1.0.0 | T.J. McNaboe | Server endpoints and methods for integrating with Exchange56 Github Profile cli… |
| 2026-11-18 05:04:01 | [B4n1.Db](https://www.nuget.org/packages/B4n1.Db) | 0.1.0 | Bani Montoya | b4n1-db SDK for .NET - sovereign embedded database over the b4n1-db binary |
| 2026-11-18 05:06:21 | [TensorStack.LlamaCpp](https://www.nuget.org/packages/TensorStack.LlamaCpp) | 0.15.0 | sa_ddam213 | .NET Wrapper API for llama.cpp |
| 2026-11-18 05:08:03 | [ObligacionesPorPagar.TenantProvisioning.Contratos](https://www.nuget.org/packages/ObligacionesPorPagar.TenantProvisioning.Contratos) | 0.1.0 | Cosmos | Contratos que publica el worker de tenant provisioning de Obligaciones por Paga… |
| 2026-11-18 05:12:38 | [CognitiveMemoryDatabase](https://www.nuget.org/packages/CognitiveMemoryDatabase) | 1.0.0 | CognitiveMemoryDatabase | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

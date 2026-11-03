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

## Latest list — 2026-11-03 23:20 UTC

New packages created between 2026-11-03 22:19 UTC and 2026-11-03 23:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-03T23-20-37-159891Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-03 22:24:29 | [DynaSharp](https://www.nuget.org/packages/DynaSharp) | 0.1.0 | DynaSharp | High-performance, Native AOT compatible DynamoDB client with a fluent API that… |
| 2026-11-03 22:24:30 | [DynaSharp.Testing](https://www.nuget.org/packages/DynaSharp.Testing) | 0.1.0 | DynaSharp.Testing | Test support for DynaSharp: an in-memory fake DynamoDB behind an HTTP handler,… |
| 2026-11-03 22:29:14 | [Google.Apis.DeviceRun.v1](https://www.nuget.org/packages/Google.Apis.DeviceRun.v1) | 1.78.0.4318 | Google LLC | Google APIs Client Library for working with Devicerun v1. Product documentation… |
| 2026-11-03 22:33:00 | [Skaar.NoAuth](https://www.nuget.org/packages/Skaar.NoAuth) | 1.0.1 | Skaar | A fake OAuth2/OpenID Connect server to run locally. |
| 2026-11-03 22:50:09 | [Dacke.DapperPaging.Offset](https://www.nuget.org/packages/Dacke.DapperPaging.Offset) | 1.0.4 | Dacke.DapperPaging.Offset | High-performance Dapper extension methods for offset-based pagination (Skip/Tak… |
| 2026-11-03 22:50:10 | [Dacke.EFCorePaging.Cursor](https://www.nuget.org/packages/Dacke.EFCorePaging.Cursor) | 1.0.4 | Dacke.EFCorePaging.Cursor | Cursor pagination relies on unique record pointers rather than numerical offset… |
| 2026-11-03 22:50:10 | [Dacke.EFCorePaging.Offset](https://www.nuget.org/packages/Dacke.EFCorePaging.Offset) | 1.0.4 | Dacke.EFCorePaging.Offset | Offset pagination relies on numerical page offsets. The client requests a speci… |
| 2026-11-03 22:50:11 | [Dacke.Paging.Common](https://www.nuget.org/packages/Dacke.Paging.Common) | 1.0.4 | Dacke.Paging.Common | Provides shared core contracts, models, and abstractions for pagination, dynami… |
| 2026-11-03 22:54:12 | [Quant.Infra.Net.Mcp](https://www.nuget.org/packages/Quant.Infra.Net.Mcp) | 1.6.0 | Rong (Rex) Fan | MCP server for natural-language backtesting with Claude / Copilot / any MCP cli… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

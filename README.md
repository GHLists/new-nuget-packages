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

## Latest list — 2026-11-11 09:19 UTC

New packages created between 2026-11-11 08:21 UTC and 2026-11-11 09:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-11T09-19-41-730701Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-11 08:28:25 | [OpenDCP.Framework.Configuration.Model](https://www.nuget.org/packages/OpenDCP.Framework.Configuration.Model) | 0.3.0 | OpenDCP.Framework.Configurati… | Package Description |
| 2026-11-11 08:32:20 | [VirtoCommerce.MCP.Data.PostgreSql](https://www.nuget.org/packages/VirtoCommerce.MCP.Data.PostgreSql) | 3.1000.0 | VirtoCommerce.MCP.Data.Postgr… | Package Description |
| 2026-11-11 08:32:20 | [VirtoCommerce.MCP.Core](https://www.nuget.org/packages/VirtoCommerce.MCP.Core) | 3.1000.0 | VirtoCommerce.MCP.Core | Package Description |
| 2026-11-11 08:32:21 | [VirtoCommerce.MCP.Data.MySql](https://www.nuget.org/packages/VirtoCommerce.MCP.Data.MySql) | 3.1000.0 | VirtoCommerce.MCP.Data.MySql | Package Description |
| 2026-11-11 08:32:21 | [VirtoCommerce.MCP.Data](https://www.nuget.org/packages/VirtoCommerce.MCP.Data) | 3.1000.0 | VirtoCommerce.MCP.Data | Package Description |
| 2026-11-11 08:32:22 | [VirtoCommerce.MCP.Data.SqlServer](https://www.nuget.org/packages/VirtoCommerce.MCP.Data.SqlServer) | 3.1000.0 | VirtoCommerce.MCP.Data.SqlSer… | Package Description |
| 2026-11-11 08:37:57 | [Orient.Mapping](https://www.nuget.org/packages/Orient.Mapping) | 0.1.0 | bburaksseyhan | Compile-time object mapping for .NET. The Roslyn incremental generator is packa… |
| 2026-11-11 08:37:58 | [Orient.AspNetCore](https://www.nuget.org/packages/Orient.AspNetCore) | 0.1.0 | bburaksseyhan | Maps Orient results to ASP.NET Core minimal API HTTP responses and ProblemDetai… |
| 2026-11-11 08:37:58 | [Orient.DependencyInjection](https://www.nuget.org/packages/Orient.DependencyInjection) | 0.1.0 | bburaksseyhan | Explicit dependency injection helpers for Orient validators and mapper instance… |
| 2026-11-11 08:37:59 | [Orient.Validation](https://www.nuget.org/packages/Orient.Validation) | 0.1.0 | bburaksseyhan | Fluent, strongly typed validation for .NET requests and business rules. No Flue… |
| 2026-11-11 08:38:00 | [Orient.Core](https://www.nuget.org/packages/Orient.Core) | 0.1.0 | bburaksseyhan | Explicit success and failure results for .NET. Expected business failures do no… |
| 2026-11-11 08:41:33 | [SWWL](https://www.nuget.org/packages/SWWL) | 7.0.0 | MSTendo64 | A renderer-agnostic Win32 windowing library for .NET 10 on Windows. |
| 2026-11-11 08:45:30 | [GunsNPrices](https://www.nuget.org/packages/GunsNPrices) | 0.1.0 | GunsNPrices | Parse firearm and ammunition product titles into structured data: brand and mod… |
| 2026-11-11 08:45:32 | [Umbraco.Community.GunsNPrices](https://www.nuget.org/packages/Umbraco.Community.GunsNPrices) | 0.1.0 | GunsNPrices | Read firearm and ammunition product titles in Umbraco: brand, model (e.g. "Gloc… |
| 2026-11-11 08:52:59 | [Nullean.Make](https://www.nuget.org/packages/Nullean.Make) | 0.22.1 | Nullean.Make | Property-dispatch build target DSL with Argh-quality help and per-target typed… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

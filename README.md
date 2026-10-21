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

## Latest list — 2026-10-21 20:19 UTC

New packages created between 2026-10-21 19:19 UTC and 2026-10-21 20:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-21T20-19-51-702514Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-21 19:30:24 | [T.Molodoy.Compose.Net.Patcher](https://www.nuget.org/packages/T.Molodoy.Compose.Net.Patcher) | 0.0.2 | T. Molodoy | Assembly patcher for Compose.Net. |
| 2026-10-21 19:32:35 | [Meziantou.Framework.JavaScriptEngine](https://www.nuget.org/packages/Meziantou.Framework.JavaScriptEngine) | 1.0.0 | meziantou | An ECMAScript engine written in .NET: a parser, a bytecode compiler and an inte… |
| 2026-10-21 19:32:36 | [Kododo.ConfigWay.FeatureManagement](https://www.nuget.org/packages/Kododo.ConfigWay.FeatureManagement) | 2.1.0 | Kododo | Feature flags for ConfigWay. Manage Microsoft.FeatureManagement flags from the… |
| 2026-10-21 19:32:53 | [Meziantou.Framework.WebPlatform.JavaScript](https://www.nuget.org/packages/Meziantou.Framework.WebPlatform.JavaScript) | 1.0.0 | meziantou | Runs the scripts of the documents of Meziantou.Framework.WebPlatform with Mezia… |
| 2026-10-21 19:42:50 | [BidiLint](https://www.nuget.org/packages/BidiLint) | 0.1.0 | Abdullah Hakim | Lint Arabic/English localization files for bidi pitfalls: missing keys, unisola… |
| 2026-10-21 19:58:46 | [Proxylayer.EARM](https://www.nuget.org/packages/Proxylayer.EARM) | 0.3.0 | Proxylayer | ARM-style JSON templates for Microsoft Entra ID, deployed through the Microsoft… |
| 2026-10-21 20:01:16 | [DotNetMono.Core](https://www.nuget.org/packages/DotNetMono.Core) | 0.1.0 | dotnet-mono-api contributors | HTTP infrastructure, safe errors, health checks and OpenAPI for DotNetMono modu… |
| 2026-10-21 20:01:21 | [DotNetMono.Data.Abstractions](https://www.nuget.org/packages/DotNetMono.Data.Abstractions) | 0.1.0 | dotnet-mono-api contributors | Small provider-neutral SQL execution and transaction contracts. |
| 2026-10-21 20:01:26 | [DotNetMono.Data.Dapper](https://www.nuget.org/packages/DotNetMono.Data.Dapper) | 0.1.0 | dotnet-mono-api contributors | Dapper SQL Server execution, connections, transactions and explicit migrations. |
| 2026-10-21 20:01:30 | [DotNetMono.Email](https://www.nuget.org/packages/DotNetMono.Email) | 0.1.0 | dotnet-mono-api contributors | Replaceable asynchronous SMTP email delivery with TLS and simple templates. |
| 2026-10-21 20:01:34 | [DotNetMono.Users](https://www.nuget.org/packages/DotNetMono.Users) | 0.1.0 | dotnet-mono-api contributors | Identity-backed user accounts, secure cookies, verification and password reset… |
| 2026-10-21 20:01:38 | [DotNetMono.Users.Dapper](https://www.nuget.org/packages/DotNetMono.Users.Dapper) | 0.1.0 | dotnet-mono-api contributors | SQL Server persistence adapter for the DotNetMono Users module. |
| 2026-10-21 20:03:49 | [Smpl.Mediatr](https://www.nuget.org/packages/Smpl.Mediatr) | 2.0.0 | Ekin Bulut | A lightweight mediator for commands, queries and notifications with pipeline be… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

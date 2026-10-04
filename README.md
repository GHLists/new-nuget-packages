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

## Latest list — 2026-10-04 12:19 UTC

New packages created between 2026-10-04 11:19 UTC and 2026-10-04 12:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-04T12-19-06-104021Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-04 11:24:04 | [Calcifer.Microservice.Api.Template](https://www.nuget.org/packages/Calcifer.Microservice.Api.Template) | 2.0.0 | Rakibul Hasan Rabbi | A production-ready .NET 8 Web API microservice template designed for enterprise… |
| 2026-10-04 11:31:29 | [Krivodeling.Localization.Avalonia](https://www.nuget.org/packages/Krivodeling.Localization.Avalonia) | 1.0.1 | Krivodeling | Shared JSON localization, English fallback, and live Avalonia bindings. |
| 2026-10-04 11:36:01 | [getAddress.Nz.Sdk](https://www.nuget.org/packages/getAddress.Nz.Sdk) | 1.0.1 | getAddress() | .NET client for the getAddress() New Zealand address API: autocomplete, full LI… |
| 2026-10-04 11:37:24 | [Krysalis-Database-Repository](https://www.nuget.org/packages/Krysalis-Database-Repository) | 1.0.0 | Krysalis.DBInfrastructure | Package Description |
| 2026-10-04 11:45:16 | [SecureRedact.AzureDataExplorer](https://www.nuget.org/packages/SecureRedact.AzureDataExplorer) | 1.0.0 | Sanket Singh | Azure Data Explorer (ADX / Kusto) integration for SecureRedact. Wraps IKustoIng… |
| 2026-10-04 11:45:39 | [Company.Shared.Contracts](https://www.nuget.org/packages/Company.Shared.Contracts) | 1.0.0 | Company.Shared.Contracts | Package Description |
| 2026-10-04 11:46:54 | [Company.Shared.Messaging](https://www.nuget.org/packages/Company.Shared.Messaging) | 1.0.0 | Edrees Dbwon | Enterprise-grade dynamic messaging framework wrapping MassTransit and RabbitMQ. |
| 2026-10-04 11:49:04 | [NetCraft.ModBuild.Tools](https://www.nuget.org/packages/NetCraft.ModBuild.Tools) | 0.1.0 | NetCraft Contributors | NetCraft mod development helper tools |
| 2026-10-04 11:49:13 | [NetCraft.ModsProjectType](https://www.nuget.org/packages/NetCraft.ModsProjectType) | 0.1.0 | NetCraft Contributors | NetCraft 模组项目模板 用 dotnet new ncm 创建 |
| 2026-10-04 12:10:10 | [Soenneker.Threads.OpenApiClient](https://www.nuget.org/packages/Soenneker.Threads.OpenApiClient) | 4.0.1 | Jake Soenneker | A generated OpenAPI client for the Meta Threads API. |
| 2026-10-04 12:10:20 | [Soenneker.Threads.HttpClients](https://www.nuget.org/packages/Soenneker.Threads.HttpClients) | 4.0.1 | Jake Soenneker | A thread-safe singleton HttpClient for Threads's OpenAPI integration. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

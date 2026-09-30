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

## Latest list — 2026-09-30 15:22 UTC

New packages created between 2026-09-30 14:20 UTC and 2026-09-30 15:22 UTC.

[Full CSV](data/new-nuget-packages-2026-09-30T15-22-42-489808Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-30 14:22:04 | [CedarSharp](https://www.nuget.org/packages/CedarSharp) | 1.0.0 | CedarSharp contributors | Unofficial .NET wrapper around the Cedar policy engine, preserving authorizatio… |
| 2026-09-30 14:26:26 | [Sachssoft.Sasogine](https://www.nuget.org/packages/Sachssoft.Sasogine) | 0.11.0-alpha | Tobias Sachs | Sasogine is a lightweight and flexible game engine framework based on MonoGame. |
| 2026-09-30 14:44:15 | [Acumatica.RESTClient.NonProductionLogin](https://www.nuget.org/packages/Acumatica.RESTClient.NonProductionLogin) | 5.8.1-preview | Dmitrii-Naumov | An extension for Acumatica REST API client for C# that logs in using the OAuth… |
| 2026-09-30 14:44:43 | [Shiny.Net.HttpServer.Switchboard.Client](https://www.nuget.org/packages/Shiny.Net.HttpServer.Switchboard.Client) | 2.0.0 | aritchie,ShinyLib | The .NET client for Shiny.Net.HttpServer.Switchboard: connect a line, handle ca… |
| 2026-09-30 14:44:43 | [Shiny.Net.HttpServer.Tus](https://www.nuget.org/packages/Shiny.Net.HttpServer.Tus) | 2.0.0 | aritchie,ShinyLib | Resumable uploads for Shiny.Net.HttpServer over the tus 1.0.0 protocol — a phon… |
| 2026-09-30 14:44:48 | [Shiny.Net.HttpServer.CalDav](https://www.nuget.org/packages/Shiny.Net.HttpServer.CalDav) | 2.0.0 | aritchie,ShinyLib | CalDAV (RFC 4791) and CardDAV (RFC 6352) for Shiny.Net.HttpServer — serve an ap… |
| 2026-09-30 14:44:50 | [Shiny.Net.HttpServer.Acme](https://www.nuget.org/packages/Shiny.Net.HttpServer.Acme) | 2.0.0 | aritchie,ShinyLib | Automatic TLS certificates for Shiny.Net.HttpServer from Let's Encrypt, ZeroSSL… |
| 2026-09-30 14:44:53 | [Shiny.Net.HttpServer.OAuthLoopback](https://www.nuget.org/packages/Shiny.Net.HttpServer.OAuthLoopback) | 2.0.0 | aritchie,ShinyLib | The loopback redirect receiver for OAuth 2.0 / OpenID Connect sign-in from nati… |
| 2026-09-30 14:44:53 | [Shiny.Net.HttpServer.Switchboard](https://www.nuget.org/packages/Shiny.Net.HttpServer.Switchboard) | 2.0.0 | aritchie,ShinyLib | SignalR-shaped real-time calls for Shiny.Net.HttpServer, over Server-Sent Event… |
| 2026-09-30 14:47:05 | [ReviewMe](https://www.nuget.org/packages/ReviewMe) | 0.0.1 | Philipp Kiener | A commandline tool to have an LLM of your choice review your code before a huma… |
| 2026-09-30 14:50:17 | [Eventuous.Serialization.Json.Dynamic](https://www.nuget.org/packages/Eventuous.Serialization.Json.Dynamic) | 0.17.0 | Alexey Zimarev and Eventuous… | Production-grade Event Sourcing library |
| 2026-09-30 14:50:27 | [Eventuous.Azure.Storage.Blobs](https://www.nuget.org/packages/Eventuous.Azure.Storage.Blobs) | 0.17.0 | Alexey Zimarev and Eventuous… | Production-grade Event Sourcing library |
| 2026-09-30 15:03:27 | [EzOdata.Connectors.SqlServer](https://www.nuget.org/packages/EzOdata.Connectors.SqlServer) | 1.0.5 | Noctusoft, Inc. | SQL Server connector (Microsoft.Data.SqlClient, netstandard2.0-compatible). |
| 2026-09-30 15:03:27 | [EzOdata.Connectors.MySql](https://www.nuget.org/packages/EzOdata.Connectors.MySql) | 1.0.5 | Noctusoft, Inc. | MySQL/MariaDB connector (MySqlConnector, netstandard2.0-compatible). |
| 2026-09-30 15:03:28 | [EzOdata.WebApi](https://www.nuget.org/packages/EzOdata.WebApi) | 1.0.5 | Noctusoft, Inc. | Classic ASP.NET (.NET Framework 4.8) host adapter (spec 02 §1.1, 15 EMB-9): an… |
| 2026-09-30 15:03:29 | [EzOdata.Connectors.Sqlite](https://www.nuget.org/packages/EzOdata.Connectors.Sqlite) | 1.0.5 | Noctusoft, Inc. | SQLite connector (Microsoft.Data.Sqlite 8.x: netstandard2.0-compatible line). |
| 2026-09-30 15:03:30 | [EzOdata.Connectors.Abstractions](https://www.nuget.org/packages/EzOdata.Connectors.Abstractions) | 1.0.5 | Noctusoft, Inc. | Segregated connector capability contracts: IConnectionTester, ISchemaIntrospect… |
| 2026-09-30 15:03:30 | [EzOdata.Embedded](https://www.nuget.org/packages/EzOdata.Embedded) | 1.0.5 | Noctusoft, Inc. | Host-agnostic embedded configuration: fluent service/role builders and in-memor… |
| 2026-09-30 15:03:31 | [EzOdata.Connectors.PostgreSql](https://www.nuget.org/packages/EzOdata.Connectors.PostgreSql) | 1.0.5 | Noctusoft, Inc. | PostgreSQL connector. Npgsql pinned to the 8.x line: the last release line supp… |
| 2026-09-30 15:03:32 | [EzOdata.OData](https://www.nuget.org/packages/EzOdata.OData) | 1.0.5 | Noctusoft, Inc. | OData v4 engine: dynamic EDM factory, ODataUriParser AST → Query IR, ODL-direct… |
| 2026-09-30 15:03:32 | [EzOdata.Docs](https://www.nuget.org/packages/EzOdata.Docs) | 1.0.5 | Noctusoft, Inc. | CSDL and OpenAPI 3.1 document generation from schema snapshots (spec 11). |
| 2026-09-30 15:03:33 | [EzOdata.Core](https://www.nuget.org/packages/EzOdata.Core) | 1.0.5 | Noctusoft, Inc. | ez-odata-api engine core: schema model, Query IR, policy engine, identity, abst… |
| 2026-09-30 15:03:34 | [EzOdata.AspNetCore](https://www.nuget.org/packages/EzOdata.AspNetCore) | 1.0.5 | Noctusoft, Inc. | ASP.NET Core host adapter: maps HTTP ↔ the host-agnostic engine contract (spec… |
| 2026-09-30 15:03:34 | [EzOdata.Rest](https://www.nuget.org/packages/EzOdata.Rest) | 1.0.5 | Noctusoft, Inc. | REST/JSON dialect engine over the shared Query IR (spec 06). |
| 2026-09-30 15:06:31 | [mcProgressRunner](https://www.nuget.org/packages/mcProgressRunner) | 1.0.0 | Przemysław Załuska | A lightweight WinForms progress dialog for synchronous and asynchronous operati… |
| 2026-09-30 15:15:02 | [retalia.GatewayBasket](https://www.nuget.org/packages/retalia.GatewayBasket) | 0.0.126 | RetaliaLtd | Gateway Basket - provides endpoints for Basket to talk to. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

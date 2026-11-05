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

## Latest list — 2026-11-05 21:19 UTC

New packages created between 2026-11-05 20:20 UTC and 2026-11-05 21:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-05T21-19-21-653782Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-05 20:23:02 | [Skaar.NoApi](https://www.nuget.org/packages/Skaar.NoApi) | 1.1.0 | Skaar | A local fake of any http api, serving files according to route manifests. |
| 2026-11-05 20:32:25 | [MASS4.Turian.Cli.Sdk](https://www.nuget.org/packages/MASS4.Turian.Cli.Sdk) | 3.10.0 | Bruno Massa | Command plugin contracts for the Turian CLI. |
| 2026-11-05 20:34:57 | [LHFD.CleanArch.Infrastructure](https://www.nuget.org/packages/LHFD.CleanArch.Infrastructure) | 1.0.2 | Lucas Henrique Faria de Deus | SDK completo de Arquitetura Limpa contendo Domínio Base, Repositório Genérico e… |
| 2026-11-05 20:43:04 | [Kiban.Link](https://www.nuget.org/packages/Kiban.Link) | 1.0.0 | kiban | SDK de la API pública de link de kiban cloud. |
| 2026-11-05 20:51:04 | [Dexterity.Generation](https://www.nuget.org/packages/Dexterity.Generation) | 1.0.26309.15 | Dexterity.Generation | Template- and worth-budget-based generation of Dexterity RPG characters and ite… |
| 2026-11-05 20:51:05 | [Dexterity](https://www.nuget.org/packages/Dexterity) | 1.0.26309.15 | Dexterity | Component-based, data-driven RPG rules library: stats, inventory, equipment, mo… |
| 2026-11-05 20:58:20 | [Anarchy.Toolkit.Build.Nuke](https://www.nuget.org/packages/Anarchy.Toolkit.Build.Nuke) | 1.0.0 | Leandro M. Medeiros | NUKE build components: solution/test conventions, Microsoft.Testing.Platform-aw… |
| 2026-11-05 20:58:21 | [Anarchy.Toolkit.Core](https://www.nuget.org/packages/Anarchy.Toolkit.Core) | 1.0.0 | Leandro M. Medeiros | Generic helpers, extensions, marker interfaces, the keyed client-resolver patte… |
| 2026-11-05 20:58:22 | [Anarchy.Toolkit.Core.Observability](https://www.nuget.org/packages/Anarchy.Toolkit.Core.Observability) | 1.0.0 | Leandro M. Medeiros | Observability primitives over Serilog: the Observer facade (Logger, MeasurerBas… |
| 2026-11-05 20:58:24 | [Anarchy.Toolkit.Infrastructure.CorrelationId](https://www.nuget.org/packages/Anarchy.Toolkit.Infrastructure.CorrelationId) | 1.0.0 | Leandro M. Medeiros | Correlation/attempt id propagation: async-local CorrelationContext, ASP.NET Cor… |
| 2026-11-05 20:58:25 | [Anarchy.Toolkit.Configuration](https://www.nuget.org/packages/Anarchy.Toolkit.Configuration) | 1.0.0 | Leandro M. Medeiros | Application configuration: settings contracts, environment and secret handling,… |
| 2026-11-05 20:58:26 | [Anarchy.Toolkit.Core.Messaging.Abstractions](https://www.nuget.org/packages/Anarchy.Toolkit.Core.Messaging.Abstractions) | 1.0.0 | Leandro M. Medeiros | Message broker contracts: publisher abstraction, inbound/outbound messages, and… |
| 2026-11-05 20:58:28 | [Anarchy.Toolkit.Core.Events](https://www.nuget.org/packages/Anarchy.Toolkit.Core.Events) | 1.0.0 | Leandro M. Medeiros | Events: an in-process (local) publish/subscribe bus with DI-based handler dispa… |
| 2026-11-05 20:58:29 | [Anarchy.Toolkit.Core.Health](https://www.nuget.org/packages/Anarchy.Toolkit.Core.Health) | 1.0.0 | Leandro M. Medeiros | Service health-check abstractions, report entities, and the base report and agg… |
| 2026-11-05 20:58:31 | [Anarchy.Toolkit.Core.Persistence.Abstractions](https://www.nuget.org/packages/Anarchy.Toolkit.Core.Persistence.Abstractions) | 1.0.0 | Leandro M. Medeiros | Database abstraction layer: Unit of Work, async-local flow context, storage pol… |
| 2026-11-05 20:58:32 | [Anarchy.Toolkit.Hosting](https://www.nuget.org/packages/Anarchy.Toolkit.Hosting) | 1.0.0 | Leandro M. Medeiros | Generic startup and entry-point bootstrapping for Jobs and Workers (Lambda and… |
| 2026-11-05 20:58:33 | [Anarchy.Toolkit.Hosting.Workers](https://www.nuget.org/packages/Anarchy.Toolkit.Hosting.Workers) | 1.0.0 | Leandro M. Medeiros | Worker pipeline: monitored/resilient background workers, heartbeat, and a self-… |
| 2026-11-05 20:58:35 | [Anarchy.Toolkit.Infrastructure.Http](https://www.nuget.org/packages/Anarchy.Toolkit.Infrastructure.Http) | 1.0.0 | Leandro M. Medeiros | Generic HTTP repository/client plumbing: base repositories, delegating handlers… |
| 2026-11-05 20:58:37 | [Anarchy.Toolkit.Infrastructure.Messaging.Aws](https://www.nuget.org/packages/Anarchy.Toolkit.Infrastructure.Messaging.Aws) | 1.0.0 | Leandro M. Medeiros | AWS SNS and SQS implementations of the message-broker publisher abstraction, wi… |
| 2026-11-05 20:58:38 | [Anarchy.Toolkit.Infrastructure.Observability.Serilog](https://www.nuget.org/packages/Anarchy.Toolkit.Infrastructure.Observability.Serilog) | 1.0.0 | Leandro M. Medeiros | Serilog building blocks for AWS-hosted workloads: the EC2 instance-id enricher… |
| 2026-11-05 20:58:39 | [Anarchy.Toolkit.Infrastructure.Persistence.Db](https://www.nuget.org/packages/Anarchy.Toolkit.Infrastructure.Persistence.Db) | 1.0.0 | Leandro M. Medeiros | Provider-agnostic relational database implementation of the persistence abstrac… |
| 2026-11-05 20:58:41 | [Anarchy.Toolkit.Infrastructure.Persistence.Oracle](https://www.nuget.org/packages/Anarchy.Toolkit.Infrastructure.Persistence.Oracle) | 1.0.0 | Leandro M. Medeiros | Oracle implementation of the relational persistence layer: dialect, connection… |
| 2026-11-05 20:58:42 | [Anarchy.Toolkit.Infrastructure.Persistence.Postgres](https://www.nuget.org/packages/Anarchy.Toolkit.Infrastructure.Persistence.Postgres) | 1.0.0 | Leandro M. Medeiros | PostgreSQL implementation of the relational persistence layer: dialect, connect… |
| 2026-11-05 20:58:44 | [Anarchy.Toolkit.Testing](https://www.nuget.org/packages/Anarchy.Toolkit.Testing) | 1.0.0 | Leandro M. Medeiros | Shared base test toolkit: TestCaseBase, TestHelper, in-memory observer/measurer… |
| 2026-11-05 20:58:45 | [Anarchy.Toolkit.Testing.Aws](https://www.nuget.org/packages/Anarchy.Toolkit.Testing.Aws) | 1.0.0 | Leandro M. Medeiros | AWS messaging test helpers (SNS/SQS helpers, typically against LocalStack, and… |
| 2026-11-05 20:58:47 | [Anarchy.Toolkit.Testing.Db](https://www.nuget.org/packages/Anarchy.Toolkit.Testing.Db) | 1.0.0 | Leandro M. Medeiros | Provider-agnostic relational database test helpers (DbTestHelper: enum type han… |
| 2026-11-05 20:58:48 | [Anarchy.Toolkit.Testing.Oracle](https://www.nuget.org/packages/Anarchy.Toolkit.Testing.Oracle) | 1.0.0 | Leandro M. Medeiros | Oracle integration-test fixtures: connection string, connection pool, retry/res… |
| 2026-11-05 20:58:49 | [Anarchy.Toolkit.Testing.Postgres](https://www.nuget.org/packages/Anarchy.Toolkit.Testing.Postgres) | 1.0.0 | Leandro M. Medeiros | PostgreSQL integration-test fixtures: connection string, connection pool, retry… |
| 2026-11-05 20:58:51 | [Anarchy.Toolkit.Web](https://www.nuget.org/packages/Anarchy.Toolkit.Web) | 1.0.0 | Leandro M. Medeiros | Shared REST API pipeline: startup bases, entry points, middleware, auth, swagge… |
| 2026-11-05 20:58:52 | [Anarchy.Toolkit.Testing.Web](https://www.nuget.org/packages/Anarchy.Toolkit.Testing.Web) | 1.0.0 | Leandro M. Medeiros | Web acceptance-test base (RestApiTestCaseBase exercising both the native Kestre… |
| 2026-11-05 20:58:54 | [Anarchy.Toolkit.Web.GraphQL](https://www.nuget.org/packages/Anarchy.Toolkit.Web.GraphQL) | 1.0.0 | Leandro M. Medeiros | GraphQL wiring for ASP.NET Core APIs: schema base, server registration with gra… |
| 2026-11-05 20:58:55 | [Anarchy.Toolkit.Web.Ui](https://www.nuget.org/packages/Anarchy.Toolkit.Web.Ui) | 1.0.0 | Leandro M. Medeiros | Blazor UI pipeline: cookie-session OAuth login, environment catalog, downstream… |
| 2026-11-05 20:59:46 | [GroupDocs.Parser.Mcp.linux-arm64](https://www.nuget.org/packages/GroupDocs.Parser.Mcp.linux-arm64) | 26.11.0 | GroupDocs Contributors | MCP server exposing GroupDocs.Parser for .NET — extract text, images, metadata,… |
| 2026-11-05 20:59:55 | [GroupDocs.Parser.Mcp.linux-x64](https://www.nuget.org/packages/GroupDocs.Parser.Mcp.linux-x64) | 26.11.0 | GroupDocs Contributors | MCP server exposing GroupDocs.Parser for .NET — extract text, images, metadata,… |
| 2026-11-05 21:00:07 | [GroupDocs.Parser.Mcp.osx-arm64](https://www.nuget.org/packages/GroupDocs.Parser.Mcp.osx-arm64) | 26.11.0 | GroupDocs Contributors | MCP server exposing GroupDocs.Parser for .NET — extract text, images, metadata,… |
| 2026-11-05 21:00:17 | [GroupDocs.Parser.Mcp.osx-x64](https://www.nuget.org/packages/GroupDocs.Parser.Mcp.osx-x64) | 26.11.0 | GroupDocs Contributors | MCP server exposing GroupDocs.Parser for .NET — extract text, images, metadata,… |
| 2026-11-05 21:00:30 | [GroupDocs.Parser.Mcp.win-arm64](https://www.nuget.org/packages/GroupDocs.Parser.Mcp.win-arm64) | 26.11.0 | GroupDocs Contributors | MCP server exposing GroupDocs.Parser for .NET — extract text, images, metadata,… |
| 2026-11-05 21:00:40 | [GroupDocs.Parser.Mcp.win-x64](https://www.nuget.org/packages/GroupDocs.Parser.Mcp.win-x64) | 26.11.0 | GroupDocs Contributors | MCP server exposing GroupDocs.Parser for .NET — extract text, images, metadata,… |
| 2026-11-05 21:00:40 | [GroupDocs.Parser.Mcp](https://www.nuget.org/packages/GroupDocs.Parser.Mcp) | 26.11.0 | GroupDocs Contributors | MCP server exposing GroupDocs.Parser for .NET — extract text, images, metadata,… |
| 2026-11-05 21:00:45 | [LiveMarkdown.Avalonia.WaveDrom](https://www.nuget.org/packages/LiveMarkdown.Avalonia.WaveDrom) | 0.1.1 | DearVa | This is a extension package for LiveMarkdown.Avalonia that adds support for ren… |
| 2026-11-05 21:09:57 | [Shipit.CsvValidator](https://www.nuget.org/packages/Shipit.CsvValidator) | 0.1.0 | Shipit Software | Dependency-free local CSV validation with record, field and source diagnostics. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

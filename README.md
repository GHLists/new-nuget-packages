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

## Latest list — 2026-11-27 18:20 UTC

New packages created between 2026-11-27 17:20 UTC and 2026-11-27 18:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-27T18-20-03-807286Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-27 17:23:48 | [Majorsilence.AppleTools.Cli](https://www.nuget.org/packages/Majorsilence.AppleTools.Cli) | 0.2.0 | Peter Gill | apple-tools: set up Linux, Windows and macOS machines to build .NET iOS apps wi… |
| 2026-11-27 17:23:49 | [TokenSafe.Oumv.AspNetCore](https://www.nuget.org/packages/TokenSafe.Oumv.AspNetCore) | 0.1.0 | TokenSafe | OUMV (Universal Agent-Runtime Protocol) adapter for ASP.NET Core: observe, unde… |
| 2026-11-27 17:30:40 | [Anarchy.Toolkit.Bootstrap](https://www.nuget.org/packages/Anarchy.Toolkit.Bootstrap) | 1.0.0 | Leandro Melão Medeiros | Application configuration: settings contracts, environment and secret handling,… |
| 2026-11-27 17:30:41 | [Anarchy.Toolkit.Bootstrap.Aws](https://www.nuget.org/packages/Anarchy.Toolkit.Bootstrap.Aws) | 1.0.0 | Leandro Melão Medeiros | Opt-in AWS configuration: AWS settings (IAwsAppSettings), KMS secret management… |
| 2026-11-27 17:30:46 | [Anarchy.Toolkit.Infrastructure.Http.Msal](https://www.nuget.org/packages/Anarchy.Toolkit.Infrastructure.Http.Msal) | 1.0.0 | Leandro Melão Medeiros | Microsoft Entra ID (MSAL) certificate-based client credentials authentication f… |
| 2026-11-27 17:30:55 | [Anarchy.Toolkit.Runtime](https://www.nuget.org/packages/Anarchy.Toolkit.Runtime) | 1.0.0 | Leandro Melão Medeiros | Generic startup and entry-point bootstrapping for Jobs and Workers (local, cont… |
| 2026-11-27 17:30:56 | [Anarchy.Toolkit.Runtime.Aws](https://www.nuget.org/packages/Anarchy.Toolkit.Runtime.Aws) | 1.0.0 | Leandro Melão Medeiros | Opt-in AWS Lambda hosting for Jobs and event handlers: LambdaJobEntryPointBase,… |
| 2026-11-27 17:30:57 | [Anarchy.Toolkit.Runtime.Web](https://www.nuget.org/packages/Anarchy.Toolkit.Runtime.Web) | 1.0.0 | Leandro Melão Medeiros | Shared REST API pipeline: startup bases, entry points, middleware, auth, and pr… |
| 2026-11-27 17:30:58 | [Anarchy.Toolkit.Runtime.Web.Aws](https://www.nuget.org/packages/Anarchy.Toolkit.Runtime.Web.Aws) | 1.0.0 | Leandro Melão Medeiros | Opt-in AWS Lambda hosting for toolkit REST APIs: AwsWebAppEntryPointBase behind… |
| 2026-11-27 17:31:00 | [Anarchy.Toolkit.Runtime.Web.GraphQL](https://www.nuget.org/packages/Anarchy.Toolkit.Runtime.Web.GraphQL) | 1.0.0 | Leandro Melão Medeiros | GraphQL wiring for ASP.NET Core APIs: schema base, server registration with gra… |
| 2026-11-27 17:31:01 | [Anarchy.Toolkit.Runtime.Web.MockServer](https://www.nuget.org/packages/Anarchy.Toolkit.Runtime.Web.MockServer) | 1.0.0 | Leandro Melão Medeiros | HTTP mock server for integration and end-to-end tests: JSON expectations, plugg… |
| 2026-11-27 17:31:02 | [Anarchy.Toolkit.Runtime.Web.Ui](https://www.nuget.org/packages/Anarchy.Toolkit.Runtime.Web.Ui) | 1.0.0 | Leandro Melão Medeiros | Blazor UI pipeline: cookie-session OAuth login, environment catalog, downstream… |
| 2026-11-27 17:31:03 | [Anarchy.Toolkit.Runtime.Web.MockServer.Ui](https://www.nuget.org/packages/Anarchy.Toolkit.Runtime.Web.MockServer.Ui) | 1.0.0 | Leandro Melão Medeiros | Browser UI for Anarchy.Toolkit.Runtime.Web.MockServer, built on Anarchy.Toolkit… |
| 2026-11-27 17:31:05 | [Anarchy.Toolkit.Runtime.Web.Swagger](https://www.nuget.org/packages/Anarchy.Toolkit.Runtime.Web.Swagger) | 1.0.0 | Leandro Melão Medeiros | Opt-in Swagger/OpenAPI for toolkit REST APIs: the OpenAPI document (OAuth2 sche… |
| 2026-11-27 17:31:06 | [Anarchy.Toolkit.Runtime.Workers](https://www.nuget.org/packages/Anarchy.Toolkit.Runtime.Workers) | 1.0.0 | Leandro Melão Medeiros | Worker pipeline: monitored/resilient background workers, heartbeat, and a self-… |
| 2026-11-27 17:31:13 | [Anarchy.Toolkit.Testing.Runtime.Web](https://www.nuget.org/packages/Anarchy.Toolkit.Testing.Runtime.Web) | 1.0.0 | Leandro Melão Medeiros | Web end-to-end test base (RestApiTestCaseBase exercising the native Kestrel pip… |
| 2026-11-27 17:31:15 | [Anarchy.Toolkit.Testing.Runtime.Web.Aws](https://www.nuget.org/packages/Anarchy.Toolkit.Testing.Runtime.Web.Aws) | 1.0.0 | Leandro Melão Medeiros | AWS Lambda web test toolkit: AwsRestApiTestCaseBase exercising both the native… |
| 2026-11-27 17:36:44 | [ScipSharp.Indexer.Abap](https://www.nuget.org/packages/ScipSharp.Indexer.Abap) | 26.11.8677 | SCIP Maintainers | SCIP indexer for ABAP (abapGit folders), built on a native C# port of the abapl… |
| 2026-11-27 17:36:48 | [ScipSharp.Indexer.Cobol](https://www.nuget.org/packages/ScipSharp.Indexer.Cobol) | 26.11.8677 | SCIP Maintainers | Native C# SCIP indexer for COBOL. |
| 2026-11-27 17:36:53 | [ScipSharp.Indexer.Delphi](https://www.nuget.org/packages/ScipSharp.Indexer.Delphi) | 26.11.8677 | SCIP Maintainers | Native C# SCIP indexer for Delphi / Object Pascal. |
| 2026-11-27 17:36:57 | [ScipSharp.Indexer.Fortran](https://www.nuget.org/packages/ScipSharp.Indexer.Fortran) | 26.11.8677 | SCIP Maintainers | Native C# SCIP indexer for Fortran (FORTRAN 66/77, Fortran 90-2023). |
| 2026-11-27 17:37:02 | [ScipSharp.Indexer.Pascal](https://www.nuget.org/packages/ScipSharp.Indexer.Pascal) | 26.11.8677 | SCIP Maintainers | Native C# SCIP indexer for Pascal (ISO, Turbo Pascal, Free Pascal). |
| 2026-11-27 17:37:06 | [ScipSharp.Indexer.Pli](https://www.nuget.org/packages/ScipSharp.Indexer.Pli) | 26.11.8677 | SCIP Maintainers | Native C# SCIP indexer for PL/I. |
| 2026-11-27 17:37:15 | [ScipSharp.Indexer.Sql](https://www.nuget.org/packages/ScipSharp.Indexer.Sql) | 26.11.8677 | SCIP Maintainers | Native C# SCIP indexer for SQL (ANSI, T-SQL, PL/SQL, PostgreSQL, MySQL, SQLite). |
| 2026-11-27 17:37:20 | [ScipSharp.Indexer.Vb6](https://www.nuget.org/packages/ScipSharp.Indexer.Vb6) | 26.11.8677 | SCIP Maintainers | Native C# SCIP indexer for Visual Basic 6 / VBA. |
| 2026-11-27 17:38:22 | [Triplicity.Backend](https://www.nuget.org/packages/Triplicity.Backend) | 1.0.0 | IATFusion | Server-side client for Triplicity visit creation and backend activity reporting. |
| 2026-11-27 17:53:08 | [ShiftSoftware.ADP.Cases.API](https://www.nuget.org/packages/ShiftSoftware.ADP.Cases.API) | 1.16.37 | Shift Software | The ASP.NET Core controller base for case types of the ShiftSoftware ADP.Cases… |
| 2026-11-27 17:53:15 | [ShiftSoftware.ADP.Cases.Web](https://www.nuget.org/packages/ShiftSoftware.ADP.Cases.Web) | 1.16.37 | Shift Software | Blazor components for the case and claim forms and lists of the ShiftSoftware A… |
| 2026-11-27 18:02:33 | [Canton.ProjectTemplates](https://www.nuget.org/packages/Canton.ProjectTemplates) | 0.8.2 | Peaceful Studio OÜ | dotnet new templates for the Canton .NET SDK. Installs the canton-app template:… |
| 2026-11-27 18:07:49 | [Aquarium](https://www.nuget.org/packages/Aquarium) | 0.1.0 | Marius Merschformann | A UI-independent model of simple 3D scenes made of many instanced shapes (boxes… |
| 2026-11-27 18:07:50 | [Aquarium.Avalonia](https://www.nuget.org/packages/Aquarium.Avalonia) | 0.1.0 | Marius Merschformann | An Avalonia control rendering Aquarium scenes (many instanced shapes) with Open… |
| 2026-11-27 18:09:23 | [Deedwork.DevTools.Abstractions](https://www.nuget.org/packages/Deedwork.DevTools.Abstractions) | 0.99.0 | Deedwork | Contract through which Deedwork add-ons contribute to the developer tools: cata… |
| 2026-11-27 18:09:24 | [Deedwork.Core](https://www.nuget.org/packages/Deedwork.Core) | 0.99.0 | Deedwork | Core of the Deedwork framework: commands, queries, rules and events through a s… |
| 2026-11-27 18:09:26 | [Deedwork.Core.Http](https://www.nuget.org/packages/Deedwork.Core.Http) | 0.99.0 | Deedwork | Connects Deedwork to ASP.NET Core HTTP: the request's user, the per-request aut… |
| 2026-11-27 18:09:27 | [Deedwork.Core.Sqlite](https://www.nuget.org/packages/Deedwork.Core.Sqlite) | 0.99.0 | Deedwork | SQLite support for Deedwork: the required provider registration, and unique con… |
| 2026-11-27 18:09:28 | [Deedwork.Core.PostgreSql](https://www.nuget.org/packages/Deedwork.Core.PostgreSql) | 0.99.0 | Deedwork | PostgreSQL support for Deedwork: the required provider registration, the append… |
| 2026-11-27 18:09:29 | [Deedwork.Batch](https://www.nuget.org/packages/Deedwork.Batch) | 0.99.0 | Deedwork | Batch jobs for Deedwork: command lists started by a command's decision and run… |
| 2026-11-27 18:09:30 | [Deedwork.External](https://www.nuget.org/packages/Deedwork.External) | 0.99.0 | Deedwork | External data sources for Deedwork: timeout, retry, circuit breaker, concurrenc… |
| 2026-11-27 18:09:31 | [Deedwork.OpenTelemetry](https://www.nuget.org/packages/Deedwork.OpenTelemetry) | 0.99.0 | Deedwork | Connects the traces and metrics of Deedwork packages to OpenTelemetry. |
| 2026-11-27 18:09:32 | [Deedwork.Audit](https://www.nuget.org/packages/Deedwork.Audit) | 0.99.0 | Deedwork | Read trail for Deedwork: every run of an [Audited] query records who ran it, wi… |
| 2026-11-27 18:09:33 | [Deedwork.Caching](https://www.nuget.org/packages/Deedwork.Caching) | 0.99.0 | Deedwork | Query result cache for Deedwork: [Cached] queries cleared on commit, in process… |
| 2026-11-27 18:09:35 | [Deedwork.Messaging](https://www.nuget.org/packages/Deedwork.Messaging) | 0.99.0 | Deedwork | Messaging between Deedwork modules: outbox, inbox, delivery, CloudEvents envelo… |
| 2026-11-27 18:09:36 | [Deedwork.Core.Web](https://www.nuget.org/packages/Deedwork.Core.Web) | 0.99.0 | Deedwork | Screens generated from Deedwork commands and queries: htmx with server-side Raz… |
| 2026-11-27 18:09:36 | [MalditoDespacho.Shared.Mediator](https://www.nuget.org/packages/MalditoDespacho.Shared.Mediator) | 0.3.0 | MalditoDespacho | Mediator propio, sin librería externa: ISender, un handler por comando y los pa… |
| 2026-11-27 18:09:37 | [Deedwork.Core.Web.DevTools](https://www.nuget.org/packages/Deedwork.Core.Web.DevTools) | 0.99.0 | Deedwork | Developer tools for Deedwork applications: catalog, book, architecture diagram… |
| 2026-11-27 18:09:38 | [Deedwork.Api](https://www.nuget.org/packages/Deedwork.Api) | 0.99.0 | Deedwork | HTTP API for Deedwork commands and queries with OpenAPI; endpoints are generate… |
| 2026-11-27 18:09:39 | [Deedwork.Caching.Redis](https://www.nuget.org/packages/Deedwork.Caching.Redis) | 0.99.0 | Deedwork | Redis shared store for the Deedwork query cache (Valkey and Garnet too), using… |
| 2026-11-27 18:09:40 | [Deedwork.Messaging.Http](https://www.nuget.org/packages/Deedwork.Messaging.Http) | 0.99.0 | Deedwork | HTTP transport for messaging between Deedwork applications (experimental; Stand… |
| 2026-11-27 18:09:41 | [Deedwork.Messaging.RabbitMq](https://www.nuget.org/packages/Deedwork.Messaging.RabbitMq) | 0.99.0 | Deedwork | RabbitMQ 4.3+ transport for messaging between Deedwork applications (experiment… |
| 2026-11-27 18:09:42 | [Deedwork.Messaging.Testing](https://www.nuget.org/packages/Deedwork.Messaging.Testing) | 0.99.0 | Deedwork | Test helpers for Deedwork messaging: run a module's delivery and inbox rounds w… |
| 2026-11-27 18:09:43 | [Deedwork.Core.Testing](https://www.nuget.org/packages/Deedwork.Core.Testing) | 0.99.0 | Deedwork | Test helpers for Deedwork applications: the real application on a temporary SQL… |
| 2026-11-27 18:09:44 | [Deedwork.Messaging.Web](https://www.nuget.org/packages/Deedwork.Messaging.Web) | 0.99.0 | Deedwork | Operator screens for Deedwork messaging: list, filter, retry and abandon stuck… |
| 2026-11-27 18:09:45 | [Deedwork.Core.Web.Testing](https://www.nuget.org/packages/Deedwork.Core.Web.Testing) | 0.99.0 | Deedwork | Test helpers for Deedwork screens: the web application in process, htmx-like re… |
| 2026-11-27 18:09:46 | [Deedwork.Core.Web.BrowserTesting](https://www.nuget.org/packages/Deedwork.Core.Web.BrowserTesting) | 0.99.0 | Deedwork | Browser test helpers for Deedwork screens: the application in a separate proces… |
| 2026-11-27 18:09:57 | [Krypton.Toolkit.Suite.Extended.Debug.Tools.Nightly](https://www.nuget.org/packages/Krypton.Toolkit.Suite.Extended.Debug.Tools.Nightly) | 120.26.11.331-alpha | Peter Wagner (A.K.A Wagnerp)… | An extension to the Standard Toolkit, which supports .NET Framework 4.6.2 - 4.8… |
| 2026-11-27 18:10:53 | [ParakeetRuntime.Net](https://www.nuget.org/packages/ParakeetRuntime.Net) | 0.5.0 | Krzysztof Kołodziejczak | Speech-to-text for NVIDIA Parakeet TDT models in GGUF format, written in C#: in… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

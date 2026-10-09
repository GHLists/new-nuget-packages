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

## Latest list — 2026-10-09 09:19 UTC

New packages created between 2026-10-09 08:19 UTC and 2026-10-09 09:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-09T09-19-44-777056Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-09 08:21:08 | [RustODotnet.Models.PPOCRv6.Medium.Int8](https://www.nuget.org/packages/RustODotnet.Models.PPOCRv6.Medium.Int8) | 0.3.0 | RustO Contributors | PP-OCRv6 Medium INT8 pre-trained models for RustODotnet (~76 MB highest accurac… |
| 2026-10-09 08:21:11 | [RustODotnet.Models.PPOCRv6.Small.Int8](https://www.nuget.org/packages/RustODotnet.Models.PPOCRv6.Small.Int8) | 0.3.0 | RustO Contributors | PP-OCRv6 Small INT8 pre-trained models for RustODotnet (~16 MB balanced) |
| 2026-10-09 08:21:13 | [RustODotnet.Models.PPOCRv6.Tiny.Int8](https://www.nuget.org/packages/RustODotnet.Models.PPOCRv6.Tiny.Int8) | 0.3.0 | RustO Contributors | PP-OCRv6 Tiny INT8 pre-trained models for RustODotnet (~3.4 MB lightweight) |
| 2026-10-09 08:21:26 | [ZeppelinForms](https://www.nuget.org/packages/ZeppelinForms) | 0.13.1 | YD359Team | A cross-platform UI framework drawn with SkiaSharp: controls, layout, themes, i… |
| 2026-10-09 08:24:42 | [SourceCrafter.LiteSpeedLink.Abstractions](https://www.nuget.org/packages/SourceCrafter.LiteSpeedLink.Abstractions) | 2.26.282.164 | Pedro Gil Mora | LiteSpeedLink contracts: IServiceUnit, response status, processors, retry and c… |
| 2026-10-09 08:24:43 | [SourceCrafter.LiteSpeedLink.Client](https://www.nuget.org/packages/SourceCrafter.LiteSpeedLink.Client) | 2.26.282.164 | Pedro Gil Mora | LiteSpeedLink client runtime: Memory, UDS, QUIC, TCP and UDP connections for ge… |
| 2026-10-09 08:24:45 | [SourceCrafter.LiteSpeedLink.ClientGenerator](https://www.nuget.org/packages/SourceCrafter.LiteSpeedLink.ClientGenerator) | 2.26.282.164 | Pedro Gil Mora | Client generator for LiteSpeedLink services using Memory, UDS, QUIC, TCP and UDP |
| 2026-10-09 08:24:46 | [SourceCrafter.LiteSpeedLink.Core](https://www.nuget.org/packages/SourceCrafter.LiteSpeedLink.Core) | 2.26.282.164 | Pedro Gil Mora | LiteSpeedLink wire framing shared by the generated clients and hosts. |
| 2026-10-09 08:24:48 | [SourceCrafter.LiteSpeedLink.Server](https://www.nuget.org/packages/SourceCrafter.LiteSpeedLink.Server) | 2.26.282.164 | Pedro Gil Mora | LiteSpeedLink host runtime: Memory, UDS, QUIC, TCP and UDP servers for generate… |
| 2026-10-09 08:24:50 | [SourceCrafter.LiteSpeedLink.ServerGenerator](https://www.nuget.org/packages/SourceCrafter.LiteSpeedLink.ServerGenerator) | 2.26.282.164 | Pedro Gil Mora | Host generator for LiteSpeedLink services using Memory, UDS, QUIC, TCP and UDP |
| 2026-10-09 08:39:38 | [Phoney.TUnit](https://www.nuget.org/packages/Phoney.TUnit) | 0.3.0 | Mattias Sundström | Phoney fake data for TUnit tests: [FakeData] fills test method parameters, cons… |
| 2026-10-09 08:44:11 | [Entra.EventHandlers.Security](https://www.nuget.org/packages/Entra.EventHandlers.Security) | 1.0.0 | Jakub Szubarga | Security extensions for Microsoft Entra External ID Authentication Event Handle… |
| 2026-10-09 08:57:02 | [AStarDev.InfrastructureAppDb](https://www.nuget.org/packages/AStarDev.InfrastructureAppDb) | 0.1.1 | AStar Development, Jason Bard… | Shared EF Core AppDbContext, entities, configuration and migrations for the ASt… |
| 2026-10-09 09:01:26 | [Coworkee.AuthServer](https://www.nuget.org/packages/Coworkee.AuthServer) | 0.0.1.11 | fgilde | OpenIddict auth server with login, registration, two factor and external sign-i… |
| 2026-10-09 09:01:27 | [Coworkee.Notifications](https://www.nuget.org/packages/Coworkee.Notifications) | 0.0.1.11 | fgilde | In app notifications with digests. |
| 2026-10-09 09:01:27 | [Coworkee.ResponseFilters](https://www.nuget.org/packages/Coworkee.ResponseFilters) | 0.0.1.11 | fgilde | Permission dependent response filters on Nextended.ResponseFilters. |
| 2026-10-09 09:01:28 | [Coworkee.Domain](https://www.nuget.org/packages/Coworkee.Domain) | 0.0.1.11 | fgilde | Entity and AggregateRoot with domain events, markers for audit, soft delete, te… |
| 2026-10-09 09:01:29 | [Coworkee.Contracts](https://www.nuget.org/packages/Coworkee.Contracts) | 0.0.1.11 | fgilde | DTOs, permission names and paging records shared by server and clients. |
| 2026-10-09 09:01:29 | [Coworkee.BackgroundJobs](https://www.nuget.org/packages/Coworkee.BackgroundJobs) | 0.0.1.11 | fgilde | Hangfire jobs with queues, retries and delayed follow-ups. |
| 2026-10-09 09:01:30 | [Coworkee.Theming](https://www.nuget.org/packages/Coworkee.Theming) | 0.0.1.11 | fgilde | Themes with palettes, fonts, layout and app options per tenant, editable at run… |
| 2026-10-09 09:01:31 | [Coworkee.Bff](https://www.nuget.org/packages/Coworkee.Bff) | 0.0.1.11 | fgilde | Backend for frontend for Blazor WebAssembly: cookie session, token handling and… |
| 2026-10-09 09:01:31 | [Coworkee.Social](https://www.nuget.org/packages/Coworkee.Social) | 0.0.1.11 | fgilde | Comments, tags and ratings for any entity, with realtime updates and notificati… |
| 2026-10-09 09:01:32 | [Coworkee.Ai](https://www.nuget.org/packages/Coworkee.Ai) | 0.0.1.11 | fgilde | AI assistant over the tools of all modules, MCP server and tool call audit. |
| 2026-10-09 09:01:33 | [Coworkee.Application](https://www.nuget.org/packages/Coworkee.Application) | 0.0.1.11 | fgilde | Dispatcher for commands and queries with logging, validation, permission, cachi… |
| 2026-10-09 09:01:34 | [Coworkee.Storage](https://www.nuget.org/packages/Coworkee.Storage) | 0.0.1.11 | fgilde | Blob storage on the file system, S3 or Azure. |
| 2026-10-09 09:01:34 | [Coworkee.EventBus](https://www.nuget.org/packages/Coworkee.EventBus) | 0.0.1.11 | fgilde | Integration events between apps and services through the transactional outbox,… |
| 2026-10-09 09:01:35 | [Coworkee.Client.Blazor](https://www.nuget.org/packages/Coworkee.Client.Blazor) | 0.0.1.11 | fgilde | MudBlazor shell for Blazor WebAssembly: navigation, data tables, account and ad… |
| 2026-10-09 09:01:36 | [Coworkee.Files](https://www.nuget.org/packages/Coworkee.Files) | 0.0.1.11 | fgilde | Folders and files with preview, download, upload and per-folder permissions, ke… |
| 2026-10-09 09:01:37 | [Coworkee.Features](https://www.nuget.org/packages/Coworkee.Features) | 0.0.1.11 | fgilde | Feature management with editions and per tenant overrides, tenant administratio… |
| 2026-10-09 09:01:37 | [Coworkee.ExtendedAttributes](https://www.nuget.org/packages/Coworkee.ExtendedAttributes) | 0.0.1.11 | fgilde | Extra attributes for any entity without schema changes. |
| 2026-10-09 09:01:38 | [Coworkee.Settings](https://www.nuget.org/packages/Coworkee.Settings) | 0.0.1.11 | fgilde | Typed settings per global, tenant and user scope with encrypted secrets. |
| 2026-10-09 09:01:38 | [Coworkee.Templates](https://www.nuget.org/packages/Coworkee.Templates) | 0.0.1.11 | fgilde | dotnet new template for Coworkee applications (coworkee): Aspire app host, API,… |
| 2026-10-09 09:01:39 | [Coworkee.OData](https://www.nuget.org/packages/Coworkee.OData) | 0.0.1.11 | fgilde | OData set per entity with facets, row filters and hidden properties. |
| 2026-10-09 09:01:40 | [Coworkee.Localization](https://www.nuget.org/packages/Coworkee.Localization) | 0.0.1.11 | fgilde | Languages and translations stored in the database, machine translation and live… |
| 2026-10-09 09:01:40 | [Coworkee.AspNetCore](https://www.nuget.org/packages/Coworkee.AspNetCore) | 0.0.1.11 | fgilde | AddCoworkee<TRoot>() for ASP.NET Core hosts: problem details, API groups, beare… |
| 2026-10-09 09:01:41 | [Coworkee.Mailing](https://www.nuget.org/packages/Coworkee.Mailing) | 0.0.1.11 | fgilde | Scriban mail templates with overrides and queued SMTP delivery. |
| 2026-10-09 09:01:42 | [Coworkee.Core](https://www.nuget.org/packages/Coworkee.Core) | 0.0.1.11 | fgilde | Module system with [DependsOn], Result and Error, current user and ambient user… |
| 2026-10-09 09:01:42 | [Coworkee.Realtime](https://www.nuget.org/packages/Coworkee.Realtime) | 0.0.1.11 | fgilde | SignalR push for entity changes, notifications and app events. |
| 2026-10-09 09:01:43 | [Coworkee.Account](https://www.nuget.org/packages/Coworkee.Account) | 0.0.1.11 | fgilde | Account pages and self service for the Coworkee auth server. |
| 2026-10-09 09:01:44 | [Coworkee.Auditing](https://www.nuget.org/packages/Coworkee.Auditing) | 0.0.1.11 | fgilde | Audit trail queries, entity history and restore. |
| 2026-10-09 09:01:44 | [Coworkee.Cli](https://www.nuget.org/packages/Coworkee.Cli) | 0.0.1.11 | fgilde | Coworkee command line: create a Coworkee application, run it, add migrations an… |
| 2026-10-09 09:01:45 | [Coworkee.Infrastructure](https://www.nuget.org/packages/Coworkee.Infrastructure) | 0.0.1.11 | fgilde | CoworkeeDbContext with tenants, soft delete, field level audit trail and transa… |
| 2026-10-09 09:01:45 | [Coworkee.Backup](https://www.nuget.org/packages/Coworkee.Backup) | 0.0.1.11 | fgilde | Database backups and restore from the admin pages. |
| 2026-10-09 09:01:46 | [Coworkee.Search](https://www.nuget.org/packages/Coworkee.Search) | 0.0.1.11 | fgilde | Search index abstraction for Coworkee entities. |
| 2026-10-09 09:01:47 | [Coworkee.Search.Elasticsearch](https://www.nuget.org/packages/Coworkee.Search.Elasticsearch) | 0.0.1.11 | fgilde | Elasticsearch provider for Coworkee.Search. |
| 2026-10-09 09:01:48 | [Coworkee.EventBus.RabbitMq](https://www.nuget.org/packages/Coworkee.EventBus.RabbitMq) | 0.0.1.11 | fgilde | RabbitMQ transport for Coworkee.EventBus with publisher confirms, quorum queues… |
| 2026-10-09 09:01:49 | [Coworkee.Identity](https://www.nuget.org/packages/Coworkee.Identity) | 0.0.1.11 | fgilde | Users, roles, groups, tenants and permission grants with resource level checks. |
| 2026-10-09 09:01:49 | [Coworkee.Chat](https://www.nuget.org/packages/Coworkee.Chat) | 0.0.1.11 | fgilde | Direct and group chat with realtime delivery. |
| 2026-10-09 09:01:50 | [Coworkee.Testing](https://www.nuget.org/packages/Coworkee.Testing) | 0.0.1.11 | fgilde | Postgres test container fixture, test users and a web application factory for C… |
| 2026-10-09 09:01:51 | [Coworkee.Client](https://www.nuget.org/packages/Coworkee.Client) | 0.0.1.11 | fgilde | Base for typed .NET clients (SDKs) of Coworkee APIs: JSON calls and problem det… |
| 2026-10-09 09:02:55 | [ZeppelinForms.Skia](https://www.nuget.org/packages/ZeppelinForms.Skia) | 0.13.1 | YD359Team | The SkiaSharp renderer of ZeppelinForms, shared by the platform packages. |
| 2026-10-09 09:03:31 | [kesi-sdk-gts](https://www.nuget.org/packages/kesi-sdk-gts) | 1.0.0 | kesi | kesi sdk GTS 版 |
| 2026-10-09 09:03:49 | [ZeppelinForms.Windows](https://www.nuget.org/packages/ZeppelinForms.Windows) | 0.13.1 | YD359Team | The Windows platform of ZeppelinForms: Win32 windows and input, clipboard, drag… |
| 2026-10-09 09:04:22 | [ZeppelinForms.Linux](https://www.nuget.org/packages/ZeppelinForms.Linux) | 0.13.1 | YD359Team | The Linux platform of ZeppelinForms: X11 windows and input, and the system them… |
| 2026-10-09 09:04:40 | [ZeppelinForms.Browser](https://www.nuget.org/packages/ZeppelinForms.Browser) | 0.13.1 | YD359Team | The WebAssembly platform of ZeppelinForms: a canvas hosting the forms, pointer… |
| 2026-10-09 09:04:55 | [ZeppelinForms.Android](https://www.nuget.org/packages/ZeppelinForms.Android) | 0.13.1 | YD359Team | The Android platform of ZeppelinForms: a view hosting the forms, touch input, t… |
| 2026-10-09 09:05:30 | [Galosys.Foundation.EntityFrameworkCore.Dm](https://www.nuget.org/packages/Galosys.Foundation.EntityFrameworkCore.Dm) | 26.10.9.1 | Galosys | Galosys.Foundation快速开发库 |
| 2026-10-09 09:11:40 | [SyncCronA.Contracts](https://www.nuget.org/packages/SyncCronA.Contracts) | 0.0.1 | Rinker-Informatik | Shared contracts and gRPC definitions for SyncCronA. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

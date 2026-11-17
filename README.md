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

## Latest list — 2026-11-17 08:18 UTC

New packages created between 2026-11-17 07:20 UTC and 2026-11-17 08:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-17T08-18-57-670653Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-17 07:24:15 | [PhotoMapStudio.Rendering](https://www.nuget.org/packages/PhotoMapStudio.Rendering) | 0.1.0 | scottlz0310 | ベクタータイル（MVT）を SkiaSharp で 1 枚の画像として描く。連続ズーム・物理ピクセル寸法・キャンセル・欠落タイルの判別・帯の並列描画・デコード… |
| 2026-11-17 07:48:37 | [KamuIlanlar.Core.Coordination](https://www.nuget.org/packages/KamuIlanlar.Core.Coordination) | 1.1.0 | KamuIlanlar.com, Contributors | Cross-instance coordination contracts for KamuIlanlar: short-lived distributed… |
| 2026-11-17 07:48:40 | [KamuIlanlar.Core.Coordination.Redis](https://www.nuget.org/packages/KamuIlanlar.Core.Coordination.Redis) | 1.1.0 | KamuIlanlar.com, Contributors | Redis implementations of KamuIlanlar coordination contracts (SET NX locks with… |
| 2026-11-17 07:49:07 | [KamuIlanlar.Core.Security.WebApi](https://www.nuget.org/packages/KamuIlanlar.Core.Security.WebApi) | 1.1.0 | KamuIlanlar.com, Contributors | HTTP request identity for KamuIlanlar Web API: resolves ICurrentUser (user id,… |
| 2026-11-17 07:49:12 | [KamuIlanlar.Core.ServiceBus.Outbox](https://www.nuget.org/packages/KamuIlanlar.Core.ServiceBus.Outbox) | 1.1.0 | KamuIlanlar.com, Contributors | Transactional outbox for KamuIlanlar on EF Core + PostgreSQL: OutboxMessages ta… |
| 2026-11-17 07:52:37 | [Struttura.Abstractions](https://www.nuget.org/packages/Struttura.Abstractions) | 0.2.0 | Struttura Contributors | Stable, dependency-free contracts shared by all Struttura modules. |
| 2026-11-17 07:52:38 | [Struttura.Calendars](https://www.nuget.org/packages/Struttura.Calendars) | 0.2.0 | Struttura Contributors | Portable calendar day-boundary and event-overlap calculations. |
| 2026-11-17 07:52:39 | [Struttura.Calendars.Abstractions](https://www.nuget.org/packages/Struttura.Calendars.Abstractions) | 0.2.0 | Struttura Contributors | Portable calendar capability and event-time contracts without provider or appli… |
| 2026-11-17 07:52:41 | [Struttura.Credentials.Windows](https://www.nuget.org/packages/Struttura.Credentials.Windows) | 0.2.0 | Struttura Contributors | Machine-local application credentials in Windows Credential Manager. |
| 2026-11-17 07:52:42 | [Struttura.Eventing](https://www.nuget.org/packages/Struttura.Eventing) | 0.2.0 | Struttura Contributors | Transport-neutral serialization, inbox processing, and outbox dispatch for Stru… |
| 2026-11-17 07:52:43 | [Struttura.Eventing.EntityFrameworkCore](https://www.nuget.org/packages/Struttura.Eventing.EntityFrameworkCore) | 0.2.0 | Struttura Contributors | Entity Framework Core Inbox and Outbox stores for Struttura. |
| 2026-11-17 07:52:45 | [Struttura.Google](https://www.nuget.org/packages/Struttura.Google) | 0.2.0 | Struttura Contributors | Bounded Gmail/Calendar HTTP, base64url and MIME draft wire operations without O… |
| 2026-11-17 07:52:46 | [Struttura.Google.Abstractions](https://www.nuget.org/packages/Struttura.Google.Abstractions) | 0.2.0 | Struttura Contributors | Portable Gmail and Google Calendar HTTP and draft wire contracts with host-owne… |
| 2026-11-17 07:52:47 | [Struttura.Idempotency.EntityFrameworkCore](https://www.nuget.org/packages/Struttura.Idempotency.EntityFrameworkCore) | 0.2.0 | Struttura Contributors | Transactional EF Core idempotency receipts for request replay. |
| 2026-11-17 07:52:48 | [Struttura.Identity.Blazor](https://www.nuget.org/packages/Struttura.Identity.Blazor) | 0.2.0 | Struttura Contributors | Reusable Blazor administration pages for Struttura identity and software licens… |
| 2026-11-17 07:52:50 | [Struttura.Identity.Contracts](https://www.nuget.org/packages/Struttura.Identity.Contracts) | 0.2.0 | Struttura Contributors | Transport-neutral contracts for Struttura identity administration and software… |
| 2026-11-17 07:52:51 | [Struttura.Identity.EntityFrameworkCore](https://www.nuget.org/packages/Struttura.Identity.EntityFrameworkCore) | 0.2.0 | Struttura Contributors | ASP.NET Core Identity, groups, and software licensing persistence for Struttura. |
| 2026-11-17 07:52:52 | [Struttura.Identity.MinimalApis](https://www.nuget.org/packages/Struttura.Identity.MinimalApis) | 0.2.0 | Struttura Contributors | Versioned REPR APIs for Struttura identity, groups, and software licensing admi… |
| 2026-11-17 07:52:54 | [Struttura.ImapSmtp](https://www.nuget.org/packages/Struttura.ImapSmtp) | 0.2.0 | Struttura Contributors | IMAP UID codecs, observed individual flag mutations, version stamps and single-… |
| 2026-11-17 07:52:55 | [Struttura.ImapSmtp.Abstractions](https://www.nuget.org/packages/Struttura.ImapSmtp.Abstractions) | 0.2.0 | Struttura Contributors | Portable IMAP identity/flag and SMTP submission contracts with host-owned sessi… |
| 2026-11-17 07:52:56 | [Struttura.Mail.Abstractions](https://www.nuget.org/packages/Struttura.Mail.Abstractions) | 0.2.0 | Struttura Contributors | Portable, capability-based mail contracts with caller-owned account and message… |
| 2026-11-17 07:52:57 | [Struttura.Mediator](https://www.nuget.org/packages/Struttura.Mediator) | 0.2.0 | Struttura Contributors | Dependency injection based CQRS mediator implementation for Struttura. |
| 2026-11-17 07:52:59 | [Struttura.Microsoft.Graph](https://www.nuget.org/packages/Struttura.Microsoft.Graph) | 0.2.0 | Struttura Contributors | Portable bounded Microsoft Graph transport and Outlook draft/attachment operati… |
| 2026-11-17 07:53:00 | [Struttura.Microsoft.Graph.Abstractions](https://www.nuget.org/packages/Struttura.Microsoft.Graph.Abstractions) | 0.2.0 | Struttura Contributors | Portable Microsoft Graph HTTP and Outlook mail operation contracts with caller-… |
| 2026-11-17 07:53:01 | [Struttura.MinimalApis](https://www.nuget.org/packages/Struttura.MinimalApis) | 0.2.0 | Struttura Contributors | REPR Minimal API conventions, validation, security, versioning, and Swagger int… |
| 2026-11-17 07:53:03 | [Struttura.Odoo](https://www.nuget.org/packages/Struttura.Odoo) | 0.2.0 | Struttura Contributors | Odoo 19 JSON-2 client with project, task and timesheet operations. |
| 2026-11-17 07:53:04 | [Struttura.Odoo.RemoteWrites](https://www.nuget.org/packages/Struttura.Odoo.RemoteWrites) | 0.2.0 | Struttura Contributors | Opt-in remote write journal integration for Odoo timesheets. |
| 2026-11-17 07:53:05 | [Struttura.Persistence.EntityFrameworkCore](https://www.nuget.org/packages/Struttura.Persistence.EntityFrameworkCore) | 0.2.0 | Struttura Contributors | Entity Framework Core repository, unit of work, and optimistic concurrency adap… |
| 2026-11-17 07:53:06 | [Struttura.RemoteWrites](https://www.nuget.org/packages/Struttura.RemoteWrites) | 0.2.0 | Struttura Contributors | Durable dispatch and read-only reconciliation contracts for remote writes. |
| 2026-11-17 07:53:08 | [Struttura.RemoteWrites.Sqlite](https://www.nuget.org/packages/Struttura.RemoteWrites.Sqlite) | 0.2.0 | Struttura Contributors | SQLite storage for the durable remote write journal. |
| 2026-11-17 07:53:09 | [Struttura.Resilience](https://www.nuget.org/packages/Struttura.Resilience) | 0.2.0 | Struttura Contributors | Dependency-free circuit breaker runtime for Struttura. |
| 2026-11-17 07:53:10 | [Struttura.Sagas](https://www.nuget.org/packages/Struttura.Sagas) | 0.2.0 | Struttura Contributors | Persistent integration event saga orchestration runtime for Struttura. |
| 2026-11-17 07:53:12 | [Struttura.Sagas.EntityFrameworkCore](https://www.nuget.org/packages/Struttura.Sagas.EntityFrameworkCore) | 0.2.0 | Struttura Contributors | Strongly typed Entity Framework Core saga state store for Struttura. |
| 2026-11-17 07:53:13 | [Struttura.Security](https://www.nuget.org/packages/Struttura.Security) | 0.2.0 | Struttura Contributors | Platform-neutral data protection contracts for client applications. |
| 2026-11-17 07:53:14 | [Struttura.Security.Android](https://www.nuget.org/packages/Struttura.Security.Android) | 0.2.0 | Struttura Contributors | AndroidKeyStore AES-GCM data protection adapter with non-exportable platform ke… |
| 2026-11-17 07:53:15 | [Struttura.Security.Windows](https://www.nuget.org/packages/Struttura.Security.Windows) | 0.2.0 | Struttura Contributors | Windows current-user DPAPI adapter for Struttura.Security. |
| 2026-11-17 07:53:17 | [Struttura.Speech](https://www.nuget.org/packages/Struttura.Speech) | 0.2.0 | Struttura Contributors | Portable speech synthesis contracts, WAV utilities, and an HTTP client for desk… |
| 2026-11-17 07:53:18 | [Struttura.Speech.Piper](https://www.nuget.org/packages/Struttura.Speech.Piper) | 0.2.0 | Struttura Contributors | Local desktop speech synthesis using an externally installed Piper executable a… |
| 2026-11-17 07:53:19 | [Struttura.Synchronization](https://www.nuget.org/packages/Struttura.Synchronization) | 0.2.0 | Struttura Contributors | Restarts incremental synchronization from atomically committed page checkpoints. |
| 2026-11-17 07:53:21 | [Struttura.Synchronization.MicrosoftGraph](https://www.nuget.org/packages/Struttura.Synchronization.MicrosoftGraph) | 0.2.0 | Struttura Contributors | Microsoft Graph message delta source for Struttura synchronization. |
| 2026-11-17 07:53:22 | [Struttura.Synchronization.Sqlite](https://www.nuget.org/packages/Struttura.Synchronization.Sqlite) | 0.2.0 | Struttura Contributors | SQLite document projection and checkpoint store for Struttura synchronization. |
| 2026-11-17 07:53:23 | [Struttura.Templates](https://www.nuget.org/packages/Struttura.Templates) | 0.2.0 | Struttura Contributors | dotnet new templates for Struttura applications. |
| 2026-11-17 07:53:25 | [Struttura.TikTok.Live](https://www.nuget.org/packages/Struttura.TikTok.Live) | 0.2.0 | Struttura Contributors | Cross-platform asynchronous TikTok LIVE chat reader for .NET and MAUI using the… |
| 2026-11-17 07:53:26 | [Struttura.Transport.InMemory](https://www.nuget.org/packages/Struttura.Transport.InMemory) | 0.2.0 | Struttura Contributors | In-process integration event transport and Inbox store for Struttura. |
| 2026-11-17 07:53:27 | [Struttura.Webhooks](https://www.nuget.org/packages/Struttura.Webhooks) | 0.2.0 | Struttura Contributors | Standard Webhooks v1 signature verification for incoming deliveries. |
| 2026-11-17 07:53:29 | [Struttura.Workflows](https://www.nuget.org/packages/Struttura.Workflows) | 0.2.0 | Struttura Contributors | Compiled workflow graphs and asynchronous execution with typed input and output… |
| 2026-11-17 07:53:30 | [Struttura.Workflows.AdoNet](https://www.nuget.org/packages/Struttura.Workflows.AdoNet) | 0.2.0 | Struttura Contributors | Provider-neutral ADO.NET query and stored procedure blocks for Struttura workfl… |
| 2026-11-17 07:53:32 | [Struttura.Workflows.Sqlite](https://www.nuget.org/packages/Struttura.Workflows.Sqlite) | 0.2.0 | Struttura Contributors | Durable SQLite checkpoints for Struttura workflow instances. |
| 2026-11-17 08:00:16 | [WoW2.Sdk.Beta.Be.Ai.Abstractions](https://www.nuget.org/packages/WoW2.Sdk.Beta.Be.Ai.Abstractions) | 10.0.0-beta | WoW 2.0 | Ai contract: the runner, prompt registry, model prices, inference log and evals… |
| 2026-11-17 08:00:16 | [WoW2.Sdk.Beta.Be.Ai.Testing](https://www.nuget.org/packages/WoW2.Sdk.Beta.Be.Ai.Testing) | 10.0.0-beta | WoW 2.0 | Ai test kit: a scripted model caller and the prompt registry's conformance suit… |
| 2026-11-17 08:00:16 | [WoW2.Sdk.Beta.Be.Ai.Client](https://www.nuget.org/packages/WoW2.Sdk.Beta.Be.Ai.Client) | 10.0.0-beta | WoW 2.0 | Ai Forms 2 and 3: the client entry point over the running Ai service's HTTP API. |
| 2026-11-17 08:00:17 | [WoW2.Sdk.Beta.Be.Ai.Providers](https://www.nuget.org/packages/WoW2.Sdk.Beta.Be.Ai.Providers) | 10.0.0-beta | WoW 2.0 | Ai providers: named Anthropic, OpenAI-compatible and Ollama chat clients with o… |
| 2026-11-17 08:00:17 | [WoW2.Sdk.Beta.Be.Ai.Module](https://www.nuget.org/packages/WoW2.Sdk.Beta.Be.Ai.Module) | 10.0.0-beta | WoW 2.0 | Ai Form 1: the in-process runner, prompt registry, model prices, inference log… |
| 2026-11-17 08:04:39 | [Copper.Debaser](https://www.nuget.org/packages/Copper.Debaser) | 0.38.0 | Copper.Debaser | Package Description |
| 2026-11-17 08:04:40 | [Copper.Debaser.Core](https://www.nuget.org/packages/Copper.Debaser.Core) | 0.38.0 | Copper.Debaser.Core | Package Description |
| 2026-11-17 08:04:41 | [Copper.Postgredebaser](https://www.nuget.org/packages/Copper.Postgredebaser) | 0.38.0 | Copper.Postgredebaser | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

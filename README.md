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

## Latest list — 2026-11-26 12:21 UTC

New packages created between 2026-11-26 11:20 UTC and 2026-11-26 12:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-26T12-21-15-263028Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-26 11:21:35 | [Uniphar.Platform.Telemetry.Testing](https://www.nuget.org/packages/Uniphar.Platform.Telemetry.Testing) | 2.0.55 | Uniphar | Test helpers to assert on telemetry (spans, logs) that reached Dash0 from integ… |
| 2026-11-26 11:28:46 | [DeltaECS.Unity](https://www.nuget.org/packages/DeltaECS.Unity) | 0.0.75 | Artromskiy | Unity scene authoring and editor integration for DeltaECS. Install with NuGetFo… |
| 2026-11-26 11:33:36 | [Tasselli.Detection.EntityFrameworkCore](https://www.nuget.org/packages/Tasselli.Detection.EntityFrameworkCore) | 0.29.0 | fabricators | EF Core storage for intrusion detection: decoy registry, sealed signals, alert… |
| 2026-11-26 11:33:36 | [Tasselli.Application](https://www.nuget.org/packages/Tasselli.Application) | 0.29.0 | fabricators | Application-layer contracts: CQRS, repositories and batch upserts, cache, timez… |
| 2026-11-26 11:33:37 | [Tasselli.Kernel.AspNetCore](https://www.nuget.org/packages/Tasselli.Kernel.AspNetCore) | 0.29.0 | fabricators | ASP.NET Core host bindings: Result-to-HTTP mapping, API-key authentication and… |
| 2026-11-26 11:33:37 | [Tasselli.Detection](https://www.nuget.org/packages/Tasselli.Detection) | 0.29.0 | fabricators | Intrusion detection core: decoy registry and catalog, provisioning, signal writ… |
| 2026-11-26 11:33:37 | [Tasselli.Auditing](https://www.nuget.org/packages/Tasselli.Auditing) | 0.29.0 | fabricators | Audit trail integrity core: canonical encoding, hash chain, checkpoint signing,… |
| 2026-11-26 11:33:38 | [Tasselli.Validation](https://www.nuget.org/packages/Tasselli.Validation) | 0.29.0 | fabricators | Explicit-assembly FluentValidation, Scrutor composition and CQRS handler regist… |
| 2026-11-26 11:33:38 | [Tasselli.Realtime.SignalR](https://www.nuget.org/packages/Tasselli.Realtime.SignalR) | 0.29.0 | fabricators | Optional Realtime.SignalR integration for Tasselli hosts. |
| 2026-11-26 11:33:39 | [Tasselli.Mailing.MailKit](https://www.nuget.org/packages/Tasselli.Mailing.MailKit) | 0.29.0 | fabricators | Validated SMTP mail submission through MailKit. |
| 2026-11-26 11:33:39 | [Tasselli.Scheduling.Cronos](https://www.nuget.org/packages/Tasselli.Scheduling.Cronos) | 0.29.0 | fabricators | Timezone-aware cron occurrence calculation; durable execution remains host-owne… |
| 2026-11-26 11:33:40 | [Tasselli.DeveloperMcp](https://www.nuget.org/packages/Tasselli.DeveloperMcp) | 0.29.0 | fabricators | Package Description |
| 2026-11-26 11:33:41 | [Tasselli.Auditing.Tool](https://www.nuget.org/packages/Tasselli.Auditing.Tool) | 0.29.0 | fabricators | Verifies an exported Tasselli audit bundle offline, without the application or… |
| 2026-11-26 11:33:41 | [Tasselli.OpenApi](https://www.nuget.org/packages/Tasselli.OpenApi) | 0.29.0 | fabricators | Optional OpenApi integration for Tasselli hosts. |
| 2026-11-26 11:33:42 | [Tasselli.Caching.FusionCache](https://www.nuget.org/packages/Tasselli.Caching.FusionCache) | 0.29.0 | fabricators | Optional FusionCache adapter without an EF dependency. |
| 2026-11-26 11:33:42 | [Tasselli.Documentation](https://www.nuget.org/packages/Tasselli.Documentation) | 0.29.0 | fabricators | Headless, versioned documentation content contracts and deterministic bundle co… |
| 2026-11-26 11:33:43 | [Tasselli.Authoring](https://www.nuget.org/packages/Tasselli.Authoring) | 0.29.0 | fabricators | Versioned developer analyzer rules and formatter templates. |
| 2026-11-26 11:33:44 | [Tasselli.Documentation.Tool](https://www.nuget.org/packages/Tasselli.Documentation.Tool) | 0.29.0 | fabricators | Versioned documentation bundle and metadata API exporter. |
| 2026-11-26 11:33:45 | [Tasselli.Authentication.AspNetCore](https://www.nuget.org/packages/Tasselli.Authentication.AspNetCore) | 0.29.0 | fabricators | Native ASP.NET Core WebAuthn and protected-state adapters. |
| 2026-11-26 11:33:45 | [Tasselli.Detection.Drill.Tool](https://www.nuget.org/packages/Tasselli.Detection.Drill.Tool) | 0.29.0 | fabricators | Runs the Tasselli security drill against a test environment over HTTP. |
| 2026-11-26 11:33:46 | [Tasselli.Infrastructure](https://www.nuget.org/packages/Tasselli.Infrastructure) | 0.29.0 | fabricators | Infrastructure implementations: EF persistence and batch upserts, FusionCache,… |
| 2026-11-26 11:33:46 | [Tasselli.Mailing.MicrosoftGraph](https://www.nuget.org/packages/Tasselli.Mailing.MicrosoftGraph) | 0.29.0 | fabricators | Connection-authorized Microsoft Graph MIME submission with explicit outcomes. |
| 2026-11-26 11:33:47 | [Tasselli.Observability.AspNetCore](https://www.nuget.org/packages/Tasselli.Observability.AspNetCore) | 0.29.0 | fabricators | Optional Observability.AspNetCore integration for Tasselli hosts. |
| 2026-11-26 11:33:47 | [Tasselli.Observability.EntityFrameworkCore](https://www.nuget.org/packages/Tasselli.Observability.EntityFrameworkCore) | 0.29.0 | fabricators | Optional Observability.EntityFrameworkCore integration for Tasselli hosts. |
| 2026-11-26 11:33:47 | [MagicGlyphs.Avalonia](https://www.nuget.org/packages/MagicGlyphs.Avalonia) | 0.8.9 | Lewis John Villamor | Animated icons with sound for Avalonia: 120 free Magic Glyphs icons with spring… |
| 2026-11-26 11:33:48 | [Tasselli.Detection.AspNetCore](https://www.nuget.org/packages/Tasselli.Detection.AspNetCore) | 0.29.0 | fabricators | ASP.NET Core parts of intrusion detection: honeypot routes, webhook alert sink… |
| 2026-11-26 11:33:48 | [Tasselli.Templating.Scriban](https://www.nuget.org/packages/Tasselli.Templating.Scriban) | 0.29.0 | fabricators | Bounded JSON-data template rendering through Scriban. |
| 2026-11-26 11:33:49 | [Tasselli.Authentication.EntityFrameworkCore](https://www.nuget.org/packages/Tasselli.Authentication.EntityFrameworkCore) | 0.29.0 | fabricators | Transactional strong authentication storage and owned EF configurations. |
| 2026-11-26 11:33:49 | [Tasselli.Security.DataProtection](https://www.nuget.org/packages/Tasselli.Security.DataProtection) | 0.29.0 | fabricators | Purpose-bound secret protection and certificate-protected Data Protection regis… |
| 2026-11-26 11:33:50 | [Tasselli.Observability](https://www.nuget.org/packages/Tasselli.Observability) | 0.29.0 | fabricators | Optional Observability integration for Tasselli hosts. |
| 2026-11-26 11:33:50 | [Tasselli.Mcp](https://www.nuget.org/packages/Tasselli.Mcp) | 0.29.0 | fabricators | Progressive MCP discovery and typed dispatch using the official SDK. |
| 2026-11-26 11:33:51 | [Tasselli.Auditing.AspNetCore](https://www.nuget.org/packages/Tasselli.Auditing.AspNetCore) | 0.29.0 | fabricators | Optional ASP.NET Core routes for audit trail export and verification. |
| 2026-11-26 11:33:51 | [Tasselli.Kernel](https://www.nuget.org/packages/Tasselli.Kernel) | 0.29.0 | fabricators | Domain-agnostic kernel: Result/Error, domain events, aggregate roots, value obj… |
| 2026-11-26 11:33:52 | [Tasselli.Security.DataProtection.EntityFrameworkCore](https://www.nuget.org/packages/Tasselli.Security.DataProtection.EntityFrameworkCore) | 0.29.0 | fabricators | EF-backed Data Protection key-ring integration for host-owned contexts and migr… |
| 2026-11-26 11:33:52 | [Tasselli.Mcp.Contracts](https://www.nuget.org/packages/Tasselli.Mcp.Contracts) | 0.29.0 | fabricators | Provider-free MCP tool, caller and authorization contracts. |
| 2026-11-26 11:33:53 | [Tasselli.Mcp.AspNetCore](https://www.nuget.org/packages/Tasselli.Mcp.AspNetCore) | 0.29.0 | fabricators | Authenticated stateless HTTP MCP host adapter. |
| 2026-11-26 11:33:53 | [Tasselli.Mailing](https://www.nuget.org/packages/Tasselli.Mailing) | 0.29.0 | fabricators | Connection-bound mail dispatch and bounded MIME composition. |
| 2026-11-26 11:33:54 | [Tasselli.Authentication.OpenIdConnect](https://www.nuget.org/packages/Tasselli.Authentication.OpenIdConnect) | 0.29.0 | fabricators | Maintained OIDC and OAuth code-flow bridges, tenant-scoped runtime provider con… |
| 2026-11-26 11:33:54 | [Tasselli.Authentication](https://www.nuget.org/packages/Tasselli.Authentication) | 0.29.0 | fabricators | Provider-neutral strong authentication, TOTP, recovery and assurance orchestrat… |
| 2026-11-26 11:33:55 | [Tasselli.Mailing.Google](https://www.nuget.org/packages/Tasselli.Mailing.Google) | 0.29.0 | fabricators | Google Workspace service-account Gmail API MIME submission with explicit outcom… |
| 2026-11-26 11:33:55 | [Tasselli.Auditing.EntityFrameworkCore](https://www.nuget.org/packages/Tasselli.Auditing.EntityFrameworkCore) | 0.29.0 | fabricators | EF Core operation audit trail: SaveChanges capture, audit tables, sealer, check… |
| 2026-11-26 11:33:56 | [Tasselli.Authoring.Tool](https://www.nuget.org/packages/Tasselli.Authoring.Tool) | 0.29.0 | fabricators | Roslyn source layout verification for Tasselli app authors. |
| 2026-11-26 11:35:12 | [ITBees.AdConversions](https://www.nuget.org/packages/ITBees.AdConversions) | 8.0.13 | ITBees.AdConversions | Ad conversions for ITBees FAS applications: a paid purchase is reported to the… |
| 2026-11-26 11:45:43 | [CPOSPS](https://www.nuget.org/packages/CPOSPS) | 1.0.0 | CPOSPS contributors | Chrome POS Peripheral Simulator — Hardware Station PosTerminal.Web engine (in-p… |
| 2026-11-26 11:47:26 | [ZeroC.OpenSSL](https://www.nuget.org/packages/ZeroC.OpenSSL) | 3.5.9 | The OpenSSL Project Authors | OpenSSL built as DLLs with Visual Studio 2019 (v142). OpenSSL is a toolkit for… |
| 2026-11-26 11:47:40 | [Novior.MentorAgent.Cli](https://www.nuget.org/packages/Novior.MentorAgent.Cli) | 1.5.0 | Emanuele Longo, Antonio Macrì | The command line of Novior.MentorAgent: novior-mentor scan reads the pages of a… |
| 2026-11-26 11:47:42 | [Novior.MentorAgent.Scanner](https://www.nuget.org/packages/Novior.MentorAgent.Scanner) | 1.5.0 | Emanuele Longo, Antonio Macrì | Development-time scan of a Blazor application's pages for Novior.MentorAgent's… |
| 2026-11-26 11:59:20 | [AtomUI.Icons.Gravity](https://www.nuget.org/packages/AtomUI.Icons.Gravity) | 6.3.0 | Qinware Technologies Ltd. | Gravity UI icons library for AtomUI OSS |
| 2026-11-26 12:07:24 | [NodeRings.Pulumi](https://www.nuget.org/packages/NodeRings.Pulumi) | 0.1.3 | NodeRings | A Pulumi package for the NodeRings infrastructure marketplace: order and manage… |
| 2026-11-26 12:11:07 | [LibreSharp.Templates.WolverineFxReact](https://www.nuget.org/packages/LibreSharp.Templates.WolverineFxReact) | 0.1.0 | LibreSharp | A dotnet new template pairing a WolverineFx backend with a React (Vite + TypeSc… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

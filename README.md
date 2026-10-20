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

## Latest list — 2026-10-20 16:20 UTC

New packages created between 2026-10-20 15:20 UTC and 2026-10-20 16:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-20T16-20-58-420406Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-20 15:24:22 | [JeffOps.Authentication.Testing](https://www.nuget.org/packages/JeffOps.Authentication.Testing) | 0.1.0-alpha | JeffOps | Test helpers for JeffOps.Authentication consumers: an in-memory token issuer th… |
| 2026-10-20 15:24:23 | [JeffOps.Authorization.Application](https://www.nuget.org/packages/JeffOps.Authorization.Application) | 0.1.0-alpha | JeffOps | Authorization management use cases (vertical slices): roles, assignments, appro… |
| 2026-10-20 15:24:23 | [JeffOps.Authentication.Enterprise.SqlServer](https://www.nuget.org/packages/JeffOps.Authentication.Enterprise.SqlServer) | 0.1.0-alpha | JeffOps | SQL Server persistence and migrations for JeffOps enterprise features. |
| 2026-10-20 15:24:24 | [JeffOps.Security.AspNetCore](https://www.nuget.org/packages/JeffOps.Security.AspNetCore) | 0.1.0-alpha | JeffOps | ASP.NET Core hardening: security headers, forwarded headers, CORS defaults, Dat… |
| 2026-10-20 15:24:25 | [JeffOps.Authentication.SharedKernel](https://www.nuget.org/packages/JeffOps.Authentication.SharedKernel) | 0.1.0-alpha | JeffOps | Shared kernel for JeffOps libraries: Result and Error, handler and validator in… |
| 2026-10-20 15:24:26 | [JeffOps.Authentication.Bff.Yarp](https://www.nuget.org/packages/JeffOps.Authentication.Bff.Yarp) | 0.1.0-alpha | JeffOps | YARP integration for the JeffOps BFF: cookie stripping, bearer forwarding, PAT… |
| 2026-10-20 15:24:27 | [JeffOps.Authentication.Delegation.SqlServer](https://www.nuget.org/packages/JeffOps.Authentication.Delegation.SqlServer) | 0.1.0-alpha | JeffOps | SQL Server persistence and migrations for JeffOps delegated access. |
| 2026-10-20 15:24:28 | [JeffOps.Authentication.Delegation](https://www.nuget.org/packages/JeffOps.Authentication.Delegation) | 0.1.0-alpha | JeffOps | Delegated access for the JeffOps token server: impersonation with target approv… |
| 2026-10-20 15:24:28 | [JeffOps.Authentication.Domain](https://www.nuget.org/packages/JeffOps.Authentication.Domain) | 0.1.0-alpha | JeffOps | Domain model of the JeffOps token server: accounts, external logins, personal a… |
| 2026-10-20 15:24:29 | [JeffOps.Entitlements](https://www.nuget.org/packages/JeffOps.Entitlements) | 0.1.0-alpha | JeffOps | Entitlement (licensing) checks for ASP.NET Core endpoints. |
| 2026-10-20 15:24:30 | [JeffOps.Authorization.AspNetCore](https://www.nuget.org/packages/JeffOps.Authorization.AspNetCore) | 0.1.0-alpha | JeffOps | Permission-based authorization for ASP.NET Core resource services: policy provi… |
| 2026-10-20 15:24:31 | [JeffOps.Authorization.Endpoints](https://www.nuget.org/packages/JeffOps.Authorization.Endpoints) | 0.1.0-alpha | JeffOps | Minimal API endpoints of JeffOps authorization management. |
| 2026-10-20 15:24:35 | [JeffOps.Authentication.Bff](https://www.nuget.org/packages/JeffOps.Authentication.Bff) | 0.1.0-alpha | JeffOps | Backend-for-frontend for browser apps: server-side sessions, cookie-to-bearer,… |
| 2026-10-20 15:24:36 | [JeffOps.Authentication.Federation.Entra](https://www.nuget.org/packages/JeffOps.Authentication.Federation.Entra) | 0.1.0-alpha | JeffOps | Microsoft Entra ID identity provider for the JeffOps token server. |
| 2026-10-20 15:24:37 | [JeffOps.Authentication.Persistence.SqlServer](https://www.nuget.org/packages/JeffOps.Authentication.Persistence.SqlServer) | 0.1.0-alpha | JeffOps | SQL Server persistence and migrations for the JeffOps token server. |
| 2026-10-20 15:24:38 | [JeffOps.Authentication.Federation.Oidc](https://www.nuget.org/packages/JeffOps.Authentication.Federation.Oidc) | 0.1.0-alpha | JeffOps | Generic OpenID Connect and OAuth 2.0 identity providers for the JeffOps token s… |
| 2026-10-20 15:24:38 | [JeffOps.Authentication.UI](https://www.nuget.org/packages/JeffOps.Authentication.UI) | 0.1.0-alpha | JeffOps | Hosted login UI of the JeffOps token server (Razor components, static SSR). |
| 2026-10-20 15:24:39 | [JeffOps.Authentication.Abstractions](https://www.nuget.org/packages/JeffOps.Authentication.Abstractions) | 0.1.0-alpha | JeffOps | Public contracts of JeffOps.Authentication: ICurrentUser, claim names, host por… |
| 2026-10-20 15:24:40 | [JeffOps.Authentication.Enterprise](https://www.nuget.org/packages/JeffOps.Authentication.Enterprise) | 0.1.0-alpha | JeffOps | Enterprise features for the JeffOps token server: verified tenant domains, per-… |
| 2026-10-20 15:24:41 | [JeffOps.Authentication.LocalAccounts.SqlServer](https://www.nuget.org/packages/JeffOps.Authentication.LocalAccounts.SqlServer) | 0.1.0-alpha | JeffOps | SQL Server persistence and migrations for JeffOps local accounts. |
| 2026-10-20 15:24:41 | [JeffOps.Authentication.Tenancy](https://www.nuget.org/packages/JeffOps.Authentication.Tenancy) | 0.1.0-alpha | JeffOps | Tenancy for the JeffOps token server: tenants, memberships (linked directories,… |
| 2026-10-20 15:24:42 | [JeffOps.Authorization.Contracts](https://www.nuget.org/packages/JeffOps.Authorization.Contracts) | 0.1.0-alpha | JeffOps | Wire contracts of JeffOps authorization: read-API DTOs and integration events s… |
| 2026-10-20 15:24:43 | [JeffOps.Authentication.Application](https://www.nuget.org/packages/JeffOps.Authentication.Application) | 0.1.0-alpha | JeffOps | Use cases (vertical slices) of the JeffOps token server: grants, accounts, pers… |
| 2026-10-20 15:24:44 | [JeffOps.Authorization.Persistence.SqlServer](https://www.nuget.org/packages/JeffOps.Authorization.Persistence.SqlServer) | 0.1.0-alpha | JeffOps | SQL Server persistence and migrations for JeffOps authorization management. |
| 2026-10-20 15:24:45 | [JeffOps.Authorization.Domain](https://www.nuget.org/packages/JeffOps.Authorization.Domain) | 0.1.0-alpha | JeffOps | Authorization model and decision engine: permissions, roles, assignments, scope… |
| 2026-10-20 15:24:45 | [JeffOps.Authorization.Infrastructure](https://www.nuget.org/packages/JeffOps.Authorization.Infrastructure) | 0.1.0-alpha | JeffOps | Infrastructure for JeffOps authorization management: EF Core, change intercepti… |
| 2026-10-20 15:24:46 | [JeffOps.Authentication.Client](https://www.nuget.org/packages/JeffOps.Authentication.Client) | 0.1.0-alpha | JeffOps | JWT bearer authentication, current user and service-to-service tokens for resou… |
| 2026-10-20 15:24:47 | [JeffOps.Authentication.Endpoints](https://www.nuget.org/packages/JeffOps.Authentication.Endpoints) | 0.1.0-alpha | JeffOps | Minimal API endpoints of the JeffOps token server. |
| 2026-10-20 15:24:48 | [JeffOps.Authentication.KeyVault](https://www.nuget.org/packages/JeffOps.Authentication.KeyVault) | 0.1.0-alpha | JeffOps | Azure Key Vault / Managed HSM signing key provider for the JeffOps token server. |
| 2026-10-20 15:24:48 | [JeffOps.Authentication.Federation.Saml](https://www.nuget.org/packages/JeffOps.Authentication.Federation.Saml) | 0.1.0-alpha | JeffOps | SAML 2.0 identity providers (ADFS, Okta, Entra, Ping, ...) for the JeffOps toke… |
| 2026-10-20 15:24:49 | [JeffOps.Authentication.LocalAccounts](https://www.nuget.org/packages/JeffOps.Authentication.LocalAccounts) | 0.1.0-alpha | JeffOps | Local accounts for the JeffOps token server: passwords, passkeys, TOTP, lockout… |
| 2026-10-20 15:24:50 | [JeffOps.Authentication.Tenancy.SqlServer](https://www.nuget.org/packages/JeffOps.Authentication.Tenancy.SqlServer) | 0.1.0-alpha | JeffOps | SQL Server persistence and migrations for JeffOps tenancy. |
| 2026-10-20 15:24:51 | [JeffOps.Authentication.Infrastructure](https://www.nuget.org/packages/JeffOps.Authentication.Infrastructure) | 0.1.0-alpha | JeffOps | Infrastructure for the JeffOps token server: OpenIddict, EF Core, signing keys,… |
| 2026-10-20 15:26:08 | [LicenseMan.Sdk](https://www.nuget.org/packages/LicenseMan.Sdk) | 0.1.5 | LicenseManager | C# client for the LicenseManager API: products, policies, customers, licenses,… |
| 2026-10-20 15:31:26 | [AvroCodeGen](https://www.nuget.org/packages/AvroCodeGen) | 1.0.0 | AvroCodeGen | Package Description |
| 2026-10-20 15:31:26 | [AvroCodeGen.Tool](https://www.nuget.org/packages/AvroCodeGen.Tool) | 1.0.0 | AvroCodeGen.Cli | Package Description |
| 2026-10-20 15:44:33 | [Musictopia2.BasicBlazorLibrary](https://www.nuget.org/packages/Musictopia2.BasicBlazorLibrary) | 10.0.1 | BasicBlazorLibrary | Package Description |
| 2026-10-20 15:55:46 | [Facturexa.ZugferdCreator](https://www.nuget.org/packages/Facturexa.ZugferdCreator) | 7.3.0 | Zanyar Systems | Creates ZUGFeRD / Factur-X e-invoices for .NET; profiles: XRechnung, EN 16931,… |
| 2026-10-20 15:56:00 | [BorrowedTorch.Architecture](https://www.nuget.org/packages/BorrowedTorch.Architecture) | 0.0.1 | Vladyslav Pysarenko | Procedural level architecture for grid- and tile-based games: cell-space footpr… |
| 2026-10-20 15:56:21 | [LinKit.Outbox](https://www.nuget.org/packages/LinKit.Outbox) | 1.0.0 | Linh Nguyen | Transactional Outbox and Idempotent Inbox patterns for LinKit. 100% Native AOT… |
| 2026-10-20 15:56:26 | [LinKit.Caching](https://www.nuget.org/packages/LinKit.Caching) | 1.0.0 | Linh Nguyen | High-performance, Zero-Reflection, Native AOT compatible hybrid caching abstrac… |
| 2026-10-20 15:56:30 | [LinKit.Resilience](https://www.nuget.org/packages/LinKit.Resilience) | 1.0.0 | Linh Nguyen | Zero-allocation, compile-time resilience primitives (Retry, Circuit Breaker, Ti… |
| 2026-10-20 15:56:33 | [LinKit.Tenancy](https://www.nuget.org/packages/LinKit.Tenancy) | 1.0.0 | Linh Nguyen | SaaS Multi-Tenancy context and propagation for LinKit. 100% Native AOT compatib… |
| 2026-10-20 15:56:36 | [LinKit.Sagas](https://www.nuget.org/packages/LinKit.Sagas) | 1.0.0 | Linh Nguyen | Distributed Saga Orchestration and automated compensation workflow for LinKit.… |
| 2026-10-20 16:08:57 | [PanoramicData.MusicGeneration.SoundFonts](https://www.nuget.org/packages/PanoramicData.MusicGeneration.SoundFonts) | 0.1.14 | Panoramic Data Limited | Optional SoundFont instrument-bank rendering for PanoramicData.MusicGeneration… |
| 2026-10-20 16:10:11 | [OCI.DotNetSDK.Generativeaisandbox](https://www.nuget.org/packages/OCI.DotNetSDK.Generativeaisandbox) | 150.0.0 | Oracle Cloud Infrastructure | Oracle Cloud Infrastructure Cloud Generative Ai Sandbox Service |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-08 11:19 UTC

New packages created between 2026-10-08 10:19 UTC and 2026-10-08 11:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-08T11-19-56-464822Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-08 10:22:05 | [TLio.Extensions.Looping](https://www.nuget.org/packages/TLio.Extensions.Looping) | 1.1.0 | Frans van Ek | TLio looping extension commands: forEach, while. Format-agnostic via INodeAdapt… |
| 2026-10-08 10:22:07 | [TLio.JsonPath](https://www.nuget.org/packages/TLio.JsonPath) | 1.1.0 | Frans van Ek | Drop-in replacement for Newtonsoft's SelectToken/SelectTokens on System.Text.Js… |
| 2026-10-08 10:39:59 | [Packata-cli](https://www.nuget.org/packages/Packata-cli) | 0.43.0 | Cédric L. Charlier | Cross-platform command-line interface for Packata. |
| 2026-10-08 10:41:48 | [Patware.Pipeline.Contracts](https://www.nuget.org/packages/Patware.Pipeline.Contracts) | 0.3.0 | Patware | Transport-independent contracts for monitoring pipeline runs. |
| 2026-10-08 10:43:30 | [Patware.Pipeline.AspNetCore](https://www.nuget.org/packages/Patware.Pipeline.AspNetCore) | 0.3.0 | Patware | ASP.NET Core endpoints for pipeline monitoring and retry. |
| 2026-10-08 10:43:45 | [Patware.Pipeline.HttpClient](https://www.nuget.org/packages/Patware.Pipeline.HttpClient) | 0.3.0 | Patware | HTTP client integration for remote pipeline monitoring. |
| 2026-10-08 10:56:00 | [mimic-browser](https://www.nuget.org/packages/mimic-browser) | 0.1.0 | Mimic.Sdk | Verified Mimic runtime management and typed CDP extensions. |
| 2026-10-08 10:58:52 | [Pinqponq.Configuration.Vault](https://www.nuget.org/packages/Pinqponq.Configuration.Vault) | 1.0.0 | Pinqponq | HashiCorp Vault configuration provider: loads one KV v2 record shaped like apps… |
| 2026-10-08 10:59:41 | [TALXIS.Platform.Metadata.DataMigration](https://www.nuget.org/packages/TALXIS.Platform.Metadata.DataMigration) | 0.12.0 | TALXIS.Platform.Metadata.Data… | Configuration Migration Tool (CMT) package model for Dataverse data migration:… |
| 2026-10-08 11:01:49 | [OptimizelyCms13ReadinessScanner](https://www.nuget.org/packages/OptimizelyCms13ReadinessScanner) | 1.0.0 | Adnan Zameer | Pre-flight static analysis scanner for auditing Optimizely CMS 12 codebases ahe… |
| 2026-10-08 11:04:26 | [Lycen](https://www.nuget.org/packages/Lycen) | 0.4.4 | NRTH | Lycen runtime licensing for .NET: signed entitlements, grants, installation ide… |
| 2026-10-08 11:04:27 | [Lycen.AspNetCore](https://www.nuget.org/packages/Lycen.AspNetCore) | 0.4.4 | NRTH | Lycen ASP.NET Core integration for runtime licensing headers and domain validat… |
| 2026-10-08 11:04:29 | [Lycen.Remote](https://www.nuget.org/packages/Lycen.Remote) | 0.4.4 | NRTH | Remote and hybrid certificate delivery for Lycen. Optional — only required for… |
| 2026-10-08 11:04:36 | [Lycen.Grants](https://www.nuget.org/packages/Lycen.Grants) | 0.4.4 | NRTH | Lycen grant models and abstractions for runtime licensing entitlements and usag… |
| 2026-10-08 11:04:37 | [Lycen.Metering](https://www.nuget.org/packages/Lycen.Metering) | 0.4.4 | NRTH | Lycen usage metering abstractions and local ledger implementations for runtime… |
| 2026-10-08 11:04:39 | [Lycen.Storage](https://www.nuget.org/packages/Lycen.Storage) | 0.4.4 | NRTH | Lycen provider-neutral client-side storage abstractions for artifacts, grants,… |
| 2026-10-08 11:04:40 | [Lycen.Storage.EntityFramework](https://www.nuget.org/packages/Lycen.Storage.EntityFramework) | 0.4.4 | NRTH | Lycen provider-neutral Entity Framework Core storage support for runtime licens… |
| 2026-10-08 11:04:43 | [Lycen.Sync](https://www.nuget.org/packages/Lycen.Sync) | 0.4.4 | NRTH | Lycen issuer activation, synchronization, and usage upload contracts for runtim… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

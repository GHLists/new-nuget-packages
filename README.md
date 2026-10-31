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

## Latest list — 2026-10-31 21:19 UTC

New packages created between 2026-10-31 20:18 UTC and 2026-10-31 21:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-31T21-19-54-732875Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-31 20:37:50 | [AIContext](https://www.nuget.org/packages/AIContext) | 0.1.0 | aicontext.dev | Open format standard for AI coding assistant project context. Specification and… |
| 2026-10-31 20:38:09 | [AIContext.CLI](https://www.nuget.org/packages/AIContext.CLI) | 0.1.0 | aicontext.dev | CLI tool for the AIContext open format standard. Coming soon. |
| 2026-10-31 20:38:26 | [AIContext.Spec](https://www.nuget.org/packages/AIContext.Spec) | 0.1.0 | aicontext.dev | Specification types and JSON schema for the AIContext open format standard. Com… |
| 2026-10-31 20:49:21 | [AmgadWriteSignature](https://www.nuget.org/packages/AmgadWriteSignature) | 1.0.0 | Amgad Edward | A reusable electronic signature component for Blazor, designed and developed by… |
| 2026-10-31 21:02:33 | [StanzaSharp.TasmanianDevil](https://www.nuget.org/packages/StanzaSharp.TasmanianDevil) | 1.15.0 | Jakob Boman | StanzaSharp for TasmanianDevil (PII detection and de-identification): StanzaNer… |
| 2026-10-31 21:07:35 | [BrutalSystems.Atlas](https://www.nuget.org/packages/BrutalSystems.Atlas) | 0.2.10-dbg | BrutalSystems | Atlas application framework: data access, multi-tenancy and API plumbing for Br… |
| 2026-10-31 21:12:59 | [BrutalSystems.Atlas.Email](https://www.nuget.org/packages/BrutalSystems.Atlas.Email) | 0.2.10-dbg | BrutalSystems | Email delivery for Atlas apps (SMTP via MailKit). |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

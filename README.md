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

## Latest list — 2026-11-10 12:21 UTC

New packages created between 2026-11-10 11:21 UTC and 2026-11-10 12:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-10T12-21-51-175868Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-10 11:22:55 | [EfCore.FileSeeding](https://www.nuget.org/packages/EfCore.FileSeeding) | 1.0.0 | caftooz | Seed an EF Core database from JSON, CSV and Excel (.xlsx) files: one file or sh… |
| 2026-11-10 11:43:25 | [ComiCraft](https://www.nuget.org/packages/ComiCraft) | 0.1.0 | Jeff Nyman | A viewer for digital comics (CBZ, CBR, CB7 and PDF), with commands to convert t… |
| 2026-11-10 11:43:26 | [ComiCraft.Comics](https://www.nuget.org/packages/ComiCraft.Comics) | 0.1.0 | Jeff Nyman | Reads digital comics (CBZ, CBR, CB7 and PDF) page by page, reads and writes the… |
| 2026-11-10 11:55:17 | [Mihenk](https://www.nuget.org/packages/Mihenk) | 1.0.0 | Gökhan Aravi | Türkiye'ye özgü kimlik, vergi, araç plakası, IBAN, kredi kartı, iletişim, Türkç… |
| 2026-11-10 11:55:18 | [Mihenk.Date](https://www.nuget.org/packages/Mihenk.Date) | 1.0.0 | Gökhan Aravi | Mihenk.Date - Diyanet takvimine dayalı Türkiye ulusal/dini resmi tatil günleri… |
| 2026-11-10 11:55:18 | [Mihenk.Geography](https://www.nuget.org/packages/Mihenk.Geography) | 1.0.0 | Gökhan Aravi | Mihenk.Geography - Türkiye'nin 81 ili, 973 ilçesi, telefon alan kodları, bölgel… |
| 2026-11-10 11:55:19 | [Mihenk.Validation.FluentValidation](https://www.nuget.org/packages/Mihenk.Validation.FluentValidation) | 1.0.0 | Gökhan Aravi | Mihenk.Validation.FluentValidation - FluentValidation için Türkiye'ye özgü (TCK… |
| 2026-11-10 12:04:17 | [Martlet.AspnetCore.RuntimeDiagnostics](https://www.nuget.org/packages/Martlet.AspnetCore.RuntimeDiagnostics) | 1.0.0 | Martlet.AspnetCore.RuntimeDia… | Visual runtime diagnostics for ASP.NET Core applications |
| 2026-11-10 12:07:17 | [GreatDevelopers.SupaCortex.Connector](https://www.nuget.org/packages/GreatDevelopers.SupaCortex.Connector) | 1.0.0 | Tushar Agarwal | SupaCortex contract v1: connector DTOs, request signing, the context assertion,… |
| 2026-11-10 12:07:44 | [GreatDevelopers.SupaCortex.Connector.AspNetCore](https://www.nuget.org/packages/GreatDevelopers.SupaCortex.Connector.AspNetCore) | 1.0.0 | Tushar Agarwal | Everything a product needs for SupaCortex: write its lookups and actions once (… |
| 2026-11-10 12:10:04 | [Olve.Template.Api](https://www.nuget.org/packages/Olve.Template.Api) | 2026.11.10.15 | Oliver Vea | A dotnet new template for a .NET 10 spec-first API service: a TypeSpec contract… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

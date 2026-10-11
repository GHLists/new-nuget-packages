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

## Latest list — 2026-10-11 07:22 UTC

New packages created between 2026-10-11 06:21 UTC and 2026-10-11 07:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-11T07-22-03-528337Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-11 06:32:00 | [Coworkee.Reporting](https://www.nuget.org/packages/Coworkee.Reporting) | 0.0.1.15 | fgilde | Reports and dashboards over OData entity sets: server side aggregation, sharing… |
| 2026-10-11 06:32:01 | [Coworkee.Client.Blazor.Reporting](https://www.nuget.org/packages/Coworkee.Client.Blazor.Reporting) | 0.0.1.15 | fgilde | Report designer for Blazor WebAssembly: GridStack layout, ApexCharts, KPI, tabl… |
| 2026-10-11 06:36:12 | [Alternet.Studio.Scripter.Communication](https://www.nuget.org/packages/Alternet.Studio.Scripter.Communication) | 11.0.1 | AlterNET Software | Alternet.Studio.Scripter.Communication |
| 2026-10-11 06:37:35 | [NuGetSecurityInfoDoc](https://www.nuget.org/packages/NuGetSecurityInfoDoc) | 1.0.0-alpha2 | Informatica Documental S.A.S | Validacion del JWT de Keycloak y de su vinculo con el emisor (gateway o certifi… |
| 2026-10-11 06:39:19 | [Catalyst.Rampart](https://www.nuget.org/packages/Catalyst.Rampart) | 26.10.6591 | Curiosity GmbH | Rampart for .NET: on-device PII detection and reversible redaction. A native C#… |
| 2026-10-11 06:56:36 | [DocuLift](https://www.nuget.org/packages/DocuLift) | 1.0.0 | DocuLift | Lift text out of txt, rtf, pdf, docx, and pptx into a string or a TXT file. |
| 2026-10-11 07:15:10 | [Fayakun.AspNetCore.Authentication.JwtBearer](https://www.nuget.org/packages/Fayakun.AspNetCore.Authentication.JwtBearer) | 1.0.0 | Fayakun Services | A lightweight, modular, and high-performance extension package for ASP.NET Core… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

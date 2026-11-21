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

## Latest list — 2026-11-21 14:20 UTC

New packages created between 2026-11-21 13:20 UTC and 2026-11-21 14:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-21T14-20-28-269943Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-21 13:21:00 | [BouncyHsm.Aspire.Hosting](https://www.nuget.org/packages/BouncyHsm.Aspire.Hosting) | 2.4.0 | harrison314 - Jozef Gajdos | Package Description |
| 2026-11-21 13:30:15 | [O24Engine](https://www.nuget.org/packages/O24Engine) | 2.5.50 | Linh Nguyen | Nền tảng thư viện dùng chung cho các dự án O24. |
| 2026-11-21 13:37:46 | [Milvasoft.BulkExtensions](https://www.nuget.org/packages/Milvasoft.BulkExtensions) | 11.0.2 | Milvasoft Corporation | Provider independent bulk operations (insert, update, delete, upsert, read, sav… |
| 2026-11-21 13:37:57 | [Kebechet.Types.Health](https://www.nuget.org/packages/Kebechet.Types.Health) | 6.0.0 | Kebechet | The health data types of Kebechet.Maui.Health (DTOs, enums, results, workout se… |
| 2026-11-21 13:38:11 | [Milvasoft.BulkExtensions.PostgreSql](https://www.nuget.org/packages/Milvasoft.BulkExtensions.PostgreSql) | 11.0.2 | Milvasoft Corporation | PostgreSQL provider for Milvasoft.BulkExtensions. Bulk insert, update, delete,… |
| 2026-11-21 13:43:05 | [Antinet](https://www.nuget.org/packages/Antinet) | 0.1.0 | Anet | The local Antinet service from .NET: Microsoft.Extensions.AI and the OpenAI cli… |
| 2026-11-21 13:49:08 | [Dackel.Log](https://www.nuget.org/packages/Dackel.Log) | 1.0.1 | Dackel Lab | Dackel.Log: componente de logging estruturado para APIs .NET 8 e .NET 10 com Se… |
| 2026-11-21 14:08:27 | [Cruma.Tron.Runner](https://www.nuget.org/packages/Cruma.Tron.Runner) | 0.1.0 | Cruma | Runner SDK for Tron: connect with a worker API key, announce handlers, accept w… |
| 2026-11-21 14:08:59 | [MeengDev.Sdk](https://www.nuget.org/packages/MeengDev.Sdk) | 0.1.0 | Meeng.dev | Meeng.dev's SDK for .NET: emails, domains, contacts, contact books, campaigns,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

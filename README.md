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

## Latest list — 2026-11-18 15:22 UTC

New packages created between 2026-11-18 14:21 UTC and 2026-11-18 15:22 UTC.

[Full CSV](data/new-nuget-packages-2026-11-18T15-22-02-250494Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-18 14:22:58 | [Indigina.Data.SS](https://www.nuget.org/packages/Indigina.Data.SS) | 5.2.8 | Indigina | This NuGet package contains Data Access Layer for Indigina projects. |
| 2026-11-18 14:23:00 | [Argoshot](https://www.nuget.org/packages/Argoshot) | 0.1.0 | Argoshot | Official client for the Argoshot screenshot API: screenshots, PDFs and signed o… |
| 2026-11-18 14:26:09 | [LilyDesignSystem.Blazor.Headless.Identifiers](https://www.nuget.org/packages/LilyDesignSystem.Blazor.Headless.Identifiers) | 0.1.0 | Joel Parker Henderson | Lily Design System Blazor headless national identifier components: the 164 nati… |
| 2026-11-18 14:30:51 | [Ekom.Payments.PayPal](https://www.nuget.org/packages/Ekom.Payments.PayPal) | 1.1.1 | Vettvangur | Ekom Payments PayPal - Vettvangur E-Commerce solution |
| 2026-11-18 14:34:25 | [Resto.Front.Api.V10Preview3](https://www.nuget.org/packages/Resto.Front.Api.V10Preview3) | 9.8.1133-alpha | iiko | This library allows you to develop plugins to extend functionality and change b… |
| 2026-11-18 15:04:17 | [Umbraco.Community.CFCacheClearer](https://www.nuget.org/packages/Umbraco.Community.CFCacheClearer) | 0.1.0 | Gwyl Richards | Adds a dashboard to the Umbraco backoffice that can purge the CloudFlare cache… |
| 2026-11-18 15:08:13 | [Brivio.Sdk](https://www.nuget.org/packages/Brivio.Sdk) | 0.1.0 | Brivio | Official Brivio SDK — invoicing, e-Factura, contacts and more for the Romanian… |
| 2026-11-18 15:12:57 | [Pulumi.Delivery](https://www.nuget.org/packages/Pulumi.Delivery) | 0.1.0 | pulumi | Define Delivery pipelines, stages, jobs and sources in a Pulumi program. |
| 2026-11-18 15:15:40 | [SpanFlow.Mapping.Formats](https://www.nuget.org/packages/SpanFlow.Mapping.Formats) | 1.1.0 | farazahmed614 | Reads and writes the wire formats around a SpanFlow mapping: the raw input is d… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

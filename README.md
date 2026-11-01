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

## Latest list — 2026-11-01 04:19 UTC

New packages created between 2026-11-01 03:21 UTC and 2026-11-01 04:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-01T04-19-57-084871Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-01 03:27:34 | [BaryoDev.Umbraco.AiAssistant](https://www.nuget.org/packages/BaryoDev.Umbraco.AiAssistant) | 0.1.0 | BaryoDev | Claude writing help for the Umbraco backoffice: polish, translate, SEO pack, al… |
| 2026-11-01 03:28:10 | [Imazeo](https://www.nuget.org/packages/Imazeo) | 1.0.0 | Imazeo | Official Imazeo .NET SDK for server-side image, transform, PDF, QR, and barcode… |
| 2026-11-01 03:33:42 | [PowerPortalsPro.Identity.Saml2](https://www.nuget.org/packages/PowerPortalsPro.Identity.Saml2) | 12.0.0 | Power Portals Pro | SAML 2.0 sign-in for PowerPortalsPro portals: any SAML identity provider — Okta… |
| 2026-11-01 03:33:47 | [PowerPortalsPro.Web.Blazor.PowerBI](https://www.nuget.org/packages/PowerPortalsPro.Web.Blazor.PowerBI) | 12.0.0 | Power Portals Pro | Power BI report embedding for PowerPortalsPro Blazor portals, with tokens issue… |
| 2026-11-01 03:44:57 | [Mansiper.ArgsToConfig.Aot](https://www.nuget.org/packages/Mansiper.ArgsToConfig.Aot) | 1.0.1 | Pavel Razboynikov | A library for parsing command-line arguments into strongly-typed configuration… |
| 2026-11-01 04:03:54 | [BaryoDev.Umbraco.ReadAloud.Azure](https://www.nuget.org/packages/BaryoDev.Umbraco.ReadAloud.Azure) | 0.2.0 | BaryoDev | Adds Azure AI Speech to BaryoDev.Umbraco.ReadAloud, the supported Microsoft ser… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

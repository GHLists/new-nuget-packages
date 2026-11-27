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

## Latest list — 2026-11-27 14:19 UTC

New packages created between 2026-11-27 13:21 UTC and 2026-11-27 14:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-27T14-19-43-936321Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-27 13:22:59 | [BetterStack.Pulumi](https://www.nuget.org/packages/BetterStack.Pulumi) | 1.4.0 | Better Stack | A Pulumi package for managing Better Stack Account, Errors, Incidents and Telem… |
| 2026-11-27 13:28:39 | [OurOwn.DocKit](https://www.nuget.org/packages/OurOwn.DocKit) | 0.5.2 | CTNS | OurOwn DocKit - dependency-free Excel (XLSX), CSV and PDF for .NET 8, 9 and 10.… |
| 2026-11-27 13:28:42 | [OurOwn.DocKit.Fonts](https://www.nuget.org/packages/OurOwn.DocKit.Fonts) | 0.5.2 | CTNS | Default fonts for OurOwn DocKit PDFs: Noto Sans, Noto Sans Gujarati and Noto Sa… |
| 2026-11-27 13:28:45 | [OurOwn.Templates](https://www.nuget.org/packages/OurOwn.Templates) | 0.5.2 | CTNS | dotnet new templates for OurOwn UI: ourown-admin, a Blazor Web App with an admi… |
| 2026-11-27 13:28:49 | [OurOwn.UI](https://www.nuget.org/packages/OurOwn.UI) | 0.5.2 | CTNS | OurOwn UI - 200+ Blazor components for business applications: layout, inputs, p… |
| 2026-11-27 13:35:39 | [Lokad.GZip](https://www.nuget.org/packages/Lokad.GZip) | 0.1.0 | Lokad | Deterministic managed gzip streams for .NET. |
| 2026-11-27 13:38:57 | [HRBN.Dynatrace.Api.Client](https://www.nuget.org/packages/HRBN.Dynatrace.Api.Client) | 0.1.0 | Paweł Harbuz | Asynchronous, trimming- and Native-AOT-compatible .NET client for the Dynatrace… |
| 2026-11-27 13:38:58 | [HRBN.Dynatrace.Api.Client.DependencyInjection](https://www.nuget.org/packages/HRBN.Dynatrace.Api.Client.DependencyInjection) | 0.1.0 | Paweł Harbuz | Microsoft.Extensions.DependencyInjection registrations for Dynatrace.Api.Client… |
| 2026-11-27 13:42:34 | [OpenCertServer.Amd.Native](https://www.nuget.org/packages/OpenCertServer.Amd.Native) | 5.0.0-beta-82 | OpenCertServer | Native AMD SEV-SNP user-space driver (amd_snp_driver) packaged using .NET RID c… |
| 2026-11-27 13:42:38 | [opencertserver.attestation](https://www.nuget.org/packages/opencertserver.attestation) | 5.0.0-beta-82 | Jacob Reimers | ASP.NET Core implementation of RFC 7030 certificate authority and issuer and RF… |
| 2026-11-27 13:48:41 | [Umbraco.Community.PunkTwoFactor](https://www.nuget.org/packages/Umbraco.Community.PunkTwoFactor) | 18.3.2.9 | Gareth Wright | An app_plugin for Umbraco that sets up Two Factor Authentication. |
| 2026-11-27 13:52:30 | [bb-mask](https://www.nuget.org/packages/bb-mask) | 0.3.1 | BigBrains | bb-mask client. anonymize and restore; no model calls. |
| 2026-11-27 14:01:57 | [FEPBA.Helper.WebSocket](https://www.nuget.org/packages/FEPBA.Helper.WebSocket) | 10.0.0 | Mauricio Agosta | Librería del bloque para WebSockets sacado de FEPBA.Helper. |
| 2026-11-27 14:11:57 | [Ogooreck.Marten](https://www.nuget.org/packages/Ogooreck.Marten) | 1.0.0 | Oskar Dudycz | Ogooreck plugin for Marten: records the events an in-process app appends and wa… |
| 2026-11-27 14:11:58 | [Ogooreck.Kafka](https://www.nuget.org/packages/Ogooreck.Kafka) | 1.0.0 | Oskar Dudycz | Ogooreck plugin for Kafka: records the messages an app publishes and, for an in… |
| 2026-11-27 14:11:59 | [Ogooreck.Mcp](https://www.nuget.org/packages/Ogooreck.Mcp) | 1.0.0 | Oskar Dudycz | MCP server that runs .NET tests and explains them to coding agents with the Ope… |
| 2026-11-27 14:12:00 | [Ogooreck.Wolverine](https://www.nuget.org/packages/Ogooreck.Wolverine) | 1.0.0 | Oskar Dudycz | Ogooreck plugin for Wolverine: records the messages an in-process app publishes… |
| 2026-11-27 14:12:00 | [Ogooreck.RabbitMQ](https://www.nuget.org/packages/Ogooreck.RabbitMQ) | 1.0.0 | Oskar Dudycz | Ogooreck plugin for RabbitMQ: records the messages an in-process app publishes… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

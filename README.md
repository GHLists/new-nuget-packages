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

## Latest list — 2026-11-09 09:19 UTC

New packages created between 2026-11-09 08:21 UTC and 2026-11-09 09:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-09T09-19-54-427417Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-09 08:26:02 | [HKW.CommonValueConverters.Avalonia](https://www.nuget.org/packages/HKW.CommonValueConverters.Avalonia) | 0.2.1 | HKW | Avalonia wrappers for HKW.CommonValueConverters. |
| 2026-11-09 08:26:03 | [HKW.CommonValueConverters.WPF](https://www.nuget.org/packages/HKW.CommonValueConverters.WPF) | 0.2.1 | HKW | WPF wrappers for HKW.CommonValueConverters. |
| 2026-11-09 08:28:22 | [CuiSharp](https://www.nuget.org/packages/CuiSharp) | 0.1.0 | yappologistic | Idiomatic C# bindings for CUI, the 160-component native UI library written in C… |
| 2026-11-09 08:28:24 | [CuiSharp.Templates](https://www.nuget.org/packages/CuiSharp.Templates) | 0.1.0 | yappologistic | dotnet new templates for CuiSharp: a native desktop app in plain C# with no XAM… |
| 2026-11-09 08:28:26 | [CuiSharp.Testing](https://www.nuget.org/packages/CuiSharp.Testing) | 0.1.0 | yappologistic | Drive a CuiSharp interface without a window: find a control by its label, click… |
| 2026-11-09 08:28:27 | [CuiSharp.Tools](https://www.nuget.org/packages/CuiSharp.Tools) | 0.1.0 | yappologistic | Screenshot a CuiSharp app, print the controls of its last frame, and click or t… |
| 2026-11-09 08:40:43 | [Syndew.Oluso.Imaging](https://www.nuget.org/packages/Syndew.Oluso.Imaging) | 1.30.0 | Oluso | Image resizing for Oluso public assets. Isolates the image library behind IImag… |
| 2026-11-09 08:40:43 | [Syndew.Oluso.Enterprise.AzureWebhooks](https://www.nuget.org/packages/Syndew.Oluso.Enterprise.AzureWebhooks) | 1.30.0 | Oluso | Azure-based webhook processing for Oluso identity platform. Provides queue-base… |
| 2026-11-09 08:40:44 | [Syndew.Oluso.Contracts](https://www.nuget.org/packages/Syndew.Oluso.Contracts) | 1.30.0 | Oluso | Shared zero-dependency enums and POCOs reused by Oluso.Core entities and the DT… |
| 2026-11-09 08:40:45 | [Syndew.Oluso.Enterprise.Scim](https://www.nuget.org/packages/Syndew.Oluso.Enterprise.Scim) | 1.30.0 | Oluso | SCIM 2.0 provisioning support for Oluso. Professional tier and above. |
| 2026-11-09 08:40:45 | [Syndew.Oluso.Dto](https://www.nuget.org/packages/Syndew.Oluso.Dto) | 1.30.0 | Oluso | Wire-contract DTOs for the Oluso platform module. Shared by backend controllers… |
| 2026-11-09 08:40:46 | [Syndew.Oluso.Enterprise.Fido2](https://www.nuget.org/packages/Syndew.Oluso.Enterprise.Fido2) | 1.30.0 | Oluso | FIDO2/WebAuthn Passkey support for Oluso. Professional tier and above. |
| 2026-11-09 08:40:47 | [Syndew.Oluso.Functions.Common](https://www.nuget.org/packages/Syndew.Oluso.Functions.Common) | 1.30.0 | Akin Odeyale | Shared infrastructure for Oluso Azure Functions projects — tenant job dispatchi… |
| 2026-11-09 08:40:48 | [Syndew.Oluso.Enterprise.Verification.Dto](https://www.nuget.org/packages/Syndew.Oluso.Enterprise.Verification.Dto) | 1.30.0 | Oluso | Wire-contract DTOs for Oluso business (KYB) verification. Shared by backend con… |
| 2026-11-09 08:40:49 | [Syndew.Oluso.Account.Dto](https://www.nuget.org/packages/Syndew.Oluso.Account.Dto) | 1.30.0 | Oluso | Wire-contract DTOs for the Oluso Account module. Shared by backend controllers… |
| 2026-11-09 08:40:49 | [Syndew.Oluso.Enterprise.Verification](https://www.nuget.org/packages/Syndew.Oluso.Enterprise.Verification) | 1.30.0 | Oluso | Business (KYB) verification for Oluso: company registry checks through Dojah an… |
| 2026-11-09 08:40:50 | [Syndew.Oluso](https://www.nuget.org/packages/Syndew.Oluso) | 1.30.0 | Akin Odeyale | Modern OAuth 2.0 and OpenID Connect identity server for ASP.NET Core. Multi-ten… |
| 2026-11-09 08:40:51 | [Syndew.Oluso.Enterprise.Saml](https://www.nuget.org/packages/Syndew.Oluso.Enterprise.Saml) | 1.30.0 | Oluso | SAML 2.0 Service Provider and Identity Provider support for Oluso. Enterprise t… |
| 2026-11-09 08:40:52 | [Syndew.Oluso.Account](https://www.nuget.org/packages/Syndew.Oluso.Account) | 1.30.0 | Akin Odeyale | Account API controllers for Oluso identity server. Provides REST endpoints for… |
| 2026-11-09 08:40:52 | [Syndew.Oluso.Enterprise.AzureKeyVault](https://www.nuget.org/packages/Syndew.Oluso.Enterprise.AzureKeyVault) | 1.30.0 | Oluso | Azure Key Vault integration for Oluso identity platform. Provides HSM-backed si… |
| 2026-11-09 08:40:53 | [Syndew.Oluso.Core](https://www.nuget.org/packages/Syndew.Oluso.Core) | 1.30.0 | Akin Odeyale | Core abstractions and domain entities for Oluso identity server. |
| 2026-11-09 08:40:54 | [Syndew.Oluso.Enterprise.AzureDataProtection](https://www.nuget.org/packages/Syndew.Oluso.Enterprise.AzureDataProtection) | 1.30.0 | Oluso | Shared ASP.NET Core data protection key ring for Oluso hosts: keys kept in Azur… |
| 2026-11-09 08:40:54 | [Syndew.Oluso.Telemetry.OpenTelemetry](https://www.nuget.org/packages/Syndew.Oluso.Telemetry.OpenTelemetry) | 1.30.0 | Oluso | OpenTelemetry implementation for Oluso telemetry. Provides metrics, tracing, an… |
| 2026-11-09 08:40:55 | [Syndew.Oluso.Enterprise.AzureBlob](https://www.nuget.org/packages/Syndew.Oluso.Enterprise.AzureBlob) | 1.30.0 | Oluso | Azure Blob Storage IFileUploader implementation for Oluso identity platform. Pr… |
| 2026-11-09 08:40:56 | [Syndew.Oluso.Admin](https://www.nuget.org/packages/Syndew.Oluso.Admin) | 1.30.0 | Akin Odeyale | Admin API controllers for Oluso identity server. Provides REST endpoints for us… |
| 2026-11-09 08:40:57 | [Syndew.Oluso.Enterprise.Ldap](https://www.nuget.org/packages/Syndew.Oluso.Enterprise.Ldap) | 1.30.0 | Oluso | LDAP/Active Directory authentication and user sync for Oluso. Enterprise tier. |
| 2026-11-09 08:40:57 | [Syndew.Oluso.Telemetry.Abstractions](https://www.nuget.org/packages/Syndew.Oluso.Telemetry.Abstractions) | 1.30.0 | Oluso | Telemetry abstractions for Oluso. Vendor-neutral interfaces for metrics, tracin… |
| 2026-11-09 08:40:58 | [Syndew.Oluso.Enterprise.Cloudflare](https://www.nuget.org/packages/Syndew.Oluso.Enterprise.Cloudflare) | 1.30.0 | Oluso | Cloudflare integration for Oluso identity platform. Provisions custom tenant do… |
| 2026-11-09 08:40:59 | [Syndew.Oluso.UI](https://www.nuget.org/packages/Syndew.Oluso.UI) | 1.30.0 | Your Name | Default UI views for Oluso User Journey Engine. Provides ready-to-use views for… |
| 2026-11-09 08:40:59 | [Syndew.Oluso.Core.Generators](https://www.nuget.org/packages/Syndew.Oluso.Core.Generators) | 1.30.0 | Akin Odeyale | Source generators for Oluso event property definitions. |
| 2026-11-09 08:41:00 | [Syndew.Oluso.Admin.Dto](https://www.nuget.org/packages/Syndew.Oluso.Admin.Dto) | 1.30.0 | Oluso | Wire-contract DTOs for the Oluso Admin module. Shared by backend controllers an… |
| 2026-11-09 08:41:01 | [Syndew.Oluso.EntityFramework](https://www.nuget.org/packages/Syndew.Oluso.EntityFramework) | 1.30.0 | Akin Odeyale | Entity Framework Core stores for Oluso identity server. Supports SQL Server, Po… |
| 2026-11-09 08:57:48 | [FlexibleArray](https://www.nuget.org/packages/FlexibleArray) | 0.0.1 | ghostflyby | C flexible array members for .NET: a fixed header with a contiguous trailing el… |
| 2026-11-09 09:02:04 | [OLAX.InnovativeLab.Messaging](https://www.nuget.org/packages/OLAX.InnovativeLab.Messaging) | 1.0.0 | Udesh | Broker-neutral messaging for OLAX services: a transactional outbox and inbox on… |
| 2026-11-09 09:02:06 | [OLAX.InnovativeLab.Messaging.Abstractions](https://www.nuget.org/packages/OLAX.InnovativeLab.Messaging.Abstractions) | 1.0.0 | Udesh | Integration event contracts for OLAX services: IntegrationEvent, IEventPublishe… |
| 2026-11-09 09:02:07 | [OLAX.InnovativeLab.Messaging.AmazonSqs](https://www.nuget.org/packages/OLAX.InnovativeLab.Messaging.AmazonSqs) | 1.0.0 | Udesh | AWS transport for OLAX.InnovativeLab.Messaging: one SNS topic fanned out to one… |
| 2026-11-09 09:02:09 | [OLAX.InnovativeLab.Messaging.AzureServiceBus](https://www.nuget.org/packages/OLAX.InnovativeLab.Messaging.AzureServiceBus) | 1.0.0 | Udesh | Azure Service Bus transport for OLAX.InnovativeLab.Messaging: one topic, one su… |
| 2026-11-09 09:02:10 | [DsgWeb.Client](https://www.nuget.org/packages/DsgWeb.Client) | 0.1.0 | Pascal Pomper | Typed HTTP client for the DsgWeb REST API, which starts and stops MQTT data str… |
| 2026-11-09 09:02:10 | [OLAX.InnovativeLab.Messaging.GooglePubSub](https://www.nuget.org/packages/OLAX.InnovativeLab.Messaging.GooglePubSub) | 1.0.0 | Udesh | Google Cloud Pub/Sub transport for OLAX.InnovativeLab.Messaging: a topic per ev… |
| 2026-11-09 09:02:11 | [OLAX.InnovativeLab.Messaging.Kafka](https://www.nuget.org/packages/OLAX.InnovativeLab.Messaging.Kafka) | 1.0.0 | Udesh | Kafka transport for OLAX.InnovativeLab.Messaging, also serving Azure Event Hubs… |
| 2026-11-09 09:02:13 | [OLAX.InnovativeLab.Messaging.RabbitMq](https://www.nuget.org/packages/OLAX.InnovativeLab.Messaging.RabbitMq) | 1.0.0 | Udesh | RabbitMQ transport for OLAX.InnovativeLab.Messaging: a topic exchange, one quor… |
| 2026-11-09 09:04:57 | [Beep.PDF](https://www.nuget.org/packages/Beep.PDF) | 1.0.3 | Beep.PDF | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-23 21:20 UTC

New packages created between 2026-10-23 20:22 UTC and 2026-10-23 21:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-23T21-20-22-407799Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-23 20:27:45 | [Aarkam.Kdouja.Primitives](https://www.nuget.org/packages/Aarkam.Kdouja.Primitives) | 1.0.6 | Aarkam Team - Kdouja LSM Prim… | Zero-allocation, hardware-accelerated storage engine primitives engineered for… |
| 2026-10-23 20:39:37 | [Stellaegis.Registry.SqlServer](https://www.nuget.org/packages/Stellaegis.Registry.SqlServer) | 6.0.0 | FRi | The SQL Server stores of Stellaegis.Registry: the compartments, the users, the… |
| 2026-10-23 20:40:05 | [Bsa.Exchange.WebServices](https://www.nuget.org/packages/Bsa.Exchange.WebServices) | 2.2.2 | Microsoft Corporation (origin… | Exchange Web Services (EWS) Managed API 2.2, перенесённый на .NET 6 с сохранени… |
| 2026-10-23 20:40:29 | [Sufficit.Telephony.Panel.Core](https://www.nuget.org/packages/Sufficit.Telephony.Panel.Core) | 1.26.1023.2040 | Hugo Castro de Deco | Package Description |
| 2026-10-23 20:46:00 | [NorthGomel.ElectrumXClient.Abstractions](https://www.nuget.org/packages/NorthGomel.ElectrumXClient.Abstractions) | 1.0.0-rc-1 | eudjien | Shared Electrum Cash Protocol JSON-RPC method names, wire-format models, client… |
| 2026-10-23 20:46:23 | [NorthGomel.ElectrumXClient](https://www.nuget.org/packages/NorthGomel.ElectrumXClient) | 1.0.0-rc-1 | eudjien | A .NET Standard 2.1 client for Electrum Cash Protocol servers, with typed JSON-… |
| 2026-10-23 20:47:45 | [BeneficialStrategies.Iso20022.Messages.Validation](https://www.nuget.org/packages/BeneficialStrategies.Iso20022.Messages.Validation) | 1.0.0-alpha | Jeff Ward,Beneficial Strategi… | FluentValidation validators for the interfaces of the ISO 20022 messages, compo… |
| 2026-10-23 20:50:16 | [BeneficialStrategies.Iso20022.Validation.Xml.Payloads](https://www.nuget.org/packages/BeneficialStrategies.Iso20022.Validation.Xml.Payloads) | 1.0.0-alpha | Jeff Ward,Beneficial Strategi… | Validate raw ISO 20022 XML or JSON payloads as they arrive from a queue, an HTT… |
| 2026-10-23 20:56:39 | [ConventionMapper.SourceGenerator](https://www.nuget.org/packages/ConventionMapper.SourceGenerator) | 1.2.0 | Katragadda | Build-time object mapping for .NET. Declare partial mapping methods in a [Gener… |
| 2026-10-23 21:02:02 | [IdentityNexus](https://www.nuget.org/packages/IdentityNexus) | 1.0.0 | IdentityNexus | A Blazor UI for administering ASP.NET Core Identity users and roles. |
| 2026-10-23 21:02:06 | [IdentityNexus.Services](https://www.nuget.org/packages/IdentityNexus.Services) | 1.0.0 | IdentityNexus.Services | Services for administering an ASP.NET Core Identity store. |
| 2026-10-23 21:05:03 | [Shade](https://www.nuget.org/packages/Shade) | 0.1.0 | Dominik Jurasek | A dark-first design system for Avalonia desktop apps, with a live light mode: c… |
| 2026-10-23 21:06:02 | [Sakura.Framework.iOS](https://www.nuget.org/packages/Sakura.Framework.iOS) | 2026.1024.0 | HelloYeew | Runs a Sakura Framework app on iOS |
| 2026-10-23 21:14:28 | [OneAddress.PartnerSdk](https://www.nuget.org/packages/OneAddress.PartnerSdk) | 0.2.0 | OneAddress | Official .NET SDK for OneAddress partner integrations — webhook signature verif… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

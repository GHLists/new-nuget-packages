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

## Latest list — 2026-10-21 11:19 UTC

New packages created between 2026-10-21 10:21 UTC and 2026-10-21 11:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-21T11-19-44-131329Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-21 10:26:44 | [Fdw.Services.Data.Etl](https://www.nuget.org/packages/Fdw.Services.Data.Etl) | 1.4.0 | Fdw Team | Development tools and utilities for the Fdw ecosystem. |
| 2026-10-21 10:26:47 | [Hosihikari.Plugin.Abstractions](https://www.nuget.org/packages/Hosihikari.Plugin.Abstractions) | 1.0.0 | HosihikariFramework | Plugin contract for the Hosihikari framework: IPlugin, IPluginContext, IPluginL… |
| 2026-10-21 10:27:27 | [Hosihikari.Plugin.Templates](https://www.nuget.org/packages/Hosihikari.Plugin.Templates) | 1.0.0 | 星光 | dotnet new template for a precompiled Hosihikari plugin. |
| 2026-10-21 10:28:10 | [nanoFramework.Iot.Device.Cst816D](https://www.nuget.org/packages/nanoFramework.Iot.Device.Cst816D) | 1.0.1 | nanoFramework | CST816D single-point capacitive touch controller binding for .NET nanoFramework… |
| 2026-10-21 10:32:11 | [Zhomfr.Validation.Rules](https://www.nuget.org/packages/Zhomfr.Validation.Rules) | 0.2.1 | zhuolyan (Oleg Zhuravskiy) | Package Description |
| 2026-10-21 10:32:11 | [Zhomfr.Validation.Rules.Abstractions](https://www.nuget.org/packages/Zhomfr.Validation.Rules.Abstractions) | 0.2.1 | zhuolyan (Oleg Zhuravskiy) | Package Description |
| 2026-10-21 10:34:59 | [DeepSharp.Export.Onnx](https://www.nuget.org/packages/DeepSharp.Export.Onnx) | 0.14.0 | H.P. Gansevoort | Writes a DeepSharp network as an ONNX graph that any ONNX runtime answers throu… |
| 2026-10-21 10:38:00 | [Manasija.Drishti](https://www.nuget.org/packages/Manasija.Drishti) | 1.0.0 | Manasija | Official .NET client for the Drishti market-intelligence API: news, announcemen… |
| 2026-10-21 10:38:44 | [Stellaegis.Identity.PostgreSQL](https://www.nuget.org/packages/Stellaegis.Identity.PostgreSQL) | 5.0.0 | FRi | The PostgreSQL stores of Stellaegis.Identity: the accounts, their second factor… |
| 2026-10-21 10:38:45 | [Stellaegis.Identity.Server](https://www.nuget.org/packages/Stellaegis.Identity.Server) | 5.0.0 | FRi | The pages a person signs in and manages their account with — login, second fact… |
| 2026-10-21 10:38:45 | [Stellaegis.Identity](https://www.nuget.org/packages/Stellaegis.Identity) | 5.0.0 | FRi | Stellaegis Identity: the accounts of an application assembled on Stellaegis.Pri… |
| 2026-10-21 10:38:46 | [Stellaegis.Identity.Client](https://www.nuget.org/packages/Stellaegis.Identity.Client) | 5.0.0 | FRi | The HTTP client of Stellaegis.Identity for a resource server apart from the hos… |
| 2026-10-21 10:38:46 | [Stellaegis.Identity.AspNetCore](https://www.nuget.org/packages/Stellaegis.Identity.AspNetCore) | 5.0.0 | FRi | Stellaegis Identity in an ASP.NET Core host: the cookie a person signs in with,… |
| 2026-10-21 10:39:52 | [ClassicEPPlus](https://www.nuget.org/packages/ClassicEPPlus) | 4.5.3 | GreatBear | EPPlus 4.5.3.3 (the last LGPL version) rebuilt from source with bug fixes, targ… |
| 2026-10-21 10:41:34 | [Monq.Plugins.Extensions](https://www.nuget.org/packages/Monq.Plugins.Extensions) | 1.0.0 | Yaroslav Lobov | Reusable extensions, parsers and utilities for MONQ Agent plugins. |
| 2026-10-21 10:46:07 | [Moberg.Beacon.AI.Bedrock](https://www.nuget.org/packages/Moberg.Beacon.AI.Bedrock) | 5.0.0 | Moberg | Amazon Bedrock LLM provider for Beacon AI. Optional add-on for Beacon AI. |
| 2026-10-21 10:46:21 | [Moberg.Beacon.Doctor](https://www.nuget.org/packages/Moberg.Beacon.Doctor) | 5.0.0 | Moberg | Checks a deployed Beacon MCP endpoint the way an MCP client (Claude's connector… |
| 2026-10-21 10:46:22 | [Moberg.Beacon.Gateway](https://www.nuget.org/packages/Moberg.Beacon.Gateway) | 5.0.0 | Moberg | Beacon as the MCP gateway for an existing ASP.NET Core application: one call wi… |
| 2026-10-21 10:46:24 | [Moberg.Beacon.Testing](https://www.nuget.org/packages/Moberg.Beacon.Testing) | 5.0.0 | Moberg | Test helpers for a host that embeds Beacon as its MCP gateway: Entra-shaped tes… |
| 2026-10-21 10:58:16 | [nanoFramework.Iot.Device.Qmi8658](https://www.nuget.org/packages/nanoFramework.Iot.Device.Qmi8658) | 1.0.1 | nanoFramework | QMI8658 six-axis accelerometer and gyroscope binding for .NET nanoFramework, in… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

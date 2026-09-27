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

## Latest list — 2026-09-27 15:20 UTC

New packages created between 2026-09-27 14:20 UTC and 2026-09-27 15:20 UTC.

[Full CSV](data/new-nuget-packages-2026-09-27T15-20-10-430835Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-27 14:27:17 | [EIAM.Security.Package.DAF](https://www.nuget.org/packages/EIAM.Security.Package.DAF) | 2.1.0 | EIAM Team | Centralized EIAM authorization for ASP.NET Core applications: every protected c… |
| 2026-09-27 14:30:21 | [Soenneker.OpenApi.Converters.Meta](https://www.nuget.org/packages/Soenneker.OpenApi.Converters.Meta) | 4.0.1 | Jake Soenneker | Converts Meta Graph API JSON specifications into OpenAPI documents. |
| 2026-09-27 14:35:28 | [VintageStoryModKit.Settings.Core](https://www.nuget.org/packages/VintageStoryModKit.Settings.Core) | 0.2.0 | Gabriel Andreescu | JSON settings storage and validation for Vintage Story mods. |
| 2026-09-27 14:37:57 | [pdn-soundmodem-linux](https://www.nuget.org/packages/pdn-soundmodem-linux) | 0.82.0 | Tom Fanning M0LTE and Packet.… | Linux radio interface discovery (ALSA, hidraw, serial by USB device), device ac… |
| 2026-09-27 14:48:48 | [BrainEnterprise.Api.Twilio](https://www.nuget.org/packages/BrainEnterprise.Api.Twilio) | 1.0.0 | Gianluca Plevani, Brain Enter… | Twilio messaging client: SMS, MMS and WhatsApp, single and bulk send, delivery… |
| 2026-09-27 14:57:42 | [OfficeIMO.Html.Core](https://www.nuget.org/packages/OfficeIMO.Html.Core) | 3.4.4 | Przemyslaw Klys | Owned HTML document, node, editing and parser provider contracts for OfficeIMO. |
| 2026-09-27 14:57:43 | [OfficeIMO.Html.AngleSharp](https://www.nuget.org/packages/OfficeIMO.Html.AngleSharp) | 3.4.4 | Przemyslaw Klys | AngleSharp-backed HTML parsing and syntax services for the owned OfficeIMO HTML… |
| 2026-09-27 14:59:18 | [OfficeIMO.Project](https://www.nuget.org/packages/OfficeIMO.Project) | 3.4.4 | Przemyslaw Klys | Managed Microsoft Project XML and modern MPP/MPT authoring and editing, explici… |
| 2026-09-27 15:00:07 | [KiteKey.AI.Abstractions](https://www.nuget.org/packages/KiteKey.AI.Abstractions) | 0.1.0 | Kite & Key | Provider-neutral AI function, text-processing, and audio transport contracts. |
| 2026-09-27 15:00:07 | [KiteKey.AI](https://www.nuget.org/packages/KiteKey.AI) | 0.1.0 | Kite & Key | Provider-neutral AI function dispatch and JSON handler implementation. |
| 2026-09-27 15:00:14 | [Kapso.Client.Net](https://www.nuget.org/packages/Kapso.Client.Net) | 0.1.0 | Alexandre Costa | Typed .NET client for the Kapso APIs (WhatsApp, Platform, Workflows and Agent),… |
| 2026-09-27 15:08:07 | [DotDbg](https://www.nuget.org/packages/DotDbg) | 0.1.0 | Akito Inoue | Command-line debugger for managed .NET programs, designed for AI agents and ter… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

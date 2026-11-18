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

## Latest list — 2026-11-18 16:21 UTC

New packages created between 2026-11-18 15:22 UTC and 2026-11-18 16:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-18T16-21-30-210869Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-18 15:29:15 | [CachedEfCore.Caching](https://www.nuget.org/packages/CachedEfCore.Caching) | 1.1.7 | henriquewr | Caching abstractions for caching providers of CachedEfCore |
| 2026-11-18 15:33:10 | [PocketCalculator](https://www.nuget.org/packages/PocketCalculator) | 26.11.8209 | Curiosity GmbH,the Obscura au… | PocketCalculator: an embeddable headless browser engine with real JavaScript (V… |
| 2026-11-18 15:33:13 | [PocketCalculator.Cdp](https://www.nuget.org/packages/PocketCalculator.Cdp) | 26.11.8209 | Curiosity GmbH,the Obscura au… | PocketCalculator Chrome DevTools Protocol server, for driving the engine with P… |
| 2026-11-18 15:33:15 | [PocketCalculator.Mcp](https://www.nuget.org/packages/PocketCalculator.Mcp) | 26.11.8209 | Curiosity GmbH,the Obscura au… | PocketCalculator MCP server: browser tools for AI agents over the Model Context… |
| 2026-11-18 15:35:49 | [Dot0.Rubika](https://www.nuget.org/packages/Dot0.Rubika) | 10.0.1 | Dot0.Rubika | Reusable Rubika bot clients, HTTP registration and update forwarding. |
| 2026-11-18 15:35:52 | [Dot0.SoroushPlus](https://www.nuget.org/packages/Dot0.SoroushPlus) | 10.0.1 | Dot0.SoroushPlus | Reusable SoroushPlus bot clients, HTTP registration and update forwarding. |
| 2026-11-18 15:36:21 | [Dot0.Bale](https://www.nuget.org/packages/Dot0.Bale) | 10.0.1 | Dot0.Bale | Reusable Bale bot clients, HTTP registration and update forwarding. |
| 2026-11-18 15:36:45 | [AbpAdmin.EntityExplorer.Web](https://www.nuget.org/packages/AbpAdmin.EntityExplorer.Web) | 0.3.1 | ABP Admin contributors | ABP Admin Razor Pages UI for the entity explorer: browse and edit the entities… |
| 2026-11-18 15:37:00 | [MotorDsl.Pax](https://www.nuget.org/packages/MotorDsl.Pax) | 1.0.18 | Fernando Rafael Filipuzzi | Transport de impresion para la impresora interna del PAX A910S (Android) para M… |
| 2026-11-18 15:52:42 | [Dot0.SmsIr](https://www.nuget.org/packages/Dot0.SmsIr) | 10.0.1 | Dot0.SmsIr | Reusable sms.ir verification-template delivery with real and fake HTTP registra… |
| 2026-11-18 16:09:58 | [OfficeIMO.Yaml.Configuration](https://www.nuget.org/packages/OfficeIMO.Yaml.Configuration) | 3.6.2 | Przemyslaw Klys | YAML configuration provider for Microsoft.Extensions.Configuration, built on th… |
| 2026-11-18 16:10:01 | [OfficeIMO.Yaml](https://www.nuget.org/packages/OfficeIMO.Yaml) | 3.6.2 | Przemyslaw Klys | A dependency-free YAML 1.2 engine for OfficeIMO: a lossless document model that… |
| 2026-11-18 16:10:28 | [OfficeIMO.Word.CodeGlyphX](https://www.nuget.org/packages/OfficeIMO.Word.CodeGlyphX) | 3.6.2 | Przemyslaw Klys | QR codes and barcodes for OfficeIMO.Word, rendered by CodeGlyphX as SVG picture… |
| 2026-11-18 16:11:41 | [OfficeIMO.Toml.Configuration](https://www.nuget.org/packages/OfficeIMO.Toml.Configuration) | 3.6.2 | Przemyslaw Klys | TOML configuration provider for Microsoft.Extensions.Configuration, built on th… |
| 2026-11-18 16:11:43 | [OfficeIMO.Toml](https://www.nuget.org/packages/OfficeIMO.Toml) | 3.6.2 | Przemyslaw Klys | A dependency-free TOML 1.1 engine for OfficeIMO: a low-allocation pull reader,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

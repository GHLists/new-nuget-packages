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

## Latest list — 2026-11-17 16:21 UTC

New packages created between 2026-11-17 15:20 UTC and 2026-11-17 16:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-17T16-21-16-000796Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-17 15:23:40 | [Exchange56.GeoZipcode.Components](https://www.nuget.org/packages/Exchange56.GeoZipcode.Components) | 1.0.0 | T.J. McNaboe | Blazor UI components for rendering Exchange56 Geo Zipcode. |
| 2026-11-17 15:26:54 | [Exchange56.GeoZipcode.Components.Server](https://www.nuget.org/packages/Exchange56.GeoZipcode.Components.Server) | 1.0.1 | T.J. McNaboe | Server endpoints and methods for integrating with Exchange56 Geo Zipcode client. |
| 2026-11-17 15:41:21 | [WeatherExtension](https://www.nuget.org/packages/WeatherExtension) | 0.1.0 | MjepWare | Current conditions and forecasts for WindowSill, with favorite locations, multi… |
| 2026-11-17 15:42:42 | [Froststrap.DiscordRPC](https://www.nuget.org/packages/Froststrap.DiscordRPC) | 1.0.0 | Froststrap,Invra | A high-performance, Native AOT compatible Discord Rich Presence client for .NET… |
| 2026-11-17 15:44:10 | [Burgr.Templates.Mini](https://www.nuget.org/packages/Burgr.Templates.Mini) | 1.9.0 | Damien Lechat | Burgr's default template set: an ASP.NET Core Minimal API with EF Core in one p… |
| 2026-11-17 15:53:00 | [PicoCalcNano.Keyboard](https://www.nuget.org/packages/PicoCalcNano.Keyboard) | 0.1.0 | Stéphane Sibué | Keyboard driver for the Clockwork PicoCalc on .NET nanoFramework. Community pro… |
| 2026-11-17 15:57:31 | [DubUrl.Parser](https://www.nuget.org/packages/DubUrl.Parser) | 0.69.0 | Cédric L. Charlier | Parses SQL check expressions into a DubUrl syntax tree. |
| 2026-11-17 15:59:07 | [Dataverse.Fluent.Sales](https://www.nuget.org/packages/Dataverse.Fluent.Sales) | 1.0.0 | Craig Franchuk | Dynamics 365 Sales models and typed actions (QualifyLead, WinOpportunity, Close… |
| 2026-11-17 15:59:08 | [Dataverse.Fluent](https://www.nuget.org/packages/Dataverse.Fluent) | 1.0.0 | Craig Franchuk | A fluent, strongly typed client for the Microsoft Dataverse Web API: LINQ-style… |
| 2026-11-17 16:00:10 | [Gurux.Serial.Avalonia](https://www.nuget.org/packages/Gurux.Serial.Avalonia) | 9.0.2611.1706 | Gurux Ltd | Avalonia settings editor for Gurux Serial media. |
| 2026-11-17 16:00:27 | [Gurux.Serial.Blazor](https://www.nuget.org/packages/Gurux.Serial.Blazor) | 9.0.2611.1706 | Gurux Ltd | Optional Blazor settings components for Gurux media libraries. |
| 2026-11-17 16:00:52 | [Gurux.Net.Avalonia](https://www.nuget.org/packages/Gurux.Net.Avalonia) | 9.0.2611.1705 | Gurux Ltd | Avalonia settings editor for Gurux Net media. |
| 2026-11-17 16:00:57 | [XConnect.Sdk](https://www.nuget.org/packages/XConnect.Sdk) | 2.1.0 | Chaitanya Krishna Jonnagaddala | A lightweight, trimming- and Native AOT-friendly .NET SDK for the X API v2: Pos… |
| 2026-11-17 16:01:09 | [Gurux.Net.Blazor](https://www.nuget.org/packages/Gurux.Net.Blazor) | 9.0.2611.1705 | Gurux Ltd | Optional Blazor settings components for Gurux media libraries. |
| 2026-11-17 16:01:25 | [Gurux.Net.Maui](https://www.nuget.org/packages/Gurux.Net.Maui) | 9.0.2611.1705 | Gurux Ltd | Native MAUI settings editor for Gurux Net media. |
| 2026-11-17 16:05:49 | [PROBIS-ZUGFeRD.CDAR](https://www.nuget.org/packages/PROBIS-ZUGFeRD.CDAR) | 19.0.4 | Johannes Mauch | PROBIS-ZUGFeRD.CDAR: .NET library for reading and writing UN/CEFACT Cross Domai… |
| 2026-11-17 16:15:05 | [NewLife.MySql.Zstd](https://www.nuget.org/packages/NewLife.MySql.Zstd) | 1.5.2026.1117-beta1… | 新生命开发团队 | NewLife.MySql 的可选 zstd 压缩包。需要 CompressionAlgorithm=zstd 时安装；核心驱动保持零第三方依赖。Option… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

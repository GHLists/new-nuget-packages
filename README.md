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

## Latest list — 2026-10-19 19:22 UTC

New packages created between 2026-10-19 18:22 UTC and 2026-10-19 19:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-19T19-22-47-084785Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-19 18:26:11 | [Alvecta.Foundation.Application.Ports.Testing](https://www.nuget.org/packages/Alvecta.Foundation.Application.Ports.Testing) | 6.3.64 | Alvecta | Moq helpers for testing code written against Alvecta.Foundation.Application.Por… |
| 2026-10-19 18:26:24 | [LondonDataServices.OlidsToFhirMapper.STU3](https://www.nuget.org/packages/LondonDataServices.OlidsToFhirMapper.STU3) | 0.2.1 | North East London ICB | LondonDataServices.OlidsToFhirMapper.STU3 provides mapper conversions from OLID… |
| 2026-10-19 18:30:14 | [NewEdenKit.Sde](https://www.nuget.org/packages/NewEdenKit.Sde) | 0.1.0 | SimplyUnnamed | Downloads, caches and reads the EVE Online Static Data Export (SDE), and loads… |
| 2026-10-19 18:34:58 | [OpBlazorUI.Charts](https://www.nuget.org/packages/OpBlazorUI.Charts) | 2.0.2 | OpenNG | Charts for OpBlazorUI, built on Blazor-ApexCharts. |
| 2026-10-19 18:34:58 | [OpBlazorUI](https://www.nuget.org/packages/OpBlazorUI) | 2.0.2 | OpenNG | Optimus UI components for Blazor. |
| 2026-10-19 18:45:15 | [diagnostic-hooks](https://www.nuget.org/packages/diagnostic-hooks) | 0.0.1-preview1 | diagnostic-hooks | Package Description |
| 2026-10-19 18:49:22 | [VoiceTel.Sdk](https://www.nuget.org/packages/VoiceTel.Sdk) | 2.2.17 | VoiceTel | Official C# / .NET SDK for the VoiceTel REST API (v2.2.17). Provision numbers,… |
| 2026-10-19 18:50:25 | [VoiceML](https://www.nuget.org/packages/VoiceML) | 0.9.3 | VoiceTel | Official .NET SDK for VoiceML — VoiceTel's outbound voice + AMD service with a… |
| 2026-10-19 18:57:18 | [Umbraco.Community.WhoIsHere](https://www.nuget.org/packages/Umbraco.Community.WhoIsHere) | 0.9.0 | Lee Mills | Shows, live on the document edit screen, which other backoffice users have the… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

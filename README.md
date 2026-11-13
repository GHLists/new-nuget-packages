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

## Latest list — 2026-11-13 21:21 UTC

New packages created between 2026-11-13 20:21 UTC and 2026-11-13 21:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-13T21-21-53-449826Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-13 20:22:01 | [Spillgate](https://www.nuget.org/packages/Spillgate) | 0.1.0 | Felix Middelhoff | Decodes untrusted gzip, deflate and identity data (HTTP Content-Encoding and ra… |
| 2026-11-13 20:22:02 | [Spillgate.Brotli](https://www.nuget.org/packages/Spillgate.Brotli) | 0.1.0 | Felix Middelhoff | Brotli codec for Spillgate, built on the brotli decoder of the .NET runtime (Sy… |
| 2026-11-13 20:22:03 | [Spillgate.Http](https://www.nuget.org/packages/Spillgate.Http) | 0.1.0 | Felix Middelhoff | HttpClient handler and ASP.NET Core middleware that decode Content-Encoding thr… |
| 2026-11-13 20:22:05 | [Spillgate.Zstd](https://www.nuget.org/packages/Spillgate.Zstd) | 0.1.0 | Felix Middelhoff | Zstandard codec for Spillgate: a managed decoder with window, dictionary and fr… |
| 2026-11-13 20:26:46 | [LunchMoney.Sdk](https://www.nuget.org/packages/LunchMoney.Sdk) | 0.1.0 | Bruno Felix | A typed .NET client for the Lunch Money v2 API, with dependency injection, Http… |
| 2026-11-13 20:33:37 | [MASS4.Guinevere.DevTools](https://www.nuget.org/packages/MASS4.Guinevere.DevTools) | 6.7.0 | Bruno Massa | Package Description |
| 2026-11-13 20:33:46 | [MASS4.Guinevere.Profiling](https://www.nuget.org/packages/MASS4.Guinevere.Profiling) | 6.7.0 | Bruno Massa | Package Description |
| 2026-11-13 20:36:31 | [Sondor.Results.Localization](https://www.nuget.org/packages/Sondor.Results.Localization) | 0.1.0 | Sondor Dev | Translated text for a Sondor.Results Error, from the application's own resource… |
| 2026-11-13 20:36:41 | [ConsoleMonster.Extensions.Serilog](https://www.nuget.org/packages/ConsoleMonster.Extensions.Serilog) | 2.4.1 | Przemyslaw Klys | Serilog output through ConsoleMonster: structured log lines, exceptions and coo… |
| 2026-11-13 20:36:43 | [ConsoleMonster.Extensions.NLog](https://www.nuget.org/packages/ConsoleMonster.Extensions.NLog) | 2.4.1 | Przemyslaw Klys | NLog output through ConsoleMonster: structured log lines, exceptions and coordi… |
| 2026-11-13 20:51:49 | [Naravel.Routing.Cache](https://www.nuget.org/packages/Naravel.Routing.Cache) | 0.2.0 | Naravel contributors | A shared store for the Naravel.Routing throttle middleware, counting in a Narav… |
| 2026-11-13 21:01:31 | [Hto3.OpenApi.JsonMultipartFormDataSupport](https://www.nuget.org/packages/Hto3.OpenApi.JsonMultipartFormDataSupport) | 1.0.0 | HTO3 | Support JSON Multipart data in OpenApi. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

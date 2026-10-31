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

## Latest list — 2026-10-31 19:21 UTC

New packages created between 2026-10-31 18:20 UTC and 2026-10-31 19:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-31T19-21-09-073513Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-31 18:41:56 | [SkyrimForge.PrismaUi](https://www.nuget.org/packages/SkyrimForge.PrismaUi) | 0.1.0 | Wessley Mitchell | Create and script PrismaUI views from a SkyrimForge plugin in C#. PrismaUI rend… |
| 2026-10-31 18:42:09 | [SkyrimForge.PrismaUi.PluginTemplate](https://www.nuget.org/packages/SkyrimForge.PrismaUi.PluginTemplate) | 0.1.0 | Wessley Mitchell | The dotnet new template for a SkyrimForge plugin with a PrismaUI view: a .NET 1… |
| 2026-10-31 18:44:15 | [Arienlabs.IpLocationClient](https://www.nuget.org/packages/Arienlabs.IpLocationClient) | 1.0.0 | Arienlabs | Klient .NET 10 dla IP Location API: lokalizacja IPv4/IPv6, ASN, batch i stan us… |
| 2026-10-31 18:51:45 | [BicycleRentalSystem.Generic](https://www.nuget.org/packages/BicycleRentalSystem.Generic) | 1.0.0 | BicycleRentalSystem.Generic | Generic entity contract and in-memory repository. |
| 2026-10-31 19:03:29 | [Soenneker.Anthropic.OpenApiClientUtil](https://www.nuget.org/packages/Soenneker.Anthropic.OpenApiClientUtil) | 11.0.2 | Jake Soenneker | A thread-safe utility for obtaining Anthropic's OpenApiClient singleton. |
| 2026-10-31 19:03:39 | [Soenneker.Klaviyo.OpenApiClientUtil](https://www.nuget.org/packages/Soenneker.Klaviyo.OpenApiClientUtil) | 11.0.2 | Jake Soenneker | A thread-safe utility for obtaining Klaviyo's OpenApiClient singleton. |
| 2026-10-31 19:12:32 | [ByTalset.ResultPattern](https://www.nuget.org/packages/ByTalset.ResultPattern) | 1.0.0 | Antonio L. | Implementación ligera del patrón Result para C#: representa operaciones exitosa… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-16 18:19 UTC

New packages created between 2026-11-16 17:21 UTC and 2026-11-16 18:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-16T18-19-07-822606Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-16 17:24:52 | [Swealium](https://www.nuget.org/packages/Swealium) | 0.1.0 | HumoyunMirzo | A .NET 10 retained-mode desktop GUI framework with SDL3 windowing, GPU/raster d… |
| 2026-11-16 17:43:12 | [TrakHound.Debug](https://www.nuget.org/packages/TrakHound.Debug) | 1.0.0.6-prerelease | TrakHound | Contains classes for running TrakHound packages locally, without an Instance |
| 2026-11-16 17:43:12 | [TrakHound.AspNetCore](https://www.nuget.org/packages/TrakHound.AspNetCore) | 1.0.0.6-prerelease | TrakHound | Contains the ASP.NET Core classes shared by the TrakHound Instance and the debu… |
| 2026-11-16 17:43:12 | [TrakHound.Hosting](https://www.nuget.org/packages/TrakHound.Hosting) | 1.0.0.6-prerelease | TrakHound | Contains classes for hosting TrakHound modules outside of an Instance (ex. crea… |
| 2026-11-16 17:43:12 | [TrakHound.Hosting.AspNetCore](https://www.nuget.org/packages/TrakHound.Hosting.AspNetCore) | 1.0.0.6-prerelease | TrakHound | Contains classes for hosting TrakHound Apis in ASP.NET Core outside of an Insta… |
| 2026-11-16 17:43:12 | [TrakHound.Testing](https://www.nuget.org/packages/TrakHound.Testing) | 1.0.0.6-prerelease | TrakHound | Contains classes for unit testing TrakHound packages without an Instance (an in… |
| 2026-11-16 17:45:00 | [Soenneker.Blazor.Notifications.Audio](https://www.nuget.org/packages/Soenneker.Blazor.Notifications.Audio) | 11.0.3 | Jake Soenneker | Audio notifications for Blazor applications. |
| 2026-11-16 17:46:53 | [IpsoFacto.Identity](https://www.nuget.org/packages/IpsoFacto.Identity) | 1.0.0 | Luciano Circelli | Public identity proof and metadata package. |
| 2026-11-16 17:55:32 | [cCoder.Eventing.Sql](https://www.nuget.org/packages/cCoder.Eventing.Sql) | 2026.11.16.1754 | cCoder | SQL-backed cCoder event transport |
| 2026-11-16 17:57:22 | [NymBroker.Dashboard](https://www.nuget.org/packages/NymBroker.Dashboard) | 0.25.1 | nymankla@gmail.com | Live web dashboard for NymBroker: endpoints, queue contents, health, throughput… |
| 2026-11-16 18:06:54 | [Testcontainers.Vault](https://www.nuget.org/packages/Testcontainers.Vault) | 4.17.0 | Andre Hofmeister and contribu… | Testcontainers for .NET is a library to support tests with throwaway instances… |
| 2026-11-16 18:07:23 | [Testcontainers.Chroma](https://www.nuget.org/packages/Testcontainers.Chroma) | 4.17.0 | Andre Hofmeister and contribu… | Testcontainers for .NET is a library to support tests with throwaway instances… |
| 2026-11-16 18:07:27 | [Testcontainers.MongoDbAtlasLocal](https://www.nuget.org/packages/Testcontainers.MongoDbAtlasLocal) | 4.17.0 | Andre Hofmeister and contribu… | Testcontainers for .NET is a library to support tests with throwaway instances… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

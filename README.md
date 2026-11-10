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

## Latest list — 2026-11-10 08:21 UTC

New packages created between 2026-11-10 07:21 UTC and 2026-11-10 08:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-10T08-21-27-300686Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-10 07:36:47 | [WebsiteScreenshotWorld.Extensions.DependencyInjection](https://www.nuget.org/packages/WebsiteScreenshotWorld.Extensions.DependencyInjection) | 0.1.0 | Silhouettec Solutions | Registers the Website Screenshot World client with Microsoft.Extensions.Depende… |
| 2026-11-10 07:36:48 | [WebsiteScreenshotWorld](https://www.nuget.org/packages/WebsiteScreenshotWorld) | 0.1.0 | Silhouettec Solutions | Client for the Website Screenshot World APIs: capture web pages as images, vide… |
| 2026-11-10 07:41:57 | [Larik.Data](https://www.nuget.org/packages/Larik.Data) | 1.0.0 | Larik SQL Studio Contributors | Provider contracts, the SQL language seam, and the add-on loader for Larik SQL… |
| 2026-11-10 07:45:37 | [Fingerly.Server.AspNetCore](https://www.nuget.org/packages/Fingerly.Server.AspNetCore) | 0.1.0 | Fingerly | ASP.NET Core middleware, endpoint routing and dependency injection for the Fing… |
| 2026-11-10 07:45:37 | [Fingerly.Server](https://www.nuget.org/packages/Fingerly.Server) | 0.1.0 | Fingerly | Server-side Fingerly SDK: read stored identification events, verify signed webh… |
| 2026-11-10 07:57:41 | [Uniform.Matrix.Video](https://www.nuget.org/packages/Uniform.Matrix.Video) | 0.1.21 | Uniform.Matrix.Video | Video for Matrix calls in pure C#: a VP8 decoder ported from the reference deco… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

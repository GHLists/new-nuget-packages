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

## Latest list — 2026-10-08 22:19 UTC

New packages created between 2026-10-08 21:19 UTC and 2026-10-08 22:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-08T22-19-08-963028Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-08 21:29:53 | [Stormware.Mpohoda.OpenApi.Client.GraphQl](https://www.nuget.org/packages/Stormware.Mpohoda.OpenApi.Client.GraphQl) | 20.0.0 | Stormware | Strawberry Shake GraphQL SDK client for the mPohoda Open API, shared by Czech a… |
| 2026-10-08 21:29:56 | [Stormware.Mpohoda.OpenApi.Client.Transport](https://www.nuget.org/packages/Stormware.Mpohoda.OpenApi.Client.Transport) | 20.0.0 | Stormware | Transport layer (authentication handlers, OAuth token client, shared connection… |
| 2026-10-08 21:34:40 | [Altinn.Authorization.RepoCtl.Checks](https://www.nuget.org/packages/Altinn.Authorization.RepoCtl.Checks) | 2.0.0 | Altinn.Authorization.RepoCtl.… | Package Description |
| 2026-10-08 21:34:42 | [Altinn.Authorization.RepoCtl.GitHub](https://www.nuget.org/packages/Altinn.Authorization.RepoCtl.GitHub) | 2.0.0 | Altinn.Authorization.RepoCtl.… | Package Description |
| 2026-10-08 21:34:44 | [Altinn.Authorization.RepoCtl.MsBuild](https://www.nuget.org/packages/Altinn.Authorization.RepoCtl.MsBuild) | 2.0.0 | Altinn.Authorization.RepoCtl.… | Package Description |
| 2026-10-08 21:41:04 | [BepInExUtilities](https://www.nuget.org/packages/BepInExUtilities) | 0.1.0 | BepInExUtilities | Package Description |
| 2026-10-08 21:43:27 | [Altinn.Authorization.RepoCtl.Cli](https://www.nuget.org/packages/Altinn.Authorization.RepoCtl.Cli) | 2.0.0 | repoctl | Package Description |
| 2026-10-08 22:04:54 | [DragonFly.Assets.SkiaSharp](https://www.nuget.org/packages/DragonFly.Assets.SkiaSharp) | 1.0.40 | usercode | Headless CMS based on ASP.NET Core and Blazor |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-08 10:19 UTC

New packages created between 2026-11-08 09:20 UTC and 2026-11-08 10:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-08T10-19-24-321139Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-08 09:45:22 | [LFDCC.IEC60870.CS103](https://www.nuget.org/packages/LFDCC.IEC60870.CS103) | 6.1.0 | LFDCC | IEC 60870-5-103 (DL/T 667-1999) protective equipment protocol library: native F… |
| 2026-11-08 10:04:17 | [BaryoDev.Umbraco.Comments](https://www.nuget.org/packages/BaryoDev.Umbraco.Comments) | 0.1.0 | BaryoDev | Moderated comments for Umbraco 17. Plain text, pending by default, works withou… |
| 2026-11-08 10:04:26 | [BaryoDev.Umbraco.SocialPost](https://www.nuget.org/packages/BaryoDev.Umbraco.SocialPost) | 0.1.0 | BaryoDev | Post published Umbraco 17 content to LinkedIn, Bluesky and Mastodon from a retr… |
| 2026-11-08 10:11:16 | [monorepo-dotnet](https://www.nuget.org/packages/monorepo-dotnet) | 0.1.0 | Trần Gia Phúc | Interactive generator for ASP.NET Core solutions (DDD, Clean, 1-Layer, MVC) wit… |
| 2026-11-08 10:13:08 | [BaryoDev.Umbraco.Analytics](https://www.nuget.org/packages/BaryoDev.Umbraco.Analytics) | 0.1.0 | BaryoDev | Cookie-free page view analytics for Umbraco 17, stored in the site's own databa… |
| 2026-11-08 10:13:08 | [BaryoDev.Umbraco.RelatedPosts](https://www.nuget.org/packages/BaryoDev.Umbraco.RelatedPosts) | 0.1.0 | BaryoDev | Read next related posts for Umbraco 17: shared tags, category and optional text… |
| 2026-11-08 10:13:10 | [BaryoDev.Umbraco.ShareLike](https://www.nuget.org/packages/BaryoDev.Umbraco.ShareLike) | 0.1.0 | BaryoDev | Share buttons, a rate-limited like count and reading time for Umbraco 17, with… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

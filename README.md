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

## Latest list — 2026-10-01 05:20 UTC

New packages created between 2026-10-01 04:22 UTC and 2026-10-01 05:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-01T05-20-57-422529Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-01 04:31:42 | [Zymergi.Rendering](https://www.nuget.org/packages/Zymergi.Rendering) | 11.1.0-alpha | Oliver Yu | HTML, Markdown, and XSLT rendering for Zymergi. Implements Core's IMarkdownRend… |
| 2026-10-01 04:48:42 | [Webority.Seo.AspNetCore](https://www.nuget.org/packages/Webority.Seo.AspNetCore) | 0.1.0 | Webority Technologies | SEO for Webority Razor Pages websites: one options section, index protection ou… |
| 2026-10-01 04:58:40 | [ManInBlack.AI.Persistence.Sqlite](https://www.nuget.org/packages/ManInBlack.AI.Persistence.Sqlite) | 0.1.0 | fengb3 | ManInBlack.AI 的可选 SQLite 持久化包：基于 EF Core 10 + SQLite 实现 ISessionStorage、IUserSt… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

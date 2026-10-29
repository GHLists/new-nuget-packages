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

## Latest list — 2026-10-29 09:19 UTC

New packages created between 2026-10-29 08:22 UTC and 2026-10-29 09:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-29T09-19-44-057371Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-29 08:50:32 | [DouyinOpenApi](https://www.nuget.org/packages/DouyinOpenApi) | 1.0.3 | zhangliang2008 | 抖音开放平台 OpenAPI SDK 的 C# 实现，兼容 .NET Framework 4.7+ 与 .NET Standard 2.0 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

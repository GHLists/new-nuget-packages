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

## Latest list — 2026-11-16 16:18 UTC

New packages created between 2026-11-16 15:21 UTC and 2026-11-16 16:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-16T16-18-57-068404Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-16 15:26:34 | [uSync.Engage.Complete](https://www.nuget.org/packages/uSync.Engage.Complete) | 17.0.0-beta02 | Kevin Jump | uSync.Complete push and pull for Umbraco Engage settings - personas, customer j… |
| 2026-11-16 15:38:07 | [MyNuget_smu](https://www.nuget.org/packages/MyNuget_smu) | 1.0.0 | Sathyan | Simple calculator with Add method |
| 2026-11-16 15:42:14 | [Cangming.Data.Contracts](https://www.nuget.org/packages/Cangming.Data.Contracts) | 0.1.7.1116 | Fangyu,lukan@xknife.net,Asong… | Cangming 客户端通用基座框架库（插件化宿主）。 |
| 2026-11-16 15:42:17 | [Cangming.Data.Sqlite](https://www.nuget.org/packages/Cangming.Data.Sqlite) | 0.1.7.1116 | Fangyu,lukan@xknife.net,Asong… | Cangming 客户端通用基座框架库（插件化宿主）。 |
| 2026-11-16 15:42:33 | [Cangming.Logs.UI](https://www.nuget.org/packages/Cangming.Logs.UI) | 0.1.7.1116 | Fangyu,lukan@xknife.net,Asong… | 仅组织内部使用。把日志条目投递到 UI 线程集合的辅助层，不依赖具体日志框架。 |
| 2026-11-16 15:46:29 | [Bitwarden.Server.Sdk.PasswordHashing](https://www.nuget.org/packages/Bitwarden.Server.Sdk.PasswordHashing) | 0.1.0 | Bitwarden Inc. | Server-side hashing of client-derived password hashes, compatible with hashes s… |
| 2026-11-16 15:48:09 | [Moberg.EntityFrameworkCore.DesignerlessMigrations](https://www.nuget.org/packages/Moberg.EntityFrameworkCore.DesignerlessMigrations) | 10.0.0 | Moberg | Single-file EF Core migrations: dotnet ef migrations add writes one file with [… |
| 2026-11-16 15:48:10 | [Moberg.EntityFrameworkCore.DesignerlessMigrations.Npgsql](https://www.nuget.org/packages/Moberg.EntityFrameworkCore.DesignerlessMigrations.Npgsql) | 10.0.0 | Moberg | Runtime support for designerless EF Core migrations on PostgreSQL. Without a De… |
| 2026-11-16 15:58:22 | [KaizenIO.Seo](https://www.nuget.org/packages/KaizenIO.Seo) | 0.1.0 | Kaizenio, Inc. | Kaizen.Seo: head component (title, description, canonical, Open Graph, Twitter)… |
| 2026-11-16 15:58:23 | [KaizenIO.StaticSite](https://www.nuget.org/packages/KaizenIO.StaticSite) | 0.1.0 | Kaizenio, Inc. | Kaizen.StaticSite: exports a Blazor SSR app to flat files (route/index.html, as… |
| 2026-11-16 15:58:23 | [KaizenIO.BlogEngine](https://www.nuget.org/packages/KaizenIO.BlogEngine) | 0.1.0 | Kaizenio, Inc. | Kaizen.BlogEngine: Markdig + YamlDotNet post service (YAML front matter) for Bl… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

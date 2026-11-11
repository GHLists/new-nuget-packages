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

## Latest list — 2026-11-11 19:19 UTC

New packages created between 2026-11-11 18:21 UTC and 2026-11-11 19:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-11T19-19-33-772437Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-11 18:29:38 | [Alexpivo394.ToadDesign](https://www.nuget.org/packages/Alexpivo394.ToadDesign) | 1.0.0 | Alexpivo394 | WPF controls and styles in the ToadFlow (Mantine) look for windows hosted insid… |
| 2026-11-11 18:32:28 | [Bitwarden.Server.Sdk.Infrastructure](https://www.nuget.org/packages/Bitwarden.Server.Sdk.Infrastructure) | 0.1.0 | Bitwarden Inc. | Lets libraries declare the infrastructure (databases, caches, message topics, c… |
| 2026-11-11 18:34:52 | [Tubatools.Xiaoheihe](https://www.nuget.org/packages/Tubatools.Xiaoheihe) | 1.0.13 | 图吧工具箱 | 小黑盒社区客户端：扫码登录、推荐流、社区、搜索、帖子评论、签到、收藏、历史、游戏库 |
| 2026-11-11 18:37:31 | [Bitvantage.InternetProtocol.IPNetworkExtensions](https://www.nuget.org/packages/Bitvantage.InternetProtocol.IPNetworkExtensions) | 1.0.0 | Michael Crino | C# 14 extension members for System.Net.IPNetwork and IPAddress that add CIDR, s… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-14 18:21 UTC

New packages created between 2026-11-14 17:19 UTC and 2026-11-14 18:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-14T18-21-22-779623Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-14 17:19:17 | [MailPier.Inbox.Client](https://www.nuget.org/packages/MailPier.Inbox.Client) | 0.1.1 | Solutions Group Unlimited LLC | .NET client for MailPier Inbox: create test addresses, wait for an email in you… |
| 2026-11-14 17:24:08 | [Inertia.Net.MongoDB](https://www.nuget.org/packages/Inertia.Net.MongoDB) | 1.9.0 | Inertia.Net contributors | MongoDB pagination for Inertia.Net (not Native AOT compatible). |
| 2026-11-14 17:24:10 | [Inertia.Net.Redis](https://www.nuget.org/packages/Inertia.Net.Redis) | 1.9.0 | Inertia.Net contributors | A Redis cache store for Inertia.Net: cached props and SSR renders shared by eve… |
| 2026-11-14 17:31:32 | [BccCode.Privacy.EntityFrameworkCore](https://www.nuget.org/packages/BccCode.Privacy.EntityFrameworkCore) | 0.1.0 | BCC | Purpose-bound access to personal data in EF Core and PostgreSQL: a basis per or… |
| 2026-11-14 17:38:04 | [NAPS2.Images.Skia](https://www.nuget.org/packages/NAPS2.Images.Skia) | 1.6.1 | Ben Olden-Cooligan | Images based on SkiaSharp for NAPS2.Sdk. |
| 2026-11-14 17:49:19 | [DataJuggler.Excelerate.Office](https://www.nuget.org/packages/DataJuggler.Excelerate.Office) | 11.0.0 | DataJuggler,Tony Qu,NPOI Cont… | Independent build of NPOI (a .NET port of Apache POI) under the Apache 2.0 lice… |
| 2026-11-14 17:51:21 | [OpenRAR.NET](https://www.nuget.org/packages/OpenRAR.NET) | 2.4.0 | OpenRAR Project | OpenRAR C# SDK — P/Invoke binding over the frozen OpenRAR C ABI (RAR 5.0 read,… |
| 2026-11-14 17:55:30 | [Bitzsoft.Integrations.AI.Testing](https://www.nuget.org/packages/Bitzsoft.Integrations.AI.Testing) | 1.1.0 | Bitzsoft | Bitzsoft AI 与 MCP 测试支持包 — 无测试框架锁定的存储端口契约测试基类、进程内测试替身、受控测试时钟与 FDE 黄金评估运行器 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

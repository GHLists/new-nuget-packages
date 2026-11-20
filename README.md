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

## Latest list — 2026-11-20 01:20 UTC

New packages created between 2026-11-20 00:20 UTC and 2026-11-20 01:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-20T01-20-23-65637Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-20 00:28:15 | [LsMsgPack.SignalR](https://www.nuget.org/packages/LsMsgPack.SignalR) | 2026.11.20.1 | Louis Somers | A MessagePack hub protocol for ASP.NET Core SignalR (server and .NET client) on… |
| 2026-11-20 01:03:22 | [ForEach.Email.MailKit](https://www.nuget.org/packages/ForEach.Email.MailKit) | 0.1.0 | For-Each Smederevo | MailKit implementation of ForEach.Email.Abstractions: AddMailKitEmail registers… |
| 2026-11-20 01:03:22 | [ForEach.Email.Abstractions](https://www.nuget.org/packages/ForEach.Email.Abstractions) | 0.1.0 | For-Each Smederevo | IEmailSender and IEmlBuilder: the vendor-neutral contracts for sending one HTML… |
| 2026-11-20 01:05:44 | [Pulumi.Labs.Anthropic](https://www.nuget.org/packages/Pulumi.Labs.Anthropic) | 0.1.0 | Pulumi Labs | Manage the Anthropic platform as code: Claude Managed Agents, skills, workspace… |
| 2026-11-20 01:07:54 | [OpenRobot.Edge.Variable.Client](https://www.nuget.org/packages/OpenRobot.Edge.Variable.Client) | 0.2.0 | OpenRobot | 业务变量消费客户端：按稳定引用读取快照、订阅变化、续租，屏蔽 DC / 配置 / 其他 EXE 的来源差异。 |
| 2026-11-20 01:15:19 | [Moli.Net](https://www.nuget.org/packages/Moli.Net) | 0.1.6 | Moli.Net | Downloads, starts, and stops Moli, a headless browser that speaks CDP. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

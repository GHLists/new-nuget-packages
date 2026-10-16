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

## Latest list — 2026-10-16 05:22 UTC

New packages created between 2026-10-16 04:20 UTC and 2026-10-16 05:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-16T05-22-40-120413Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-16 04:25:37 | [Milvus.Client](https://www.nuget.org/packages/Milvus.Client) | 2.6.0 | Milvus.Client | Milvus C# SDK |
| 2026-10-16 04:52:26 | [Kewl.Metrics](https://www.nuget.org/packages/Kewl.Metrics) | 1.0.0 | KewlMetrics | A library for generating logs that are workflow oriented. Instead of logging as… |
| 2026-10-16 04:59:53 | [Coworkee.Workflows.Elsa](https://www.nuget.org/packages/Coworkee.Workflows.Elsa) | 0.0.1.26 | fgilde | Elsa Workflows 3 for Coworkee apps: hosted in the app database, with activities… |
| 2026-10-16 04:59:55 | [Coworkee.Webhooks](https://www.nuget.org/packages/Coworkee.Webhooks) | 0.0.1.26 | fgilde | Outgoing webhooks: signed events about entity changes, workflow transitions and… |
| 2026-10-16 04:59:56 | [Coworkee.Workflows](https://www.nuget.org/packages/Coworkee.Workflows) | 0.0.1.26 | fgilde | States, transitions and approvals with deadlines, reminders and a history for a… |
| 2026-10-16 05:00:22 | [NSmithy.Protocols.RpcV2](https://www.nuget.org/packages/NSmithy.Protocols.RpcV2) | 0.13.0 | Thomas Laich | Routing, errors, and event streams shared by the Smithy RPC v2 protocols in NSm… |
| 2026-10-16 05:00:25 | [NSmithy.Protocols.RpcV2Json](https://www.nuget.org/packages/NSmithy.Protocols.RpcV2Json) | 0.13.0 | Thomas Laich | Smithy rpcv2Json protocol for NSmithy clients and ASP.NET Core servers. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

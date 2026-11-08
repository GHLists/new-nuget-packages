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

## Latest list — 2026-11-08 16:19 UTC

New packages created between 2026-11-08 15:21 UTC and 2026-11-08 16:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-08T16-19-42-71286Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-08 15:36:08 | [PayChangu.NET](https://www.nuget.org/packages/PayChangu.NET) | 0.1.0 | PayChangu.NET Contributors | A strongly typed .NET SDK for integrating with the PayChangu payment gateway, s… |
| 2026-11-08 15:49:30 | [Zenvoy.Abstractions](https://www.nuget.org/packages/Zenvoy.Abstractions) | 10.0.0 | Maxsud Mutalov | Zenvoy abstractions: request, notification, stream and pipeline contracts. Refe… |
| 2026-11-08 15:49:31 | [Zenvoy](https://www.nuget.org/packages/Zenvoy) | 10.0.0 | Maxsud Mutalov | Zenvoy: a high-performance, zero-allocation, reflection-free mediator powered b… |
| 2026-11-08 15:54:57 | [AgentSpace.SDK](https://www.nuget.org/packages/AgentSpace.SDK) | 0.1.0 | Jihad Khawaja | Embeddable .NET workspaces for agents with policy-controlled storage, memory, a… |
| 2026-11-08 15:55:35 | [KeelMatrix.KeyRingGuard](https://www.nuget.org/packages/KeelMatrix.KeyRingGuard) | 0.1.0 | KeelMatrix | Prove ASP.NET Core Data Protection key continuity, sharing, rotation, and isola… |
| 2026-11-08 16:11:00 | [Belin.Should](https://www.nuget.org/packages/Belin.Should) | 2026.11.0 | CedX | A thin BDD wrapper around MSTest assertions. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-15 06:19 UTC

New packages created between 2026-11-15 05:20 UTC and 2026-11-15 06:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-15T06-19-25-341778Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-15 05:22:39 | [Tralys.BehaviorTree](https://www.nuget.org/packages/Tralys.BehaviorTree) | 0.7.0 | vrimar | Zero/low-allocation behavior tree library: one shared immutable tree per archet… |
| 2026-11-15 05:40:52 | [Squeaky](https://www.nuget.org/packages/Squeaky) | 0.1.0 | CodeByDylan | A .NET library of Clean Architecture building blocks that enforce layer boundar… |
| 2026-11-15 06:12:01 | [Migadu](https://www.nuget.org/packages/Migadu) | 0.1.0 | orlys | Typed .NET client for the Migadu REST API: domains, mailboxes, identities, forw… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

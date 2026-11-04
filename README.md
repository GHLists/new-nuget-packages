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

## Latest list — 2026-11-04 03:21 UTC

New packages created between 2026-11-04 02:20 UTC and 2026-11-04 03:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-04T03-21-02-671059Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-04 02:22:51 | [NSail.Harness.Hosting](https://www.nuget.org/packages/NSail.Harness.Hosting) | 0.1.472 | Leonardo Porro,Emmanuel Arias | NSail.Harness.Hosting, part of NSail Stack: a .NET modular-monolith framework (… |
| 2026-11-04 02:22:55 | [NSail.Harness.Sdk](https://www.nuget.org/packages/NSail.Harness.Sdk) | 0.1.472 | Leonardo Porro,Emmanuel Arias | NSail.Harness.Sdk, part of NSail Stack: a .NET modular-monolith framework (mess… |
| 2026-11-04 02:22:57 | [NSail.Harness](https://www.nuget.org/packages/NSail.Harness) | 0.1.472 | Leonardo Porro,Emmanuel Arias | NSail.Harness, part of NSail Stack: a .NET modular-monolith framework (messagin… |
| 2026-11-04 02:23:04 | [NSail.Harness.GitHub](https://www.nuget.org/packages/NSail.Harness.GitHub) | 0.1.472 | Leonardo Porro,Emmanuel Arias | NSail.Harness.GitHub, part of NSail Stack: a .NET modular-monolith framework (m… |
| 2026-11-04 02:23:04 | [NSail.Harness.Claude](https://www.nuget.org/packages/NSail.Harness.Claude) | 0.1.472 | Leonardo Porro,Emmanuel Arias | NSail.Harness.Claude, part of NSail Stack: a .NET modular-monolith framework (m… |
| 2026-11-04 03:09:14 | [HHO.LV.NetClaw.Providers.Anthropic](https://www.nuget.org/packages/HHO.LV.NetClaw.Providers.Anthropic) | 1.2.14 | HuyHo | Package Description |
| 2026-11-04 03:09:39 | [HHO.LV.NetClaw.Providers.Google](https://www.nuget.org/packages/HHO.LV.NetClaw.Providers.Google) | 1.2.14 | HuyHo | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

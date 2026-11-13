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

## Latest list — 2026-11-13 05:21 UTC

New packages created between 2026-11-13 04:21 UTC and 2026-11-13 05:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-13T05-21-42-78099Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-13 04:24:24 | [uTPro.Feature.MailHub](https://www.nuget.org/packages/uTPro.Feature.MailHub) | 18.0.0 | T4VN | Self-contained email monitoring, delivery tracking, and history dashboard for U… |
| 2026-11-13 04:34:06 | [Runna.Fs](https://www.nuget.org/packages/Runna.Fs) | 0.2.0 | Nullean and contributors | F# DU/match binding over Nullean.Runna — exhaustive, typed, namespaced build ta… |
| 2026-11-13 04:34:07 | [Runna](https://www.nuget.org/packages/Runna) | 0.2.0 | Nullean and contributors | Property-dispatch build target DSL with Argh-quality help and per-target typed… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

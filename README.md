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

## Latest list — 2026-10-04 15:21 UTC

New packages created between 2026-10-04 14:18 UTC and 2026-10-04 15:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-04T15-21-55-309634Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-04 14:33:09 | [Delta.Diagnostics](https://www.nuget.org/packages/Delta.Diagnostics) | 0.0.6 | Artromskiy | Implementation-neutral diagnostics, logging, and profiling APIs for .NET. |
| 2026-10-04 14:33:29 | [Regira.Entities.Validation.FluentValidation](https://www.nuget.org/packages/Regira.Entities.Validation.FluentValidation) | 6.5.0 | Regira bv | FluentValidation integration for Regira entity validation: AbstractValidator ru… |
| 2026-10-04 14:45:56 | [ArkMirage.NetherNet.Endpoint](https://www.nuget.org/packages/ArkMirage.NetherNet.Endpoint) | 1.0.0 | BE-Community-Dev | HTTP signaling endpoints for NetherNet, providing client and server implementat… |
| 2026-10-04 14:45:57 | [ArkMirage.NetherNet.Discovery](https://www.nuget.org/packages/ArkMirage.NetherNet.Discovery) | 1.0.0 | BE-Community-Dev | LAN discovery signaling for NetherNet, broadcasting encrypted server informatio… |
| 2026-10-04 14:45:57 | [ArkMirage.NetherNet](https://www.nuget.org/packages/ArkMirage.NetherNet) | 1.0.0 | BE-Community-Dev | A pure C# implementation of the NetherNet networking protocol for Minecraft Bed… |
| 2026-10-04 14:54:44 | [Nihil](https://www.nuget.org/packages/Nihil) | 0.1.0 | Alice | minimalist C# game engine |
| 2026-10-04 15:01:46 | [Pondhawk.Logging.CloudWatch](https://www.nuget.org/packages/Pondhawk.Logging.CloudWatch) | 1.0.21 | Pond Hawk Technologies Inc. | Amazon CloudWatch Logs provider for Pondhawk.Logging: a ZLogger-based Microsoft… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

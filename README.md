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

## Latest list — 2026-10-16 15:21 UTC

New packages created between 2026-10-16 14:19 UTC and 2026-10-16 15:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-16T15-21-06-199202Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-16 14:22:30 | [Activout.DatabaseClient.Extensions.DependencyInjection](https://www.nuget.org/packages/Activout.DatabaseClient.Extensions.DependencyInjection) | 5.0.0-rc5 | Activout.DatabaseClient.Exten… | Microsoft.Extensions.DependencyInjection extensions for Activout.DatabaseClient. |
| 2026-10-16 14:22:31 | [Activout.DatabaseClient.Dapper.Extensions.DependencyInjection](https://www.nuget.org/packages/Activout.DatabaseClient.Dapper.Extensions.DependencyInjection) | 5.0.0-rc5 | Activout.DatabaseClient.Dappe… | Microsoft.Extensions.DependencyInjection extensions for Activout.DatabaseClient… |
| 2026-10-16 14:29:35 | [NWERP.ControleOperacional](https://www.nuget.org/packages/NWERP.ControleOperacional) | 1.0.1 | NWERP.ControleOperacional | Protocolo e admissão coordenada dos processos NWERP. |
| 2026-10-16 14:34:50 | [Engarde.Testing](https://www.nuget.org/packages/Engarde.Testing) | 1.0.0 | Artem Ovechko | Compile-time generated guard overrides for Engarde tests. |
| 2026-10-16 14:41:47 | [En-Garde](https://www.nuget.org/packages/En-Garde) | 1.0.0 | Artem Ovechko | En garde! Prepare your code to guard against unwanted access. Put feature toggl… |
| 2026-10-16 14:41:48 | [En-Garde.Testing](https://www.nuget.org/packages/En-Garde.Testing) | 1.0.0 | Artem Ovechko | Compile-time generated guard overrides for Engarde tests. |
| 2026-10-16 14:55:33 | [Aiursoft.NiBot.Archive](https://www.nuget.org/packages/Aiursoft.NiBot.Archive) | 10.0.1 | Aiursoft.NiBot.Archive | Incremental image archiving into existing visual categories. |
| 2026-10-16 15:09:45 | [BorrowedTorch.ECS](https://www.nuget.org/packages/BorrowedTorch.ECS) | 1.0.0 | Vladyslav Pysarenko | A small, dependency-free entity component system: generational entity handles,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-20 13:21 UTC

New packages created between 2026-10-20 12:22 UTC and 2026-10-20 13:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-20T13-21-42-687139Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-20 12:42:12 | [BorrowedTorch.Randomness](https://www.nuget.org/packages/BorrowedTorch.Randomness) | 1.1.0 | Borrowed Torch | Seeded random streams that give the same numbers on every platform and .NET ver… |
| 2026-10-20 13:03:51 | [EtAlii.Lark](https://www.nuget.org/packages/EtAlii.Lark) | 0.1.0 | Peter Vrenken | A full-featured port of the Lark parsing toolkit to .NET: Lark EBNF grammars, E… |
| 2026-10-20 13:05:37 | [ASEI.general-helpers](https://www.nuget.org/packages/ASEI.general-helpers) | 1.0.0 | ASEI | General helper library for Crestron SIMPL# and SIMPL# Pro control systems. Prov… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

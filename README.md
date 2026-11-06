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

## Latest list — 2026-11-06 04:19 UTC

New packages created between 2026-11-06 03:20 UTC and 2026-11-06 04:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-06T04-19-46-73551Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-06 03:58:50 | [Touchstone.Xunit2Adapter](https://www.nuget.org/packages/Touchstone.Xunit2Adapter) | 1.0.0 | jchristn | xUnit v2 adapter for Touchstone. Run shared test descriptors under xUnit 2.9 as… |
| 2026-11-06 03:58:51 | [Touchstone.Xunit3Adapter](https://www.nuget.org/packages/Touchstone.Xunit3Adapter) | 1.0.0 | jchristn | xUnit v3 adapter for Touchstone. Run shared test descriptors under xUnit v3 as… |
| 2026-11-06 04:03:37 | [Pacs.DangerWordMatching](https://www.nuget.org/packages/Pacs.DangerWordMatching) | 1.0.0 | LongHeng | 危险词多模式匹配（Aho-Corasick）与区间冲突消解。纯算法、零 UI 零 DB 依赖。 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

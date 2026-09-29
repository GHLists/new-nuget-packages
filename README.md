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

## Latest list — 2026-09-29 04:19 UTC

New packages created between 2026-09-29 03:20 UTC and 2026-09-29 04:19 UTC.

[Full CSV](data/new-nuget-packages-2026-09-29T04-19-15-05428Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-29 03:31:42 | [IIChartBasic](https://www.nuget.org/packages/IIChartBasic) | 1.1.0.1 | XuweiIntelligentTechnology | The basic edition provides only fundamental chart rendering. IIChartBasic is th… |
| 2026-09-29 03:31:49 | [siwooLib](https://www.nuget.org/packages/siwooLib) | 1.1.1 | siwoo | 시우의 강의용 라이브러리 |
| 2026-09-29 03:32:39 | [IIChartStandard](https://www.nuget.org/packages/IIChartStandard) | 1.1.0.1 | XuweiIntelligentTechnology | The standard edition adds visual style customization for charts on top of the b… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

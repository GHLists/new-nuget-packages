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

## Latest list — 2026-11-10 00:19 UTC

New packages created between 2026-11-09 23:19 UTC and 2026-11-10 00:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-10T00-19-27-632709Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-09 23:19:58 | [BorrowedTorch.Animations](https://www.nuget.org/packages/BorrowedTorch.Animations) | 1.0.0 | Vladyslav Pysarenko | Animations: a time line that runs once, loops, ping-pongs or accumulates, and k… |
| 2026-11-09 23:22:45 | [VitaliySimkin.TPlatform.Server.Testing](https://www.nuget.org/packages/VitaliySimkin.TPlatform.Server.Testing) | 1.3.0 | Vitaliy Simkin | Test kit for services built on T-Platform: platform data reset, user seeding an… |
| 2026-11-09 23:39:41 | [PocketCsvReader.Arrow.ColumnarJson](https://www.nuget.org/packages/PocketCsvReader.Arrow.ColumnarJson) | 2.67.0 | Cédric L. Charlier | Reads column-oriented JSON formats as Apache Arrow record batches. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

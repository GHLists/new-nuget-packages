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

## Latest list — 2026-09-28 21:22 UTC

New packages created between 2026-09-28 20:21 UTC and 2026-09-28 21:22 UTC.

[Full CSV](data/new-nuget-packages-2026-09-28T21-22-58-583893Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-28 20:27:09 | [TencentCloudSDKIntlEN.Alb](https://www.nuget.org/packages/TencentCloudSDKIntlEN.Alb) | 3.0.1402 | Tencent Cloud API Team | Tencent Cloud API 3.0 SDK for .NET |
| 2026-09-28 21:02:47 | [Kuestenlogik.Bowire.Protocol.Akka.Remote](https://www.nuget.org/packages/Kuestenlogik.Bowire.Protocol.Akka.Remote) | 1.1.0 | Kuestenlogik | Remote tap for the Bowire Akka.NET plugin: a relay the host opts into, reachabl… |
| 2026-09-28 21:10:52 | [SunamoPerformance](https://www.nuget.org/packages/SunamoPerformance) | 26.9.28.10 | www.sunamo.cz | Manual performance benchmarks for string replacing, file IO and string lookup s… |
| 2026-09-28 21:16:45 | [Epsilon](https://www.nuget.org/packages/Epsilon) | 1.0.0 | Max Zakharov | Symbolic math for .NET: parse formulas, simplify them exactly with rational ari… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

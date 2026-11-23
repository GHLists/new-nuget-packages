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

## Latest list — 2026-11-23 05:19 UTC

New packages created between 2026-11-23 04:21 UTC and 2026-11-23 05:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-23T05-19-03-825239Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-23 04:32:11 | [BehaviorLock](https://www.nuget.org/packages/BehaviorLock) | 0.2.0 | Vadim Albarov | Active security for ASP.NET Core APIs. Records what each endpoint touches and b… |
| 2026-11-23 05:00:30 | [ThinkGeo.Gpu.Native.iOS](https://www.nuget.org/packages/ThinkGeo.Gpu.Native.iOS) | 15.0.0 | ThinkGeo | Native library for ThinkGeo.Gpu on iOS: ANGLE, which runs the engine's OpenGL E… |
| 2026-11-23 05:01:06 | [ObisLaser.Net](https://www.nuget.org/packages/ObisLaser.Net) | 0.1.0 | Bruno F. Cruz | Client for Coherent OBIS LX/LS lasers over USB or RS-232 (unofficial, not affil… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

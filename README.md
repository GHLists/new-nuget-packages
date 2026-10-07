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

## Latest list — 2026-10-07 01:21 UTC

New packages created between 2026-10-07 00:20 UTC and 2026-10-07 01:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-07T01-21-18-093537Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-07 00:24:55 | [Troolio.Projection.Redis](https://www.nuget.org/packages/Troolio.Projection.Redis) | 10.0.2 | Fifty3North (F3N Limited) | Redis derived read models and partition change feeds for Troolio applications. |
| 2026-10-07 00:46:46 | [Ourogen.Templates](https://www.nuget.org/packages/Ourogen.Templates) | 0.0.1-alpha | Scott Sanderson | Package Description |
| 2026-10-07 00:57:03 | [Shiny.GameCenter](https://www.nuget.org/packages/Shiny.GameCenter) | 5.9.0-beta-0012 | Allan Ritchie | Shiny Game Center - achievements and leaderboards over Apple Game Center (iOS,… |
| 2026-10-07 01:08:35 | [ZeroBus.Core](https://www.nuget.org/packages/ZeroBus.Core) | 1.1.0 | Phong Võ | Pure C# Industrial Motion Fieldbus: Real-Time CAN / CANopen (CiA 301 & CiA 402… |
| 2026-10-07 01:08:40 | [ZeroMotion.Core](https://www.nuget.org/packages/ZeroMotion.Core) | 1.1.0 | Phong Võ | Pure C# Industrial Robotics Kinematics (6-Axis, SCARA, Delta, Cartesian), CCD &… |
| 2026-10-07 01:08:42 | [ZeroScan3D.Core](https://www.nuget.org/packages/ZeroScan3D.Core) | 1.0.0 | Phong Võ | Pure C# 3D spatial scanning, Visual SLAM, RGB-D point cloud unprojector, spatia… |
| 2026-10-07 01:09:36 | [Epiforge.Extensions.Blazor](https://www.nuget.org/packages/Epiforge.Extensions.Blazor) | 1.0.0 | Epiforge | This package re-renders Blazor components when the objects they read announce c… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

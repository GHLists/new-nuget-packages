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

## Latest list — 2026-11-27 01:21 UTC

New packages created between 2026-11-27 00:19 UTC and 2026-11-27 01:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-27T01-21-55-345694Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-27 00:21:05 | [NetOcc.runtime.linux-x64](https://www.nuget.org/packages/NetOcc.runtime.linux-x64) | 8.0.1.1 | Paul Büchner | Native libraries of NetOcc for linux-x64: the NetOcc libraries and OCCT 8.0.1 w… |
| 2026-11-27 00:21:07 | [NetOcc.runtime.osx-arm64](https://www.nuget.org/packages/NetOcc.runtime.osx-arm64) | 8.0.1.1 | Paul Büchner | Native libraries of NetOcc for osx-arm64: the NetOcc libraries and OCCT 8.0.1 w… |
| 2026-11-27 00:21:10 | [NetOcc.runtime.win-x64](https://www.nuget.org/packages/NetOcc.runtime.win-x64) | 8.0.1.1 | Paul Büchner | Native libraries of NetOcc for win-x64: the NetOcc libraries and OCCT 8.0.1 wit… |
| 2026-11-27 00:21:12 | [NetOcc.runtime.win-x86](https://www.nuget.org/packages/NetOcc.runtime.win-x86) | 8.0.1.1 | Paul Büchner | Native libraries of NetOcc for win-x86: the NetOcc libraries and OCCT 8.0.1 wit… |
| 2026-11-27 00:21:16 | [NetOcc](https://www.nuget.org/packages/NetOcc) | 8.0.1.1 | Paul Büchner | C# bindings for Open CASCADE Technology (OCCT) 8.0.1, with OCCT's names, one na… |
| 2026-11-27 00:21:22 | [NetOcc.Vtk.runtime.linux-x64](https://www.nuget.org/packages/NetOcc.Vtk.runtime.linux-x64) | 8.0.1.1 | Paul Büchner | Native libraries of NetOcc.Vtk for linux-x64: NetOccVtk and OCCT 8.0.1's TKIVtk… |
| 2026-11-27 00:21:23 | [NetOcc.Vtk.runtime.osx-arm64](https://www.nuget.org/packages/NetOcc.Vtk.runtime.osx-arm64) | 8.0.1.1 | Paul Büchner | Native libraries of NetOcc.Vtk for osx-arm64: NetOccVtk and OCCT 8.0.1's TKIVtk… |
| 2026-11-27 00:21:23 | [NetOcc.Vtk.runtime.win-x64](https://www.nuget.org/packages/NetOcc.Vtk.runtime.win-x64) | 8.0.1.1 | Paul Büchner | Native libraries of NetOcc.Vtk for win-x64: NetOccVtk and OCCT 8.0.1's TKIVtk.… |
| 2026-11-27 00:21:24 | [NetOcc.Vtk.runtime.win-x86](https://www.nuget.org/packages/NetOcc.Vtk.runtime.win-x86) | 8.0.1.1 | Paul Büchner | Native libraries of NetOcc.Vtk for win-x86: NetOccVtk and OCCT 8.0.1's TKIVtk.… |
| 2026-11-27 00:21:25 | [NetOcc.Vtk](https://www.nuget.org/packages/NetOcc.Vtk) | 8.0.1.1 | Paul Büchner | OCCT shapes in VTK scenes: C# bindings for Open CASCADE Technology's TKIVtk (IV… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

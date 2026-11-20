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

## Latest list — 2026-11-20 06:19 UTC

New packages created between 2026-11-20 05:22 UTC and 2026-11-20 06:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-20T06-19-22-012939Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-20 05:22:48 | [Devinno.UI.Scene3D](https://www.nuget.org/packages/Devinno.UI.Scene3D) | 0.8.0 | Devinno | 3D view for Devinno.UI: shows a glTF model and moves, colors and picks its part… |
| 2026-11-20 05:31:00 | [Zlink.Framework.Locations.Etcd](https://www.nuget.org/packages/Zlink.Framework.Locations.Etcd) | 0.33.0 | Zlink.Framework.Locations.Etcd | Official etcd Location Store provider for the ZLink .NET framework. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

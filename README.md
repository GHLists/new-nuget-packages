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

## Latest list — 2026-11-20 02:19 UTC

New packages created between 2026-11-20 01:20 UTC and 2026-11-20 02:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-20T02-19-09-500456Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-20 02:04:55 | [Antd.Wpf.Tokens](https://www.nuget.org/packages/Antd.Wpf.Tokens) | 1.0.0 | Antd.Wpf contributors | antd design tokens (seed to map to alias) ported to C#, with JavaScript-exact r… |
| 2026-11-20 02:05:04 | [Antd.Wpf.Theme](https://www.nuget.org/packages/Antd.Wpf.Theme) | 1.0.0 | Antd.Wpf contributors | Theme engine for Antd.Wpf: immutable token snapshots, frozen brushes and runtim… |
| 2026-11-20 02:05:08 | [Antd.Wpf.Icons](https://www.nuget.org/packages/Antd.Wpf.Icons) | 1.0.0 | Antd.Wpf contributors | 847 antd icons as lazily frozen WPF Geometry: outlined, filled and two-tone. |
| 2026-11-20 02:05:12 | [Antd.Wpf.Controls](https://www.nuget.org/packages/Antd.Wpf.Controls) | 1.0.0 | Antd.Wpf contributors | 69 Ant Design controls for WPF on net48 and net8-windows, token driven, no thir… |
| 2026-11-20 02:08:53 | [Johnwikix.ScottPlot.D3D12.WPF](https://www.nuget.org/packages/Johnwikix.ScottPlot.D3D12.WPF) | 5.1.60.4 | ScottPlot contributors | Complete ScottPlot WPF Figures rendered with hardware D3D12 through D3DImage, w… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

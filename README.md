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

## Latest list — 2026-10-25 07:20 UTC

New packages created between 2026-10-25 06:22 UTC and 2026-10-25 07:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-25T07-20-35-338889Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-25 06:33:31 | [Zoorce.Web.UI](https://www.nuget.org/packages/Zoorce.Web.UI) | 1.0.0 | Zoorce.Web.UI | Reusable Razor Pages web shell and UI components for ASP.NET Core applications. |
| 2026-10-25 06:33:32 | [Zoorce.Web.UI.Abstractions](https://www.nuget.org/packages/Zoorce.Web.UI.Abstractions) | 1.0.0 | Zoorce.Web.UI.Abstractions | Host-facing contracts for the Zoorce Razor Pages UI package. |
| 2026-10-25 06:33:33 | [Zoorce.Web.UI.Charts](https://www.nuget.org/packages/Zoorce.Web.UI.Charts) | 1.0.0 | Zoorce.Web.UI.Charts | Composable native-SVG charts for Zoorce web UI. |
| 2026-10-25 06:33:34 | [Zoorce.Web.UI.Data](https://www.nuget.org/packages/Zoorce.Web.UI.Data) | 1.0.0 | Zoorce.Web.UI.Data | Transport-neutral data lifecycle runtime for Zoorce web UI components. |
| 2026-10-25 06:33:35 | [Zoorce.Web.UI.DataGrid](https://www.nuget.org/packages/Zoorce.Web.UI.DataGrid) | 1.0.0 | Zoorce.Web.UI.DataGrid | Composable data grid components for Zoorce web UI. |
| 2026-10-25 06:33:36 | [Zoorce.Web.UI.Diagrams](https://www.nuget.org/packages/Zoorce.Web.UI.Diagrams) | 1.0.0 | Zoorce.Web.UI.Diagrams | Interactive, importable and exportable diagram components for Zoorce web UI. |
| 2026-10-25 06:33:37 | [Zoorce.Web.UI.Forms](https://www.nuget.org/packages/Zoorce.Web.UI.Forms) | 1.0.0 | Zoorce.Web.UI.Forms | Reusable and independently configurable form controls for Zoorce web UI. |
| 2026-10-25 06:33:38 | [Zoorce.Web.UI.Layout](https://www.nuget.org/packages/Zoorce.Web.UI.Layout) | 1.0.0 | Zoorce.Web.UI.Layout | Reusable application shell and layout components for Zoorce web UI. |
| 2026-10-25 06:33:38 | [Zoorce.Web.UI.Foundation](https://www.nuget.org/packages/Zoorce.Web.UI.Foundation) | 1.0.0 | Zoorce.Web.UI.Foundation | Reusable visual primitives and asynchronous feedback components for Zoorce web… |
| 2026-10-25 06:33:39 | [Zoorce.Web.UI.Navigation](https://www.nuget.org/packages/Zoorce.Web.UI.Navigation) | 1.0.0 | Zoorce.Web.UI.Navigation | Navigation and workflow progression components for Zoorce web UI. |
| 2026-10-25 06:33:40 | [Zoorce.Web.UI.Realtime.SignalR](https://www.nuget.org/packages/Zoorce.Web.UI.Realtime.SignalR) | 1.0.0 | Zoorce.Web.UI.Realtime.SignalR | Optional SignalR adapter for transport-neutral Zoorce data invalidations. |
| 2026-10-25 06:33:41 | [Zoorce.Web.UI.Theming](https://www.nuget.org/packages/Zoorce.Web.UI.Theming) | 1.0.0 | Zoorce.Web.UI.Theming | Dynamic semantic theming runtime for Zoorce web UI components. |
| 2026-10-25 06:33:42 | [Zoorce.Web.UI.Timelines](https://www.nuget.org/packages/Zoorce.Web.UI.Timelines) | 1.0.0 | Zoorce.Web.UI.Timelines | Composable, data-aware timeline components for Zoorce web UI. |
| 2026-10-25 06:56:32 | [Alexpivo394.Revit.ParamCheck](https://www.nuget.org/packages/Alexpivo394.Revit.ParamCheck) | 2027.1.0 | Alexpivo394 | UI-free Revit parameter fill (LOI) check: detached opening, rule-based element… |
| 2026-10-25 06:56:39 | [Alexpivo394.Revit.ParamCheck.Profiles](https://www.nuget.org/packages/Alexpivo394.Revit.ParamCheck.Profiles) | 1.0.0 | Alexpivo394 | ParamChecker profiles without the Revit API: check rules, JSON format of the Pa… |
| 2026-10-25 07:04:04 | [Simorgh.AI.Abstractions](https://www.nuget.org/packages/Simorgh.AI.Abstractions) | 0.1.0 | Simorgh AI Contributors | Public contracts and shared types for the Simorgh.AI framework. |
| 2026-10-25 07:04:05 | [Simorgh.AI.Core](https://www.nuget.org/packages/Simorgh.AI.Core) | 0.1.0 | Simorgh AI Contributors | Core runtime and orchestration components for the Simorgh.AI framework. |
| 2026-10-25 07:04:05 | [Simorgh.AI.Extensions](https://www.nuget.org/packages/Simorgh.AI.Extensions) | 0.1.0 | Simorgh AI Contributors | Built-in extensions for the Simorgh.AI framework, such as ready-made tool-calli… |
| 2026-10-25 07:04:06 | [Simorgh.AI.Integrations](https://www.nuget.org/packages/Simorgh.AI.Integrations) | 0.1.0 | Simorgh AI Contributors | Provider and service integrations for the Simorgh.AI framework. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

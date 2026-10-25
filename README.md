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

## Latest list — 2026-10-25 11:21 UTC

New packages created between 2026-10-25 10:19 UTC and 2026-10-25 11:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-25T11-21-20-173015Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-25 10:21:24 | [Plover.Protocol](https://www.nuget.org/packages/Plover.Protocol) | 1.0.0 | Bas Mulder | Package Description |
| 2026-10-25 10:21:24 | [Plover.Client](https://www.nuget.org/packages/Plover.Client) | 1.0.0 | Bas Mulder | Package Description |
| 2026-10-25 10:38:45 | [Proteus.Tui](https://www.nuget.org/packages/Proteus.Tui) | 0.1.0 | Przemyslaw Rachwal | Fast ANSI/VT terminal renderer for .NET: frame buffer, cell-level diff renderer… |
| 2026-10-25 10:38:46 | [Proteus.Tui.Testing](https://www.nuget.org/packages/Proteus.Tui.Testing) | 0.1.0 | Przemyslaw Rachwal | Headless testing pilot for Proteus.Tui: drive controls with keys, mouse and res… |
| 2026-10-25 10:38:46 | [Proteus.Tui.Mvvm](https://www.nuget.org/packages/Proteus.Tui.Mvvm) | 0.1.0 | Przemyslaw Rachwal | Minimal MVVM helpers for Proteus.Tui: ViewModelBase (INotifyPropertyChanged) an… |
| 2026-10-25 10:38:47 | [Proteus.Tui.Controls](https://www.nuget.org/packages/Proteus.Tui.Controls) | 0.1.0 | Przemyslaw Rachwal | Retained-mode TUI controls for .NET: window, layouts (stack, grid, dock), butto… |
| 2026-10-25 10:38:48 | [Proteus.Tui.Abstractions](https://www.nuget.org/packages/Proteus.Tui.Abstractions) | 0.1.0 | Przemyslaw Rachwal | Core abstractions for Proteus.Tui: terminal and frame-buffer interfaces, cells,… |
| 2026-10-25 10:51:38 | [Kinetix.Services.DependencyInjection](https://www.nuget.org/packages/Kinetix.Services.DependencyInjection) | 10.1.0 | JabX | Injection de dépendances avec interception pour Kinetix. |
| 2026-10-25 10:52:31 | [RabbitMcp.Contracts](https://www.nuget.org/packages/RabbitMcp.Contracts) | 1.0.0 | lazogio | [MessageContract] attribute for rabbit-mcp contract assemblies: every contract… |
| 2026-10-25 10:52:31 | [RabbitMcp.Server](https://www.nuget.org/packages/RabbitMcp.Server) | 1.0.0 | lazogio | Contract-first MCP server for RabbitMQ: one typed tool per message contract (Ma… |
| 2026-10-25 10:56:16 | [JavaScriptEventRegistrationAuditor](https://www.nuget.org/packages/JavaScriptEventRegistrationAuditor) | 1.2026.10.1 | Gagan Deep Singh | XrmToolBox plugin that audits JavaScript form event registrations in Microsoft… |
| 2026-10-25 11:01:10 | [DimensionalQuantities.Extensions.Imperial](https://www.nuget.org/packages/DimensionalQuantities.Extensions.Imperial) | 2.0.0 | GoSim | Named Imperial and US customary conversions for dimensional quantities. |
| 2026-10-25 11:01:11 | [DimensionalQuantities.Extensions.CgsEmag](https://www.nuget.org/packages/DimensionalQuantities.Extensions.CgsEmag) | 2.0.0 | GoSim | Named CGS electromagnetic and mechanical conversions for dimensional quantities. |
| 2026-10-25 11:01:12 | [DimensionalQuantities.Extensions.Nautical](https://www.nuget.org/packages/DimensionalQuantities.Extensions.Nautical) | 2.0.0 | GoSim | Named nautical conversions for dimensional quantities. |
| 2026-10-25 11:01:13 | [DimensionalQuantities.Extensions.Metric](https://www.nuget.org/packages/DimensionalQuantities.Extensions.Metric) | 2.0.0 | GoSim | Named metric conversions for dimensional quantities. |
| 2026-10-25 11:11:43 | [DrewSoft.Collections](https://www.nuget.org/packages/DrewSoft.Collections) | 1.0.0 | DrewSoft | A bucketed priority queue collection for .NET. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-27 19:21 UTC

New packages created between 2026-10-27 18:20 UTC and 2026-10-27 19:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-27T19-21-01-935317Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-27 18:21:39 | [Caladesi.Sdk](https://www.nuget.org/packages/Caladesi.Sdk) | 1.0.0 | Caladesi contributors | MSBuild SDK for the Caladesi language (.calaproj). Includes the calac compiler. |
| 2026-10-27 18:21:40 | [Caladesi.Runtime](https://www.nuget.org/packages/Caladesi.Runtime) | 1.0.0 | Caladesi contributors | Runtime support library for assemblies produced by the Caladesi compiler. |
| 2026-10-27 18:21:41 | [Caladesi.Templates](https://www.nuget.org/packages/Caladesi.Templates) | 1.0.0 | Caladesi contributors | Project templates for the Caladesi language (calaconsole, calalib, calatest). |
| 2026-10-27 18:25:43 | [Paintty](https://www.nuget.org/packages/Paintty) | 1.0.0 | Tom Laird-McConnell | A paint program for the terminal, in the spirit of Paint and Paint.NET. |
| 2026-10-27 18:32:25 | [Octeka.UI.Wpf.PropertyGrid](https://www.nuget.org/packages/Octeka.UI.Wpf.PropertyGrid) | 1.0.0 | Patrick Robichaud | Enterprise-grade, high-performance WPF property grid control powered by Octeka.… |
| 2026-10-27 18:32:26 | [Octeka.UI.Wpf.PropertyGrid.Abstractions](https://www.nuget.org/packages/Octeka.UI.Wpf.PropertyGrid.Abstractions) | 1.0.0 | Patrick Robichaud | Core abstractions, interfaces, descriptors, and attributes for the Octeka WPF P… |
| 2026-10-27 18:32:26 | [Octeka.UI.Wpf.PropertyGrid.Editors.Advanced](https://www.nuget.org/packages/Octeka.UI.Wpf.PropertyGrid.Editors.Advanced) | 1.0.0 | Patrick Robichaud | Advanced modal and popup editors for the Octeka WPF PropertyGrid suite, includi… |
| 2026-10-27 18:45:59 | [RecursiveAI.OneEcma.Cli](https://www.nuget.org/packages/RecursiveAI.OneEcma.Cli) | 1.0.0 | Recursive AI, LLC | The oneecma command-line tool: run, repl and check. |
| 2026-10-27 18:46:00 | [RecursiveAI.OneEcma.Generators](https://www.nuget.org/packages/RecursiveAI.OneEcma.Generators) | 1.0.0 | Recursive AI, LLC | Source generator that writes .NET host bindings for the OneEcma interpreter. |
| 2026-10-27 18:46:01 | [RecursiveAI.OneEcma](https://www.nuget.org/packages/RecursiveAI.OneEcma) | 1.0.0 | Recursive AI, LLC | An interpreter for .NET implementing ECMA-262 / ECMAScript®, whose product is i… |
| 2026-10-27 18:46:56 | [squalor.squalify](https://www.nuget.org/packages/squalor.squalify) | 0.1.0 | Jon Robbins | Profiles one data file into a deterministic JSON descriptor: encoding, format,… |
| 2026-10-27 18:46:58 | [squalor.squalify.Cli](https://www.nuget.org/packages/squalor.squalify.Cli) | 0.1.0 | Jon Robbins | Command-line tool that profiles a data file into a deterministic JSON descripto… |
| 2026-10-27 18:56:08 | [CompuMaster.Dms.BrowserUI.WinUI](https://www.nuget.org/packages/CompuMaster.Dms.BrowserUI.WinUI) | 2026.10.27.1 | Jochen Wezel | Native WinUI 3 DMS browser controls and dialogs for Windows, including selectio… |
| 2026-10-27 18:57:16 | [Render.NET.Tgs](https://www.nuget.org/packages/Render.NET.Tgs) | 0.3.16 | Vadim Belov | Managed selected-frame rendering of Telegram TGS and Lottie animations to PNG u… |
| 2026-10-27 18:57:17 | [Render.NET.Svg](https://www.nuget.org/packages/Render.NET.Svg) | 0.3.16 | Vadim Belov | Managed SVG vector rendering to RGBA and PNG using the Render.NET raster canvas… |
| 2026-10-27 19:01:45 | [Octeka.UI.Wpf.DockingManager](https://www.nuget.org/packages/Octeka.UI.Wpf.DockingManager) | 1.0.0 | Patrick Robichaud | Visual Studio-grade docking manager control for WPF applications. |
| 2026-10-27 19:01:46 | [Octeka.UI.Wpf.DockingManager.Sample](https://www.nuget.org/packages/Octeka.UI.Wpf.DockingManager.Sample) | 1.0.0 | Patrick Robichaud | Package Description |
| 2026-10-27 19:11:49 | [Fnode.Core](https://www.nuget.org/packages/Fnode.Core) | 0.1.0 | Devon Burriss | Shared document core: the Node tree, JSON Pointer paths, errors with source loc… |
| 2026-10-27 19:11:50 | [Fnode.Json](https://www.nuget.org/packages/Fnode.Json) | 0.1.0 | Devon Burriss | JSON adapter for Fnode: parses JSON text to a Node with source locations and pr… |
| 2026-10-27 19:11:51 | [Fnode.Yaml](https://www.nuget.org/packages/Fnode.Yaml) | 0.1.0 | Devon Burriss | YAML adapter for Fnode: parses YAML text to a Node with source locations and th… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

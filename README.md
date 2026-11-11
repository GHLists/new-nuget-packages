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

## Latest list — 2026-11-11 14:21 UTC

New packages created between 2026-11-11 13:21 UTC and 2026-11-11 14:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-11T14-21-19-875749Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-11 13:21:36 | [Arc56.Generated.daemonmarlik.CertiChain](https://www.nuget.org/packages/Arc56.Generated.daemonmarlik.CertiChain) | 1.0.1.2026111113 | daemonmarlik | Generated ARC-56 Algorand smart-contract clients for daemonmarlik/CertiChain. |
| 2026-11-11 13:21:51 | [Arc56.Generated.d13co.algod-mesh](https://www.nuget.org/packages/Arc56.Generated.d13co.algod-mesh) | 1.0.1.2026111113 | d13co | Generated ARC-56 Algorand smart-contract clients for d13co/algod-mesh. |
| 2026-11-11 13:37:16 | [MasterUI.WinForms.Common](https://www.nuget.org/packages/MasterUI.WinForms.Common) | 1.0.0 | MasterUI | MasterUI 配套的纯逻辑工具：表格文本（TSV）解析、CSV 写出、轻量 xlsx 写出。 |
| 2026-11-11 13:37:25 | [DotNop.Channels.Redis](https://www.nuget.org/packages/DotNop.Channels.Redis) | 1.0.20-preview | Andrii Kurochka | System.Threading.Channels implementation backed by Redis. |
| 2026-11-11 13:37:27 | [MasterUI.WinForms](https://www.nuget.org/packages/MasterUI.WinForms) | 1.0.0 | MasterUI | 面向 WinForms 业务系统的现代化扁平控件库，支持多主题与高 DPI。 |
| 2026-11-11 13:37:50 | [Meziantou.Framework.Pdf.VectorGraphics](https://www.nuget.org/packages/Meziantou.Framework.Pdf.VectorGraphics) | 1.0.0 | meziantou | Draws the scenes of Meziantou.Framework.VectorGraphics (charts, diagrams) as PD… |
| 2026-11-11 13:39:20 | [LibMentor](https://www.nuget.org/packages/LibMentor) | 0.1.0 | Florian Gilde | Generate versioned AI documentation, API references and agent skills from your… |
| 2026-11-11 13:43:17 | [AppMare.MauiWeb.Controls](https://www.nuget.org/packages/AppMare.MauiWeb.Controls) | 1.0.4 | AppMare | Web-specific platform configuration for MauiWeb apps: tab bar placement, the de… |
| 2026-11-11 13:43:24 | [AppMare.MauiWeb.Toolkit](https://www.nuget.org/packages/AppMare.MauiWeb.Toolkit) | 1.0.4 | AppMare | .NET MAUI Community Toolkit support for MauiWeb (behaviors, Snackbar, Toast, Me… |
| 2026-11-11 13:43:26 | [AppMare.MauiWeb.SkiaSharp](https://www.nuget.org/packages/AppMare.MauiWeb.SkiaSharp) | 1.0.4 | AppMare | SkiaSharp support for MauiWeb: SKCanvasView and custom drawing rendered on the… |
| 2026-11-11 13:43:29 | [AppMare.MauiWeb.Mopups](https://www.nuget.org/packages/AppMare.MauiWeb.Mopups) | 1.0.4 | AppMare | Web support for Mopups, not a new popup library: your existing Mopups code (Pop… |
| 2026-11-11 13:43:31 | [AppMare.MauiWeb.FFImageLoading](https://www.nuget.org/packages/AppMare.MauiWeb.FFImageLoading) | 1.0.4 | AppMare | Web support for FFImageLoading.Maui, not a new image library: your existing Cac… |
| 2026-11-11 13:43:32 | [AppMare.MauiWeb.Audio](https://www.nuget.org/packages/AppMare.MauiWeb.Audio) | 1.0.4 | AppMare | Web support for Plugin.Maui.Audio, not a new audio library: your existing Plugi… |
| 2026-11-11 13:44:34 | [Damianh.NuGetOrgManage](https://www.nuget.org/packages/Damianh.NuGetOrgManage) | 1.0.0 | Damian Hickey,Thomas Galliker | Utilities for managing NuGet.org packages. |
| 2026-11-11 13:46:25 | [Solurum.Stride.VisualStudioTemplates](https://www.nuget.org/packages/Solurum.Stride.VisualStudioTemplates) | 1.0.0 | Solurum | Visual Studio and dotnet CLI templates for code-only Stride games. |
| 2026-11-11 13:47:56 | [HoneyDrunk.Agents](https://www.nuget.org/packages/HoneyDrunk.Agents) | 0.1.0 | HoneyDrunk Studios | Runtime for HoneyDrunk Grid agents: an in-process lifecycle, tool invocation th… |
| 2026-11-11 13:47:59 | [HoneyDrunk.Agents.Testing](https://www.nuget.org/packages/HoneyDrunk.Agents.Testing) | 0.1.0 | HoneyDrunk Studios | Test fixtures for HoneyDrunk Grid agents: a harness over the real runtime with… |
| 2026-11-11 13:48:33 | [HoneyDrunk.Operator.Data](https://www.nuget.org/packages/HoneyDrunk.Operator.Data) | 0.2.0 | HoneyDrunk Studios | Durable storage for HoneyDrunk.Operator over HoneyDrunk.Data's Entity Framework… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

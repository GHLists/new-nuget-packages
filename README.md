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

## Latest list — 2026-10-07 06:21 UTC

New packages created between 2026-10-07 05:19 UTC and 2026-10-07 06:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-07T06-21-54-944316Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-07 05:25:09 | [ComponentSpace.Saml2.Net.Extension.Database](https://www.nuget.org/packages/ComponentSpace.Saml2.Net.Extension.Database) | 1.0.0 | ComponentSpace | Adds support for storing SAML session state in a database. Production use requi… |
| 2026-10-07 05:28:51 | [EGO.Nimozyn](https://www.nuget.org/packages/EGO.Nimozyn) | 0.1.6-alpha | EGO.Nimozyn | Package Description |
| 2026-10-07 05:29:57 | [SheetizeMCPServer](https://www.nuget.org/packages/SheetizeMCPServer) | 26.9.0-beta | Smallize | An MCP server using the MCP C# SDK. |
| 2026-10-07 06:03:27 | [StanzaSharp.Tool](https://www.nuget.org/packages/StanzaSharp.Tool) | 0.4.0 | Jakob Boman | The stanzasharp command: downloads Stanza's English models for StanzaSharp, che… |
| 2026-10-07 06:07:32 | [SentenceTransformers.EmbeddingGemma2](https://www.nuget.org/packages/SentenceTransformers.EmbeddingGemma2) | 26.10.6445 | Curiosity GmbH | A 100% managed, dependency-free (no LiteRT / TFLite runtime, no native tokenize… |
| 2026-10-07 06:10:18 | [Deskling.Core](https://www.nuget.org/packages/Deskling.Core) | 0.1.1 | Vlad Mihalachi | Pure building blocks for little desktop apps: an interval scheduler with active… |
| 2026-10-07 06:10:19 | [Deskling.Windows](https://www.nuget.org/packages/Deskling.Windows) | 0.1.1 | Vlad Mihalachi | Windows services for little tray apps: a raw Shell_NotifyIcon tray icon host wi… |
| 2026-10-07 06:12:35 | [Mori.SkyScope.Blazor](https://www.nuget.org/packages/Mori.SkyScope.Blazor) | 0.1.0 | Cristian Mori | Blazor components for Mori.SkyScope (TrendChart, Gauge, Chart, SceneView) with… |
| 2026-10-07 06:12:35 | [Mori.SkyScope.Core](https://www.nuget.org/packages/Mori.SkyScope.Core) | 0.1.0 | Cristian Mori | Headless engine for Mori.SkyScope: ring buffers, M4 decimation, SkyScopeFrame c… |
| 2026-10-07 06:12:36 | [Mori.SkyScope.Render.OpenTK](https://www.nuget.org/packages/Mori.SkyScope.Render.OpenTK) | 0.1.0 | Cristian Mori | OpenGL (OpenTK) 3D painter for Mori.SkyScope: GlPainter3D implements IPainter3D… |
| 2026-10-07 06:12:36 | [Mori.SkyScope.Render.Skia](https://www.nuget.org/packages/Mori.SkyScope.Render.Skia) | 0.1.0 | Cristian Mori | SkiaSharp painter for Mori.SkyScope (desktop rendering, offscreen snapshots). |
| 2026-10-07 06:12:37 | [Mori.SkyScope.Sources.Mqtt](https://www.nuget.org/packages/Mori.SkyScope.Sources.Mqtt) | 0.1.0 | Cristian Mori | MQTT source plugin for Mori.SkyScope: topic filters with JSON-path extraction i… |
| 2026-10-07 06:12:37 | [Mori.SkyScope.Sources.Ros2](https://www.nuget.org/packages/Mori.SkyScope.Sources.Ros2) | 0.1.0 | Cristian Mori | ROS 2 source plugin for Mori.SkyScope: subscribes to topics through Mori.Ros2Sh… |
| 2026-10-07 06:12:38 | [Mori.SkyScope.Streaming](https://www.nuget.org/packages/Mori.SkyScope.Streaming) | 0.1.0 | Cristian Mori | ASP.NET Core WebSocket broadcaster for Mori.SkyScope frames and scene layers. |
| 2026-10-07 06:12:38 | [Mori.SkyScope.WinForms](https://www.nuget.org/packages/Mori.SkyScope.WinForms) | 0.1.0 | Cristian Mori | Windows Forms controls for Mori.SkyScope: TrendChartControl with designer prope… |
| 2026-10-07 06:12:39 | [Mori.SkyScope.Wpf](https://www.nuget.org/packages/Mori.SkyScope.Wpf) | 0.1.0 | Cristian Mori | WPF controls for Mori.SkyScope: TrendChartControl, GaugeControl, ChartControl,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

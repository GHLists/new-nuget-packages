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

## Latest list — 2026-10-14 13:20 UTC

New packages created between 2026-10-14 12:20 UTC and 2026-10-14 13:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-14T13-20-43-548061Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-14 12:21:11 | [Fluently.Core](https://www.nuget.org/packages/Fluently.Core) | 0.1.0 | taner04 | Async, view-model-first navigation with back and forward history and rollback o… |
| 2026-10-14 12:23:30 | [TheBuilder.ApiOidc](https://www.nuget.org/packages/TheBuilder.ApiOidc) | 0.2.0 | Daniel Schmidt | Let Vercel, GitHub Actions and other workloads call the Umbraco Delivery API an… |
| 2026-10-14 12:25:03 | [Plan9.Utf](https://www.nuget.org/packages/Plan9.Utf) | 0.1.0 | Scott J Guyton | 9front's UTF-8: libc's rune and utf functions, and a System.Text.Encoding that… |
| 2026-10-14 12:26:50 | [DemaConsulting.DocDown.PowerPoint.Rendering](https://www.nuget.org/packages/DemaConsulting.DocDown.PowerPoint.Rendering) | 0.2.0 | DEMA Consulting | Optional PowerPoint slide rendering (rasterization) for DEMA Consulting DocDown |
| 2026-10-14 12:26:53 | [DemaConsulting.DocDown.Visio.Rendering](https://www.nuget.org/packages/DemaConsulting.DocDown.Visio.Rendering) | 0.2.0 | DEMA Consulting | Optional Visio page rendering (rasterization) for DEMA Consulting DocDown |
| 2026-10-14 12:37:46 | [Dagger.Analyzers](https://www.nuget.org/packages/Dagger.Analyzers) | 0.1.0 | Dagger contributors | Shared C# analyzers and editorconfig. Enables the SDK recommended rules and bun… |
| 2026-10-14 12:38:52 | [DamianH.Http.ForwardedHeaders](https://www.nuget.org/packages/DamianH.Http.ForwardedHeaders) | 0.1.0 | Damian Hickey | RFC 7239 Forwarded header parsing and trusted-proxy middleware for ASP.NET Core. |
| 2026-10-14 12:40:50 | [Bibui.Raster.Skia](https://www.nuget.org/packages/Bibui.Raster.Skia) | 0.9.0 | Navisurg ApS | Bibui's SkiaSharp raster backend. Referencing it makes Skia the default for new… |
| 2026-10-14 12:40:50 | [Bibui.Platform.Silk](https://www.nuget.org/packages/Bibui.Platform.Silk) | 0.9.0 | Navisurg ApS | Bibui cross-platform window host: GLFW + OpenGL through Silk.NET, clipboard thr… |
| 2026-10-14 12:40:51 | [Bibui.Raster.Managed.Backend](https://www.nuget.org/packages/Bibui.Raster.Managed.Backend) | 0.9.0 | Navisurg ApS | bibui's IRasterBackend on the managed rasterizer, with text from Bibui.Text.Fre… |
| 2026-10-14 12:40:51 | [Bibui](https://www.nuget.org/packages/Bibui) | 0.9.0 | Navisurg ApS | Bibui, a code-first native UI library: nodes, layout, the painter and BibuiRend… |
| 2026-10-14 12:40:51 | [Bibui.Raster.Managed](https://www.nuget.org/packages/Bibui.Raster.Managed) | 0.9.0 | Navisurg ApS | A deterministic managed CPU rasterizer for bibui: analytic-coverage path fill,… |
| 2026-10-14 12:40:51 | [Bibui.Platform.Wayland](https://www.nuget.org/packages/Bibui.Platform.Wayland) | 0.9.0 | Navisurg ApS | Bibui window host for Wayland compositors: xdg-shell toplevel, wl_shm buffers,… |
| 2026-10-14 12:40:52 | [Bibui.Text.FreeType](https://www.nuget.org/packages/Bibui.Text.FreeType) | 0.9.0 | Navisurg ApS | bibui text on the system FreeType and HarfBuzz: shaping, exact subpixel measuri… |
| 2026-10-14 12:40:52 | [Bibui.Testing](https://www.nuget.org/packages/Bibui.Testing) | 0.9.0 | Navisurg ApS | Playwright-style semantic testing API for Bibui apps. Provides BibuiPage and IB… |
| 2026-10-14 12:48:11 | [A2A.Grpc](https://www.nuget.org/packages/A2A.Grpc) | 1.0.0-preview3 | Community Contributors | gRPC client and protocol mapping for the Agent2Agent (A2A) protocol. |
| 2026-10-14 12:48:11 | [A2A.Grpc.AspNetCore](https://www.nuget.org/packages/A2A.Grpc.AspNetCore) | 1.0.0-preview3 | Community Contributors | ASP.NET Core gRPC server host for the Agent2Agent (A2A) protocol. |
| 2026-10-14 12:49:30 | [XiaQue.QQBot.Connector](https://www.nuget.org/packages/XiaQue.QQBot.Connector) | 1.0.0 | XiaQue | Unofficial .NET QR connector for QQ Bot agent onboarding. |
| 2026-10-14 13:00:04 | [HostLoom.NodeLeasing](https://www.nuget.org/packages/HostLoom.NodeLeasing) | 0.16.0 | Aleksandr Pavlov | Lease-based node-ID leasing for HostLoom over the distributed lock: one elector… |
| 2026-10-14 13:00:05 | [HostLoom.NodeLeasing.DependencyInjection](https://www.nuget.org/packages/HostLoom.NodeLeasing.DependencyInjection) | 0.16.0 | Aleksandr Pavlov | Microsoft.Extensions.DependencyInjection registration, keyed pools, options val… |
| 2026-10-14 13:00:06 | [HostLoom.NodeLeasing.Testing](https://www.nuget.org/packages/HostLoom.NodeLeasing.Testing) | 0.16.0 | Aleksandr Pavlov | A scripted INodeLeasing for testing node-ID consumers of HostLoom without an el… |
| 2026-10-14 13:04:09 | [EingabeAussen](https://www.nuget.org/packages/EingabeAussen) | 1.0.0 | Sandra Gangelmaier | EingabeAussen: ASP.NET Core MVC Projektvorlage (Einträge, Kategorien, Eintragst… |
| 2026-10-14 13:06:48 | [Umbraco.Community.SearchManager.UmbracoSearch](https://www.nuget.org/packages/Umbraco.Community.SearchManager.UmbracoSearch) | 17.0.0 | Jack Stunell | Adds Umbraco Search indexes to Umbraco Search Manager. Install it on sites that… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

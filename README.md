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

## Latest list — 2026-11-05 02:18 UTC

New packages created between 2026-11-05 01:19 UTC and 2026-11-05 02:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-05T02-18-23-803909Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-05 01:26:19 | [Dotwire.Host](https://www.nuget.org/packages/Dotwire.Host) | 0.2.0 | Dotwire | Host-side .NET SDK for dotwire: mints RS256 tokens with the host's own key and… |
| 2026-11-05 01:28:47 | [NHibernate.UserTypes.NodaTime](https://www.nuget.org/packages/NHibernate.UserTypes.NodaTime) | 0.1.0 | Jacob Mojiwat | NHibernate custom user types and mapping helpers for NodaTime types. |
| 2026-11-05 01:56:21 | [Tamp.Migrate](https://www.nuget.org/packages/Tamp.Migrate) | 1.19.0 | Scott Singleton | Preview. Migrates a NUKE 8+ build to Tamp (ADR 0021); run it as `tamp migrate n… |
| 2026-11-05 02:00:23 | [Mediana.Documents.Word](https://www.nuget.org/packages/Mediana.Documents.Word) | 0.1.17 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-05 02:00:30 | [Mediana.Documents.OpenXml](https://www.nuget.org/packages/Mediana.Documents.OpenXml) | 0.1.17 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-05 02:04:10 | [Kazo.Os.App.Abstractions](https://www.nuget.org/packages/Kazo.Os.App.Abstractions) | 3.0.0 | Benoit Robin | Kazo OS App SDK contracts: AppDefinition and [AppManifest], the schema-v1 app m… |
| 2026-11-05 02:04:12 | [Kazo.Os.App.Build](https://www.nuget.org/packages/Kazo.Os.App.Build) | 3.0.0 | Benoit Robin | Build integration of Kazo OS apps: generated manifest.json, SDK boundary checks… |
| 2026-11-05 02:04:13 | [Kazo.Os.AppSdk](https://www.nuget.org/packages/Kazo.Os.AppSdk) | 3.0.0 | Benoit Robin | Kazo OS App SDK: the Kazo* APIs an app uses (KazoFile, KazoStream, KazoDirector… |
| 2026-11-05 02:04:14 | [Kazo.Os.AppSdk.Blazor](https://www.nuget.org/packages/Kazo.Os.AppSdk.Blazor) | 3.0.0 | Benoit Robin | Kazo OS App SDK for window apps: KazoComponentBase, window base classes, dialog… |
| 2026-11-05 02:04:16 | [Kazo.Os.AppSdk.Icons](https://www.nuget.org/packages/Kazo.Os.AppSdk.Icons) | 3.0.0 | Benoit Robin | Framework-independent icon catalog and native Blazor SVG renderer used by Kazo… |
| 2026-11-05 02:04:18 | [Kazo.Os.AppSdk.Terminal](https://www.nuget.org/packages/Kazo.Os.AppSdk.Terminal) | 3.0.0 | Benoit Robin | Kazo OS App SDK for terminal commands and the embeddable terminal contract (IKa… |
| 2026-11-05 02:04:19 | [Kazo.Os.AppSdk.VirtualKeyboard](https://www.nuget.org/packages/Kazo.Os.AppSdk.VirtualKeyboard) | 3.0.0 | Benoit Robin | A reusable, host-agnostic on-screen keyboard and a keyboard-aware split contain… |
| 2026-11-05 02:04:21 | [Kazo.Os.AppSdk.Web](https://www.nuget.org/packages/Kazo.Os.AppSdk.Web) | 3.0.0 | Benoit Robin | ASP.Kazo: MVC-like web sites hosted inside Kazo OS (controllers, routing, model… |
| 2026-11-05 02:04:22 | [Kazo.Os.AppSdk.Web.Blazor](https://www.nuget.org/packages/Kazo.Os.AppSdk.Web.Blazor) | 3.0.0 | Benoit Robin | Interactive Blazor sites of ASP.Kazo: site router, navigation and the view the… |
| 2026-11-05 02:04:23 | [Kazo.Os.Apps.Browser](https://www.nuget.org/packages/Kazo.Os.Apps.Browser) | 3.0.0 | Benoit Robin | The base Kazo OS web browser app, to include in an OS host (ProjectReference or… |
| 2026-11-05 02:04:24 | [Kazo.Os.Apps.Calculator](https://www.nuget.org/packages/Kazo.Os.Apps.Calculator) | 3.0.0 | Benoit Robin | The base Kazo OS calculator app, to include in an OS host (ProjectReference or… |
| 2026-11-05 02:04:26 | [Kazo.Os.Apps.CodeEditor](https://www.nuget.org/packages/Kazo.Os.Apps.CodeEditor) | 3.0.0 | Benoit Robin | The base Kazo OS code editor workbench app, to include in an OS host (ProjectRe… |
| 2026-11-05 02:04:27 | [Kazo.Os.Apps.Desktop](https://www.nuget.org/packages/Kazo.Os.Apps.Desktop) | 3.0.0 | Benoit Robin | The Kazo OS desktop: the icons of ~/Desktop, Home and Trash, drawn by the shell… |
| 2026-11-05 02:04:29 | [Kazo.Os.Apps.Diagnostic](https://www.nuget.org/packages/Kazo.Os.Apps.Diagnostic) | 3.0.0 | Benoit Robin | The base Kazo OS diagnostic tool app, to include in an OS host (ProjectReferenc… |
| 2026-11-05 02:04:30 | [Kazo.Os.Apps.ErrorLogViewer](https://www.nuget.org/packages/Kazo.Os.Apps.ErrorLogViewer) | 3.0.0 | Benoit Robin | The base Kazo OS log viewer app, to include in an OS host (ProjectReference or… |
| 2026-11-05 02:04:31 | [Kazo.Os.Apps.FileExplorer](https://www.nuget.org/packages/Kazo.Os.Apps.FileExplorer) | 3.0.0 | Benoit Robin | The base Kazo OS file explorer app, to include in an OS host (ProjectReference… |
| 2026-11-05 02:04:33 | [Kazo.Os.Apps.IconViewer](https://www.nuget.org/packages/Kazo.Os.Apps.IconViewer) | 3.0.0 | Benoit Robin | The base Kazo OS icon viewer app, to include in an OS host (ProjectReference or… |
| 2026-11-05 02:04:34 | [Kazo.Os.Apps.KazoPaint](https://www.nuget.org/packages/Kazo.Os.Apps.KazoPaint) | 3.0.0 | Benoit Robin | The base Kazo OS Kazo Paint image editor app, to include in an OS host (Project… |
| 2026-11-05 02:04:35 | [Kazo.Os.Apps.Settings](https://www.nuget.org/packages/Kazo.Os.Apps.Settings) | 3.0.0 | Benoit Robin | The base Kazo OS Settings app, to include in an OS host (ProjectReference or Pa… |
| 2026-11-05 02:04:36 | [Kazo.Os.Apps.Store](https://www.nuget.org/packages/Kazo.Os.Apps.Store) | 3.0.0 | Benoit Robin | The Kazo OS Store, the Kazo OS system app that installs, updates and removes ap… |
| 2026-11-05 02:04:37 | [Kazo.Os.Apps.SystemMonitor](https://www.nuget.org/packages/Kazo.Os.Apps.SystemMonitor) | 3.0.0 | Benoit Robin | The base Kazo OS system monitor (task manager) app, to include in an OS host (P… |
| 2026-11-05 02:04:38 | [Kazo.Os.Apps.Terminal](https://www.nuget.org/packages/Kazo.Os.Apps.Terminal) | 3.0.0 | Benoit Robin | The base Kazo OS terminal app, to include in an OS host (ProjectReference or Pa… |
| 2026-11-05 02:04:39 | [Kazo.Os.Apps.TextEditor](https://www.nuget.org/packages/Kazo.Os.Apps.TextEditor) | 3.0.0 | Benoit Robin | The base Kazo OS text editor app, to include in an OS host (ProjectReference or… |
| 2026-11-05 02:04:40 | [Kazo.Os.Apps.ThemeEditor](https://www.nuget.org/packages/Kazo.Os.Apps.ThemeEditor) | 3.0.0 | Benoit Robin | The base Kazo OS Theme Editor app, to include in an OS host (ProjectReference o… |
| 2026-11-05 02:04:42 | [Kazo.Os.Apps.WebServer](https://www.nuget.org/packages/Kazo.Os.Apps.WebServer) | 3.0.0 | Benoit Robin | The base Kazo OS kazowebd web server and Web Server Manager app, to include in… |
| 2026-11-05 02:04:43 | [Kazo.Os.Commands](https://www.nuget.org/packages/Kazo.Os.Commands) | 3.0.0 | Benoit Robin | The built-in Kazo OS terminal commands (ls, cat, grep, curl, nano...), one lazy… |
| 2026-11-05 02:04:44 | [Kazo.Os.Ecosystem.Host](https://www.nuget.org/packages/Kazo.Os.Ecosystem.Host) | 3.0.0 | Benoit Robin | The Kazo OS host: desktop shell, boot coordinator, service composition and brow… |
| 2026-11-05 02:04:45 | [Kazo.Os.Infrastructure.Browser](https://www.nuget.org/packages/Kazo.Os.Infrastructure.Browser) | 3.0.0 | Benoit Robin | Browser infrastructure of Kazo OS: IndexedDB storage, Web Worker runtime and th… |
| 2026-11-05 02:04:46 | [Kazo.Os.MobileShell.Blazor](https://www.nuget.org/packages/Kazo.Os.MobileShell.Blazor) | 3.0.0 | Benoit Robin | Mobile shell chrome Razor components driven entirely by host-supplied contracts… |
| 2026-11-05 02:04:47 | [Kazo.Os.Platform.Blazor](https://www.nuget.org/packages/Kazo.Os.Platform.Blazor) | 3.0.0 | Benoit Robin | Kazo OS Blazor shell: desktop, launcher, window launching, dialogs and lazy app… |
| 2026-11-05 02:04:49 | [Kazo.Os.Platform.Core](https://www.nuget.org/packages/Kazo.Os.Platform.Core) | 3.0.0 | Benoit Robin | Kazo OS platform core: app catalog, process manager, policy, shell, settings an… |
| 2026-11-05 02:04:50 | [Kazo.Os.Platform.RemoteRendering](https://www.nuget.org/packages/Kazo.Os.Platform.RemoteRendering) | 3.0.0 | Benoit Robin | Trial of Kazo OS window apps rendered in a Web Worker (ADR 0129, ADR 0133): a B… |
| 2026-11-05 02:04:51 | [Kazo.Os.Platform.ResourceAccounting](https://www.nuget.org/packages/Kazo.Os.Platform.ResourceAccounting) | 3.0.0 | Benoit Robin | Optional measured CPU time and process memory for Kazo OS (ADR 0066). Reference… |
| 2026-11-05 02:04:52 | [Kazo.Os.Platform.WorkerHost](https://www.nuget.org/packages/Kazo.Os.Platform.WorkerHost) | 3.0.0 | Benoit Robin | Headless Kazo OS processes (commands, services) in Web Workers: worker pool, re… |
| 2026-11-05 02:04:53 | [Kazo.Os.Server.Contracts](https://www.nuget.org/packages/Kazo.Os.Server.Contracts) | 3.0.0 | Benoit Robin | Shared API versioning, sync record envelope, and proxy request/response contrac… |
| 2026-11-05 02:04:55 | [Kazo.Os.Simulation.Abstractions](https://www.nuget.org/packages/Kazo.Os.Simulation.Abstractions) | 3.0.0 | Benoit Robin | Contracts of the simulated machine (file system, processes, sessions, network,… |
| 2026-11-05 02:04:56 | [Kazo.Os.Taskbar.Blazor](https://www.nuget.org/packages/Kazo.Os.Taskbar.Blazor) | 3.0.0 | Benoit Robin | A taskbar Razor component driven entirely by host-supplied contracts (window so… |
| 2026-11-05 02:04:57 | [Kazo.Os.Templates](https://www.nuget.org/packages/Kazo.Os.Templates) | 3.0.0 | Benoit Robin | dotnet new templates for Kazo OS: window app, terminal command, service, ASP.Ka… |
| 2026-11-05 02:04:58 | [Kazo.Os.Theming.Abstractions](https://www.nuget.org/packages/Kazo.Os.Theming.Abstractions) | 3.0.0 | Benoit Robin | Framework-neutral Kazo OS theme catalog, identifiers, form factors, and persist… |
| 2026-11-05 02:04:59 | [Kazo.Os.Theming.Blazor](https://www.nuget.org/packages/Kazo.Os.Theming.Blazor) | 3.0.0 | Benoit Robin | Theme scope and token-driven previews shared by Kazo OS shell surfaces and reus… |
| 2026-11-05 02:05:00 | [Kazo.Os.Windowing.Abstractions](https://www.nuget.org/packages/Kazo.Os.Windowing.Abstractions) | 3.0.0 | Benoit Robin | Renderer- and host-independent window contracts: identity, geometry, constraint… |
| 2026-11-05 02:05:01 | [Kazo.Os.Windowing.Blazor](https://www.nuget.org/packages/Kazo.Os.Windowing.Blazor) | 3.0.0 | Benoit Robin | Razor components (DesktopArea, WindowHost, WindowChrome) that render a Kazo.Os.… |
| 2026-11-05 02:05:03 | [Kazo.Os.Windowing.Core](https://www.nuget.org/packages/Kazo.Os.Windowing.Core) | 3.0.0 | Benoit Robin | Headless, renderer-independent window manager engine: applies Kazo.Os.Windowing… |
| 2026-11-05 02:10:36 | [Holler.Cloudflare](https://www.nuget.org/packages/Holler.Cloudflare) | 0.9.0 | Tom Laird-McConnell | Cloudflare Realtime TURN for Holler: short-lived TURN credentials per user, so… |
| 2026-11-05 02:10:37 | [Holler.Server](https://www.nuget.org/packages/Holler.Server) | 0.9.0 | Tom Laird-McConnell | Server side of Holler: the SignalR signaling hub and Blazor Server support for… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

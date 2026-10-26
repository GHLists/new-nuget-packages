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

## Latest list — 2026-10-26 03:19 UTC

New packages created between 2026-10-26 02:19 UTC and 2026-10-26 03:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-26T03-19-42-531939Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-26 02:32:35 | [HackerOs.App.Abstractions](https://www.nuget.org/packages/HackerOs.App.Abstractions) | 2.1.0 | Benoit Robin | HackerOs App SDK contracts: AppDefinition and [AppManifest], the schema-v1 app… |
| 2026-10-26 02:32:36 | [HackerOs.App.Build](https://www.nuget.org/packages/HackerOs.App.Build) | 2.1.0 | Benoit Robin | Build integration of HackerOS apps: generated manifest.json, SDK boundary check… |
| 2026-10-26 02:32:37 | [HackerOs.AppSdk](https://www.nuget.org/packages/HackerOs.AppSdk) | 2.1.0 | Benoit Robin | HackerOS App SDK: the Hack* APIs an app uses (HackFile, HackStream, HackDirecto… |
| 2026-10-26 02:32:38 | [HackerOs.AppSdk.Blazor](https://www.nuget.org/packages/HackerOs.AppSdk.Blazor) | 2.1.0 | Benoit Robin | HackerOS App SDK for window apps: HackComponentBase, window base classes, dialo… |
| 2026-10-26 02:32:40 | [HackerOs.AppSdk.Icons](https://www.nuget.org/packages/HackerOs.AppSdk.Icons) | 2.1.0 | Benoit Robin | Framework-independent icon catalog and native Blazor SVG renderer used by Hacke… |
| 2026-10-26 02:32:41 | [HackerOs.AppSdk.Terminal](https://www.nuget.org/packages/HackerOs.AppSdk.Terminal) | 2.1.0 | Benoit Robin | HackerOS App SDK for terminal commands and the embeddable terminal contract (IH… |
| 2026-10-26 02:32:42 | [HackerOs.AppSdk.VirtualKeyboard](https://www.nuget.org/packages/HackerOs.AppSdk.VirtualKeyboard) | 2.1.0 | Benoit Robin | A reusable, host-agnostic on-screen keyboard and a keyboard-aware split contain… |
| 2026-10-26 02:32:43 | [HackerOs.AppSdk.Web](https://www.nuget.org/packages/HackerOs.AppSdk.Web) | 2.1.0 | Benoit Robin | ASP.Hack: MVC-like web sites hosted inside HackerOS (controllers, routing, mode… |
| 2026-10-26 02:32:44 | [HackerOs.AppSdk.Web.Blazor](https://www.nuget.org/packages/HackerOs.AppSdk.Web.Blazor) | 2.1.0 | Benoit Robin | Interactive Blazor sites of ASP.Hack: site router, navigation and the view the… |
| 2026-10-26 02:32:48 | [HackerOs.Apps.Browser](https://www.nuget.org/packages/HackerOs.Apps.Browser) | 2.1.0 | Benoit Robin | The base HackerOS web browser app, to include in an OS host (ProjectReference o… |
| 2026-10-26 02:32:50 | [HackerOs.Apps.Calculator](https://www.nuget.org/packages/HackerOs.Apps.Calculator) | 2.1.0 | Benoit Robin | The base HackerOS calculator app, to include in an OS host (ProjectReference or… |
| 2026-10-26 02:32:51 | [HackerOs.Apps.CodeEditor](https://www.nuget.org/packages/HackerOs.Apps.CodeEditor) | 2.1.0 | Benoit Robin | The base HackerOS code editor workbench app, to include in an OS host (ProjectR… |
| 2026-10-26 02:32:52 | [HackerOs.Apps.Desktop](https://www.nuget.org/packages/HackerOs.Apps.Desktop) | 2.1.0 | Benoit Robin | The HackerOS desktop: the icons of ~/Desktop, Home and Trash, drawn by the shel… |
| 2026-10-26 02:32:53 | [HackerOs.Apps.Diagnostic](https://www.nuget.org/packages/HackerOs.Apps.Diagnostic) | 2.1.0 | Benoit Robin | The base HackerOS diagnostic tool app, to include in an OS host (ProjectReferen… |
| 2026-10-26 02:32:54 | [HackerOs.Apps.ErrorLogViewer](https://www.nuget.org/packages/HackerOs.Apps.ErrorLogViewer) | 2.1.0 | Benoit Robin | The base HackerOS log viewer app, to include in an OS host (ProjectReference or… |
| 2026-10-26 02:32:56 | [HackerOs.Apps.FileExplorer](https://www.nuget.org/packages/HackerOs.Apps.FileExplorer) | 2.1.0 | Benoit Robin | The base HackerOS file explorer app, to include in an OS host (ProjectReference… |
| 2026-10-26 02:32:57 | [HackerOs.Apps.HackPaint](https://www.nuget.org/packages/HackerOs.Apps.HackPaint) | 2.1.0 | Benoit Robin | The base HackerOS Hack Paint image editor app, to include in an OS host (Projec… |
| 2026-10-26 02:32:58 | [HackerOs.Apps.IconViewer](https://www.nuget.org/packages/HackerOs.Apps.IconViewer) | 2.1.0 | Benoit Robin | The base HackerOS icon viewer app, to include in an OS host (ProjectReference o… |
| 2026-10-26 02:32:59 | [HackerOs.Apps.Settings](https://www.nuget.org/packages/HackerOs.Apps.Settings) | 2.1.0 | Benoit Robin | The base HackerOS Settings app, to include in an OS host (ProjectReference or P… |
| 2026-10-26 02:33:00 | [HackerOs.Apps.SystemMonitor](https://www.nuget.org/packages/HackerOs.Apps.SystemMonitor) | 2.1.0 | Benoit Robin | The base HackerOS system monitor (task manager) app, to include in an OS host (… |
| 2026-10-26 02:33:01 | [HackerOs.Apps.Terminal](https://www.nuget.org/packages/HackerOs.Apps.Terminal) | 2.1.0 | Benoit Robin | The base HackerOS terminal app, to include in an OS host (ProjectReference or P… |
| 2026-10-26 02:33:02 | [HackerOs.Apps.TextEditor](https://www.nuget.org/packages/HackerOs.Apps.TextEditor) | 2.1.0 | Benoit Robin | The base HackerOS text editor app, to include in an OS host (ProjectReference o… |
| 2026-10-26 02:33:04 | [HackerOs.Apps.ThemeEditor](https://www.nuget.org/packages/HackerOs.Apps.ThemeEditor) | 2.1.0 | Benoit Robin | The base HackerOS Theme Editor app, to include in an OS host (ProjectReference… |
| 2026-10-26 02:33:05 | [HackerOs.Apps.WebServer](https://www.nuget.org/packages/HackerOs.Apps.WebServer) | 2.1.0 | Benoit Robin | The base HackerOS hackwebd web server and Web Server Manager app, to include in… |
| 2026-10-26 02:33:06 | [HackerOs.Commands](https://www.nuget.org/packages/HackerOs.Commands) | 2.1.0 | Benoit Robin | The built-in HackerOS terminal commands (ls, cat, grep, curl, nano...), one laz… |
| 2026-10-26 02:33:07 | [HackerOs.Ecosystem.Host](https://www.nuget.org/packages/HackerOs.Ecosystem.Host) | 2.1.0 | Benoit Robin | The HackerOS host: desktop shell, boot coordinator, service composition and bro… |
| 2026-10-26 02:33:08 | [HackerOs.Infrastructure.Browser](https://www.nuget.org/packages/HackerOs.Infrastructure.Browser) | 2.1.0 | Benoit Robin | Browser infrastructure of HackerOS: IndexedDB storage, Web Worker runtime and t… |
| 2026-10-26 02:33:09 | [HackerOs.MobileShell.Blazor](https://www.nuget.org/packages/HackerOs.MobileShell.Blazor) | 2.1.0 | Benoit Robin | Mobile shell chrome Razor components driven entirely by host-supplied contracts… |
| 2026-10-26 02:33:10 | [HackerOs.Platform.Blazor](https://www.nuget.org/packages/HackerOs.Platform.Blazor) | 2.1.0 | Benoit Robin | HackerOS Blazor shell: desktop, launcher, window launching, dialogs and lazy ap… |
| 2026-10-26 02:33:12 | [HackerOs.Platform.Core](https://www.nuget.org/packages/HackerOs.Platform.Core) | 2.1.0 | Benoit Robin | HackerOS platform core: app catalog, process manager, policy, shell, settings a… |
| 2026-10-26 02:33:13 | [HackerOs.Platform.RemoteRendering](https://www.nuget.org/packages/HackerOs.Platform.RemoteRendering) | 2.1.0 | Benoit Robin | Trial of HackerOS window apps rendered in a Web Worker (ADR 0129, ADR 0133): a… |
| 2026-10-26 02:33:14 | [HackerOs.Platform.ResourceAccounting](https://www.nuget.org/packages/HackerOs.Platform.ResourceAccounting) | 2.1.0 | Benoit Robin | Optional measured CPU time and process memory for HackerOS (ADR 0066). Referenc… |
| 2026-10-26 02:33:15 | [HackerOs.Platform.WorkerHost](https://www.nuget.org/packages/HackerOs.Platform.WorkerHost) | 2.1.0 | Benoit Robin | Headless HackerOS processes (commands, services) in Web Workers: worker pool, r… |
| 2026-10-26 02:33:16 | [HackerOs.Server.Contracts](https://www.nuget.org/packages/HackerOs.Server.Contracts) | 2.1.0 | Benoit Robin | Shared API versioning, sync record envelope, and proxy request/response contrac… |
| 2026-10-26 02:33:22 | [HackerOs.Simulation.Abstractions](https://www.nuget.org/packages/HackerOs.Simulation.Abstractions) | 2.1.0 | Benoit Robin | Contracts of the simulated machine (file system, processes, sessions, network,… |
| 2026-10-26 02:33:23 | [HackerOs.Taskbar.Blazor](https://www.nuget.org/packages/HackerOs.Taskbar.Blazor) | 2.1.0 | Benoit Robin | A taskbar Razor component driven entirely by host-supplied contracts (window so… |
| 2026-10-26 02:33:25 | [HackerOs.Templates](https://www.nuget.org/packages/HackerOs.Templates) | 2.1.0 | Benoit Robin | dotnet new templates for HackerOS: window app, terminal command, service, ASP.H… |
| 2026-10-26 02:33:26 | [HackerOs.Theming.Abstractions](https://www.nuget.org/packages/HackerOs.Theming.Abstractions) | 2.1.0 | Benoit Robin | Framework-neutral HackerOS theme catalog, identifiers, form factors, and persis… |
| 2026-10-26 02:33:27 | [HackerOs.Theming.Blazor](https://www.nuget.org/packages/HackerOs.Theming.Blazor) | 2.1.0 | Benoit Robin | Theme scope and token-driven previews shared by HackerOS shell surfaces and reu… |
| 2026-10-26 02:33:28 | [HackerOs.Windowing.Abstractions](https://www.nuget.org/packages/HackerOs.Windowing.Abstractions) | 2.1.0 | Benoit Robin | Renderer- and host-independent window contracts: identity, geometry, constraint… |
| 2026-10-26 02:33:29 | [HackerOs.Windowing.Blazor](https://www.nuget.org/packages/HackerOs.Windowing.Blazor) | 2.1.0 | Benoit Robin | Razor components (DesktopArea, WindowHost, WindowChrome) that render a HackerOs… |
| 2026-10-26 02:33:31 | [HackerOs.Windowing.Core](https://www.nuget.org/packages/HackerOs.Windowing.Core) | 2.1.0 | Benoit Robin | Headless, renderer-independent window manager engine: applies HackerOs.Windowin… |
| 2026-10-26 03:01:52 | [Octeka.Scripting](https://www.nuget.org/packages/Octeka.Scripting) | 1.0.0 | Patrick Robichaud | Modular, high-performance runtime C# script compilation and assembly emitting f… |
| 2026-10-26 03:01:53 | [Octeka.Scripting.Abstractions](https://www.nuget.org/packages/Octeka.Scripting.Abstractions) | 1.0.0 | Patrick Robichaud | Core abstractions, attributes, and contracts for the Octeka Scripting runtime c… |
| 2026-10-26 03:05:09 | [Mezon.Net.Sdk.Sfu](https://www.nuget.org/packages/Mezon.Net.Sdk.Sfu) | 1.8.0 | Mezon.Net Contributors | Client for the Mezon meeting SFU (mezon-sfu): join rooms, publish Opus audio an… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

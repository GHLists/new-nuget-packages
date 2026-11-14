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

## Latest list — 2026-11-14 07:18 UTC

New packages created between 2026-11-14 06:20 UTC and 2026-11-14 07:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-14T07-18-28-356901Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-14 06:22:24 | [Ranvier.Anime.Traced](https://www.nuget.org/packages/Ranvier.Anime.Traced) | 0.1.0 | shayanhabibi | The traced build of Ranvier.Anime, a .NET port of anime.js 4.5 for Ranvier host… |
| 2026-11-14 06:22:25 | [Fable.Ranvier.Anime.Traced](https://www.nuget.org/packages/Fable.Ranvier.Anime.Traced) | 0.1.45 | shayanhabibi | The traced build of Fable.Ranvier.Anime: typed anime.js 4.5 bindings for Fable.… |
| 2026-11-14 06:22:25 | [Fable.Ranvier.Anime](https://www.nuget.org/packages/Fable.Ranvier.Anime) | 0.1.45 | shayanhabibi | Typed anime.js 4.5 bindings for Fable, with Ranvier integration: parameters as… |
| 2026-11-14 06:22:25 | [Ranvier.Anime](https://www.nuget.org/packages/Ranvier.Anime) | 0.1.0 | shayanhabibi | A .NET port of anime.js 4.5 for Ranvier hosts: timers, timelines, keyframes, ty… |
| 2026-11-14 06:32:09 | [Medical.Sync](https://www.nuget.org/packages/Medical.Sync) | 2.0.0 | Gravicode Studios (Kang Fadhi… | Medical.Net offline-first synchronisation: hybrid logical clocks, per-type conf… |
| 2026-11-14 06:32:10 | [Medical.Hospital](https://www.nuget.org/packages/Medical.Hospital) | 2.0.0 | Gravicode Studios (Kang Fadhi… | Medical.Net hospital information system core: multi-tenant EF Core model and se… |
| 2026-11-14 06:32:28 | [Electrical.IEC61850](https://www.nuget.org/packages/Electrical.IEC61850) | 1.0.0 | Gravicode Studios (Kang Fadhi… | IEC 61850: SCL (ICD/CID/SCD) parsing, logical-node data model, GOOSE and Sample… |
| 2026-11-14 06:32:29 | [Electrical.Harmonic](https://www.nuget.org/packages/Electrical.Harmonic) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Power quality and harmonics: FFT, THD/TDD, IEEE 519 and IEC 61000 limits, harmo… |
| 2026-11-14 06:32:29 | [Electrical.Visualization.Blazor](https://www.nuget.org/packages/Electrical.Visualization.Blazor) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Blazor components for Electrical.Net: single-line diagram with power-flow overl… |
| 2026-11-14 06:32:30 | [Electrical.StateEstimation](https://www.nuget.org/packages/Electrical.StateEstimation) | 1.0.0 | Gravicode Studios (Kang Fadhi… | State estimation: weighted least squares AC estimator with sparse gain matrix,… |
| 2026-11-14 06:32:31 | [Electrical.Circuit](https://www.nuget.org/packages/Electrical.Circuit) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Circuit simulation: modified nodal analysis (DC operating point, AC phasor swee… |
| 2026-11-14 06:32:32 | [Electrical.Simulation](https://www.nuget.org/packages/Electrical.Simulation) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Simulation: quasi-static time-series (QSTS) simulation over load/PV profiles, M… |
| 2026-11-14 06:32:32 | [Electrical.Forecasting](https://www.nuget.org/packages/Electrical.Forecasting) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Forecasting: short-term load forecasting (Holt-Winters, regression with weather… |
| 2026-11-14 06:32:33 | [Electrical.Stability](https://www.nuget.org/packages/Electrical.Stability) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Power system stability: transient stability (classical and two-axis models, RK4… |
| 2026-11-14 06:32:34 | [Electrical.Visualization](https://www.nuget.org/packages/Electrical.Visualization) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Visualization: automatic single-line diagram layout and SVG rendering with powe… |
| 2026-11-14 06:32:34 | [Electrical.Cloud](https://www.nuget.org/packages/Electrical.Cloud) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Cloud: study job runner with JSON contracts, ASP.NET Core minimal API endpoints… |
| 2026-11-14 06:32:35 | [Electrical.Protection](https://www.nuget.org/packages/Electrical.Protection) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Protection engineering: IEC 60255 / IEEE C37.112 inverse-time overcurrent curve… |
| 2026-11-14 06:32:36 | [Electrical.Core](https://www.nuget.org/packages/Electrical.Core) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Electrical.Net core: complex/sparse linear algebra, per-unit system, phasors an… |
| 2026-11-14 06:32:37 | [Electrical.HPC](https://www.nuget.org/packages/Electrical.HPC) | 1.0.0 | Gravicode Studios (Kang Fadhi… | High-performance computing: parallel batch and Monte-Carlo power flow, probabil… |
| 2026-11-14 06:32:37 | [Electrical.SCADA](https://www.nuget.org/packages/Electrical.SCADA) | 1.0.0 | Gravicode Studios (Kang Fadhi… | SCADA: Modbus TCP client/server and codec, tag database, alarm management (ISA-… |
| 2026-11-14 06:32:38 | [Electrical.AI](https://www.nuget.org/packages/Electrical.AI) | 1.0.0 | Gravicode Studios (Kang Fadhi… | AI for power systems: LLM grid-operator agent with tool calling (OpenAI, Azure… |
| 2026-11-14 06:32:39 | [Electrical.Renewable](https://www.nuget.org/packages/Electrical.Renewable) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Renewable energy: solar PV (single-diode, irradiance and temperature models, MP… |
| 2026-11-14 06:32:39 | [Electrical.PowerFlow](https://www.nuget.org/packages/Electrical.PowerFlow) | 1.0.0 | Gravicode Studios (Kang Fadhi… | AC/DC power flow for Electrical.Net: sparse Newton–Raphson, Gauss–Seidel, fast-… |
| 2026-11-14 06:32:40 | [Electrical.GIS](https://www.nuget.org/packages/Electrical.GIS) | 1.0.0 | Gravicode Studios (Kang Fadhi… | GIS for grids: GeoJSON export/import of networks, Web Mercator projection, line… |
| 2026-11-14 06:32:41 | [Electrical.Templates](https://www.nuget.org/packages/Electrical.Templates) | 1.0.0 | Gravicode Studios (Kang Fadhi… | dotnet new templates for Electrical.Net: power-system study console, Blazor gri… |
| 2026-11-14 06:32:42 | [Electrical.CIM](https://www.nuget.org/packages/Electrical.CIM) | 1.0.0 | Gravicode Studios (Kang Fadhi… | IEC CIM / CGMES: RDF/XML import and export of power networks (IEC 61970-301 equ… |
| 2026-11-14 06:32:43 | [Electrical.SmartGrid](https://www.nuget.org/packages/Electrical.SmartGrid) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Smart grid: demand response, EV charging scheduling, microgrid energy managemen… |
| 2026-11-14 06:32:43 | [Electrical.ShortCircuit](https://www.nuget.org/packages/Electrical.ShortCircuit) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Short-circuit analysis per IEC 60909 / ANSI: three-phase, single-line-to-ground… |
| 2026-11-14 06:32:44 | [Electrical.DigitalTwin](https://www.nuget.org/packages/Electrical.DigitalTwin) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Digital twin: live grid twin synchronised from SCADA measurements via state est… |
| 2026-11-14 06:32:45 | [Electrical.Optimization](https://www.nuget.org/packages/Electrical.Optimization) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Optimization: economic dispatch, DC optimal power flow (interior-point QP), sec… |
| 2026-11-14 06:32:46 | [Electrical.Cli](https://www.nuget.org/packages/Electrical.Cli) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Electrical.Net command-line tool (eln): power flow, N-1 contingency, short circ… |
| 2026-11-14 06:32:46 | [Electrical.Native](https://www.nuget.org/packages/Electrical.Native) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Native (Rust) high-performance kernels for Electrical.Net � FFT/THD, batch comp… |
| 2026-11-14 06:43:43 | [Interop.JS.MobX](https://www.nuget.org/packages/Interop.JS.MobX) | 7.0.6 | Interop.JS.MobX | Package Description |
| 2026-11-14 06:45:35 | [Interop.JS.Browser](https://www.nuget.org/packages/Interop.JS.Browser) | 1.0.0 | Interop.JS.Browser | Package Description |
| 2026-11-14 06:46:17 | [Interop.JS.Browser.fecs](https://www.nuget.org/packages/Interop.JS.Browser.fecs) | 1.0.0 | Interop.JS.Browser.fecs | Package Description |
| 2026-11-14 06:46:43 | [Interop.JS.LucideIcons](https://www.nuget.org/packages/Interop.JS.LucideIcons) | 1.72.0 | Interop.JS.LucideIcons | Package Description |
| 2026-11-14 06:46:58 | [Interop.JS.LucideIcons.fecs](https://www.nuget.org/packages/Interop.JS.LucideIcons.fecs) | 1.72.0 | Interop.JS.LucideIcons.fecs | Package Description |
| 2026-11-14 06:47:36 | [Interop.JS.MobX.fecs](https://www.nuget.org/packages/Interop.JS.MobX.fecs) | 7.0.6 | Interop.JS.MobX.fecs | Package Description |
| 2026-11-14 06:48:06 | [Interop.JS.MobX.React](https://www.nuget.org/packages/Interop.JS.MobX.React) | 5.1.0 | Interop.JS.MobX.React | Package Description |
| 2026-11-14 06:48:22 | [Interop.JS.MobX.React.fecs](https://www.nuget.org/packages/Interop.JS.MobX.React.fecs) | 5.1.0 | Interop.JS.MobX.React.fecs | Package Description |
| 2026-11-14 06:48:36 | [Interop.JS.Motion](https://www.nuget.org/packages/Interop.JS.Motion) | 14.4.0 | Interop.JS.Motion | Package Description |
| 2026-11-14 06:48:48 | [Interop.JS.Motion.fecs](https://www.nuget.org/packages/Interop.JS.Motion.fecs) | 14.4.0 | Interop.JS.Motion.fecs | Package Description |
| 2026-11-14 06:49:28 | [Interop.JS.React](https://www.nuget.org/packages/Interop.JS.React) | 19.3.1 | Interop.JS.React | Package Description |
| 2026-11-14 06:49:56 | [Interop.JS.React.fecs](https://www.nuget.org/packages/Interop.JS.React.fecs) | 19.3.1 | Interop.JS.React.fecs | Package Description |
| 2026-11-14 06:50:34 | [Interop.JS.Shadcn.BaseUI](https://www.nuget.org/packages/Interop.JS.Shadcn.BaseUI) | 1.9.0 | Interop.JS.Shadcn.BaseUI | Package Description |
| 2026-11-14 06:50:58 | [Interop.JS.Shadcn.BaseUI.fecs](https://www.nuget.org/packages/Interop.JS.Shadcn.BaseUI.fecs) | 1.9.0 | Interop.JS.Shadcn.BaseUI.fecs | Package Description |
| 2026-11-14 06:51:11 | [Interop.JS.Shadcn.Cn](https://www.nuget.org/packages/Interop.JS.Shadcn.Cn) | 0.5.2 | Interop.JS.Shadcn.Cn | Package Description |
| 2026-11-14 06:51:23 | [Interop.JS.Shadcn.Cn.fecs](https://www.nuget.org/packages/Interop.JS.Shadcn.Cn.fecs) | 0.5.2 | Interop.JS.Shadcn.Cn.fecs | Package Description |
| 2026-11-14 06:51:37 | [Interop.JS.Shadcn.Recharts](https://www.nuget.org/packages/Interop.JS.Shadcn.Recharts) | 3.8.0 | Interop.JS.Shadcn.Recharts | Package Description |
| 2026-11-14 06:51:49 | [Interop.JS.Shadcn.Recharts.fecs](https://www.nuget.org/packages/Interop.JS.Shadcn.Recharts.fecs) | 3.8.0 | Interop.JS.Shadcn.Recharts.fe… | Package Description |
| 2026-11-14 06:58:32 | [Dagline](https://www.nuget.org/packages/Dagline) | 0.1.0 | Craig Quillen | A lightweight, in-process library for running directed acyclic graphs (DAGs) of… |
| 2026-11-14 06:58:33 | [Dagline.Testing](https://www.nuget.org/packages/Dagline.Testing) | 0.1.0 | Craig Quillen | Test helpers for Dagline task authors: a harness that runs one task body and re… |
| 2026-11-14 06:58:34 | [Dagline.Spectre](https://www.nuget.org/packages/Dagline.Spectre) | 0.1.0 | Craig Quillen | Spectre.Console terminal UI for Dagline: live views of queued, running and comp… |
| 2026-11-14 06:58:47 | [Ranvier.WebCore.Native.Gpu](https://www.nuget.org/packages/Ranvier.WebCore.Native.Gpu) | 0.1.1 | Ranvier | Former name of Ranvier.WebCore.Native, on which it depends: reference Ranvier.W… |
| 2026-11-14 06:58:49 | [Ranvier.WebCore.Native.Cpu.osx-arm64](https://www.nuget.org/packages/Ranvier.WebCore.Native.Cpu.osx-arm64) | 0.1.1 | Ranvier | WebCore, JavaScriptCore and the Ranvier C ABI host (RanvierWebCoreHost) for osx… |
| 2026-11-14 06:58:50 | [Ranvier.WebCore.Native.linux-x64](https://www.nuget.org/packages/Ranvier.WebCore.Native.linux-x64) | 0.1.1 | Ranvier | WebCore, JavaScriptCore and the Ranvier C ABI host (RanvierWebCoreHost) for lin… |
| 2026-11-14 06:58:51 | [Ranvier.WebCore.Native.Cpu.win-x64](https://www.nuget.org/packages/Ranvier.WebCore.Native.Cpu.win-x64) | 0.1.1 | Ranvier | WebCore, JavaScriptCore and the Ranvier C ABI host (RanvierWebCoreHost) for win… |
| 2026-11-14 06:58:53 | [Ranvier.WebCore.Native.Cpu.linux-x64](https://www.nuget.org/packages/Ranvier.WebCore.Native.Cpu.linux-x64) | 0.1.1 | Ranvier | WebCore, JavaScriptCore and the Ranvier C ABI host (RanvierWebCoreHost) for lin… |
| 2026-11-14 06:58:55 | [Ranvier.WebCore.Native.Cpu.linux-arm64](https://www.nuget.org/packages/Ranvier.WebCore.Native.Cpu.linux-arm64) | 0.1.1 | Ranvier | WebCore, JavaScriptCore and the Ranvier C ABI host (RanvierWebCoreHost) for lin… |
| 2026-11-14 06:58:56 | [Ranvier.WebCore.Native.Cpu.win-arm64](https://www.nuget.org/packages/Ranvier.WebCore.Native.Cpu.win-arm64) | 0.1.1 | Ranvier | WebCore, JavaScriptCore and the Ranvier C ABI host (RanvierWebCoreHost) for win… |
| 2026-11-14 06:59:02 | [Ranvier.WebCore.Native.osx-arm64](https://www.nuget.org/packages/Ranvier.WebCore.Native.osx-arm64) | 0.1.1 | Ranvier | WebCore, JavaScriptCore and the Ranvier C ABI host (RanvierWebCoreHost) for osx… |
| 2026-11-14 06:59:02 | [Ranvier.WebCore](https://www.nuget.org/packages/Ranvier.WebCore) | 0.1.1 | Ranvier | Managed interop for the versioned Ranvier WebCore C ABI. |
| 2026-11-14 06:59:04 | [Ranvier.WebCore.Native.linux-arm64](https://www.nuget.org/packages/Ranvier.WebCore.Native.linux-arm64) | 0.1.1 | Ranvier | WebCore, JavaScriptCore and the Ranvier C ABI host (RanvierWebCoreHost) for lin… |
| 2026-11-14 06:59:06 | [Ranvier.WebCore.Native.win-x64](https://www.nuget.org/packages/Ranvier.WebCore.Native.win-x64) | 0.1.1 | Ranvier | WebCore, JavaScriptCore and the Ranvier C ABI host (RanvierWebCoreHost) for win… |
| 2026-11-14 06:59:06 | [Ranvier.WebCore.Native](https://www.nuget.org/packages/Ranvier.WebCore.Native) | 0.1.1 | Ranvier | Native WebCore host for Windows x64/ARM64, Linux x64/ARM64 and macOS ARM64: acc… |
| 2026-11-14 06:59:06 | [Ranvier.WebCore.Native.Cpu](https://www.nuget.org/packages/Ranvier.WebCore.Native.Cpu) | 0.1.1 | Ranvier | CPU-only native WebCore host (the Slim flavor) for Windows x64/ARM64, Linux x64… |
| 2026-11-14 06:59:07 | [Ranvier.WebCore.Accessibility.Atspi](https://www.nuget.org/packages/Ranvier.WebCore.Accessibility.Atspi) | 0.1.1 | Ranvier | Optional native AT-SPI modules for the matching Ranvier.WebCore Linux host. |
| 2026-11-14 07:02:58 | [KumaEngine.Glfw](https://www.nuget.org/packages/KumaEngine.Glfw) | 1.0.0 | KumaEngine.Glfw | managed bindings for glfw |
| 2026-11-14 07:03:32 | [ChromaFx.Retro](https://www.nuget.org/packages/ChromaFx.Retro) | 0.6.3 | Ho Tzin Mein | Retro hardware palettes, 90s web/Win9x UI looks, and early-2000s filter effects… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

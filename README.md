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

## Latest list — 2026-11-09 03:18 UTC

New packages created between 2026-11-09 02:21 UTC and 2026-11-09 03:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-09T03-18-49-100807Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-09 02:46:14 | [RazorConsole.Cli](https://www.nuget.org/packages/RazorConsole.Cli) | 0.7.0 | RazorConsole | Drive and inspect RazorConsole apps from the command line: run them in a pseudo… |
| 2026-11-09 02:46:20 | [RazorConsole.Testing](https://www.nuget.org/packages/RazorConsole.Testing) | 0.7.0 | RazorConsole | Test hosts for RazorConsole: mount components headlessly at a fixed terminal si… |
| 2026-11-09 02:48:05 | [TKCode.Arc.Foundation](https://www.nuget.org/packages/TKCode.Arc.Foundation) | 1.0.0 | TKCode.Arc contributors | Theme and token runtime for TKCode.Arc: design tokens, light and dark publishin… |
| 2026-11-09 02:48:06 | [TKCode.Arc.Core](https://www.nuget.org/packages/TKCode.Arc.Core) | 1.0.0 | TKCode.Arc contributors | Arc-style component library for Avalonia. Ports the free components of Arc (uia… |
| 2026-11-09 02:48:07 | [TKCode.Arc.Fonts](https://www.nuget.org/packages/TKCode.Arc.Fonts) | 1.0.0 | TKCode.Arc contributors | Geist and Geist Mono (SIL OFL 1.1, Vercel) for TKCode.Arc, registered as fonts:… |
| 2026-11-09 02:48:08 | [TKCode.Arc.Icons.Lucide](https://www.nuget.org/packages/TKCode.Arc.Icons.Lucide) | 1.0.0 | TKCode.Arc contributors | The complete Lucide icon set (ISC) for TKCode.Arc: LucideIcon control and Lucid… |
| 2026-11-09 02:48:08 | [TKCode.Arc.Audio](https://www.nuget.org/packages/TKCode.Arc.Audio) | 1.0.0 | TKCode.Arc contributors | Audio playback abstraction for TKCode.Arc (IAudioPlayer, AudioSource) with a si… |
| 2026-11-09 02:48:09 | [TKCode.Arc.Audio.Native](https://www.nuget.org/packages/TKCode.Arc.Audio.Native) | 1.0.0 | TKCode.Arc contributors | Desktop audio backend for TKCode.Arc.Audio (Windows, macOS, Linux; x64 and arm6… |
| 2026-11-09 02:48:10 | [TKCode.Arc.Audio.Browser](https://www.nuget.org/packages/TKCode.Arc.Audio.Browser) | 1.0.0 | TKCode.Arc contributors | WebAssembly audio backend for TKCode.Arc.Audio: one HTML audio element per play… |
| 2026-11-09 02:48:11 | [TKCode.Arc](https://www.nuget.org/packages/TKCode.Arc) | 1.0.0 | TKCode.Arc contributors | Arc-style component library for Avalonia. Ports the free components of Arc (uia… |
| 2026-11-09 02:48:12 | [TKCode.Arc.Pdf](https://www.nuget.org/packages/TKCode.Arc.Pdf) | 1.0.0 | TKCode.Arc contributors | PDF viewing for TKCode.Arc: PdfViewer (PageViewer plus a sidebar with thumbnail… |
| 2026-11-09 02:48:14 | [TKCode.Arc.Pdf.Native](https://www.nuget.org/packages/TKCode.Arc.Pdf.Native) | 1.0.0 | TKCode.Arc contributors | Desktop PDF backend for TKCode.Arc.Pdf (Windows, macOS, Linux; x64 and arm64),… |
| 2026-11-09 02:48:15 | [TKCode.Arc.Pdf.Browser](https://www.nuget.org/packages/TKCode.Arc.Pdf.Browser) | 1.0.0 | TKCode.Arc contributors | WebAssembly PDF backend for TKCode.Arc.Pdf, built on pdf.js. Call await ArcPdfB… |
| 2026-11-09 02:48:16 | [TKCode.Arc.Blocks](https://www.nuget.org/packages/TKCode.Arc.Blocks) | 1.0.0 | TKCode.Arc contributors | Page-level block compositions for TKCode.Arc, built from Arc components. Ports… |
| 2026-11-09 02:48:17 | [TKCode.Arc.AdvancedCharts](https://www.nuget.org/packages/TKCode.Arc.AdvancedCharts) | 1.0.0 | TKCode.Arc contributors | Advanced charts for TKCode.Arc: Sunburst, SankeyFlow, FunnelChart, RadarChart,… |
| 2026-11-09 02:48:19 | [TKCode.Arc.Special](https://www.nuget.org/packages/TKCode.Arc.Special) | 1.0.0 | TKCode.Arc contributors | Special components for TKCode.Arc, the uiarc.dev "Special components" section:… |
| 2026-11-09 02:48:20 | [TKCode.Arc.Terminal](https://www.nuget.org/packages/TKCode.Arc.Terminal) | 1.0.0 | TKCode.Arc contributors | Terminal emulator for Avalonia: the TerminalView control and a managed facade o… |
| 2026-11-09 02:48:20 | [TKCode.Arc.Workflow](https://www.nuget.org/packages/TKCode.Arc.Workflow) | 1.0.0 | TKCode.Arc contributors | Workflow canvas for TKCode.Arc: show and edit graphs of steps and connections o… |
| 2026-11-09 02:48:21 | [TKCode.Arc.Dock](https://www.nuget.org/packages/TKCode.Arc.Dock) | 1.0.0 | TKCode.Arc contributors | IDE-style dock layout for TKCode.Arc: panes in tab groups, nested horizontal an… |
| 2026-11-09 02:48:22 | [TKCode.Arc.Themes.Pixel](https://www.nuget.org/packages/TKCode.Arc.Themes.Pixel) | 1.0.0 | TKCode.Arc contributors | Pixel-art theme (token overrides only, no controls) for TKCode.Arc: square corn… |
| 2026-11-09 02:48:23 | [TKCode.Arc.Themes.Corners](https://www.nuget.org/packages/TKCode.Arc.Themes.Corners) | 1.0.0 | TKCode.Arc contributors | Global corner style for TKCode.Arc (token overrides only, no controls): square… |
| 2026-11-09 02:48:24 | [TKCode.Arc.Mobile](https://www.nuget.org/packages/TKCode.Arc.Mobile) | 1.0.0 | TKCode.Arc contributors | Touch-first Arc components for Avalonia (first slice: page, navbar, tabbar, but… |
| 2026-11-09 02:48:24 | [TKCode.Arc.Templates](https://www.nuget.org/packages/TKCode.Arc.Templates) | 1.0.0 | TKCode.Arc contributors | dotnet new templates for TKCode.Arc: desktop and cross-platform (desktop + WebA… |
| 2026-11-09 02:54:43 | [Sevencat.ImgproSharp](https://www.nuget.org/packages/Sevencat.ImgproSharp) | 0.1.0 | sevencat | Drawing for Sdcb.SimdCodecs: shapes, gradients, strokes and TrueType text over… |
| 2026-11-09 02:54:49 | [Sylvanas.CascadeComboBox](https://www.nuget.org/packages/Sylvanas.CascadeComboBox) | 1.0.0 | Sylvanas | WPF 两级（父/子）级联下拉选择框：左右分栏面板，点父类不关闭、点子类才选中关闭；零第三方主题依赖，支持外部样式注入。 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

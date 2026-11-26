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

## Latest list — 2026-11-26 15:20 UTC

New packages created between 2026-11-26 14:21 UTC and 2026-11-26 15:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-26T15-20-09-76425Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-26 14:32:35 | [Muzzle.Theme](https://www.nuget.org/packages/Muzzle.Theme) | 1.0.0 | Mr. Squirrely | Muzzle: a cozy, pastel design system for WPF. Light and Dark themes with Coral,… |
| 2026-11-26 14:37:05 | [WinForms.Easel.Templates](https://www.nuget.org/packages/WinForms.Easel.Templates) | 2.0.0 | Axvser | Item templates for Easel XAML views and resource dictionaries. |
| 2026-11-26 14:37:33 | [VkRadio.WebTools.WebGrabber](https://www.nuget.org/packages/VkRadio.WebTools.WebGrabber) | 0.0.1 | vkradio | WebGrabber utilities to read partially structured data from some types of websi… |
| 2026-11-26 14:37:53 | [Agile.Infra.License](https://www.nuget.org/packages/Agile.Infra.License) | 1.0.0 | Agile.Cai | 是一个轻量级授权控制类库，为应用程序提供许可校验、有效期管理与使用权限控制能力。 |
| 2026-11-26 14:40:30 | [Nirs4all.Formats](https://www.nuget.org/packages/Nirs4all.Formats) | 0.3.1 | Gregory Beurier | Read NIRS and spectroscopy vendor files and export them to exchange formats, th… |
| 2026-11-26 14:46:51 | [VkRadio.LowCode.Libs.Utils](https://www.nuget.org/packages/VkRadio.LowCode.Libs.Utils) | 0.0.1 | vkradio | Miscellaneous utils used in VkRadio.LowCode toolset or in dependent app projects |
| 2026-11-26 14:47:38 | [VkRadio.LowCode.Libs.Orm](https://www.nuget.org/packages/VkRadio.LowCode.Libs.Orm) | 0.0.1 | vkradio | Simple micro-ORM base library used in VkRadio.LowCode toolset |
| 2026-11-26 14:48:21 | [VkRadio.LowCode.Libs.Orm.MsSql](https://www.nuget.org/packages/VkRadio.LowCode.Libs.Orm.MsSql) | 0.0.1 | vkradio | IDbProviderFactory implementation for MS SQL (used in VkRadio.LowCode toolset) |
| 2026-11-26 14:49:05 | [VkRadio.LowCode.Libs.Gui.WinForms](https://www.nuget.org/packages/VkRadio.LowCode.Libs.Gui.WinForms) | 0.0.1 | vkradio | WinForms GUI components library used in VkRadio.LowCode toolset |
| 2026-11-26 14:53:57 | [NoComments.Analyzers](https://www.nuget.org/packages/NoComments.Analyzers) | 0.1.0 | Lee Sanderson | Roslyn analyzers that report comments in C# and Razor code, with a code fix tha… |
| 2026-11-26 14:56:02 | [xdelta](https://www.nuget.org/packages/xdelta) | 1.0.0 | Israel Lot | Create and apply RFC 3284 VCDIFF binary patches in .NET 8. Encode at levels 0–9… |
| 2026-11-26 14:56:04 | [xdelta.Blake3](https://www.nuget.org/packages/xdelta.Blake3) | 1.0.0 | Israel Lot | Verify whole-file source and target digests in xdelta3 BLAKE3 armor. Adds opt-i… |
| 2026-11-26 14:56:05 | [xdelta.Lzma](https://www.nuget.org/packages/xdelta.Lzma) | 1.0.0 | Israel Lot | Apply xdelta3 VCDIFF patches with LZMA secondary compression in .NET 8. Decode… |
| 2026-11-26 14:59:18 | [Etalon](https://www.nuget.org/packages/Etalon) | 1.0.0 | Finity Software | Compile-time type-safe physical quantities for .NET. Every quantity (voltage, f… |
| 2026-11-26 14:59:31 | [tman](https://www.nuget.org/packages/tman) | 0.1.0 | Kyle Kukshtel | Pick and run VS Code tasks.json tasks from the terminal. Tasks open in Rex floa… |
| 2026-11-26 15:04:52 | [DotNetElements.UndoRedo](https://www.nuget.org/packages/DotNetElements.UndoRedo) | 0.1.0 | Felix-CodingClimber | Lightweight, AOT-friendly, reflection-free undo/redo framework for .NET, design… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

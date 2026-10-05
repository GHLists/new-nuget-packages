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

## Latest list — 2026-10-05 09:20 UTC

New packages created between 2026-10-05 08:20 UTC and 2026-10-05 09:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-05T09-20-24-732297Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-05 08:21:31 | [umBlogGenerator](https://www.nuget.org/packages/umBlogGenerator) | 1.0.0 | OSKI solutions | Generate SEO comparison blogs in Umbraco with AI — peer research, logos, and Bl… |
| 2026-10-05 08:34:48 | [LilyDesignSystem.Blazor.SearchPicker](https://www.nuget.org/packages/LilyDesignSystem.Blazor.SearchPicker) | 0.1.0 | Joel Parker Henderson | Lily Design System Blazor search picker: a magnifying-glass icon button opening… |
| 2026-10-05 08:45:57 | [cef.runtime.win-arm64](https://www.nuget.org/packages/cef.runtime.win-arm64) | 154.0.33 | The Chromium Embedded Framewo… | Chromium Embedded Framework (CEF) Release Distribution NOTE: This package is ma… |
| 2026-10-05 08:46:05 | [cef.runtime.win-x64](https://www.nuget.org/packages/cef.runtime.win-x64) | 154.0.33 | The Chromium Embedded Framewo… | Chromium Embedded Framework (CEF) Release Distribution NOTE: This package is ma… |
| 2026-10-05 08:47:21 | [Stimulsoft.WebP](https://www.nuget.org/packages/Stimulsoft.WebP) | 2026.4.1 | Stimulsoft | A library for decoding WebP images in Stimulsoft products. |
| 2026-10-05 08:49:35 | [MirrorPulse.Adapter.Sdk](https://www.nuget.org/packages/MirrorPulse.Adapter.Sdk) | 0.2.1 | MirrorPulse Team | Canonical public contracts and runtime for MirrorPulse Adapter Workers. |
| 2026-10-05 08:50:53 | [WinUia](https://www.nuget.org/packages/WinUia) | 0.0.1 | Buning Software | Automate Windows applications through UI Automation: launch, attach, find and i… |
| 2026-10-05 08:50:54 | [WinUia.Core](https://www.nuget.org/packages/WinUia.Core) | 0.0.1 | Buning Software | A dependency-free .NET wrapper around the Windows UI Automation (UIA3) COM API. |
| 2026-10-05 08:50:55 | [WinUia.Input](https://www.nuget.org/packages/WinUia.Input) | 0.0.1 | Buning Software | Physical mouse and keyboard input (SendInput) in physical pixels, for WinUia. |
| 2026-10-05 08:50:56 | [WinUia.NUnit](https://www.nuget.org/packages/WinUia.NUnit) | 0.0.1 | Buning Software | NUnit integration for WinUia: [UiTest], which gives each UI test the desktop to… |
| 2026-10-05 09:00:48 | [EmbedIO-Neo.DependencyInjection](https://www.nuget.org/packages/EmbedIO-Neo.DependencyInjection) | 1.0.1 | William Smith,EmbedIO contrib… | Optional dependency injection and Generic Host integration for EmbedIO-Neo. |
| 2026-10-05 09:05:18 | [Appliman.LongTaskNotifier](https://www.nuget.org/packages/Appliman.LongTaskNotifier) | 1.2.12 | Appliman | Composants Blazor pour la notification et le suivi de tâches longues dans les a… |
| 2026-10-05 09:05:20 | [Appliman.LongTaskNotifier.Abstractions](https://www.nuget.org/packages/Appliman.LongTaskNotifier.Abstractions) | 1.2.12 | Appliman | Abstractions pour la notification de tâches longues dans Appliman. Contient les… |
| 2026-10-05 09:05:21 | [Appliman.MetaEntityGenerator](https://www.nuget.org/packages/Appliman.MetaEntityGenerator) | 1.0.7 | Appliman | Meta Entity Generator |
| 2026-10-05 09:05:22 | [Appliman.MetaEntityGenerator.Abstraction](https://www.nuget.org/packages/Appliman.MetaEntityGenerator.Abstraction) | 1.0.7 | Appliman | Meta Entity Generator Abstraction |
| 2026-10-05 09:05:29 | [Astroway.Sdk](https://www.nuget.org/packages/Astroway.Sdk) | 0.1.0 | AstroWay | Official .NET client for the AstroWay astrology API: natal charts, synastry, tr… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

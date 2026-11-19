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

## Latest list — 2026-11-19 22:20 UTC

New packages created between 2026-11-19 21:21 UTC and 2026-11-19 22:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-19T22-20-22-370718Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-19 21:21:45 | [Nazor.Themes.Fluent](https://www.nuget.org/packages/Nazor.Themes.Fluent) | 0.1.0-alpha | Nazor | Optional Fluent theme for Nazor with private Fluent System Icons fonts and a ty… |
| 2026-11-19 21:25:02 | [Nazor.DevTools.Agent](https://www.nuget.org/packages/Nazor.DevTools.Agent) | 0.1.0-alpha | Nazor | Optional Nazor window diagnostics attachment, input inspection, overlays and fr… |
| 2026-11-19 21:25:21 | [Nazor.Graphics](https://www.nuget.org/packages/Nazor.Graphics) | 0.1.0-alpha | Nazor | Nazor: native desktop UI for .NET written with Razor components and NSS styles.… |
| 2026-11-19 21:25:23 | [Nazor.Hosting.Desktop.Windows](https://www.nuget.org/packages/Nazor.Hosting.Desktop.Windows) | 0.1.0-alpha | Nazor | Nazor desktop hosting with windows backends. |
| 2026-11-19 21:30:58 | [Nazor.Sdk](https://www.nuget.org/packages/Nazor.Sdk) | 0.1.0-alpha | Nazor | MSBuild project SDK for Nazor applications and component libraries: compiles .n… |
| 2026-11-19 21:34:45 | [Nazor.Layout](https://www.nuget.org/packages/Nazor.Layout) | 0.1.0-alpha | Nazor | Nazor: native desktop UI for .NET written with Razor components and NSS styles.… |
| 2026-11-19 21:34:51 | [Nazor.Platform.Windows](https://www.nuget.org/packages/Nazor.Platform.Windows) | 0.1.0-alpha | Nazor | Nazor: native desktop UI for .NET written with Razor components and NSS styles.… |
| 2026-11-19 21:35:05 | [Nazor.Style](https://www.nuget.org/packages/Nazor.Style) | 0.1.0-alpha | Nazor | Nazor: native desktop UI for .NET written with Razor components and NSS styles.… |
| 2026-11-19 21:35:16 | [Nazor.Themes.NazorLeaf](https://www.nuget.org/packages/Nazor.Themes.NazorLeaf) | 0.1.0-alpha | Nazor | NazorLeaf, the Nazor visual language: leaf corners, the seed selection mark, ac… |
| 2026-11-19 21:35:28 | [Nazor.DevTools.Protocol](https://www.nuget.org/packages/Nazor.DevTools.Protocol) | 0.1.0-alpha | Nazor | Versioned, platform-independent Nazor DevTools wire contracts and bounded JSON-… |
| 2026-11-19 21:35:30 | [Nazor.Hosting.Desktop](https://www.nuget.org/packages/Nazor.Hosting.Desktop) | 0.1.0-alpha | Nazor | Nazor desktop hosting with portable backends. |
| 2026-11-19 21:35:32 | [Nazor.Hosting.Windows](https://www.nuget.org/packages/Nazor.Hosting.Windows) | 0.1.0-alpha | Nazor | Nazor: native desktop UI for .NET written with Razor components and NSS styles.… |
| 2026-11-19 21:35:36 | [Nazor.Platform](https://www.nuget.org/packages/Nazor.Platform) | 0.1.0-alpha | Nazor | Nazor: native desktop UI for .NET written with Razor components and NSS styles.… |
| 2026-11-19 21:35:39 | [Nazor.Presentation](https://www.nuget.org/packages/Nazor.Presentation) | 0.1.0-alpha | Nazor | Nazor: native desktop UI for .NET written with Razor components and NSS styles.… |
| 2026-11-19 21:57:03 | [BbQ.MockLite.AutoFixture](https://www.nuget.org/packages/BbQ.MockLite.AutoFixture) | 2.0.1 | Jean Marc Mbouma | Freeze MockLite test doubles for injection by AutoFixture. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-25 21:20 UTC

New packages created between 2026-10-25 20:20 UTC and 2026-10-25 21:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-25T21-20-12-775697Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-25 20:24:26 | [Sidub.Platform.Search](https://www.nuget.org/packages/Sidub.Platform.Search) | 1.12.0 | Sidub Inc. | Package Description |
| 2026-10-25 20:24:28 | [Sidub.Platform.Search.AzureSearch](https://www.nuget.org/packages/Sidub.Platform.Search.AzureSearch) | 1.12.0 | Sidub Inc. | Package Description |
| 2026-10-25 20:32:16 | [aspneticons](https://www.nuget.org/packages/aspneticons) | 1.0.0 | aspneticons | 391 classic 16x16 ASP.NET Icons as GIFs, PNGs, and a CSS sprite sheet for class… |
| 2026-10-25 20:32:37 | [aspneticons.AspNetCore](https://www.nuget.org/packages/aspneticons.AspNetCore) | 1.0.0 | aspneticons | 391 classic 16x16 ASP.NET Icons as GIFs, PNGs, and a CSS sprite sheet for ASP.N… |
| 2026-10-25 20:51:59 | [Tesserae.Themes.Zeitung](https://www.nuget.org/packages/Tesserae.Themes.Zeitung) | 26.10.72826 | Curiosity GmbH | A broadsheet-newspaper Tesserae custom theme: off-white newsprint, serif text,… |
| 2026-10-25 20:52:09 | [Tesserae.Themes.Blaupause](https://www.nuget.org/packages/Tesserae.Themes.Blaupause) | 26.10.72826 | Curiosity GmbH | An engineering-blueprint Tesserae custom theme: Prussian-blue drafting paper wi… |
| 2026-10-25 20:52:20 | [Tesserae.Themes.Phosphor](https://www.nuget.org/packages/Tesserae.Themes.Phosphor) | 26.10.72826 | Curiosity GmbH | A character-terminal Tesserae custom theme: green phosphor on black glass with… |
| 2026-10-25 20:52:30 | [Tesserae.Themes.Glas](https://www.nuget.org/packages/Tesserae.Themes.Glas) | 26.10.72826 | Curiosity GmbH | A frosted-glass Tesserae custom theme: translucent blurred panels over a soft c… |
| 2026-10-25 20:52:43 | [Tesserae.Themes.Kontrast](https://www.nuget.org/packages/Tesserae.Themes.Kontrast) | 26.10.72826 | Curiosity GmbH | A high-contrast, accessibility-first Tesserae custom theme: AAA contrast, thick… |
| 2026-10-25 20:52:53 | [Tesserae.Themes.Memphis](https://www.nuget.org/packages/Tesserae.Themes.Memphis) | 26.10.72826 | Curiosity GmbH | A 1980s Memphis-style Tesserae custom theme: squiggles and confetti patterns, c… |
| 2026-10-25 20:53:04 | [Tesserae.Themes.Washi](https://www.nuget.org/packages/Tesserae.Themes.Washi) | 26.10.72826 | Curiosity GmbH | A Japanese paper-and-ink Tesserae custom theme: rice-paper texture, sumi-ink bl… |
| 2026-10-25 20:53:17 | [Tesserae.Themes.Graustufe](https://www.nuget.org/packages/Tesserae.Themes.Graustufe) | 26.10.72826 | Curiosity GmbH | An e-paper Tesserae custom theme: pure greys, no motion at all, dithered shadow… |
| 2026-10-25 20:53:29 | [Tesserae.Themes.Kristall](https://www.nuget.org/packages/Tesserae.Themes.Kristall) | 26.10.72826 | Curiosity GmbH | A desktop-glass Tesserae custom theme after the translucent macOS look: vibranc… |
| 2026-10-25 21:00:59 | [JetPack.Web](https://www.nuget.org/packages/JetPack.Web) | 0.1.0 | Martin Kirk | The JetPack theme of JetPack.Wpf for ASP.NET Core: CSS for every control, a dep… |
| 2026-10-25 21:05:43 | [BulletSharp.Double](https://www.nuget.org/packages/BulletSharp.Double) | 1.0.0 | vojnar-autonomous | Idiomatic, SWIG-like double-precision C# binding for the Bullet Physics Library… |
| 2026-10-25 21:09:54 | [PCox.ServiceDefaults](https://www.nuget.org/packages/PCox.ServiceDefaults) | 0.1.0 | Peter Cox | Shared Aspire service defaults for ASP.NET Core applications. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

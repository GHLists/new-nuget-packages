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

## Latest list — 2026-11-28 08:21 UTC

New packages created between 2026-11-28 07:19 UTC and 2026-11-28 08:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-28T08-21-50-889532Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-28 07:51:58 | [MfxHub.Sdk](https://www.nuget.org/packages/MfxHub.Sdk) | 0.1.0 | KUDMANI PTY LTD | Typed .NET client for the MFX Hub API: hosted trading terminals, market data, e… |
| 2026-11-28 07:53:36 | [NativeTheme.Avalonia](https://www.nuget.org/packages/NativeTheme.Avalonia) | 1.0.0 | NativeTheme.Avalonia contribu… | Avalonia styles that paint common controls with the current Windows UxTheme vis… |
| 2026-11-28 08:00:41 | [SqlQueryBuilderAot](https://www.nuget.org/packages/SqlQueryBuilderAot) | 1.0.0 | Amir Hesamian | A SQL query builder for AOT (Ahead-of-Time) compilation. |
| 2026-11-28 08:11:11 | [ClassPixelPro.ColorDocument.Avalonia](https://www.nuget.org/packages/ClassPixelPro.ColorDocument.Avalonia) | 11.0.3.4 | whistyun | Package Description |
| 2026-11-28 08:11:13 | [ClassPixelPro.ColorTextBlock.Avalonia](https://www.nuget.org/packages/ClassPixelPro.ColorTextBlock.Avalonia) | 11.0.3.4 | whistyun | Package Description |
| 2026-11-28 08:11:14 | [ClassPixelPro.Markdown.Avalonia](https://www.nuget.org/packages/ClassPixelPro.Markdown.Avalonia) | 11.0.3.4 | Bevan Arps(original),whistyun… | Markdown Controls for Avalonia |
| 2026-11-28 08:11:16 | [ClassPixelPro.Markdown.Avalonia.Html](https://www.nuget.org/packages/ClassPixelPro.Markdown.Avalonia.Html) | 11.0.3.4 | whistyun | html tag processor for Markdown.Avalonia |
| 2026-11-28 08:11:17 | [ClassPixelPro.Markdown.Avalonia.Svg](https://www.nuget.org/packages/ClassPixelPro.Markdown.Avalonia.Svg) | 11.0.3.4 | grifsun,whistyun | Package Description |
| 2026-11-28 08:11:21 | [ClassPixelPro.Markdown.Avalonia.SyntaxHigh](https://www.nuget.org/packages/ClassPixelPro.Markdown.Avalonia.SyntaxHigh) | 11.0.3.4 | whistyun | Package Description |
| 2026-11-28 08:11:23 | [ClassPixelPro.Markdown.Avalonia.Tight](https://www.nuget.org/packages/ClassPixelPro.Markdown.Avalonia.Tight) | 11.0.3.4 | Bevan Arps(original),whistyun | Markdown Controls for Avalonia |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-06 11:19 UTC

New packages created between 2026-10-06 10:19 UTC and 2026-10-06 11:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-06T11-19-19-962165Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-06 11:05:31 | [iPlus.Avalonia.iOS](https://www.nuget.org/packages/iPlus.Avalonia.iOS) | 12.2.903 | iPlus | iPlus fork of Avalonia - a cross-platform UI framework for .NET providing a fle… |
| 2026-10-06 11:06:05 | [iPlus.Avalonia.WinUI](https://www.nuget.org/packages/iPlus.Avalonia.WinUI) | 12.2.903 | iPlus | Windows App SDK (WinUI 3) integration for Avalonia, enabling Avalonia content t… |
| 2026-10-06 11:07:57 | [StanzaSharp](https://www.nuget.org/packages/StanzaSharp) | 0.1.0 | Jakob Boman | Stanza's English NLP pipeline in .NET: tokenization and sentence splitting, mul… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

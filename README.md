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

## Latest list — 2026-10-02 03:19 UTC

New packages created between 2026-10-02 02:21 UTC and 2026-10-02 03:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-02T03-19-45-875897Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-02 03:02:06 | [BrycensRanch.StaticLink.Avalonia.Native](https://www.nuget.org/packages/BrycensRanch.StaticLink.Avalonia.Native) | 12.1.3.1 | greepar | Static AvaloniaNative library for macOS Avalonia NativeAOT publishing. |
| 2026-10-02 03:11:45 | [Gori.CompressedStatics](https://www.nuget.org/packages/Gori.CompressedStatics) | 1.0.0 | Tim Koopman | Gori.CompressedStatics can compress selected static property or method values a… |
| 2026-10-02 03:15:17 | [Openquote.Gil](https://www.nuget.org/packages/Openquote.Gil) | 0.6.0 | iyulab | Suggested classification codes for a record being entered, learned from the vau… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

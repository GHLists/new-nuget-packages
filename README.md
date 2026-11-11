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

## Latest list — 2026-11-11 04:21 UTC

New packages created between 2026-11-11 03:19 UTC and 2026-11-11 04:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-11T04-21-51-052827Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-11 03:26:49 | [Doxify](https://www.nuget.org/packages/Doxify) | 1.2.1 | UDS | Doxify document engine (Rust core) for .NET. This package is the server-side PD… |
| 2026-11-11 03:27:15 | [Doxify.Blazor](https://www.nuget.org/packages/Doxify.Blazor) | 1.2.1 | UDS | Drop-in document editor component for Blazor and ASP.NET Core that opens and ed… |
| 2026-11-11 03:37:49 | [Aprillz.MewUI.MewvalonEdit](https://www.nuget.org/packages/Aprillz.MewUI.MewvalonEdit) | 0.22.1 | Aprillz | AvalonEdit-compatible editing components built on the MewUI text engine. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

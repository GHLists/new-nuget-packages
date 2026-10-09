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

## Latest list — 2026-10-09 13:20 UTC

New packages created between 2026-10-09 12:20 UTC and 2026-10-09 13:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-09T13-20-29-109951Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-09 12:22:55 | [Filestar.win-x64](https://www.nuget.org/packages/Filestar.win-x64) | 30.0.0 | Bosma Interactive AB | Filestar CLI for win-x64. Install the tool package 'Filestar' instead. |
| 2026-10-09 12:23:02 | [Filestar.win-x86](https://www.nuget.org/packages/Filestar.win-x86) | 30.0.0 | Bosma Interactive AB | Filestar CLI for win-x86. Install the tool package 'Filestar' instead. |
| 2026-10-09 12:23:08 | [Filestar.osx-x64](https://www.nuget.org/packages/Filestar.osx-x64) | 30.0.0 | Bosma Interactive AB | Filestar CLI for osx-x64. Install the tool package 'Filestar' instead. |
| 2026-10-09 12:23:14 | [Filestar.osx-arm64](https://www.nuget.org/packages/Filestar.osx-arm64) | 30.0.0 | Bosma Interactive AB | Filestar CLI for osx-arm64. Install the tool package 'Filestar' instead. |
| 2026-10-09 12:23:30 | [Filestar.linux-x64](https://www.nuget.org/packages/Filestar.linux-x64) | 30.0.0 | Bosma Interactive AB | Filestar CLI for linux-x64. Install the tool package 'Filestar' instead. |
| 2026-10-09 12:23:48 | [Filestar](https://www.nuget.org/packages/Filestar) | 30.0.0 | Bosma Interactive AB | Filestar converts, compresses, resizes, renames and transforms files: thousands… |
| 2026-10-09 12:36:02 | [FS.GG.Governance.Config](https://www.nuget.org/packages/FS.GG.Governance.Config) | 0.3.0 | FS-GG | Package Description |
| 2026-10-09 12:59:15 | [TensionDev.UUID.v8.CryptographicHash](https://www.nuget.org/packages/TensionDev.UUID.v8.CryptographicHash) | 0.1.0 | TensionDev amsga | TensionDev.UUID.v8.CryptographicHash is a .NET library that supports UUID versi… |
| 2026-10-09 13:00:06 | [GreatUtilities.Web.Api](https://www.nuget.org/packages/GreatUtilities.Web.Api) | 0.1.569-beta | Rodrigo Leal | Essencial tools to agile development. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

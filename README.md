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

## Latest list — 2026-10-26 17:21 UTC

New packages created between 2026-10-26 16:22 UTC and 2026-10-26 17:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-26T17-21-30-212362Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-26 16:27:17 | [PuneethDC.DotNetSearch](https://www.nuget.org/packages/PuneethDC.DotNetSearch) | 1.0.3 | Puneeth DC | Token-efficient MCP server for codebase search, NuGet decompilation, and deep P… |
| 2026-10-26 16:28:34 | [SoulRipper.Tool](https://www.nuget.org/packages/SoulRipper.Tool) | 0.1.3 | SuperJMN | Rips the music, jingles and sound effects of NES and Game Boy ROMs to VGM files… |
| 2026-10-26 16:28:54 | [RepoDocsCli](https://www.nuget.org/packages/RepoDocsCli) | 0.2.2 | RepoDocsCli | Agent docs (CLAUDE.md-style) stored as YAML feature files inside your repositor… |
| 2026-10-26 16:44:10 | [VisioForge.DotNet.Core.Redist.Base.arm64](https://www.nuget.org/packages/VisioForge.DotNet.Core.Redist.Base.arm64) | 2026.10.26 | VisioForge | Core DirectShow filters for the VisioForge .NET SDKs (Windows engines) on Windo… |
| 2026-10-26 16:44:43 | [VisioForge.DotNet.Core.Redist.VirtualCamera.arm64](https://www.nuget.org/packages/VisioForge.DotNet.Core.Redist.VirtualCamera.arm64) | 2026.10.26 | VisioForge | VisioForge Virtual Camera and virtual audio card DirectShow filters, with the a… |
| 2026-10-26 16:44:52 | [VisioForge.DotNet.Core.Redist.VLC.arm64](https://www.nuget.org/packages/VisioForge.DotNet.Core.Redist.VLC.arm64) | 2026.10.26 | VisioForge | libVLC and the VisioForge VLC Source DirectShow filter for the VisioForge .NET… |
| 2026-10-26 16:48:23 | [Pagehaus.Ssi](https://www.nuget.org/packages/Pagehaus.Ssi) | 0.1.0 | Pagehaus | Server Side Includes as Apache's mod_include does them (include, echo, set, con… |
| 2026-10-26 16:48:25 | [pagehaus](https://www.nuget.org/packages/pagehaus) | 0.1.0 | Pagehaus | Preview plain HTML sites with Server Side Includes, check them for broken links… |
| 2026-10-26 16:51:13 | [AiMetadataCleaner.UrlTools](https://www.nuget.org/packages/AiMetadataCleaner.UrlTools) | 0.1.0 | wangneo276-lgtm | Offline URL builder for AI Metadata Cleaner image, video, and PDF metadata page… |
| 2026-10-26 17:04:48 | [Octeka.Mirror](https://www.nuget.org/packages/Octeka.Mirror) | 1.0.0 | Patrick Robichaud | Command-line interface and console package manager for Octeka.Mirror. |
| 2026-10-26 17:04:50 | [Octeka.Mirror.Integration](https://www.nuget.org/packages/Octeka.Mirror.Integration) | 1.0.0 | Patrick Robichaud | Client integration library for applications managed by Octeka.Mirror, providing… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-20 05:22 UTC

New packages created between 2026-11-20 04:19 UTC and 2026-11-20 05:22 UTC.

[Full CSV](data/new-nuget-packages-2026-11-20T05-22-19-049265Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-20 04:37:42 | [EcoSQL.Dbms.PostgreSql](https://www.nuget.org/packages/EcoSQL.Dbms.PostgreSql) | 0.1.0 | Sleddie | Package Description |
| 2026-11-20 04:48:56 | [Krill](https://www.nuget.org/packages/Krill) | 1.3.0 | Chase Huegel | A zero-dependency, struct-based Entity-Component-System. |
| 2026-11-20 04:54:10 | [MacOSX.Symbols.Toolsets.win-x64](https://www.nuget.org/packages/MacOSX.Symbols.Toolsets.win-x64) | 23.1.3.14 | LLVM Project,DotNet-AGPL | LLVM dsymutil for the win-x64 host. Generates the .dSYM bundle when cross-compi… |
| 2026-11-20 04:54:17 | [MacOSX.Symbols.Toolsets.win-arm64](https://www.nuget.org/packages/MacOSX.Symbols.Toolsets.win-arm64) | 23.1.3.14 | LLVM Project,DotNet-AGPL | LLVM dsymutil for the win-arm64 host. Generates the .dSYM bundle when cross-com… |
| 2026-11-20 04:54:25 | [MacOSX.Symbols.Toolsets.linux-x64](https://www.nuget.org/packages/MacOSX.Symbols.Toolsets.linux-x64) | 23.1.3.14 | LLVM Project,DotNet-AGPL | LLVM dsymutil for the linux-x64 host (stripped). Generates the .dSYM bundle whe… |
| 2026-11-20 04:54:31 | [MacOSX.Symbols.Toolsets.linux-arm64](https://www.nuget.org/packages/MacOSX.Symbols.Toolsets.linux-arm64) | 23.1.3.14 | LLVM Project,DotNet-AGPL | LLVM dsymutil for the linux-arm64 host (stripped). Generates the .dSYM bundle w… |
| 2026-11-20 04:54:33 | [MacOSX.Symbols.Toolsets](https://www.nuget.org/packages/MacOSX.Symbols.Toolsets) | 23.1.3.14 | LLVM Project,DotNet-AGPL | Meta package: LLVM dsymutil for every supported host (win-x64, win-arm64, linux… |
| 2026-11-20 04:54:35 | [LLD.Link.Toolsets](https://www.nuget.org/packages/LLD.Link.Toolsets) | 23.1.3.14 | LLVM Project,DotNet-AGPL | Meta package: lld-link (LLD COFF linker) for every supported host (win-x64, win… |
| 2026-11-20 04:54:37 | [XWin.Store](https://www.nuget.org/packages/XWin.Store) | 0.10.0.14 | Microsoft,DotNet-AGPL | Meta package: Windows SDK/CRT import library store (xwin splat output) for ever… |
| 2026-11-20 05:00:25 | [CommunityToolkit.Aspire.Chroma](https://www.nuget.org/packages/CommunityToolkit.Aspire.Chroma) | 17.0.0 | Microsoft.Toolkit,dotnetfound… | A ChromaDB client that integrates with Aspire, including health checks, traces… |
| 2026-11-20 05:00:28 | [CommunityToolkit.Aspire.Hosting.Chroma](https://www.nuget.org/packages/CommunityToolkit.Aspire.Hosting.Chroma) | 17.0.0 | Microsoft.Toolkit,dotnetfound… | ChromaDB hosting support for Aspire. |
| 2026-11-20 05:00:31 | [CommunityToolkit.Aspire.Hosting.Flare](https://www.nuget.org/packages/CommunityToolkit.Aspire.Hosting.Flare) | 17.0.0 | Microsoft.Toolkit,dotnetfound… | Flare support for Aspire. Flare is a self-hosted, OpenTelemetry-native observab… |
| 2026-11-20 05:00:35 | [CommunityToolkit.Aspire.Hosting.Loki](https://www.nuget.org/packages/CommunityToolkit.Aspire.Hosting.Loki) | 17.0.0 | Microsoft.Toolkit,dotnetfound… | An Aspire hosting integration for the Grafana Loki log aggregation server. |
| 2026-11-20 05:00:45 | [CommunityToolkit.Aspire.Hosting.Tempo](https://www.nuget.org/packages/CommunityToolkit.Aspire.Hosting.Tempo) | 17.0.0 | Microsoft.Toolkit,dotnetfound… | An Aspire hosting integration for the Grafana Tempo distributed tracing backend. |
| 2026-11-20 05:15:09 | [Daniel15.TextMateSharp](https://www.nuget.org/packages/Daniel15.TextMateSharp) | 2.1.0-alpha1 | Daniel Peñalba | Temporary fork until https://github.com/danipen/TextMateSharp/pull/144 is merged |
| 2026-11-20 05:15:24 | [Daniel15.TextMateSharp.Markdown](https://www.nuget.org/packages/Daniel15.TextMateSharp.Markdown) | 2.1.0-alpha1 | Daniel Lo Nigro | Temporary fork until https://github.com/danipen/TextMateSharp/pull/144 is merged |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

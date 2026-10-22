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

## Latest list — 2026-10-22 19:21 UTC

New packages created between 2026-10-22 18:19 UTC and 2026-10-22 19:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-22T19-21-36-831848Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-22 18:19:39 | [NetApiFlow.Storage.SqlServer](https://www.nuget.org/packages/NetApiFlow.Storage.SqlServer) | 0.1.0 | Douglas Lima | Package Description |
| 2026-10-22 18:19:39 | [NetApiFlow.EntityFrameworkCore](https://www.nuget.org/packages/NetApiFlow.EntityFrameworkCore) | 0.1.0 | Douglas Lima | Package Description |
| 2026-10-22 18:19:40 | [NetApiFlow.Storage.PostgreSql](https://www.nuget.org/packages/NetApiFlow.Storage.PostgreSql) | 0.1.0 | Douglas Lima | Package Description |
| 2026-10-22 18:19:41 | [NetApiFlow](https://www.nuget.org/packages/NetApiFlow) | 0.1.0 | Douglas Lima | Package Description |
| 2026-10-22 18:19:41 | [NetApiFlow.Dashboard](https://www.nuget.org/packages/NetApiFlow.Dashboard) | 0.1.0 | Douglas Lima | Package Description |
| 2026-10-22 18:19:42 | [NetApiFlow.MediatR](https://www.nuget.org/packages/NetApiFlow.MediatR) | 0.1.0 | Douglas Lima | Package Description |
| 2026-10-22 18:20:34 | [Octeka.CodeAnalysis.Strings](https://www.nuget.org/packages/Octeka.CodeAnalysis.Strings) | 1.0.0 | Patrick Robichaud | Fast, flexible template string expansion library with configurable delimiters a… |
| 2026-10-22 18:20:34 | [Octeka.CodeAnalysis.Strings.Abstractions](https://www.nuget.org/packages/Octeka.CodeAnalysis.Strings.Abstractions) | 1.0.0 | Patrick Robichaud | Core abstractions and contracts for template string expansion and property reso… |
| 2026-10-22 18:26:06 | [SFSharp.Protocol](https://www.nuget.org/packages/SFSharp.Protocol) | 5.0.0 | AllahPower | Native-free SA-MP packet and RPC models, parsers and RakNet-compatible managed… |
| 2026-10-22 18:26:07 | [SFSharp.Abstractions](https://www.nuget.org/packages/SFSharp.Abstractions) | 5.0.0 | AllahPower | Managed plugin contracts for SF: GTA and SA-MP services, module lifecycle, stor… |
| 2026-10-22 18:28:00 | [InitializeNL.Dapper.TypeMapping](https://www.nuget.org/packages/InitializeNL.Dapper.TypeMapping) | 1.0.0 | Frank Hommers | Explicit column mapping for Dapper. Scans assemblies for types marked with [Tab… |
| 2026-10-22 18:36:22 | [Egami.Heic](https://www.nuget.org/packages/Egami.Heic) | 1.1.0 | Lars Dytterud | HEIC for Egami: reads HEIF files with HEVC-coded images, such as iPhone and And… |
| 2026-10-22 18:36:23 | [Egami.Cli](https://www.nuget.org/packages/Egami.Cli) | 1.1.0 | Lars Dytterud | The egami command: convert, inspect, resize and edit images from a shell or a b… |
| 2026-10-22 18:51:59 | [Egap.Preview](https://www.nuget.org/packages/Egap.Preview) | 2.1.0 | Lars Dytterud | egap-preview: a live preview of Egap documents on a local web page. It shows th… |
| 2026-10-22 18:58:40 | [Google.Apis.DisplayVideo.v5](https://www.nuget.org/packages/Google.Apis.DisplayVideo.v5) | 1.77.0.4309 | Google LLC | Google APIs Client Library for working with Displayvideo v5. Product documentat… |
| 2026-10-22 18:58:45 | [PdfPecker.Fluent](https://www.nuget.org/packages/PdfPecker.Fluent) | 1.19.0 | Moonwalker1307 | Fluent C# API for building PDFs with PdfPecker: pages, headers, footers, column… |
| 2026-10-22 18:58:52 | [AWSSDK.Continuum](https://www.nuget.org/packages/AWSSDK.Continuum) | 4.0.100 | Amazon Web Services | Releasing Continuum for Code Vulnerabilities APIs for SDKs |
| 2026-10-22 19:04:16 | [WpfToolkitAutoCompleteBoxExtended](https://www.nuget.org/packages/WpfToolkitAutoCompleteBoxExtended) | 1.0.0 | gszobi | The WPF Toolkit AutoCompleteBox (Ms-PL) for .NET 8 and .NET Framework 4.8, with… |
| 2026-10-22 19:05:21 | [JJMasterData.Data.SourceGenerators](https://www.nuget.org/packages/JJMasterData.Data.SourceGenerators) | 5.0.16 | JJMasterData.Data.SourceGener… | Incremental SQL result materializers for JJMasterData DataAccess. |
| 2026-10-22 19:13:18 | [Themis.Inference.Foundry](https://www.nuget.org/packages/Themis.Inference.Foundry) | 1.7.0 | Themis contributors | Optional Microsoft Foundry remote provider for typed Themis decisions. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

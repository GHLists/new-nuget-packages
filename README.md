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

## Latest list — 2026-10-19 15:19 UTC

New packages created between 2026-10-19 14:22 UTC and 2026-10-19 15:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-19T15-19-17-099687Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-19 14:28:55 | [ElBruno.MarkItDotNet.Markdown](https://www.nuget.org/packages/ElBruno.MarkItDotNet.Markdown) | 0.9.3 | Bruno Capuano (ElBruno) | Parse Markdown into structured MarkItDotNet documents using Markdig. |
| 2026-10-19 14:30:18 | [DevOpsTest.AiExternalNetLibrary](https://www.nuget.org/packages/DevOpsTest.AiExternalNetLibrary) | 1.0.4 | CH Robinson | Test Net External Library |
| 2026-10-19 14:41:53 | [CanopyX.Data](https://www.nuget.org/packages/CanopyX.Data) | 0.2.1 | Evotec | Server-side execution of the CanopyX remote grid protocol: typed request parsin… |
| 2026-10-19 14:41:55 | [CanopyX.AspNetCore](https://www.nuget.org/packages/CanopyX.AspNetCore) | 0.2.1 | Evotec | Minimal-API endpoints for the CanopyX remote grid protocol: query, value-list,… |
| 2026-10-19 14:45:29 | [Dloizides.ArchitectureTests](https://www.nuget.org/packages/Dloizides.ArchitectureTests) | 1.0.0 | DLoizides | House architecture rules as xUnit tests on ArchUnitNET. PAT-LAYER-1: Domain dep… |
| 2026-10-19 14:49:56 | [CriticalManufacturing.CLI.Core](https://www.nuget.org/packages/CriticalManufacturing.CLI.Core) | 6.0.0 | CriticalManufacturing | These are the core classes from Critical Manufacturing CLI. They serve as a bas… |
| 2026-10-19 14:50:39 | [ManagedCode.Orleans.RapidMembership](https://www.nuget.org/packages/ManagedCode.Orleans.RapidMembership) | 10.4.0 | ManagedCode,Reuben Bond | Self-hosted quorum membership and gateway discovery for Microsoft Orleans, base… |
| 2026-10-19 14:50:40 | [ManagedCode.Orleans.RapidMembership.Grpc](https://www.nuget.org/packages/ManagedCode.Orleans.RapidMembership.Grpc) | 10.4.0 | ManagedCode,Reuben Bond | gRPC transport for RAPID membership, based on Reuben Bond’s RapidCluster. |
| 2026-10-19 14:50:41 | [ManagedCode.Orleans.RapidMembership.Protocol](https://www.nuget.org/packages/ManagedCode.Orleans.RapidMembership.Protocol) | 10.4.0 | ManagedCode,Reuben Bond | RAPID group membership protocol from Reuben Bond’s RapidCluster, used by Manage… |
| 2026-10-19 15:06:28 | [AlchiwebApp.Cli](https://www.nuget.org/packages/AlchiwebApp.Cli) | 0.6.2.8 | Alchiweb | AlchiwebApp.Cli |
| 2026-10-19 15:06:37 | [Pixata.AspNetCore.Pdf.Playwright](https://www.nuget.org/packages/Pixata.AspNetCore.Pdf.Playwright) | 1.0.0 | Avrohom Yisroel Silver | Playwright and Chromium PDF converter for Pixata.AspNetCore's DocumentTemplateH… |
| 2026-10-19 15:08:17 | [RaTeX](https://www.nuget.org/packages/RaTeX) | 1.0.0 | Sylinko | Unofficial .NET bindings for the RaTeX (LaTeX math layout engine), providing im… |
| 2026-10-19 15:08:18 | [RaTeX.Avalonia](https://www.nuget.org/packages/RaTeX.Avalonia) | 1.0.0 | Sylinko | Render LaTeX math in Avalonia with RaTeX, including a formula control, reusable… |
| 2026-10-19 15:08:31 | [AlchiwebApp.Cli.Core](https://www.nuget.org/packages/AlchiwebApp.Cli.Core) | 0.6.2.8 | Alchiweb | AlchiwebApp.Cli.Core |
| 2026-10-19 15:09:00 | [Palanca.Client](https://www.nuget.org/packages/Palanca.Client) | 0.1.0 | Yann Roux | Client for Palanca, a self-hosted on/off feature flag service. Serves flags fro… |
| 2026-10-19 15:14:14 | [NanosSharp.Shared](https://www.nuget.org/packages/NanosSharp.Shared) | 0.2.0 | DasDarki | .NET scripting API shared by nanos world servers and game clients. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-05 16:22 UTC

New packages created between 2026-11-05 15:19 UTC and 2026-11-05 16:22 UTC.

[Full CSV](data/new-nuget-packages-2026-11-05T16-22-10-813842Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-05 15:28:43 | [Puppis.Contracts](https://www.nuget.org/packages/Puppis.Contracts) | 0.1.0 | NewWorldOrg | The contract between the Carina app and the Puppis driver: the endpoints, event… |
| 2026-11-05 15:28:45 | [Puppis.Driver](https://www.nuget.org/packages/Puppis.Driver) | 0.1.0 | NewWorldOrg | The Puppis driver as a library, so that the integration tests of an app that sp… |
| 2026-11-05 15:29:44 | [Fdw.Documents.Records](https://www.nuget.org/packages/Fdw.Documents.Records) | 1.5.0 | Fdw Team | Development tools and utilities for the Fdw ecosystem. |
| 2026-11-05 15:29:52 | [Fdw.TUI.Management.App](https://www.nuget.org/packages/Fdw.TUI.Management.App) | 1.5.0 | Fdw | Development tools and utilities for the Fdw ecosystem. |
| 2026-11-05 15:30:09 | [Fdw.Services.Tags](https://www.nuget.org/packages/Fdw.Services.Tags) | 1.5.0 | Fdw Team | Development tools and utilities for the Fdw ecosystem. |
| 2026-11-05 15:30:16 | [Fdw.Documents.Records.Abstractions](https://www.nuget.org/packages/Fdw.Documents.Records.Abstractions) | 1.5.0 | Fdw Team | Development tools and utilities for the Fdw ecosystem. |
| 2026-11-05 15:30:53 | [Fdw.Services.Tags.Abstractions](https://www.nuget.org/packages/Fdw.Services.Tags.Abstractions) | 1.5.0 | Fdw Team | Development tools and utilities for the Fdw ecosystem. |
| 2026-11-05 15:31:25 | [Fdw.Services.Tags.Endpoints](https://www.nuget.org/packages/Fdw.Services.Tags.Endpoints) | 1.5.0 | Fdw Team | Development tools and utilities for the Fdw ecosystem. |
| 2026-11-05 15:36:55 | [Pulumi.Labs.Huggingface](https://www.nuget.org/packages/Pulumi.Labs.Huggingface) | 0.1.0 | Pulumi Labs | Experimental: manage Hugging Face resources — Inference Endpoints, Spaces, and… |
| 2026-11-05 15:38:25 | [KenyaLocations](https://www.nuget.org/packages/KenyaLocations) | 0.1.0 | David Amunga | Kenyan administrative divisions (counties, sub-counties, constituencies, wards,… |
| 2026-11-05 15:39:40 | [Mnemosyne.NET.AgentFramework](https://www.nuget.org/packages/Mnemosyne.NET.AgentFramework) | 0.7.0 | Marcel Roozekrans | A Microsoft Agent Framework context provider that recalls Reasonlets into an ag… |
| 2026-11-05 15:43:23 | [KamoCore.Cli.linux-arm64](https://www.nuget.org/packages/KamoCore.Cli.linux-arm64) | 0.1.0 | KamoCore | Run KamoCore API Tester suites and UI Tester tracks from your own machine or pi… |
| 2026-11-05 15:43:38 | [KamoCore.Cli.linux-x64](https://www.nuget.org/packages/KamoCore.Cli.linux-x64) | 0.1.0 | KamoCore | Run KamoCore API Tester suites and UI Tester tracks from your own machine or pi… |
| 2026-11-05 15:43:51 | [KamoCore.Cli.osx-arm64](https://www.nuget.org/packages/KamoCore.Cli.osx-arm64) | 0.1.0 | KamoCore | Run KamoCore API Tester suites and UI Tester tracks from your own machine or pi… |
| 2026-11-05 15:44:03 | [KamoCore.Cli.osx-x64](https://www.nuget.org/packages/KamoCore.Cli.osx-x64) | 0.1.0 | KamoCore | Run KamoCore API Tester suites and UI Tester tracks from your own machine or pi… |
| 2026-11-05 15:44:18 | [KamoCore.Cli.win-x64](https://www.nuget.org/packages/KamoCore.Cli.win-x64) | 0.1.0 | KamoCore | Run KamoCore API Tester suites and UI Tester tracks from your own machine or pi… |
| 2026-11-05 15:44:20 | [KamoCore.Cli](https://www.nuget.org/packages/KamoCore.Cli) | 0.1.0 | KamoCore | Run KamoCore API Tester suites and UI Tester tracks from your own machine or pi… |
| 2026-11-05 16:09:45 | [AnerCloud.Sdk](https://www.nuget.org/packages/AnerCloud.Sdk) | 0.1.1 | Aner SoftEnv | SDK de Aner Cloud para .NET: archivos (FSV), secretos (SSV) y autenticación de… |
| 2026-11-05 16:09:58 | [hgFastWindows](https://www.nuget.org/packages/hgFastWindows) | 0.0.0.23 | FastHg | Native Mercurial (hg.exe) for Windows: drop-in replacement for hgWindows-* pack… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

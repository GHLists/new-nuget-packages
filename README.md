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

## Latest list — 2026-09-29 03:20 UTC

New packages created between 2026-09-29 02:22 UTC and 2026-09-29 03:20 UTC.

[Full CSV](data/new-nuget-packages-2026-09-29T03-20-12-140068Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-29 02:23:59 | [CasCap.Signalizr.Client.Testing](https://www.nuget.org/packages/CasCap.Signalizr.Client.Testing) | 0.1.1 | Alex Vincent | In-memory ISignalizrClient for testing signalizr consumers without a gateway: f… |
| 2026-09-29 02:27:32 | [Chargehand](https://www.nuget.org/packages/Chargehand) | 0.4.0 | chargehand contributors | MCP server and CLI that runs coding-agent workers on a codebase question and re… |
| 2026-09-29 02:27:33 | [Chargehand.Contracts](https://www.nuget.org/packages/Chargehand.Contracts) | 1.2.0-alpha | chargehand contributors | JSON Schemas request/v1, task-spec/v1, result/v1, run-status/v1 and preset/v1 f… |
| 2026-09-29 02:28:59 | [Indtec.ParallelBatch](https://www.nuget.org/packages/Indtec.ParallelBatch) | 0.1.0 | Indtec | Lightweight .NET library for parallel batch processing with bounded concurrency… |
| 2026-09-29 02:35:23 | [Deskcheck](https://www.nuget.org/packages/Deskcheck) | 0.0.1 | Deskcheck | Deskcheck — AI-driven GUI testing for Windows desktop apps (Delphi/VCL, WinForm… |
| 2026-09-29 03:03:57 | [LibTiffCore](https://www.nuget.org/packages/LibTiffCore) | 2.0.1 | MarsPanda | 高性能 BigTIFF/SVS 数字病理全片图像（Whole Slide Image）读取库（.NET Standard 2.0，跨平台）。 High-per… |
| 2026-09-29 03:04:14 | [LibCspCore](https://www.nuget.org/packages/LibCspCore) | 1.3.1 | MarsPanda | CSP 数字病理全片图像（Whole Slide Image）跨平台快速读取库（.NET Standard 2.0）。 遵循中华医学会病理学分会《CSP 数字… |
| 2026-09-29 03:05:25 | [Syncfusion.DocumentChunking.WinForms](https://www.nuget.org/packages/Syncfusion.DocumentChunking.WinForms) | 35.1.37 | Syncfusion Inc. | The Syncfusion® DocumentChunking library is a .NET Standard library that helps… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

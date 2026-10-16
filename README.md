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

## Latest list — 2026-10-16 12:22 UTC

New packages created between 2026-10-16 11:21 UTC and 2026-10-16 12:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-16T12-22-23-518711Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-16 11:30:37 | [Termina.Demo.Inline](https://www.nuget.org/packages/Termina.Demo.Inline) | 0.17.0 | Aaron Stannard | Reactive terminal UI (TUI) framework for .NET with custom ANSI rendering, MVVM… |
| 2026-10-16 11:40:07 | [MAFUtils.Tools](https://www.nuget.org/packages/MAFUtils.Tools) | 0.5.1 | Dean Chalk | Offline inspection of names, descriptions and input schemas for Microsoft.Exten… |
| 2026-10-16 11:45:06 | [KeelMatrix.LogSchema](https://www.nuget.org/packages/KeelMatrix.LogSchema) | 0.1.0 | KeelMatrix | Detects breaking changes in source-generated .NET structured logging contracts.… |
| 2026-10-16 11:46:01 | [Deidentify](https://www.nuget.org/packages/Deidentify) | 1.0.1 | Deidentify.NET contributors | A .NET port of Presidio: local, in-process PII and PHI detection and de-identif… |
| 2026-10-16 11:46:04 | [Deidentify.Imaging](https://www.nuget.org/packages/Deidentify.Imaging) | 1.0.1 | Deidentify.NET contributors | Image, PDF and DICOM redaction for Deidentify.NET, the .NET port of Presidio: l… |
| 2026-10-16 11:46:35 | [SGuard.AspNetCore](https://www.nuget.org/packages/SGuard.AspNetCore) | 1.0.0 | Selçuk Güral | Returns SGuard guard failures from ASP.NET Core as 400 Bad Request validation p… |
| 2026-10-16 12:00:12 | [ErinnTask](https://www.nuget.org/packages/ErinnTask) | 1.0.0 | Molth Nevin | Lightweight task-like asynchronous primitives and timer scheduling for .NET. |
| 2026-10-16 12:08:33 | [BTDB.LSM](https://www.nuget.org/packages/BTDB.LSM) | 35.11.3-preview | Boris Letocha | Log-structured merge tree implementation of the BTDB key value database stored… |
| 2026-10-16 12:08:36 | [BTDB.LSM.Azure](https://www.nuget.org/packages/BTDB.LSM.Azure) | 35.11.3-preview | Boris Letocha | Azure Blob Storage adapter for BTDB.LSM. |
| 2026-10-16 12:13:03 | [Xeniorn.ProcessTools](https://www.nuget.org/packages/Xeniorn.ProcessTools) | 0.1.0 | Juraj Ahel | Cross-platform (Windows, Linux) process monitoring: select processes by PID, na… |
| 2026-10-16 12:13:03 | [Xeniorn.ProcessTools.Persistence.Sqlite](https://www.nuget.org/packages/Xeniorn.ProcessTools.Persistence.Sqlite) | 0.1.0 | Juraj Ahel | SQLite storage for Xeniorn.ProcessTools: an EF Core DbContext designed to be in… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

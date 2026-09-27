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

## Latest list — 2026-09-27 12:20 UTC

New packages created between 2026-09-27 11:19 UTC and 2026-09-27 12:20 UTC.

[Full CSV](data/new-nuget-packages-2026-09-27T12-20-42-029144Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-27 11:39:25 | [Cratis.Screenplay.Contexts](https://www.nuget.org/packages/Cratis.Screenplay.Contexts) | 4.43.0 | all contributors | Portable runtime context contracts for Screenplay code bodies |
| 2026-09-27 11:46:30 | [FluentBgWords.DependencyInjection](https://www.nuget.org/packages/FluentBgWords.DependencyInjection) | 0.2.0 | Aleksandar Milev | Microsoft.Extensions.DependencyInjection integration for FluentBgWords: configu… |
| 2026-09-27 11:49:09 | [StingrayDbMasking.SqlServer](https://www.nuget.org/packages/StingrayDbMasking.SqlServer) | 1.1.0 | StingrayDbMasking contributors | SQL Server / Azure SQL provider for StingrayDbMasking using native Dynamic Data… |
| 2026-09-27 11:49:10 | [StingrayDbMasking](https://www.nuget.org/packages/StingrayDbMasking) | 1.1.0 | StingrayDbMasking contributors | All-in-one StingrayDbMasking package: database-level data masking engine, SQL S… |
| 2026-09-27 11:49:11 | [StingrayDbMasking.Core](https://www.nuget.org/packages/StingrayDbMasking.Core) | 1.1.0 | StingrayDbMasking contributors | Database-level data masking engine: schema discovery, masking profiles, script… |
| 2026-09-27 11:49:12 | [StingrayDbMasking.MySql](https://www.nuget.org/packages/StingrayDbMasking.MySql) | 1.1.0 | StingrayDbMasking contributors | MySQL / MariaDB provider for StingrayDbMasking using a masked-view schema and p… |
| 2026-09-27 11:49:13 | [StingrayDbMasking.Oracle](https://www.nuget.org/packages/StingrayDbMasking.Oracle) | 1.1.0 | StingrayDbMasking contributors | Oracle provider for StingrayDbMasking using native Oracle Data Redaction (DBMS_… |
| 2026-09-27 11:49:14 | [StingrayDbMasking.PostgreSql](https://www.nuget.org/packages/StingrayDbMasking.PostgreSql) | 1.1.0 | StingrayDbMasking contributors | PostgreSQL provider for StingrayDbMasking using the PostgreSQL Anonymizer exten… |
| 2026-09-27 11:49:16 | [StingrayDbMasking.Blazor](https://www.nuget.org/packages/StingrayDbMasking.Blazor) | 1.1.0 | StingrayDbMasking contributors | Blazor (Interactive Server) management UI for StingrayDbMasking: pick a connect… |
| 2026-09-27 11:50:50 | [ManagedBackgroundServices.RCL](https://www.nuget.org/packages/ManagedBackgroundServices.RCL) | 1.0.0 | Adam O'Neil | Blazor components for monitoring background job health |
| 2026-09-27 12:04:49 | [pdn-soundmodem-windows](https://www.nuget.org/packages/pdn-soundmodem-windows) | 0.81.0 | Tom Fanning M0LTE and Packet.… | Windows audio (WASAPI) and PTT (CM108/AIOC HID, serial) backends for pdn-soundm… |
| 2026-09-27 12:10:34 | [SyntaxEditor](https://www.nuget.org/packages/SyntaxEditor) | 1.0.0 | GreatBear | Lightweight, high-performance, self-drawn syntax-highlighting editor control fo… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

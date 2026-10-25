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

## Latest list — 2026-10-25 02:21 UTC

New packages created between 2026-10-25 01:21 UTC and 2026-10-25 02:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-25T02-21-51-46232Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-25 01:30:30 | [Laim.Hangfire.LiteDB](https://www.nuget.org/packages/Laim.Hangfire.LiteDB) | 1.0.0 | codeyu,Laim | LiteDB storage provider for Hangfire. Maintained fork of Hangfire.LiteDB. |
| 2026-10-25 01:31:41 | [Eyu.DatabaseAccessor.Sqlite](https://www.nuget.org/packages/Eyu.DatabaseAccessor.Sqlite) | 2.0.0 | Eyu | Package Description |
| 2026-10-25 01:31:46 | [Eyu.DatabaseAccessor.AspNetCore](https://www.nuget.org/packages/Eyu.DatabaseAccessor.AspNetCore) | 2.0.0 | Eyu | Package Description |
| 2026-10-25 01:44:39 | [Plgic.Dicom.Imaging](https://www.nuget.org/packages/Plgic.Dicom.Imaging) | 1.0.0 | Prologic SignTech | Decode and render DICOM images with Plgic.Dicom: native and compressed pixel da… |
| 2026-10-25 01:44:39 | [Plgic.Dicom](https://www.nuget.org/packages/Plgic.Dicom) | 1.0.0 | Prologic SignTech | High-throughput, low-allocation, fuzz-resistant DICOM toolkit for .NET: Part 10… |
| 2026-10-25 01:44:39 | [Plgic.Dicom.Web.AspNetCore](https://www.nuget.org/packages/Plgic.Dicom.Web.AspNetCore) | 1.0.0 | Prologic SignTech | DICOMweb (PS3.18) server building blocks for ASP.NET Core on Plgic.Dicom: app.M… |
| 2026-10-25 01:44:40 | [Plgic.Dicom.Web](https://www.nuget.org/packages/Plgic.Dicom.Web) | 1.0.0 | Prologic SignTech | DICOMweb for Plgic.Dicom: DICOM JSON Model and Native DICOM Model (XML) seriali… |
| 2026-10-25 01:48:53 | [Nops.Templates](https://www.nuget.org/packages/Nops.Templates) | 1.1.0 | Nops Contributors | dotnet new templates for a minimal web API and a worker service that load SOPS-… |
| 2026-10-25 02:11:13 | [LogsNet.EntityFrameworkCore](https://www.nuget.org/packages/LogsNet.EntityFrameworkCore) | 1.0.0 | LogsNet | LogsNet Entity Framework Core adapter: database command failures, SaveChanges f… |
| 2026-10-25 02:11:14 | [LogsNet.Serilog](https://www.nuget.org/packages/LogsNet.Serilog) | 1.0.0 | LogsNet | LogsNet Serilog preset: daily rolling file sink ready for LogsNet events (Logs/… |
| 2026-10-25 02:11:14 | [LogsNet.FluentValidation](https://www.nuget.org/packages/LogsNet.FluentValidation) | 1.0.0 | LogsNet | LogsNet FluentValidation adapter: report ValidationResult failures from manual… |
| 2026-10-25 02:11:15 | [Plgic.Activator](https://www.nuget.org/packages/Plgic.Activator) | 1.0.0 | Prologic SignTech | Activates Plgic.Dicom licenses on the machine that runs your application: shows… |
| 2026-10-25 02:11:15 | [LogsNet.HttpClient](https://www.nuget.org/packages/LogsNet.HttpClient) | 1.0.0 | LogsNet | LogsNet outbound HttpClient adapter: timeouts, DNS/network failures, and upstre… |
| 2026-10-25 02:11:16 | [LogsNet](https://www.nuget.org/packages/LogsNet) | 1.0.0 | LogsNet | Laravel-like error diagnostics for ASP.NET Core: validation, exceptions, and HT… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

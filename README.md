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

## Latest list — 2026-11-08 06:20 UTC

New packages created between 2026-11-08 05:19 UTC and 2026-11-08 06:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-08T06-20-30-738063Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-08 05:25:44 | [UtilityDelta.Honest.Runtime](https://www.nuget.org/packages/UtilityDelta.Honest.Runtime) | 1.0.0 | Tyson Brown | Result<T,E> and Panic: errors as values, and a FailFast abort for unrecoverable… |
| 2026-11-08 05:25:45 | [UtilityDelta.Honest.Analyzers](https://www.nuget.org/packages/UtilityDelta.Honest.Analyzers) | 1.0.0 | Tyson Brown | Roslyn analyzers that ban properties, throw, implicit operators and dynamic, so… |
| 2026-11-08 05:31:16 | [DbTest.MsSql.Dacpac](https://www.nuget.org/packages/DbTest.MsSql.Dacpac) | 0.3.0 | dbaitest | Deploys a SQL Server .dacpac (an SSDT / Microsoft.Build.Sql database project) i… |
| 2026-11-08 05:41:16 | [KeelMatrix.ForwardTrust](https://www.nuget.org/packages/KeelMatrix.ForwardTrust) | 0.1.0 | KeelMatrix | Verify ASP.NET Core forwarded-header trust behavior with executable integration… |
| 2026-11-08 05:44:28 | [Simulacra.Isolation](https://www.nuget.org/packages/Simulacra.Isolation) | 0.17.0 | Niklas Wendel | Simulacra.Isolation - simulate non-virtual members, sealed classes and statics… |
| 2026-11-08 05:50:44 | [KeelMatrix.AiToolContract](https://www.nuget.org/packages/KeelMatrix.AiToolContract) | 0.1.0 | KeelMatrix | Baseline and compatibility-check the model-visible contracts of Microsoft.Exten… |
| 2026-11-08 05:57:44 | [Twip.WinForms](https://www.nuget.org/packages/Twip.WinForms) | 0.1.0 | Jackson Casey | A WinForms DocumentEditor control over Twip.Core. |
| 2026-11-08 05:57:45 | [Twip.Core](https://www.nuget.org/packages/Twip.Core) | 0.1.0 | Jackson Casey | .NET SDK for the twip DOCX layout, editing and rendering engine. Native AOT com… |
| 2026-11-08 06:09:24 | [nextorm.extensions](https://www.nuget.org/packages/nextorm.extensions) | 1.0.9-rc5 | Alexey Shirshov | Public query-component extensions for Nextorm, including SelectWhereMinEx and S… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

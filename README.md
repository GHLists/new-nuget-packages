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

## Latest list — 2026-11-12 07:21 UTC

New packages created between 2026-11-12 06:21 UTC and 2026-11-12 07:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-12T07-21-06-127113Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-12 06:27:09 | [YS.Knife.Sms.Impl.Default](https://www.nuget.org/packages/YS.Knife.Sms.Impl.Default) | 0.0.142 | Pengbo Yang | Package Description |
| 2026-11-12 06:27:11 | [YS.Knife.Sms.Provider.Submail](https://www.nuget.org/packages/YS.Knife.Sms.Provider.Submail) | 0.0.142 | Pengbo Yang | Package Description |
| 2026-11-12 06:42:10 | [specs.BDD.VSTest](https://www.nuget.org/packages/specs.BDD.VSTest) | 0.9.0-rc | Joe Cleland (yozepi@gmail.com) | VSTest adapter for Specs.BDD: discovers and runs Specifications-based specs in… |
| 2026-11-12 06:42:11 | [specs.BDD.MTP](https://www.nuget.org/packages/specs.BDD.MTP) | 0.9.0-rc | Joe Cleland (yozepi@gmail.com) | Microsoft.Testing.Platform runner for Specs.BDD: discovers and runs Specificati… |
| 2026-11-12 06:42:11 | [specs.core](https://www.nuget.org/packages/specs.core) | 0.9.0-rc | Joe Cleland (yozepi@gmail.com) | Framework-agnostic core of the Specs BDD testing framework: hierarchical spec b… |
| 2026-11-12 06:42:12 | [specs.BDD.Templates](https://www.nuget.org/packages/specs.BDD.Templates) | 0.9.0-rc | Joe Cleland (yozepi@gmail.com) | dotnet new templates for Specs.BDD: scaffolds a ready-to-run spec project for t… |
| 2026-11-12 07:03:38 | [ScopeGate](https://www.nuget.org/packages/ScopeGate) | 1.0.0 | Yoshihiro Ito | A high-performance, non-reentrant FIFO asynchronous lock for .NET 10 and .NET 1… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

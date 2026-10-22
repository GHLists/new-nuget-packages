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

## Latest list — 2026-10-22 05:20 UTC

New packages created between 2026-10-22 04:19 UTC and 2026-10-22 05:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-22T05-20-45-214496Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-22 04:20:04 | [AcnhModding.EventFlowToCode.Core](https://www.nuget.org/packages/AcnhModding.EventFlowToCode.Core) | 1.0.0 | ACNH Modding | Compiler and decompiler for readable Nintendo EventFlow (.bfevfl) source. |
| 2026-10-22 04:26:10 | [GJJ.Keystone.Strategy](https://www.nuget.org/packages/GJJ.Keystone.Strategy) | 1.0.0 | GJJ.Keystone.Strategy | 业务启停策略契约与时间、渠道、工作日日历判断 |
| 2026-10-22 04:26:14 | [GJJ.Keystone.AspNetCore.Strategy](https://www.nuget.org/packages/GJJ.Keystone.AspNetCore.Strategy) | 1.0.0 | GJJ.Keystone.AspNetCore.Strat… | 业务启停策略执行、缓存及接口目录 |
| 2026-10-22 04:34:14 | [Tern.Cli.win-x64](https://www.nuget.org/packages/Tern.Cli.win-x64) | 0.1.0 | Mark Gibbons | Drop-in, Native AOT replacement for the Sitecore CLI. |
| 2026-10-22 04:34:16 | [Tern.Cli.linux-x64](https://www.nuget.org/packages/Tern.Cli.linux-x64) | 0.1.1 | Mark Gibbons | Drop-in, Native AOT replacement for the Sitecore CLI. |
| 2026-10-22 04:34:19 | [Tern.Cli.osx-x64](https://www.nuget.org/packages/Tern.Cli.osx-x64) | 0.1.1 | Mark Gibbons | Drop-in, Native AOT replacement for the Sitecore CLI. |
| 2026-10-22 04:34:20 | [Tern.Cli](https://www.nuget.org/packages/Tern.Cli) | 0.1.1 | Mark Gibbons | Drop-in, Native AOT replacement for the Sitecore CLI. |
| 2026-10-22 04:42:41 | [Polhem.DbManager](https://www.nuget.org/packages/Polhem.DbManager) | 1.8.0 | Polhem contributors | Polhem database manager, a dotnet tool invoked as `polhem-db`. Creates, checks… |
| 2026-10-22 04:42:45 | [Polhem.DefineEditor](https://www.nuget.org/packages/Polhem.DefineEditor) | 1.8.0 | Polhem contributors | Polhem DefineEditor, the desktop editor for Polhem definition files, as a dotne… |
| 2026-10-22 04:42:52 | [Polhem.Templates](https://www.nuget.org/packages/Polhem.Templates) | 1.8.0 | Polhem contributors | Project templates for Polhem. `dotnet new polhem-avalonia` creates an applicati… |
| 2026-10-22 04:42:56 | [Polhem.UI.Avalonia.Shell](https://www.nuget.org/packages/Polhem.UI.Avalonia.Shell) | 1.8.0 | Polhem contributors | A ready-made Avalonia front end for a Polhem backend: connect, sign in to a com… |
| 2026-10-22 04:47:31 | [NativeImpl](https://www.nuget.org/packages/NativeImpl) | 0.5.0 | dewf | Language-agnostic native bindings generator |
| 2026-10-22 05:01:47 | [DeBlasis.GhosttyVt](https://www.nuget.org/packages/DeBlasis.GhosttyVt) | 1.4.0 | Alessandro De Blasis | Unofficial .NET bindings for libghostty-vt — the standalone VT parser from the… |
| 2026-10-22 05:07:26 | [Oicana.Native.win-x64](https://www.nuget.org/packages/Oicana.Native.win-x64) | 0.10.0 | Oicana | Native library of Oicana for win-x64. The Oicana package references it; referen… |
| 2026-10-22 05:07:28 | [Oicana.Native.linux-arm64](https://www.nuget.org/packages/Oicana.Native.linux-arm64) | 0.10.0 | Oicana | Native library of Oicana for linux-arm64. The Oicana package references it; ref… |
| 2026-10-22 05:07:29 | [Oicana.Native.osx-x64](https://www.nuget.org/packages/Oicana.Native.osx-x64) | 0.10.0 | Oicana | Native library of Oicana for osx-x64. The Oicana package references it; referen… |
| 2026-10-22 05:07:29 | [Oicana.Core](https://www.nuget.org/packages/Oicana.Core) | 0.10.0 | Oicana | Managed part of Oicana, without native libraries. Either reference the Oicana p… |
| 2026-10-22 05:07:30 | [Oicana.Native.win-arm64](https://www.nuget.org/packages/Oicana.Native.win-arm64) | 0.10.0 | Oicana | Native library of Oicana for win-arm64. The Oicana package references it; refer… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

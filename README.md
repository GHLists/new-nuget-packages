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

## Latest list — 2026-11-20 04:19 UTC

New packages created between 2026-11-20 03:20 UTC and 2026-11-20 04:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-20T04-19-07-110736Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-20 03:20:38 | [FrugoCorp.AspNetCore.AutoDiscoveryIAM](https://www.nuget.org/packages/FrugoCorp.AspNetCore.AutoDiscoveryIAM) | 0.1.1 | FrugoCorp Team | Dynamic RBAC and JWT authentication for ASP.NET Core, with permissions auto-dis… |
| 2026-11-20 03:20:45 | [RoomTalkForCrestron](https://www.nuget.org/packages/RoomTalkForCrestron) | 1.22.8 | Solution AV Automation | Talk to your Crestron system in plain English. The RoomTalk for Crestron librar… |
| 2026-11-20 03:21:33 | [Misaki.CommandLine.Args](https://www.nuget.org/packages/Misaki.CommandLine.Args) | 1.0.0 | Misaki.CommandLine.Args | Package Description |
| 2026-11-20 03:26:03 | [Seawave.OpcUaHelperV2](https://www.nuget.org/packages/Seawave.OpcUaHelperV2) | 1.0.0 | Seawave | opc ua helper library for .NET 8 |
| 2026-11-20 03:39:48 | [YS.Knife.DependencyInjection](https://www.nuget.org/packages/YS.Knife.DependencyInjection) | 0.0.145 | Pengbo Yang | Package Description |
| 2026-11-20 04:04:10 | [PAN.PredicateToSql](https://www.nuget.org/packages/PAN.PredicateToSql) | 2.0.0 | Pedro Ávila Núñez | Extensiones para Dapper con soporte de expresiones lambda (igualdad, comparacio… |
| 2026-11-20 04:06:07 | [Gtk4.Forms.MarkupCompiler](https://www.nuget.org/packages/Gtk4.Forms.MarkupCompiler) | 1.0.0.26324 | Microsoft, Piero Viano | Build-time WPF XAML markup compiler for the Gtk4.Forms compatibility layer. |
| 2026-11-20 04:06:19 | [Gtk4.Forms.WindowsBase](https://www.nuget.org/packages/Gtk4.Forms.WindowsBase) | 1.0.0.26324 | Microsoft, Piero Viano | Package Description |
| 2026-11-20 04:06:24 | [Gtk4.Forms.Wpf](https://www.nuget.org/packages/Gtk4.Forms.Wpf) | 1.0.0.26324 | Microsoft, Piero Viano | Meta-package: add one PackageReference to run an existing WPF app on GTK 4 with… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

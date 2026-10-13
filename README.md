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

## Latest list — 2026-10-13 06:19 UTC

New packages created between 2026-10-13 05:19 UTC and 2026-10-13 06:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-13T06-19-22-829474Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-13 05:26:34 | [PulseSharp.PostgreSql](https://www.nuget.org/packages/PulseSharp.PostgreSql) | 0.4.0-alpha | Waqas Ahmad | PostgreSQL store for PulseSharp: durable events and jobs for servers, with seve… |
| 2026-10-13 05:29:14 | [chd.Hub.Base.Contracts](https://www.nuget.org/packages/chd.Hub.Base.Contracts) | 2.0.26286.160 | chd.Hub.Base.Contracts | Package Description |
| 2026-10-13 05:33:05 | [vinstall](https://www.nuget.org/packages/vinstall) | 1.0.0 | vinstall | Package Description |
| 2026-10-13 05:58:37 | [Tapis.Core.Reminders](https://www.nuget.org/packages/Tapis.Core.Reminders) | 1.0.0 | Tapis Organization | Tapis.Core notlar ve hatırlatıcılar modülü: kişisel notlar, hatırlatıcılar, ala… |
| 2026-10-13 06:03:37 | [Cronitor.TickerQ](https://www.nuget.org/packages/Cronitor.TickerQ) | 10.4.76 | gonace | Reports every TickerQ cron job to Cronitor: run when it starts, complete when i… |
| 2026-10-13 06:08:03 | [PixieInspector.ImGui](https://www.nuget.org/packages/PixieInspector.ImGui) | 0.1.0 | Rafael Sakamoto | The Dear ImGui view of PixieInspector, on Hexa.NET.ImGui: draws an inspector as… |
| 2026-10-13 06:08:03 | [PixieInspector](https://www.nuget.org/packages/PixieInspector) | 0.1.0 | Rafael Sakamoto | A reflection-based object inspector for .NET: point it at a type, bind one or m… |
| 2026-10-13 06:08:04 | [PixieInspector.Avalonia](https://www.nuget.org/packages/PixieInspector.Avalonia) | 0.1.0 | Rafael Sakamoto | The Avalonia view of PixieInspector: a property grid for an inspector, and the… |
| 2026-10-13 06:08:05 | [PixieInspector.Wpf](https://www.nuget.org/packages/PixieInspector.Wpf) | 0.1.0 | Rafael Sakamoto | The WPF view of PixieInspector: a property grid for an inspector, and the conve… |
| 2026-10-13 06:08:05 | [PixieInspector.WinForms](https://www.nuget.org/packages/PixieInspector.WinForms) | 0.1.0 | Rafael Sakamoto | The WinForms view of PixieInspector: a property grid for an inspector, and the… |
| 2026-10-13 06:13:56 | [KnOwl.ButterMorph.SampleTypes](https://www.nuget.org/packages/KnOwl.ButterMorph.SampleTypes) | 2.4.0 | Elysium Coding | Sample C# custom language types for KnOwl ButterMorph type bundle validation. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-12 18:21 UTC

New packages created between 2026-11-12 17:20 UTC and 2026-11-12 18:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-12T18-21-41-610865Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-12 17:29:28 | [DxFeed.Graal.Native.Oracle](https://www.nuget.org/packages/DxFeed.Graal.Native.Oracle) | 3.16.0-rc1 | dxFeed API Team | The native libraries of the dxFeed Graal Native SDK: the dxFeed Java API compil… |
| 2026-11-12 17:32:15 | [VisioForge.DotNet.VirtualCamera](https://www.nuget.org/packages/VisioForge.DotNet.VirtualCamera) | 2026.11.12 | VisioForge | VisioForge Virtual Camera SDK push API: send your own video frames and audio sa… |
| 2026-11-12 17:33:53 | [Ekom.Payments.U19](https://www.nuget.org/packages/Ekom.Payments.U19) | 1.0.0 | Vettvangur | Ekom Payments - Umbraco E-Commerce solution |
| 2026-11-12 17:36:33 | [DevelApp.PluginJobRunner.Executors](https://www.nuget.org/packages/DevelApp.PluginJobRunner.Executors) | 1.0.0 | Lars Shakya Buch-Jepsen | Sample job executor plugins for PluginJobRunner (MergeSortArray), demonstrating… |
| 2026-11-12 17:36:33 | [DevelApp.PluginJobRunner.Interface](https://www.nuget.org/packages/DevelApp.PluginJobRunner.Interface) | 1.0.0 | Lars Shakya Buch-Jepsen | Job executor contract for PluginJobRunner: IJobExecutor, IJobExecutionContext a… |
| 2026-11-12 17:36:34 | [DevelApp.PluginJobRunner.Model](https://www.nuget.org/packages/DevelApp.PluginJobRunner.Model) | 1.0.0 | Lars Shakya Buch-Jepsen | Domain and persistence model for PluginJobRunner: job entities and the EF Core… |
| 2026-11-12 17:38:01 | [ForkForward.Mediator.Contracts](https://www.nuget.org/packages/ForkForward.Mediator.Contracts) | 2.6.0 | ForkForward | ForkForward.Mediator.Contracts is the contracts package of ForkForward.Mediator… |
| 2026-11-12 17:41:02 | [STS2.RitsuLib.Compat.0.111.0](https://www.nuget.org/packages/STS2.RitsuLib.Compat.0.111.0) | 0.6.11 | OLC | Shared framework library for Slay the Spire 2 mods. |
| 2026-11-12 17:44:41 | [Co.Revington.Sightline.Hosting](https://www.nuget.org/packages/Co.Revington.Sightline.Hosting) | 0.3.0 | Ravindu Wijegunawardhana | Add it to the app you run, and Sightline, a live and editable map of your .NET… |
| 2026-11-12 17:51:45 | [KumikoUI.Uno](https://www.nuget.org/packages/KumikoUI.Uno) | 0.2.0 | Eight-Bot, Inc.,Michael Stonis | A high-performance, fully custom-drawn KumikoUI DataGrid control for the Uno Pl… |
| 2026-11-12 18:03:39 | [Concord.Waylith](https://www.nuget.org/packages/Concord.Waylith) | 0.32.1 | Concord.Waylith | Body-replacement backend for Concord, for hosts running the WaylithCLR fork of… |
| 2026-11-12 18:03:39 | [Concord.MonoMod](https://www.nuget.org/packages/Concord.MonoMod) | 0.32.1 | Concord.MonoMod | Emit backend for Concord on .NET Framework and mono runtimes, where there is no… |
| 2026-11-12 18:05:51 | [Exchange56.CareerProfile.ClientSdk](https://www.nuget.org/packages/Exchange56.CareerProfile.ClientSdk) | 1.0.0 | T.J. McNaboe | Career profile client library for Exchange56 content APIs. |
| 2026-11-12 18:06:28 | [Exchange56.CareerProfile.Components](https://www.nuget.org/packages/Exchange56.CareerProfile.Components) | 1.0.0 | T.J. McNaboe | Career profile Components library for Exchange56 content APIs. |
| 2026-11-12 18:13:35 | [InstructorSharp.FluentValidation](https://www.nuget.org/packages/InstructorSharp.FluentValidation) | 0.1.0 | Faseeh Ullah Jafar | FluentValidation adapter for InstructorSharp. Use your existing AbstractValidat… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

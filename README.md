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

## Latest list — 2026-11-14 20:21 UTC

New packages created between 2026-11-14 19:21 UTC and 2026-11-14 20:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-14T20-21-38-283534Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-14 19:31:42 | [Transiever.Common.Cli](https://www.nuget.org/packages/Transiever.Common.Cli) | 1.2.0 | Transiever.Common.Cli | Stateless secret-input mechanics for Transiever command-line tools. |
| 2026-11-14 19:34:45 | [SkyeTechnology.Umbraco.ResourceSpace](https://www.nuget.org/packages/SkyeTechnology.Umbraco.ResourceSpace) | 1.0.0 | Skye Technology | Bring Your Own DAM: ResourceSpace connector for Umbraco 17+ by Skye Technology,… |
| 2026-11-14 19:37:37 | [SignalMoat.AspNetCore](https://www.nuget.org/packages/SignalMoat.AspNetCore) | 0.3.1 | Siddharth Saraf | SignalMoat middleware for ASP.NET Core: verify AI agents, enforce per-agent pol… |
| 2026-11-14 19:38:03 | [BorrowedTorch.MonoGame.Content.Builder.Compute](https://www.nuget.org/packages/BorrowedTorch.MonoGame.Content.Builder.Compute) | 3.8.6.101 | Elzianor, cpt-max, MonoGame T… | The MonoGame 3.8.6.1 Content Builder (MGCB) command line tool, built from Borro… |
| 2026-11-14 19:38:04 | [BorrowedTorch.MonoGame.Content.Builder.Task.Compute](https://www.nuget.org/packages/BorrowedTorch.MonoGame.Content.Builder.Task.Compute) | 3.8.6.101 | Elzianor, cpt-max, MonoGame T… | MSBuild task to automatically build content for MonoGame, with BorrowedTorch's… |
| 2026-11-14 19:39:10 | [Pervaxis.Genesis.Secrets](https://www.nuget.org/packages/Pervaxis.Genesis.Secrets) | 3.4.5 | Clarivex Technologies | Package Description |
| 2026-11-14 19:39:12 | [Pervaxis.Genesis.Secrets.AWS](https://www.nuget.org/packages/Pervaxis.Genesis.Secrets.AWS) | 3.4.5 | Clarivex Technologies | Package Description |
| 2026-11-14 19:39:13 | [Pervaxis.Genesis.Parameters](https://www.nuget.org/packages/Pervaxis.Genesis.Parameters) | 3.4.5 | Clarivex Technologies | Package Description |
| 2026-11-14 19:39:13 | [Pervaxis.Genesis.Parameters.AWS](https://www.nuget.org/packages/Pervaxis.Genesis.Parameters.AWS) | 3.4.5 | Clarivex Technologies | Package Description |
| 2026-11-14 19:40:14 | [Caprine.Durations](https://www.nuget.org/packages/Caprine.Durations) | 0.1.0 | Caprine Logic | Compile-time duration literals and calendar arithmetic for .NET. |
| 2026-11-14 19:47:47 | [NinePatch.Core](https://www.nuget.org/packages/NinePatch.Core) | 2.1.0 | Duško | Nine-patch (.9.png) rendering for .NET, backed by a native C++ renderer. UI-fra… |
| 2026-11-14 19:47:50 | [NinePatchWpf](https://www.nuget.org/packages/NinePatchWpf) | 2.1.0 | Duško | WPF controls skinned with nine-patch (.9.png) images: button, toggle, check box… |
| 2026-11-14 19:59:31 | [Domore.Logs.Windows](https://www.nuget.org/packages/Domore.Logs.Windows) | 11.1.0 | Ken Yourek | Do more logs in WPF |
| 2026-11-14 20:10:47 | [AviSynthApi](https://www.nuget.org/packages/AviSynthApi) | 1.0.0 | Etienne Charland | Managed AviSynth+ script evaluation, video frames, interleaved audio samples, a… |
| 2026-11-14 20:11:09 | [VapourSynthApi](https://www.nuget.org/packages/VapourSynthApi) | 1.0.0 | Etienne Charland | Managed VapourSynth 4 script evaluation, video and planar audio frames, ordered… |
| 2026-11-14 20:11:38 | [FitnessClub.Generic](https://www.nuget.org/packages/FitnessClub.Generic) | 1.0.0 | Kristina Stetsiuk | Reusable base types: Entity, Person, IBookable and a generic in-memory reposito… |
| 2026-11-14 20:13:41 | [nDAWControls](https://www.nuget.org/packages/nDAWControls) | 1.0.0 | Duško Žigić | WPF controls for DAW and MIDI applications: knobs, faders, meters, channel stri… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

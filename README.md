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

## Latest list — 2026-10-03 15:19 UTC

New packages created between 2026-10-03 14:22 UTC and 2026-10-03 15:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-03T15-19-25-031344Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-03 14:25:30 | [StyleCopNext.Analyzers](https://www.nuget.org/packages/StyleCopNext.Analyzers) | 1.0.1 | Sam Harwell et. al., Alexande… | StyleCop's rules as Roslyn analyzers and code fixes. A maintained continuation… |
| 2026-10-03 14:45:27 | [2dog.android-arm64](https://www.nuget.org/packages/2dog.android-arm64) | 4.7.2.15 | Moritz Voss | Experimental Android arm64 runtime variants. Requires 2dog.android for Java hos… |
| 2026-10-03 14:45:29 | [2dog.android-arm64.debug](https://www.nuget.org/packages/2dog.android-arm64.debug) | 4.7.2.15 | Moritz Voss | Experimental Android arm64 debug Godot JNI runtime and C++ runtime for .NET And… |
| 2026-10-03 14:45:32 | [2dog.android-arm64.release](https://www.nuget.org/packages/2dog.android-arm64.release) | 4.7.2.15 | Moritz Voss | Experimental Android arm64 release Godot JNI runtime and C++ runtime for .NET A… |
| 2026-10-03 14:45:33 | [2dog.android-x64](https://www.nuget.org/packages/2dog.android-x64) | 4.7.2.15 | Moritz Voss | Experimental Android x64 runtime variants. Requires 2dog.android for Java host… |
| 2026-10-03 14:45:35 | [2dog.android-x64.debug](https://www.nuget.org/packages/2dog.android-x64.debug) | 4.7.2.15 | Moritz Voss | Experimental Android x64 debug Godot JNI runtime and C++ runtime for .NET Andro… |
| 2026-10-03 14:45:38 | [2dog.android-x64.release](https://www.nuget.org/packages/2dog.android-x64.release) | 4.7.2.15 | Moritz Voss | Experimental Android x64 release Godot JNI runtime and C++ runtime for .NET And… |
| 2026-10-03 14:45:39 | [2dog.android](https://www.nuget.org/packages/2dog.android) | 4.7.2.15 | Moritz Voss | Experimental Android Java host and APK build targets for 2dog. Requires an Andr… |
| 2026-10-03 15:04:10 | [PolyhydraGames.Auth.Abstractions](https://www.nuget.org/packages/PolyhydraGames.Auth.Abstractions) | 1.1.7 | Polyhydra Games | OAuth contracts and token models shared by PolyhydraGames auth flows. |
| 2026-10-03 15:04:12 | [PolyhydraGames.Platforms.Abstractions](https://www.nuget.org/packages/PolyhydraGames.Platforms.Abstractions) | 1.1.7 | Polyhydra Games | Shared platform identity and user primitives for PolyhydraGames adapters. |
| 2026-10-03 15:04:14 | [PolyhydraGames.Chat.Abstractions](https://www.nuget.org/packages/PolyhydraGames.Chat.Abstractions) | 1.1.7 | Polyhydra Games | Chat DTOs shared by PolyhydraGames chat adapters and services. |
| 2026-10-03 15:04:16 | [PolyhydraGames.Commands.Core](https://www.nuget.org/packages/PolyhydraGames.Commands.Core) | 1.1.7 | Polyhydra Games | Command parsing and command outcome helpers for PolyhydraGames chat surfaces. |
| 2026-10-03 15:04:18 | [PolyhydraGames.PostOffice.Abstractions](https://www.nuget.org/packages/PolyhydraGames.PostOffice.Abstractions) | 1.1.7 | Polyhydra Games | Contracts for routing inbound and outbound messages across platform adapters. |
| 2026-10-03 15:04:20 | [PolyhydraGames.PostOffice.Core](https://www.nuget.org/packages/PolyhydraGames.PostOffice.Core) | 1.1.7 | Polyhydra Games | Core Post Office routing and sink/source helpers for PolyhydraGames adapters. |
| 2026-10-03 15:05:32 | [PolyhydraGames.APi.Youtube](https://www.nuget.org/packages/PolyhydraGames.APi.Youtube) | 2.0.0 | Breadcrumb | A set of helpers to simplify analyzing youtube channel videos. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-04 13:19 UTC

New packages created between 2026-10-04 12:19 UTC and 2026-10-04 13:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-04T13-19-07-316264Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-04 12:24:04 | [Weasel.Firebird](https://www.nuget.org/packages/Weasel.Firebird) | 9.39.0 | Jeremy D. Miller,Babu Annamal… | Firebird 3, 4 and 5 Support and Schema Migration for Weasel |
| 2026-10-04 12:30:07 | [Soenneker.Threads.OpenApiClientUtil](https://www.nuget.org/packages/Soenneker.Threads.OpenApiClientUtil) | 4.0.2 | Jake Soenneker | A thread-safe utility for obtaining Threads's OpenApiClient singleton. |
| 2026-10-04 12:44:04 | [Pmad.Git.CliEmulator](https://www.nuget.org/packages/Pmad.Git.CliEmulator) | 0.2.7 | Julien Etelain | Managed Git CLI emulator for AI agents. Wraps Pmad.Git with a git-command surfa… |
| 2026-10-04 12:44:05 | [Pmad.Git.CliEmulator.AI](https://www.nuget.org/packages/Pmad.Git.CliEmulator.AI) | 0.2.7 | Julien Etelain | Microsoft.Extensions.AI integration for Pmad.Git.CliEmulator. Exposes the Git C… |
| 2026-10-04 12:44:17 | [I18Next.Net.Generators](https://www.nuget.org/packages/I18Next.Net.Generators) | 2.0.0 | DarkLiKally | Source generator creating typed translation keys and accessors from i18next JSO… |
| 2026-10-04 12:44:17 | [I18Next.Net.Yaml](https://www.nuget.org/packages/I18Next.Net.Yaml) | 2.0.0 | DarkLiKally | Backend for I18Next.Net reading YAML translation files. |
| 2026-10-04 12:57:13 | [HFAsif.WinUIShell.Maui](https://www.nuget.org/packages/HFAsif.WinUIShell.Maui) | 1.0.1 | HFAsif | Reusable Windows 11 / WinUI 3 inspired shell for .NET MAUI. Provides adaptive n… |
| 2026-10-04 13:01:20 | [tryAGI.WebRTC](https://www.nuget.org/packages/tryAGI.WebRTC) | 0.1.1 | tryAGI and contributors | MIT WebRTC transport for .NET 10: bounded ICE/STUN/TURN, fingerprint-authentica… |
| 2026-10-04 13:04:13 | [Cybrex.Core](https://www.nuget.org/packages/Cybrex.Core) | 1.0.1 | Revekhrell | Ядро фреймворка Cybrex |
| 2026-10-04 13:04:49 | [Novolis.Maui.Activation](https://www.nuget.org/packages/Novolis.Maui.Activation) | 2026.1.1.58 | Novolis | Generic MAUI file-activation inbox and pending-publish bridge for single-projec… |
| 2026-10-04 13:08:10 | [KirisameY.BindingBridge.NotifiableCollections](https://www.nuget.org/packages/KirisameY.BindingBridge.NotifiableCollections) | 0.0.1 | KirisameY.BindingBridge.Notif… | Package Description |
| 2026-10-04 13:09:13 | [Plain.HttpClientFactory](https://www.nuget.org/packages/Plain.HttpClientFactory) | 1.0.0 | Dmitrii Bychenko | A simple and lightweight HttpClientFactory implementation for .NET |
| 2026-10-04 13:11:10 | [Epsilon.LinearAlgebra](https://www.nuget.org/packages/Epsilon.LinearAlgebra) | 1.0.0 | Max Zakharov | Linear algebra for the Epsilon symbolic math library: immutable matrices and ve… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-09-28 10:20 UTC

New packages created between 2026-09-28 09:23 UTC and 2026-09-28 10:20 UTC.

[Full CSV](data/new-nuget-packages-2026-09-28T10-20-11-677741Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-28 09:28:35 | [Shark.PDFMerge](https://www.nuget.org/packages/Shark.PDFMerge) | 0.1.0 | Qumbar Raza | A dependency-free, from-scratch PDF engine for .NET: read, write, and merge PDF… |
| 2026-09-28 09:29:07 | [ReactiveUI.Primitives.Uno](https://www.nuget.org/packages/ReactiveUI.Primitives.Uno) | 8.4.0 | ReactiveUI Association Inc | Uno Platform dispatcher queue integration sequencers for ReactiveUI.Primitives. |
| 2026-09-28 09:29:08 | [ReactiveUI.Primitives.Uno.Reactive](https://www.nuget.org/packages/ReactiveUI.Primitives.Uno.Reactive) | 8.4.0 | ReactiveUI Association Inc | Uno Platform dispatcher queue scheduler for ReactiveUI.Primitives, recompiled a… |
| 2026-09-28 09:30:24 | [Anis.Partners](https://www.nuget.org/packages/Anis.Partners) | 1.0.0 | Anis | Client SDK for the Anis Partner API: RFC 9421 request signing, response verific… |
| 2026-09-28 09:40:52 | [DressSharp.win-x64](https://www.nuget.org/packages/DressSharp.win-x64) | 0.1.0 | Simon Oxtoby | A syntax-only, explicitly configured C# formatter. |
| 2026-09-28 09:40:54 | [DressSharp.linux-x64](https://www.nuget.org/packages/DressSharp.linux-x64) | 0.1.0 | Simon Oxtoby | A syntax-only, explicitly configured C# formatter. |
| 2026-09-28 09:40:56 | [DressSharp.osx-x64](https://www.nuget.org/packages/DressSharp.osx-x64) | 0.1.0 | Simon Oxtoby | A syntax-only, explicitly configured C# formatter. |
| 2026-09-28 09:40:58 | [DressSharp.osx-arm64](https://www.nuget.org/packages/DressSharp.osx-arm64) | 0.1.0 | Simon Oxtoby | A syntax-only, explicitly configured C# formatter. |
| 2026-09-28 09:40:59 | [DressSharp](https://www.nuget.org/packages/DressSharp) | 0.1.0 | Simon Oxtoby | A syntax-only, explicitly configured C# formatter. |
| 2026-09-28 09:42:02 | [WebWpfWindow](https://www.nuget.org/packages/WebWpfWindow) | 1.0.0 | WebWpfWindow | Package Description |
| 2026-09-28 09:43:14 | [Sagittaras.GuardClauses](https://www.nuget.org/packages/Sagittaras.GuardClauses) | 1.1.3 | Sagittaras Games | Lightweight guard clause pattern for defensive programming. |
| 2026-09-28 09:43:41 | [Sagittaras.Dices](https://www.nuget.org/packages/Sagittaras.Dices) | 1.1.3 | Sagittaras Games | Dice rolling and randomness abstractions for game logic. |
| 2026-09-28 09:43:49 | [Sagittaras.Messaging](https://www.nuget.org/packages/Sagittaras.Messaging) | 1.1.3 | Sagittaras Games | Mediator Pattern created for game development. |
| 2026-09-28 09:44:03 | [Sagittaras.Progression](https://www.nuget.org/packages/Sagittaras.Progression) | 1.1.4 | Sagittaras Games | Level and experience progression for games. |
| 2026-09-28 09:44:07 | [Sagittaras.Timing](https://www.nuget.org/packages/Sagittaras.Timing) | 1.1.4 | Sagittaras Games | Lightweight timer primitives for interval tracking, cooldown management, and ca… |
| 2026-09-28 09:56:48 | [SovietManager.Engine](https://www.nuget.org/packages/SovietManager.Engine) | 1.0.0 | Emogital | Host-agnostic game engine: protocol actions in, GameState mutation and domain e… |
| 2026-09-28 09:59:00 | [SovietManager.Engine.Configuration.Json](https://www.nuget.org/packages/SovietManager.Engine.Configuration.Json) | 1.0.0 | Emogital | JSON factory for SovietManager.Engine configuration. Returns a ready IConfigPro… |
| 2026-09-28 10:01:28 | [StingrayDbMasking.AspNetCore](https://www.nuget.org/packages/StingrayDbMasking.AspNetCore) | 1.2.1 | StingrayDbMasking contributors | ASP.NET Core server integration for StingrayDbMasking: the backend HTTP API (Ma… |
| 2026-09-28 10:09:25 | [OnTheFlySettings.AzureKeyVault.Client](https://www.nuget.org/packages/OnTheFlySettings.AzureKeyVault.Client) | 1.0.0 | Shantanu | Client for OnTheFlySettings endpoints. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

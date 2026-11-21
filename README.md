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

## Latest list — 2026-11-21 21:20 UTC

New packages created between 2026-11-21 20:21 UTC and 2026-11-21 21:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-21T21-20-32-166282Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-21 20:30:51 | [TQLApp.Plugins.YouTrack](https://www.nuget.org/packages/TQLApp.Plugins.YouTrack) | 0.11.0 | Pieter van Ginkel | Techie's Quick Launcher plugin for YouTrack by JetBrains. |
| 2026-11-21 20:36:31 | [KatziPackage](https://www.nuget.org/packages/KatziPackage) | 1.0.0 | AaronoLW | Simple library for parsing .kpg (KatziPackage) files |
| 2026-11-21 20:39:51 | [MagicCSharp.Generators](https://www.nuget.org/packages/MagicCSharp.Generators) | 1.1.1 | MagicCSharp Contributors | Source generators for a MagicCSharp codebase. The compiler writes use case inte… |
| 2026-11-21 20:39:52 | [MagicCSharp.Clients](https://www.nuget.org/packages/MagicCSharp.Clients) | 1.1.1 | MagicCSharp Contributors | Typed HTTP clients for calling another service, written by the compiler: mark a… |
| 2026-11-21 20:39:56 | [MagicCSharp.Testing.Clients](https://www.nuget.org/packages/MagicCSharp.Testing.Clients) | 1.1.1 | MagicCSharp Contributors | Checks MagicCSharp clients against the service they call: a server's test proje… |
| 2026-11-21 20:46:43 | [Egehan.Cli](https://www.nuget.org/packages/Egehan.Cli) | 0.1.0 | Bedirhan Gurler | Turn a project's git history into a living chronicle — offline, deterministic,… |
| 2026-11-21 21:00:40 | [Sundew.Injection](https://www.nuget.org/packages/Sundew.Injection) | 0.1.0 | Kim Hugener-Ohlsen | Sundew.Injection is a dependency injection framework, that generates factories… |
| 2026-11-21 21:04:21 | [GrayMint.Common.Acme](https://www.nuget.org/packages/GrayMint.Common.Acme) | 2.1.315 | GrayMint | Let's Encrypt certificates over ACME's HTTP-01 challenge: the account, the orde… |
| 2026-11-21 21:06:23 | [FakeEmailPro](https://www.nuget.org/packages/FakeEmailPro) | 0.1.0 | fake-email.pro | The official .NET client for the fake-email.pro API: create a disposable mailbo… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

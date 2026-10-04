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

## Latest list — 2026-10-04 22:20 UTC

New packages created between 2026-10-04 21:19 UTC and 2026-10-04 22:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-04T22-20-35-931543Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-04 21:30:26 | [Icod.LiteRogue](https://www.nuget.org/packages/Icod.LiteRogue) | 1.0.0 | Timothy J. Bruce | A small turn-based Rogue-style dungeon game using Icod.DCurses. |
| 2026-10-04 21:40:54 | [olaf](https://www.nuget.org/packages/olaf) | 0.1.3 | olaf contributors | License scanner: scans npm, nuget, and pip projects, resolves licenses, and wri… |
| 2026-10-04 21:46:07 | [IOKode.OpinionatedFramework.ContractImplementations.InMemoryEvents](https://www.nuget.org/packages/IOKode.OpinionatedFramework.ContractImplementations.InMemoryEvents) | 0.45.0-dev | IOKode, Ivan Montilla | OpinionatedFramework is a robust, comprehensive .NET 8+ framework designed to s… |
| 2026-10-04 21:50:49 | [BaseRz.JS](https://www.nuget.org/packages/BaseRz.JS) | 0.0.1 | Joel Gorin | JavaScript interop used by BaseRz.Core. Installed automatically with BaseRz.Cor… |
| 2026-10-04 21:50:50 | [BaseRz.Core](https://www.nuget.org/packages/BaseRz.Core) | 0.0.1 | Joel Gorin | An unstyled, accessible, headless UI component library built for Blazor (WebAss… |
| 2026-10-04 21:55:29 | [FS.GG.Game.Physics.Box2D](https://www.nuget.org/packages/FS.GG.Game.Physics.Box2D) | 0.17.0 | FS.GG Contributors | Opt-in headless Box2D.NET physics runtime with fixed ticks, immutable observati… |
| 2026-10-04 22:01:56 | [Novolis.Time.Month](https://www.nuget.org/packages/Novolis.Time.Month) | 2026.1.1.14 | Novolis | Gregorian month identity and month-based calendars. |
| 2026-10-04 22:03:00 | [HostLoom.Generators](https://www.nuget.org/packages/HostLoom.Generators) | 0.15.0 | Aleksandr Pavlov | Secure random strings, numeric codes, human-readable coupon codes, opaque token… |
| 2026-10-04 22:03:01 | [HostLoom.Generators.Testing](https://www.nuget.org/packages/HostLoom.Generators.Testing) | 0.15.0 | Aleksandr Pavlov | Deterministic and scripted random sources plus an async numeric sequence for te… |
| 2026-10-04 22:14:08 | [OutroKit](https://www.nuget.org/packages/OutroKit) | 1.5.0 | James Montemagno | OutroKit writes the titles, descriptions, chapters, and subtitles for your epis… |
| 2026-10-04 22:14:22 | [Novolis.Blazor.GraphicalProfile](https://www.nuget.org/packages/Novolis.Blazor.GraphicalProfile) | 2026.1.1.4 | Novolis | Required Novolis graphical profile for Blazor hosts: CSS tokens and the shared… |
| 2026-10-04 22:14:23 | [Novolis.Blazor.Mermaid](https://www.nuget.org/packages/Novolis.Blazor.Mermaid) | 2026.1.1.4 | Novolis | Blazor Mermaid component backed by Novolis markup and headless rendering. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

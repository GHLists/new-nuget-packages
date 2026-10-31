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

## Latest list — 2026-10-31 14:20 UTC

New packages created between 2026-10-31 13:20 UTC and 2026-10-31 14:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-31T14-20-13-740257Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-31 13:20:23 | [Soenneker.TypesafeAi.OpenApiClient](https://www.nuget.org/packages/Soenneker.TypesafeAi.OpenApiClient) | 11.0.1 | Jake Soenneker | A generated OpenAPI client for TypeSafe AI. |
| 2026-10-31 13:20:31 | [Divisionz.Scaffold.SQLScriptExecutor.SQLite](https://www.nuget.org/packages/Divisionz.Scaffold.SQLScriptExecutor.SQLite) | 1.0.0-rc858 | Isaychev Konstantin Mikhailov… | Исполнитель SQL-скриптов sql-exec для SQLite: SQLiteExecutor, фабрики ISQLExecu… |
| 2026-10-31 13:32:38 | [dotnet-inngest](https://www.nuget.org/packages/dotnet-inngest) | 1.0.0 | inngest-dotnet contributors | The dotnet inngest command for the Inngest .NET SDK: dotnet inngest dev downloa… |
| 2026-10-31 13:39:27 | [Kandra.Plugins.UA.Rates.Nbu](https://www.nuget.org/packages/Kandra.Plugins.UA.Rates.Nbu) | 0.1.2 | Kandra Tech | Official exchange rates of the National Bank of Ukraine (NBU): a typed HttpClie… |
| 2026-10-31 13:48:51 | [Gue.Audio](https://www.nuget.org/packages/Gue.Audio) | 0.1.0-alpha | GUE contributors | Audio mixer and sample playback for the GUE interpreters. |
| 2026-10-31 13:48:52 | [Gue.Core](https://www.nuget.org/packages/Gue.Core) | 0.1.0-alpha | GUE contributors | Host contract and shared primitives for the GUE interpreters. |
| 2026-10-31 13:48:53 | [Gue.Host.Sdl](https://www.nuget.org/packages/Gue.Host.Sdl) | 0.1.0-alpha | GUE contributors | SDL3 host for the GUE interpreters: window, input and audio. |
| 2026-10-31 13:48:54 | [Gue.Made](https://www.nuget.org/packages/Gue.Made) | 0.1.0-alpha | GUE contributors | The MADE interpreter for Return to Zork, ported from ScummVM. |
| 2026-10-31 13:48:57 | [Gue.Player](https://www.nuget.org/packages/Gue.Player) | 0.1.0-alpha | GUE contributors | Command line player for Return to Zork, Zork Nemesis, Zork: Grand Inquisitor an… |
| 2026-10-31 13:48:58 | [Gue.ZMachine](https://www.nuget.org/packages/Gue.ZMachine) | 0.1.0-alpha | GUE contributors | The Z-Machine engine for Infocom's text games: a C# interpreter for story files… |
| 2026-10-31 13:48:59 | [Gue.ZVision](https://www.nuget.org/packages/Gue.ZVision) | 0.1.0-alpha | GUE contributors | The Z-Vision engine for Zork Nemesis and Zork: Grand Inquisitor, ported from Sc… |
| 2026-10-31 13:49:05 | [Sandlada.RopSharp](https://www.nuget.org/packages/Sandlada.RopSharp) | 0.0.1 | Sandlada | Production-grade railway-oriented programming (ROP) for modern C#: Result<TOk,T… |
| 2026-10-31 13:53:00 | [Element-Plus](https://www.nuget.org/packages/Element-Plus) | 0.12.0 | Smart | Element-Plus is an independent Blazor UI component library aligned with the Ele… |
| 2026-10-31 13:53:01 | [Element-Plus.Markdown](https://www.nuget.org/packages/Element-Plus.Markdown) | 0.12.0 | Smart | Markdown editor components for Element-Plus, aligned with the Element Plus 2.14… |
| 2026-10-31 13:53:01 | [Element-Plus.X](https://www.nuget.org/packages/Element-Plus.X) | 0.12.0 | Smart | AI and conversation scene components for Element-Plus, inspired by Element Plus… |
| 2026-10-31 14:13:45 | [YandexTracker](https://www.nuget.org/packages/YandexTracker) | 0.1.0 | FrigaT | Unofficial asynchronous .NET client for the Yandex Tracker API (.NET 8/9/10): i… |
| 2026-10-31 14:14:12 | [Darp.Fairino.Testing](https://www.nuget.org/packages/Darp.Fairino.Testing) | 0.8.0 | rosslight GmbH | An in-memory fake of a Fairino robot controller for testing code written agains… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

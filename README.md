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

## Latest list — 2026-11-19 19:20 UTC

New packages created between 2026-11-19 18:18 UTC and 2026-11-19 19:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-19T19-20-18-669639Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-19 18:19:11 | [HacquerStudiosCore](https://www.nuget.org/packages/HacquerStudiosCore) | 0.0.1 | Hacquer Studios | Core Hacquer Studios Framework. |
| 2026-11-19 18:28:57 | [Herald.Sdk](https://www.nuget.org/packages/Herald.Sdk) | 0.3.0 | Fernando Cruz | Send notifications from your .NET apps to your phone with Herald: link by QR, d… |
| 2026-11-19 18:33:07 | [Slido.chromiumembeddedframework.runtime.win-x64](https://www.nuget.org/packages/Slido.chromiumembeddedframework.runtime.win-x64) | 144.0.30 | The Chromium Embedded Framewo… | chromiumembeddedframework.runtime.win-x64 144.0.30 repackaged for Slido for Win… |
| 2026-11-19 18:33:12 | [Slido.chromiumembeddedframework.runtime.win-x86](https://www.nuget.org/packages/Slido.chromiumembeddedframework.runtime.win-x86) | 144.0.30 | The Chromium Embedded Framewo… | chromiumembeddedframework.runtime.win-x86 144.0.30 repackaged for Slido for Win… |
| 2026-11-19 18:33:13 | [Slido.CefSharp.Common](https://www.nuget.org/packages/Slido.CefSharp.Common) | 144.0.300 | The CefSharp Authors | CefSharp.Common 144.0.300 repackaged for Slido for Windows with Authenticode-si… |
| 2026-11-19 18:33:14 | [Slido.CefSharp.WinForms](https://www.nuget.org/packages/Slido.CefSharp.WinForms) | 144.0.300 | The CefSharp Authors | CefSharp.WinForms 144.0.300 repackaged for Slido for Windows with Authenticode-… |
| 2026-11-19 18:57:52 | [Paduraksa.TypedIds.EntityFrameworkCore](https://www.nuget.org/packages/Paduraksa.TypedIds.EntityFrameworkCore) | 0.1.0 | Hizkia Felix | Entity Framework Core support for Paduraksa.TypedIds: one model convention maps… |
| 2026-11-19 18:57:53 | [Paduraksa.TypedIds](https://www.nuget.org/packages/Paduraksa.TypedIds) | 0.1.0 | Hizkia Felix | Strongly typed, prefixed IDs for .NET: a source generator makes one struct per… |
| 2026-11-19 19:05:22 | [Filin.EventStore.AdoNet](https://www.nuget.org/packages/Filin.EventStore.AdoNet) | 0.1.0 | Pavel Petukhov | ADO.NET-based IEventStore implementation with Dynamic Consistency Boundary (DCB… |
| 2026-11-19 19:05:29 | [Filin.Abstractions](https://www.nuget.org/packages/Filin.Abstractions) | 0.1.0 | Pavel Petukhov | Сore interfaces and abstractions for the Filin Event Sourcing framework with na… |
| 2026-11-19 19:05:57 | [Filin](https://www.nuget.org/packages/Filin) | 0.1.0 | Pavel Petukhov | A Mediator implementation for the Filin Event Sourcing framework. Coordinates e… |
| 2026-11-19 19:06:21 | [Filin.ProjectionStore.AdoNet](https://www.nuget.org/packages/Filin.ProjectionStore.AdoNet) | 0.1.0 | Pavel Petukhov | ADO.NET-based IProjectionStore implementation for the Filin Event Sourcing fram… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

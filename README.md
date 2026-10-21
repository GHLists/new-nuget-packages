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

## Latest list — 2026-10-21 19:19 UTC

New packages created between 2026-10-21 18:22 UTC and 2026-10-21 19:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-21T19-19-32-153852Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-21 18:25:12 | [Stellaegis.Registry.PostgreSQL](https://www.nuget.org/packages/Stellaegis.Registry.PostgreSQL) | 5.0.1 | FRi | The PostgreSQL stores of Stellaegis.Registry: the compartments, the users, the… |
| 2026-10-21 18:25:13 | [Stellaegis.Registry](https://www.nuget.org/packages/Stellaegis.Registry) | 5.0.1 | FRi | Stellaegis Registry: what gives a right its meaning in an application assembled… |
| 2026-10-21 18:25:13 | [Stellaegis.Registry.AspNetCore](https://www.nuget.org/packages/Stellaegis.Registry.AspNetCore) | 5.0.1 | FRi | Stellaegis Registry in an ASP.NET Core host: the administration routes of the r… |
| 2026-10-21 18:28:57 | [Pmad.CodeCondenser](https://www.nuget.org/packages/Pmad.CodeCondenser) | 0.0.1 | Julien Etelain | Roslyn-based static analysis CLI tool to detect C# code clones and condense ver… |
| 2026-10-21 18:47:39 | [MediatingKit](https://www.nuget.org/packages/MediatingKit) | 0.4.0 | eduvhc | An in-process mediator whose dispatch is generated at compile time: requests, n… |
| 2026-10-21 18:47:40 | [LockingKit.Azure](https://www.nuget.org/packages/LockingKit.Azure) | 0.4.0 | eduvhc | Azure blob lease provider for LockingKit, on Azure.Storage.Blobs: renewable lea… |
| 2026-10-21 18:47:42 | [LockingKit.Postgres](https://www.nuget.org/packages/LockingKit.Postgres) | 0.4.0 | eduvhc | PostgreSQL provider for LockingKit, on Npgsql: session-level advisory locks hel… |
| 2026-10-21 18:47:44 | [ValidatingKit](https://www.nuget.org/packages/ValidatingKit) | 0.4.0 | eduvhc | Small, dependency-free fluent validation that returns ResultingKit results: bui… |
| 2026-10-21 18:47:45 | [ValidatingKit.AspNetCore](https://www.nuget.org/packages/ValidatingKit.AspNetCore) | 0.4.0 | eduvhc | Runs ValidatingKit validators on ASP.NET Core requests: one call validates ever… |
| 2026-10-21 18:47:50 | [LockingKit](https://www.nuget.org/packages/LockingKit) | 0.4.0 | eduvhc | Distributed locks as a contract: try or wait for a lock by key, automatic renew… |
| 2026-10-21 18:50:10 | [JeppDev.OpenVR.Bindings](https://www.nuget.org/packages/JeppDev.OpenVR.Bindings) | 0.9.5 | Jeppevinkel | C# bindings (openvr_api.cs) for OpenVR by Valve Corporation |
| 2026-10-21 18:50:12 | [JeppDev.OpenVR](https://www.nuget.org/packages/JeppDev.OpenVR) | 0.9.4 | Jeppevinkel | OpenVR for .NET: C# bindings and native binaries (meta package) |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

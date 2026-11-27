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

## Latest list — 2026-11-27 15:20 UTC

New packages created between 2026-11-27 14:19 UTC and 2026-11-27 15:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-27T15-20-00-140734Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-27 14:35:39 | [Routebase.AspNetCore](https://www.nuget.org/packages/Routebase.AspNetCore) | 1.0.0 | Routebase GmbH | Stop the OpenAPI document of your ASP.NET Core API from drifting away from the… |
| 2026-11-27 14:37:46 | [WiDas.Sdk.Windows](https://www.nuget.org/packages/WiDas.Sdk.Windows) | 0.5.1 | Ameriband | Wi-DAS Windows SDK: Device key handling, Signing Request generation and Passpoi… |
| 2026-11-27 14:45:17 | [BeeAppie.Maui.MTAdmob](https://www.nuget.org/packages/BeeAppie.Maui.MTAdmob) | 1.0.2 | BeeAppie | Shows your BeeAppie promos in banner slots AdMob could not fill, through MTAdmo… |
| 2026-11-27 14:45:47 | [Majorsilence.AppleTools](https://www.nuget.org/packages/Majorsilence.AppleTools) | 0.1.0 | Peter Gill | Open-source C# stand-ins for the Xcode command-line tools the .NET iOS workload… |
| 2026-11-27 14:52:07 | [DS.Foundation.MultiTenancy](https://www.nuget.org/packages/DS.Foundation.MultiTenancy) | 9.0.3 | DS | Resolución de tenant_code (ITenantContext); Etapa A sin catálogo ni pool/silo. |
| 2026-11-27 14:52:23 | [DS.Foundation.MultiTenancy.AspNetCore](https://www.nuget.org/packages/DS.Foundation.MultiTenancy.AspNetCore) | 9.0.3 | DS | ASP.NET Core: ITenantContext from JWT GroupSid. |
| 2026-11-27 14:52:32 | [Pernix.OutboxRelay.Destination.Http](https://www.nuget.org/packages/Pernix.OutboxRelay.Destination.Http) | 1.1.0 | Pernix | Package Description |
| 2026-11-27 14:53:54 | [FargaStudios.Suite.Updater](https://www.nuget.org/packages/FargaStudios.Suite.Updater) | 0.2.1 | Farga Studios | Signed update manifests, verified downloads and Windows installer handoff for i… |
| 2026-11-27 14:57:56 | [Lokad.UnixTools](https://www.nuget.org/packages/Lokad.UnixTools) | 0.1.0 | Lokad | Unix-style commands for .NET applications with host-controlled I/O. |
| 2026-11-27 14:59:14 | [Meziantou.Framework.WasmEngine.Wasi](https://www.nuget.org/packages/Meziantou.Framework.WasmEngine.Wasi) | 1.0.0 | meziantou | WASI for Meziantou.Framework.WasmEngine: WASI Preview 1 (wasi_snapshot_preview1… |
| 2026-11-27 15:03:10 | [RasterizedDb.EntityFrameworkCore](https://www.nuget.org/packages/RasterizedDb.EntityFrameworkCore) | 1.1.0 | Milen Denev | Entity Framework Core provider for RasterizedDB over its native protocol (rastc… |
| 2026-11-27 15:03:11 | [RasterizedDb.Data](https://www.nuget.org/packages/RasterizedDb.Data) | 1.1.0 | Milen Denev | ADO.NET driver for RasterizedDB's native protocol (rastcp): SQL, transactions,… |
| 2026-11-27 15:03:11 | [RasterizedDb.Messaging](https://www.nuget.org/packages/RasterizedDb.Messaging) | 1.1.0 | Milen Denev | Client for RasterizedDB's message broker (rdbmq/1): queues, topics, subscriptio… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

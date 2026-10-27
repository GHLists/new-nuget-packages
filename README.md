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

## Latest list — 2026-10-27 00:20 UTC

New packages created between 2026-10-26 23:20 UTC and 2026-10-27 00:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-27T00-20-44-361628Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-26 23:22:10 | [Microsoft.StateKeeper](https://www.nuget.org/packages/Microsoft.StateKeeper) | 0.1.12 | Microsoft | Async synchronization tools for safely managing concurrent access to shared sta… |
| 2026-10-26 23:27:10 | [Zaldaryon.Pharos.Templates](https://www.nuget.org/packages/Zaldaryon.Pharos.Templates) | 0.8.0 | Zaldaryon | dotnet new templates for Pharos: pharos-mod-tests, a test project for a Vintage… |
| 2026-10-26 23:27:10 | [Zaldaryon.Pharos.Verify](https://www.nuget.org/packages/Zaldaryon.Pharos.Verify) | 0.8.0 | Zaldaryon | Snapshot testing of Vintage Story game state with Verify, for Pharos. |
| 2026-10-26 23:29:09 | [Krut.Netcode](https://www.nuget.org/packages/Krut.Netcode) | 0.1.0 | William Eklund | Authoritative-server netcode for .NET on LiteNetLib: handshake, fixed tick cloc… |
| 2026-10-26 23:39:30 | [Capital](https://www.nuget.org/packages/Capital) | 0.1.0 | robert-walsh-hrri | Typed data structures for the economic categories of Karl Marx's Capital, Volum… |
| 2026-10-26 23:43:38 | [Lers.Core](https://www.nuget.org/packages/Lers.Core) | 3.68.0-beta | Lers.Core | Package Description |
| 2026-10-26 23:51:49 | [NetProxy.PluginApi](https://www.nuget.org/packages/NetProxy.PluginApi) | 3.1.0 | NetworkDLS | The API for writing NetProxy plug-ins: derive from NpPlugin, override the event… |
| 2026-10-27 00:02:42 | [Render.NET.Pdf](https://www.nuget.org/packages/Render.NET.Pdf) | 0.3.4 | Vadim Belov | Managed PDF page rendering to RGBA and PNG for .NET. Vector paths, font outline… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

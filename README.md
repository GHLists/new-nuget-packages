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

## Latest list — 2026-10-15 17:20 UTC

New packages created between 2026-10-15 16:19 UTC and 2026-10-15 17:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-15T17-20-02-720673Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-15 16:26:08 | [hostfix](https://www.nuget.org/packages/hostfix) | 1.0.2 | Puviraj | Fast, project-aware developer machine diagnostics, PATH sanitizer, and environm… |
| 2026-10-15 16:31:55 | [Maanfee.WebSocket](https://www.nuget.org/packages/Maanfee.WebSocket) | 1.0.0 | Maanfee Team (MF) | A comprehensive WebSocket library for .NET providing both client and server imp… |
| 2026-10-15 16:40:59 | [NetCoreApiKit](https://www.nuget.org/packages/NetCoreApiKit) | 3.4.0 | NetCore_API_Structure | Asistente paso a paso para crear APIs ASP.NET Core con el kit NetCore_API_Struc… |
| 2026-10-15 16:41:45 | [bpool](https://www.nuget.org/packages/bpool) | 0.1.0 | CarbonNeuron | A colorful live terminal monitor for OpenZFS pool, disk, ARC, and L2ARC statist… |
| 2026-10-15 16:42:22 | [Qyl.Orchestration](https://www.nuget.org/packages/Qyl.Orchestration) | 13.1.0 | ancplua | Compose and supervise local .NET services and executables with qyl's process or… |
| 2026-10-15 17:06:32 | [E2e4.Chess.Fics.Client](https://www.nuget.org/packages/E2e4.Chess.Fics.Client) | 1.0.0 | th3snark | Cross-platform client library for the Free Internet Chess Server (FICS): framin… |
| 2026-10-15 17:10:36 | [Linq2GraphQL.Client.AI](https://www.nuget.org/packages/Linq2GraphQL.Client.AI) | 1.0.60-prerelease | Joakim Dangården,Magnus Ahlbe… | Agent mode for Linq2GraphQL: expose a scoped, validated GraphQL schema to AI ag… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

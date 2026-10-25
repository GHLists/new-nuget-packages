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

## Latest list — 2026-10-25 03:20 UTC

New packages created between 2026-10-25 02:21 UTC and 2026-10-25 03:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-25T03-20-03-180483Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-25 02:22:02 | [Silex.Sdk](https://www.nuget.org/packages/Silex.Sdk) | 1.0.0 | Silex | Client and IConfiguration provider for Silex (silex.sh), the encrypted secrets… |
| 2026-10-25 02:29:54 | [MajProtocol.Standard](https://www.nuget.org/packages/MajProtocol.Standard) | 2.0.0 | re-poem, fumiko | Packet types and property constants for the MajProtocol binary protocol. Ships… |
| 2026-10-25 02:30:04 | [MajProtocol.Client.WebSocketSharp](https://www.nuget.org/packages/MajProtocol.Client.WebSocketSharp) | 2.0.0 | re-poem, fumiko | WebSocket client implementation of MajProtocol, used by an editor to drive the… |
| 2026-10-25 02:30:21 | [MajProtocol.Server.WebSocketSharp](https://www.nuget.org/packages/MajProtocol.Server.WebSocketSharp) | 2.0.0 | re-poem, fumiko | WebSocket server implementation of MajProtocol, used by a player to receive pla… |
| 2026-10-25 03:14:09 | [GoldMeridian.Reflection](https://www.nuget.org/packages/GoldMeridian.Reflection) | 1.0.0 | Stephen Thiebaud et al. | Reflection helpers for .NET; expression syntax for obtaining Reflection member… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

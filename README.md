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

## Latest list — 2026-10-14 23:21 UTC

New packages created between 2026-10-14 22:22 UTC and 2026-10-14 23:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-14T23-21-53-360562Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-14 22:36:57 | [IodreamVault](https://www.nuget.org/packages/IodreamVault) | 0.3.1 | IODream | IODream Vault command line. Sign in, then run any app with its secrets as envir… |
| 2026-10-14 22:42:37 | [Tokenway.Client](https://www.nuget.org/packages/Tokenway.Client) | 0.1.0 | iyulab | Client for Tokenway: read and manage wallets, lots, caps and the event feed, an… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

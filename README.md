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

## Latest list — 2026-10-01 19:19 UTC

New packages created between 2026-10-01 18:22 UTC and 2026-10-01 19:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-01T19-19-59-729064Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-01 18:25:01 | [TUtils.AI](https://www.nuget.org/packages/TUtils.AI) | 0.0.2 | TUtils.AI | Shared AI-related utilities for TUtils projects. |
| 2026-10-01 18:53:28 | [Cosmos.Network.Ftp](https://www.nuget.org/packages/Cosmos.Network.Ftp) | 2.0.0 | Cosmos | FTP server for Cosmos Gen3 kernels. |
| 2026-10-01 18:59:42 | [AWSSDK.EndUserMessaging](https://www.nuget.org/packages/AWSSDK.EndUserMessaging) | 4.0.100 | Amazon Web Services | AWS End User Messaging now supports Brand profiles and Notify code configuratio… |
| 2026-10-01 18:59:47 | [AWSSDK.LambdaWeb](https://www.nuget.org/packages/AWSSDK.LambdaWeb) | 4.0.100 | Amazon Web Services | Lambda Web Functions GA launch. Lambda Web Functions enable customers to run we… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

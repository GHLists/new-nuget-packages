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

## Latest list — 2026-11-19 00:20 UTC

New packages created between 2026-11-18 23:19 UTC and 2026-11-19 00:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-19T00-20-53-741969Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-18 23:20:43 | [Eternal.LZMA2Simple.Native](https://www.nuget.org/packages/Eternal.LZMA2Simple.Native) | 1.0.6 | JohnJScott | A simplified implementation of the 7-Zip API for C++, based on version 25.01 of… |
| 2026-11-18 23:45:46 | [Okta.AuthFoundation](https://www.nuget.org/packages/Okta.AuthFoundation) | 0.2.0 | Okta | Foundational OAuth2/OIDC types for the Okta .NET SDK: HTTP client, token and cr… |
| 2026-11-18 23:59:24 | [Zenoh.FSharp](https://www.nuget.org/packages/Zenoh.FSharp) | 0.1.0 | mushed Research | F# bindings for Eclipse Zenoh over zenoh-c 1.10.2: sessions, pub/sub, queries,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

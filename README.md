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

## Latest list — 2026-10-10 00:19 UTC

New packages created between 2026-10-09 23:19 UTC and 2026-10-10 00:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-10T00-19-28-524175Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-10 00:09:34 | [Zaldaryon.Pharos.Cli](https://www.nuget.org/packages/Zaldaryon.Pharos.Cli) | 0.6.0 | Zaldaryon | The pharos command: smoke-test a Vintage Story mod (boot, join, play, fail on e… |
| 2026-10-10 00:10:41 | [TenaBill.Sdk](https://www.nuget.org/packages/TenaBill.Sdk) | 0.1.4 | Cyntrix | Typed application SDK for TenaBill merchant payment capabilities. |
| 2026-10-10 00:10:42 | [TenaBill.Sdk.Mobile](https://www.nuget.org/packages/TenaBill.Sdk.Mobile) | 0.1.3 | Cyntrix | App-neutral mobile payment collection contracts for TenaBill provider adapters. |
| 2026-10-10 00:12:53 | [TenancyEngine.Sdk.Maui.Auth](https://www.nuget.org/packages/TenancyEngine.Sdk.Maui.Auth) | 0.4.3 | Cyntrix | Platform-agnostic core of the TenancyEngine mobile OIDC/PKCE auth client for .N… |
| 2026-10-10 00:12:55 | [TenancyEngine.Sdk](https://www.nuget.org/packages/TenancyEngine.Sdk) | 2.0.2 | Cyntrix | TenancyEngine platform SDK for ISV applications (.NET) — typed client for the o… |
| 2026-10-10 00:12:56 | [TenancyEngine.Sdk.Maui](https://www.nuget.org/packages/TenancyEngine.Sdk.Maui) | 0.4.3 | Cyntrix | Ready-to-use TenancyEngine OIDC/PKCE auth client for .NET MAUI apps (iOS/Androi… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

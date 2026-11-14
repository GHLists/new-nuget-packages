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

## Latest list — 2026-11-14 19:21 UTC

New packages created between 2026-11-14 18:21 UTC and 2026-11-14 19:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-14T19-21-08-535317Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-14 18:27:22 | [DarkStrata.CredentialCheck.Umbraco.Automate](https://www.nuget.org/packages/DarkStrata.CredentialCheck.Umbraco.Automate) | 2.9.0 | DarkStrata | Adds a "Compromised Credential Detected" trigger to Umbraco Automate, so a brea… |
| 2026-11-14 18:45:02 | [EFCore_DaIn_11](https://www.nuget.org/packages/EFCore_DaIn_11) | 11.0.0 | ignatandrei | EF Core 11 contracts and plugin loader for dynamically loaded database provider… |
| 2026-11-14 19:00:25 | [ArionPay](https://www.nuget.org/packages/ArionPay) | 1.0.0 | ArionPay | Official .NET client for ArionPay crypto payments: create invoices, verify sign… |
| 2026-11-14 19:03:31 | [VersionFlow.Extensions.Railway](https://www.nuget.org/packages/VersionFlow.Extensions.Railway) | 1.0.1 | Bradley Ables | Dependency-free railway results with typed errors, validation, recovery, and fl… |
| 2026-11-14 19:03:56 | [VersionFlow.Extensions.Results](https://www.nuget.org/packages/VersionFlow.Extensions.Results) | 1.0.1 | Bradley Ables | Immutable operation outcomes, collection and pagination results, and UTC cursor… |
| 2026-11-14 19:03:58 | [Electrical.Markets](https://www.nuget.org/packages/Electrical.Markets) | 1.2.0 | Gravicode Studios (Kang Fadhi… | Electricity markets for Electrical.Net: security-constrained unit commitment (M… |
| 2026-11-14 19:04:00 | [Electrical.Optimization.Highs](https://www.nuget.org/packages/Electrical.Optimization.Highs) | 1.2.0 | Gravicode Studios (Kang Fadhi… | HiGHS LP/MIP solver adapter for Electrical.Net (IMilpSolver / ILpSolver backed… |
| 2026-11-14 19:04:05 | [Electrical.Optimization.OrTools](https://www.nuget.org/packages/Electrical.Optimization.OrTools) | 1.2.0 | Gravicode Studios (Kang Fadhi… | Google OR-Tools solver adapter for Electrical.Net (IMilpSolver / ILpSolver back… |
| 2026-11-14 19:04:23 | [VersionFlow.Extensions.Results.AspNetCore](https://www.nuget.org/packages/VersionFlow.Extensions.Results.AspNetCore) | 1.0.1 | Bradley Ables | ASP.NET Core HTTP mapping for VersionFlow result contracts. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

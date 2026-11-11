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

## Latest list — 2026-11-11 18:21 UTC

New packages created between 2026-11-11 17:21 UTC and 2026-11-11 18:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-11T18-21-51-876331Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-11 17:38:49 | [NextSyncListener](https://www.nuget.org/packages/NextSyncListener) | 9.7.65 | Julien Clauzel | The PC half of the NextSync ".sync5 -listen" Remote Explorer protocol: a TCP se… |
| 2026-11-11 17:40:52 | [AlibabaCloud.SDK.EcdBiz20240929](https://www.nuget.org/packages/AlibabaCloud.SDK.EcdBiz20240929) | 1.0.0 | Alibaba Cloud | Alibaba Cloud EcdBiz (20240929) SDK Library for .NET |
| 2026-11-11 17:42:55 | [Digi21.DigiNG.Dtm](https://www.nuget.org/packages/Digi21.DigiNG.Dtm) | 26.0.0 | José Ángel Martínez Torres | This package contains a reference assembly to open digital terrain models (.mdt… |
| 2026-11-11 17:48:59 | [Bitwarden.Server.Sdk.Database](https://www.nuget.org/packages/Bitwarden.Server.Sdk.Database) | 0.1.0 | Bitwarden Inc. | Database migration support for Bitwarden server services. Provides the runtime… |
| 2026-11-11 17:51:11 | [Pmad.KeySharp](https://www.nuget.org/packages/Pmad.KeySharp) | 0.1.0 | goaaats,OppOops,jetelain | Cross-platform OS keyring and credential storage access for .NET (Windows Crede… |
| 2026-11-11 18:02:18 | [Abaddax.Roslyn.Analyzers.Framework](https://www.nuget.org/packages/Abaddax.Roslyn.Analyzers.Framework) | 0.0.1-preview12 | Abaddax | A collection of C# Roslyn analyzers |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-07 07:20 UTC

New packages created between 2026-10-07 06:21 UTC and 2026-10-07 07:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-07T07-20-06-738943Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-07 06:23:22 | [Polochon.Messaging.AzureQueue](https://www.nuget.org/packages/Polochon.Messaging.AzureQueue) | 0.5.0 | Shinboku.io | Azure Queue Storage messaging integration for the Polochon kernel. |
| 2026-10-07 06:23:23 | [Polochon.Validation.FluentValidation](https://www.nuget.org/packages/Polochon.Validation.FluentValidation) | 0.5.0 | Shinboku.io | FluentValidation integration for the Polochon kernel's message validation. |
| 2026-10-07 06:23:24 | [Polochon.FeatureManagement.Azure](https://www.nuget.org/packages/Polochon.FeatureManagement.Azure) | 0.5.0 | Shinboku.io | Azure App Configuration feature flags for the Polochon kernel: host-level sourc… |
| 2026-10-07 06:23:25 | [Polochon.Telemetry.AzureMonitor](https://www.nuget.org/packages/Polochon.Telemetry.AzureMonitor) | 0.5.0 | Shinboku.io | Azure Monitor (Application Insights) export of the Polochon kernel's OpenTeleme… |
| 2026-10-07 06:23:26 | [Polochon.Telemetry.OpenTelemetry](https://www.nuget.org/packages/Polochon.Telemetry.OpenTelemetry) | 0.5.0 | Shinboku.io | OpenTelemetry export (OTLP, console) of the Polochon kernel's traces, metrics a… |
| 2026-10-07 06:23:27 | [Polochon.Persistence.SqlServer](https://www.nuget.org/packages/Polochon.Persistence.SqlServer) | 0.5.0 | Shinboku.io | SQL Server persistence integration for the Polochon kernel. |
| 2026-10-07 06:23:27 | [Polochon.Abstractions](https://www.nuget.org/packages/Polochon.Abstractions) | 0.5.0 | Shinboku.io | Shared interfaces and DTOs for the Polochon kernel. |
| 2026-10-07 06:23:28 | [Polochon.Serilog](https://www.nuget.org/packages/Polochon.Serilog) | 0.5.0 | Shinboku.io | Serilog logging integration for the Polochon kernel. |
| 2026-10-07 06:23:29 | [Polochon](https://www.nuget.org/packages/Polochon) | 0.5.0 | Shinboku.io | Core Polochon kernel: shared domain, application, and infrastructure contracts. |
| 2026-10-07 06:30:15 | [Tai.Wallet.MongoDB](https://www.nuget.org/packages/Tai.Wallet.MongoDB) | 0.1.9 | Tai | ABP wallet balances, ledger and withdrawal module |
| 2026-10-07 06:50:33 | [Egov.Extensions.WalletValidation](https://www.nuget.org/packages/Egov.Extensions.WalletValidation) | 10.0.4 | egov.md | OpenID4VP mdoc request creation and wallet response validation for .NET, includ… |
| 2026-10-07 06:56:35 | [Purview.ValueObjects](https://www.nuget.org/packages/Purview.ValueObjects) | 1.0.0 | Kieron Lanning | Source-generated scalar and complex value objects for .NET. Brings F#-style sin… |
| 2026-10-07 07:09:30 | [ESRP.Release.NuGet.ESRPRelease-BVT.Prod.Build199417](https://www.nuget.org/packages/ESRP.Release.NuGet.ESRPRelease-BVT.Prod.Build199417) | 1.0.199417 | Microsoft | Disposable package used to validate NuGet publishing through ESRP Release. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

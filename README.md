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

## Latest list — 2026-11-07 18:20 UTC

New packages created between 2026-11-07 17:19 UTC and 2026-11-07 18:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-07T18-20-45-763199Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-07 17:25:49 | [RaainTech.Guard](https://www.nuget.org/packages/RaainTech.Guard) | 1.0.1 | RAAIN Tech Pvt. Ltd. | Official .NET SDK for RAAIN Guard, the embedded decision-intelligence platform… |
| 2026-11-07 17:51:39 | [Infrastructure.Wpf](https://www.nuget.org/packages/Infrastructure.Wpf) | 1.0.0 | Sukhov A.A. | A WPF-specific NuGet package providing window management services, dialog and n… |
| 2026-11-07 17:58:53 | [Zhomfr.Storage.Abstractions](https://www.nuget.org/packages/Zhomfr.Storage.Abstractions) | 0.7.1 | zhuolyan (Oleg Zhuravskiy) | Package Description |
| 2026-11-07 17:58:56 | [Zhomfr.Storage.Local](https://www.nuget.org/packages/Zhomfr.Storage.Local) | 0.7.1 | zhuolyan (Oleg Zhuravskiy) | Package Description |
| 2026-11-07 18:12:44 | [JoinRpg.Common.WebInfrastructure.Interfaces](https://www.nuget.org/packages/JoinRpg.Common.WebInfrastructure.Interfaces) | 2026.9.651 | Leonid Tsarev and Co | Background job contracts for JoinRpg web infrastructure: IJob, IJobRepository,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

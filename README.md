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

## Latest list — 2026-11-03 07:19 UTC

New packages created between 2026-11-03 06:20 UTC and 2026-11-03 07:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-03T07-19-07-636943Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-03 06:41:24 | [keyi.templates.keyiabp8](https://www.nuget.org/packages/keyi.templates.keyiabp8) | 1.0.0 | Keyi | .NET 8 + ABP + Vue3 Admin/Web + uni-app 项目脚手架（dotnet new keyiabp8） |
| 2026-11-03 06:44:57 | [TCIS.Logging.Hosting.WinForms](https://www.nuget.org/packages/TCIS.Logging.Hosting.WinForms) | 1.0.8 | TCIS Core Community and Contr… | Centralized TCIS logging for WinForms desktop applications on .NET Framework: o… |
| 2026-11-03 06:50:50 | [Gasco_Khazeen_S4](https://www.nuget.org/packages/Gasco_Khazeen_S4) | 1.0.0 | Gasco | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

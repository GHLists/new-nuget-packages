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

## Latest list — 2026-10-07 16:20 UTC

New packages created between 2026-10-07 15:20 UTC and 2026-10-07 16:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-07T16-20-44-052873Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-07 15:41:56 | [Microsoft.Windows.AI.MachineLearning.LibLlama.Core](https://www.nuget.org/packages/Microsoft.Windows.AI.MachineLearning.LibLlama.Core) | 0.5.0.2022-experime… | Microsoft | llama.cpp runtime for Windows ML on x64 and ARM64: the Windows ML llama.cpp ada… |
| 2026-10-07 15:45:07 | [MDY.AbstractFilter](https://www.nuget.org/packages/MDY.AbstractFilter) | 1.0.0 | Davidson Moura | Biblioteca para abstração de filtros com o banco de dados. |
| 2026-10-07 15:46:34 | [TGateway.Foundation](https://www.nuget.org/packages/TGateway.Foundation) | 2.3.8 | TGateway.Foundation | Package Description |
| 2026-10-07 15:47:08 | [TGateway.Plugin](https://www.nuget.org/packages/TGateway.Plugin) | 2.3.8 | TGateway.Plugin | Package Description |
| 2026-10-07 15:59:07 | [AnointedAutomation.SSO](https://www.nuget.org/packages/AnointedAutomation.SSO) | 1.0.0 | Anointed Automation LLC, Alex… | Sign in with Anointed Automation for ASP.NET Core: an OpenID Connect handler pr… |
| 2026-10-07 16:01:28 | [Toxic.Umbraco.WelcomeDashboard](https://www.nuget.org/packages/Toxic.Umbraco.WelcomeDashboard) | 1.0.0 | Toxic | A welcome dashboard for Umbraco 17 that gives editors a clear overview of recen… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

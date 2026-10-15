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

## Latest list — 2026-10-15 15:21 UTC

New packages created between 2026-10-15 14:22 UTC and 2026-10-15 15:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-15T15-21-45-286135Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-15 14:22:54 | [Czechia.Cli](https://www.nuget.org/packages/Czechia.Cli) | 0.1.0 | rkotulan | Neoficiální CLI pro správu DNS přes REST API CZECHIA. |
| 2026-10-15 14:23:16 | [MVUish.Avalonia](https://www.nuget.org/packages/MVUish.Avalonia) | 1.0.0 | MVUish.Avalonia | Package Description |
| 2026-10-15 14:23:16 | [MVUish.Avalonia.Templates](https://www.nuget.org/packages/MVUish.Avalonia.Templates) | 1.0.0 | Angel D. Munoz | dotnet new project templates for MVUish.Avalonia apps in F# and C#. |
| 2026-10-15 14:40:22 | [ApiGuardrails.AspNetCore](https://www.nuget.org/packages/ApiGuardrails.AspNetCore) | 1.0.0 | Tirth Shah | ApiGuardrails for ASP.NET Core: Standardizes error contracts (RFC 7807 ProblemD… |
| 2026-10-15 14:44:39 | [Bitenovac.RemoteBuildTool.Service](https://www.nuget.org/packages/Bitenovac.RemoteBuildTool.Service) | 1.3.0 | Radivoje Milutinovic | The optional service for Bitenovac.RemoteBuildTool. It fills the shared build c… |
| 2026-10-15 14:47:09 | [WitchLab.Diagnostics](https://www.nuget.org/packages/WitchLab.Diagnostics) | 1.0.1 | WitchLab | Automatic HTTP 5xx error capturing, PostgreSQL diagnostics storage, and throttl… |
| 2026-10-15 14:55:27 | [YngveHestem.Quill.Abstractions](https://www.nuget.org/packages/YngveHestem.Quill.Abstractions) | 1.0.0 | Yngve J. K. Hestem | This library contains DTO's and other abstractions that is used in YngveHestem.… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

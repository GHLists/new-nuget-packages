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

## Latest list — 2026-10-11 10:19 UTC

New packages created between 2026-10-11 09:21 UTC and 2026-10-11 10:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-11T10-19-16-633712Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-11 09:33:59 | [Tai.Wallet.Voucher.Recharge](https://www.nuget.org/packages/Tai.Wallet.Voucher.Recharge) | 0.2.0 | Tai | Optional integration that lets Tai.Wallet.Recharge accept Tai.Wallet.Voucher re… |
| 2026-10-11 09:52:53 | [GitExtensions.GitLab.MergeRequests](https://www.nuget.org/packages/GitExtensions.GitLab.MergeRequests) | 2.0.0 | ahmet.urun, Alain Corchia | GitLab plugin for Git Extensions: create, review, comment, approve and merge Gi… |
| 2026-10-11 10:05:15 | [ChartForgeX.Markup.Cli](https://www.nuget.org/packages/ChartForgeX.Markup.Cli) | 2.0.0 | Evotec | Command-line renderer and code generator for ChartForgeX markup. |
| 2026-10-11 10:05:18 | [ChartForgeX.Stories](https://www.nuget.org/packages/ChartForgeX.Stories) | 2.0.0 | Evotec | Deterministic visual stories, terminal playback, motion and GIF/APNG encoding o… |
| 2026-10-11 10:05:20 | [ChartForgeX.Visuals](https://www.nuget.org/packages/ChartForgeX.Visuals) | 2.0.0 | Evotec | Dependency-free static canvas, image composition, factual tiles, tables, lists… |
| 2026-10-11 10:05:33 | [StudioElf.Module.CRM.LicenseHub](https://www.nuget.org/packages/StudioElf.Module.CRM.LicenseHub) | 1.0.0 | StudioElf | **Oqtane Marketplace order ingestion, license and trial lifecycle, with custome… |
| 2026-10-11 10:11:36 | [ELF.Modules.Diagnostics.ErrorReporting.AspNetCore](https://www.nuget.org/packages/ELF.Modules.Diagnostics.ErrorReporting.AspNetCore) | 0.8.0 | ELF INTERNATIONAL EXPRESS CO.… | 錯誤回報 ASP.NET Core 整合：未處理例外中介軟體（500 附 errorId）與最近 30 筆請求軌跡。 |
| 2026-10-11 10:11:38 | [ELF.Modules.Diagnostics.ErrorReporting.GitHub](https://www.nuget.org/packages/ELF.Modules.Diagnostics.ErrorReporting.GitHub) | 0.8.0 | ELF INTERNATIONAL EXPRESS CO.… | 錯誤回報 GitHub sink（伺服器端用）：以指紋找既有 issue，沒有就開、有就留言，同指紋每天最多一則，遵守限流。 |
| 2026-10-11 10:11:39 | [ELF.Modules.Diagnostics.ErrorReporting](https://www.nuget.org/packages/ELF.Modules.Diagnostics.ErrorReporting) | 0.8.0 | ELF INTERNATIONAL EXPRESS CO.… | 錯誤回報核心：回報格式（JSON Schema v1）、去個資、指紋、本機佇列與 HTTP 中繼 sink、ILogger 擷取。 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

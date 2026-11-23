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

## Latest list — 2026-11-23 23:21 UTC

New packages created between 2026-11-23 22:20 UTC and 2026-11-23 23:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-23T23-21-10-468993Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-23 22:23:39 | [PosInformatique.Foundations.Threading](https://www.nuget.org/packages/PosInformatique.Foundations.Threading) | 1.7.0 | Gilles TOURREAU | Provides utilities and extensions related to the System.Threading APIs of .NET. |
| 2026-11-23 22:23:40 | [PosInformatique.Foundations.Bcl](https://www.nuget.org/packages/PosInformatique.Foundations.Bcl) | 1.7.0 | Gilles TOURREAU | Provides extension methods for common .NET types, including strings, URIs, time… |
| 2026-11-23 22:23:46 | [PosInformatique.Foundations.Collections](https://www.nuget.org/packages/PosInformatique.Foundations.Collections) | 1.7.0 | Gilles TOURREAU | Provides extension methods for .NET collections and sequences. |
| 2026-11-23 22:27:29 | [Gatehouse.Captcha](https://www.nuget.org/packages/Gatehouse.Captcha) | 0.1.0 | KalliMan | Captcha checks for ASP.NET Core minimal APIs: self-hosted ALTCHA proof of work… |
| 2026-11-23 22:30:27 | [XperienceCommunity.AddonManager](https://www.nuget.org/packages/XperienceCommunity.AddonManager) | 1.0.0-prerelease-1 | Neil Powers | Admin application for Xperience by Kentico that lists the community add-ons ins… |
| 2026-11-23 22:38:10 | [Beesharp.Core](https://www.nuget.org/packages/Beesharp.Core) | 0.1.0 | Dennis | Core scenario, parameter, step-machine and runtime APIs for Beesharp load tests. |
| 2026-11-23 22:45:42 | [KryptonModern.Editor](https://www.nuget.org/packages/KryptonModern.Editor) | 2026.11.24.644 | Fungusware | A fast, themeable WinForms code editor control with syntax highlighting, minima… |
| 2026-11-23 22:46:05 | [Fdw.Services.Descriptions](https://www.nuget.org/packages/Fdw.Services.Descriptions) | 1.6.0 | Fdw Team | Development tools and utilities for the Fdw ecosystem. |
| 2026-11-23 22:46:07 | [Fdw.Services.Descriptions.Abstractions](https://www.nuget.org/packages/Fdw.Services.Descriptions.Abstractions) | 1.6.0 | Fdw Team | Development tools and utilities for the Fdw ecosystem. |
| 2026-11-23 22:46:38 | [Fdw.Services.LanguageModels](https://www.nuget.org/packages/Fdw.Services.LanguageModels) | 1.6.0 | Fdw Team | Development tools and utilities for the Fdw ecosystem. |
| 2026-11-23 22:46:39 | [Fdw.Services.LanguageModels.Abstractions](https://www.nuget.org/packages/Fdw.Services.LanguageModels.Abstractions) | 1.6.0 | Fdw Team | Development tools and utilities for the Fdw ecosystem. |
| 2026-11-23 22:59:03 | [EventfulRanges.Kurrent](https://www.nuget.org/packages/EventfulRanges.Kurrent) | 0.1.0 | Dmitry Ledentsov | A KurrentDB event log for EventfulRanges: the operations of a replica as a stre… |
| 2026-11-23 23:03:54 | [Groma](https://www.nuget.org/packages/Groma) | 0.1.1 | Alex McClure | Lays out survey plans: boxes, some holding other boxes, joined by right-angled… |
| 2026-11-23 23:04:53 | [Plasm.CSharp](https://www.nuget.org/packages/Plasm.CSharp) | 0.4.0 | Plasm contributors | What a C# host is given by an F# data layer on Plasm: the cases it switches ove… |
| 2026-11-23 23:05:40 | [Brows.MD.Windows](https://www.nuget.org/packages/Brows.MD.Windows) | 0.1.0 | Ken Yourek | A styleable WPF viewer for Markdown documents. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

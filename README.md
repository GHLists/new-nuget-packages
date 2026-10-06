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

## Latest list — 2026-10-06 19:19 UTC

New packages created between 2026-10-06 18:20 UTC and 2026-10-06 19:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-06T19-19-29-954953Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-06 18:26:25 | [AlchiwebApp.Client.Core](https://www.nuget.org/packages/AlchiwebApp.Client.Core) | 0.6.2.5 | Alchiweb | AlchiwebApp.Client.Core |
| 2026-10-06 18:26:43 | [AlchiwebApp.Core](https://www.nuget.org/packages/AlchiwebApp.Core) | 0.6.2.5 | Alchiweb | AlchiwebApp.Core |
| 2026-10-06 18:27:07 | [AlchiwebApp.PagingFiltering](https://www.nuget.org/packages/AlchiwebApp.PagingFiltering) | 0.6.2.5 | Alchiweb | AlchiwebApp.PagingFiltering |
| 2026-10-06 18:35:02 | [MSTYZ.Herald.Abstractions](https://www.nuget.org/packages/MSTYZ.Herald.Abstractions) | 1.0.0 | Muhammed Sefa Tayaz | Contracts for the Herald mediator library: request, handler, notification and p… |
| 2026-10-06 18:36:35 | [MSTYZ.Herald](https://www.nuget.org/packages/MSTYZ.Herald) | 1.0.0 | Muhammed Sefa Tayaz | A lightweight mediator library for .NET with requests and handlers, notificatio… |
| 2026-10-06 18:40:03 | [Samhammer.AspNetCore.StringTrimming](https://www.nuget.org/packages/Samhammer.AspNetCore.StringTrimming) | 1.0.0 | Samhammer AG | Common parts of the Samhammer string trimming for ASP.NET Core MVC: [NoTrim] at… |
| 2026-10-06 18:40:03 | [Samhammer.AspNetCore.StringTrimming.SystemTextJson](https://www.nuget.org/packages/Samhammer.AspNetCore.StringTrimming.SystemTextJson) | 1.0.0 | Samhammer AG | System.Text.Json support for the Samhammer string trimming: trims leading and t… |
| 2026-10-06 18:40:04 | [Samhammer.AspNetCore.StringTrimming.NewtonsoftJson](https://www.nuget.org/packages/Samhammer.AspNetCore.StringTrimming.NewtonsoftJson) | 1.0.0 | Samhammer AG | Newtonsoft.Json support for Samhammer.AspNetCore.StringTrimming: trims leading… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-20 16:19 UTC

New packages created between 2026-11-20 15:22 UTC and 2026-11-20 16:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-20T16-19-14-921496Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-20 15:23:08 | [Kitpymes.Core.Results](https://www.nuget.org/packages/Kitpymes.Core.Results) | 1.0.1 | Kitpymes, Sebastian R Ferrari | Resultados estándar para operaciones y respuestas de API (ApiResult). |
| 2026-11-20 15:25:47 | [Webority.Security.Html](https://www.nuget.org/packages/Webority.Security.Html) | 0.74.0 | Webority Technologies | The shared content HTML sanitiser: one configured IHtmlSanitizer for rendered M… |
| 2026-11-20 15:30:14 | [HostLoom.AspNetCore.DataProtection](https://www.nuget.org/packages/HostLoom.AspNetCore.DataProtection) | 0.22.0 | Aleksandr Pavlov | ASP.NET Core Data Protection key rings on shared HostLoom Redis connections. |
| 2026-11-20 15:30:35 | [Umbraco.Community.SuperSecretLoginButton](https://www.nuget.org/packages/Umbraco.Community.SuperSecretLoginButton) | 0.1.0 | Andy Cross | A "Log in with Umbraco" button on your site that only appears for browsers that… |
| 2026-11-20 15:33:36 | [Saku.GodotUtilities](https://www.nuget.org/packages/Saku.GodotUtilities) | 3.6.2 | Saku | A collection of general-purpose C# utilities and Roslyn source generators for G… |
| 2026-11-20 15:33:51 | [ToraNith.WebNook](https://www.nuget.org/packages/ToraNith.WebNook) | 0.1.0 | toras9000 | A small utility library for ASP.NET Core. |
| 2026-11-20 15:34:28 | [STI.IT2025.G6.6MQXSRC3](https://www.nuget.org/packages/STI.IT2025.G6.6MQXSRC3) | 1.0.0 | STI Group 6 | Group 6 verifier library (STI IT2025 take-home activity). |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

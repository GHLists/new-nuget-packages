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

## Latest list — 2026-11-21 02:19 UTC

New packages created between 2026-11-21 01:21 UTC and 2026-11-21 02:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-21T02-19-12-467768Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-21 01:23:05 | [TzData.Runtime.Linux](https://www.nuget.org/packages/TzData.Runtime.Linux) | 1.0.1 | DotNet-AGPL | Linux-only app-local IANA time zone data (tzdata 2026f) for .NET. Ships compile… |
| 2026-11-21 01:23:07 | [TzData.Runtime.Linux.AutoInit](https://www.nuget.org/packages/TzData.Runtime.Linux.AutoInit) | 1.0.1 | DotNet-AGPL | Opt-in automatic TZDIR setup for TzData.Runtime.Linux. Injects a module initial… |
| 2026-11-21 01:27:44 | [webhop-gen](https://www.nuget.org/packages/webhop-gen) | 2.1.0 | elebree | Issues the tokens that WebHop origins open tunnels with: creates an issuer's ke… |
| 2026-11-21 01:29:41 | [PeachBrackets.Avalonia](https://www.nuget.org/packages/PeachBrackets.Avalonia) | 0.10.1 | PeachBrackets.Avalonia | An Avalonia control that shows an HTML document laid out by PeachBrackets, draw… |
| 2026-11-21 01:47:38 | [OracleSqlParser.Cli](https://www.nuget.org/packages/OracleSqlParser.Cli) | 1.0.0 | aklein53 | Command-line tool for OracleSqlParser: parses Oracle SQL and PL/SQL and prints… |
| 2026-11-21 01:47:39 | [OracleSqlParser](https://www.nuget.org/packages/OracleSqlParser) | 1.0.0 | aklein53 | Oracle SQL and PL/SQL parser producing a typed AST, with a SQL script generator… |
| 2026-11-21 02:03:32 | [Dloizides.SecurityHeaders](https://www.nuget.org/packages/Dloizides.SecurityHeaders) | 0.1.0 | DLoizides | Global security headers for ASP.NET Core APIs: X-Content-Type-Options nosniff,… |
| 2026-11-21 02:03:45 | [Dloizides.ProblemDetails](https://www.nuget.org/packages/Dloizides.ProblemDetails) | 0.1.0 | DLoizides | RFC 9457 ProblemDetails for every ASP.NET Core error response, with the request… |
| 2026-11-21 02:03:56 | [Dloizides.Http.Resilience](https://www.nuget.org/packages/Dloizides.Http.Resilience) | 0.1.0 | DLoizides | House HttpClient defaults on Microsoft.Extensions.Http.Resilience: timeout, ret… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

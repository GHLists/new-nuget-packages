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

## Latest list — 2026-10-27 05:20 UTC

New packages created between 2026-10-27 04:20 UTC and 2026-10-27 05:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-27T05-20-27-952Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-27 04:23:59 | [Pacem.AspNetCore](https://www.nuget.org/packages/Pacem.AspNetCore) | 0.10.19-fermi | Cristian Merighi | ASP.NET Core utilities in Pacem Ecosystem: API exception handler and problem re… |
| 2026-10-27 04:24:06 | [Pacem.AspNetCore.Acme](https://www.nuget.org/packages/Pacem.AspNetCore.Acme) | 0.10.19-fermi | Cristian Merighi | ACME utilities for certificates renewal in Pacem Ecosystem. |
| 2026-10-27 04:24:11 | [Pacem.AspNetCore.CookiePolicy](https://www.nuget.org/packages/Pacem.AspNetCore.CookiePolicy) | 0.10.19-fermi | Cristian Merighi | Cookie Policy (GDPR-compliant) handling in Pacem Ecosystem. |
| 2026-10-27 04:38:58 | [LMail](https://www.nuget.org/packages/LMail) | 0.1.0 | LMail contributors | One lightweight email-sending API for SMTP, Microsoft Graph, Cloudflare, Brevo,… |
| 2026-10-27 04:52:26 | [Lemon.Pet.Look](https://www.nuget.org/packages/Lemon.Pet.Look) | 1.0.0 | Tracy Ma | How the Lemon pet looks: its models, names, pictures and the control that draws… |
| 2026-10-27 05:00:41 | [AppWeaver.Results](https://www.nuget.org/packages/AppWeaver.Results) | 1.0.0 | Team AppWeaver | Result primitives for AppWeaver: Result<T>, Unit Result, Error model, and funct… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

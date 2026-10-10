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

## Latest list — 2026-10-10 05:20 UTC

New packages created between 2026-10-10 04:18 UTC and 2026-10-10 05:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-10T05-20-53-180799Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-10 04:21:49 | [Webority.Email.Outreach.Apollo](https://www.nuget.org/packages/Webority.Email.Outreach.Apollo) | 0.39.0 | Webority Technologies | Apollo contact provider for Webority.Email.Outreach over Apollo's REST API: lis… |
| 2026-10-10 04:27:38 | [XUnitAssured.Playwright.AspNetCore](https://www.nuget.org/packages/XUnitAssured.Playwright.AspNetCore) | 6.4.1 | Carlos Andrew Costa Bezerra | Browser tests against your own ASP.NET Core API with XUnitAssured.Playwright: a… |
| 2026-10-10 04:49:21 | [AnyCAD.Interop3D.Win64](https://www.nuget.org/packages/AnyCAD.Interop3D.Win64) | 2026.10.10.1221 | AnyCAD Inc. | Interop3D runtimes for Windows. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

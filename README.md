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

## Latest list — 2026-10-02 16:19 UTC

New packages created between 2026-10-02 15:23 UTC and 2026-10-02 16:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-02T16-19-54-274346Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-02 15:31:38 | [TheSkyLite.SkyNet](https://www.nuget.org/packages/TheSkyLite.SkyNet) | 1.0.5 | HC Kim | Server-driven web framework for ASP.NET Core. C# pages, vanilla JavaScript, no… |
| 2026-10-02 15:42:41 | [Soenneker.Stripe.Dtos.JsError](https://www.nuget.org/packages/Soenneker.Stripe.Dtos.JsError) | 4.0.1 | Jake Soenneker | Stripe.js browser error payloads with forward-compatible codes and expanded pay… |
| 2026-10-02 16:08:25 | [Swallow.SiteGen](https://www.nuget.org/packages/Swallow.SiteGen) | 0.0.1 | Philipp Kiener | A small and unambitious static site-generator. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

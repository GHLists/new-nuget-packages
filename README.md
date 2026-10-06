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

## Latest list — 2026-10-06 13:22 UTC

New packages created between 2026-10-06 12:20 UTC and 2026-10-06 13:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-06T13-22-43-454596Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-06 12:22:43 | [kdyf.umbraco14.headless](https://www.nuget.org/packages/kdyf.umbraco14.headless) | 1.6.0 | VssAdministrator | Description |
| 2026-10-06 12:32:39 | [Sunsetless.EwsScan](https://www.nuget.org/packages/Sunsetless.EwsScan) | 1.0.0 | Sunsetless | Lists the EWS Managed API calls in compiled .NET assemblies and shows what each… |
| 2026-10-06 12:33:07 | [LocaleNames.Core](https://www.nuget.org/packages/LocaleNames.Core) | 48.1.0 | Jiri Slachta | Code of the LocaleNames library - lookup of localized names of languages, count… |
| 2026-10-06 12:33:27 | [LocaleNames.Data](https://www.nuget.org/packages/LocaleNames.Data) | 48.1.0 | Jiri Slachta | Unicode CLDR data (names of languages, countries and currencies) for the Locale… |
| 2026-10-06 12:34:01 | [LocaleNames.Embed](https://www.nuget.org/packages/LocaleNames.Embed) | 48.1.0 | Jiri Slachta | Embeds the LocaleNames CLDR data (names of languages, countries and currencies)… |
| 2026-10-06 12:37:41 | [VisioForge.DotNet.Core.UI.WebForms](https://www.nuget.org/packages/VisioForge.DotNet.Core.UI.WebForms) | 2026.10.6 | VisioForge | VisioForge Controls UI Wrappers for ASP.NET Web Forms |
| 2026-10-06 12:50:34 | [Luxoft.Framework.Configuration.Environment](https://www.nuget.org/packages/Luxoft.Framework.Configuration.Environment) | 28.0.5 | Luxoft BSS | Package Description |
| 2026-10-06 13:03:24 | [Soenneker.Compression.OpenZl](https://www.nuget.org/packages/Soenneker.Compression.OpenZl) | 4.0.1 | Jake Soenneker | A dependency-free managed C# implementation of OpenZL compression. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-06 03:20 UTC

New packages created between 2026-11-06 02:21 UTC and 2026-11-06 03:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-06T03-20-30-373184Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-06 02:26:48 | [Makoto](https://www.nuget.org/packages/Makoto) | 0.1.0 | Veld Labs | Source-generated validation. Rules compile to static extension methods and vali… |
| 2026-11-06 02:26:56 | [Esatto.Umbraco.Backoffice.Accessibility](https://www.nuget.org/packages/Esatto.Umbraco.Backoffice.Accessibility) | 1.0.0 | Carl Schéle | Accessibility for Umbraco: a Content-section dashboard that scans your publishe… |
| 2026-11-06 02:27:39 | [Meziantou.Framework.Iconify](https://www.nuget.org/packages/Meziantou.Framework.Iconify) | 1.0.0 | meziantou | Strongly-typed access to Iconify icons (Material Design Icons, Lucide, Tabler,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

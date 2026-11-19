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

## Latest list — 2026-11-19 11:22 UTC

New packages created between 2026-11-19 10:22 UTC and 2026-11-19 11:22 UTC.

[Full CSV](data/new-nuget-packages-2026-11-19T11-22-05-476749Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-19 10:31:03 | [Umbraco.Community.UmbraDesktop.Media](https://www.nuget.org/packages/Umbraco.Community.UmbraDesktop.Media) | 17.5.0 | Luuk Peters | Media apps for UmbraDesktop. A Media Manager that opens the media library in de… |
| 2026-11-19 10:59:34 | [Bapp.ApiClient](https://www.nuget.org/packages/Bapp.ApiClient) | 0.5.0 | BAPP | Official .NET client for the BAPP Auto API: authentication, entity CRUD, docume… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

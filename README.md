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

## Latest list — 2026-11-07 09:20 UTC

New packages created between 2026-11-07 08:20 UTC and 2026-11-07 09:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-07T09-20-48-178335Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-07 08:27:33 | [EntexInteractive.Extensions.EntityFrameworkCore](https://www.nuget.org/packages/EntexInteractive.Extensions.EntityFrameworkCore) | 10.0.6 | Entex Interactive, LLC | Provides extensions to be used with Microsoft.EntityFrameworkCore. |
| 2026-11-07 08:37:15 | [Intrlay](https://www.nuget.org/packages/Intrlay) | 0.1.1 | Intrlay | Typed storage for generated Intrlay memory views |
| 2026-11-07 08:44:05 | [StdUnit.AceOne.Templates](https://www.nuget.org/packages/StdUnit.AceOne.Templates) | 0.2.0 | itminus | Templates for StdUnit.AceOne project |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

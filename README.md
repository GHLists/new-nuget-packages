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

## Latest list — 2026-10-31 07:18 UTC

New packages created between 2026-10-31 06:19 UTC and 2026-10-31 07:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-31T07-18-59-615385Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-31 06:23:03 | [HackerOs.Apps.Store](https://www.nuget.org/packages/HackerOs.Apps.Store) | 2.2.0 | Benoit Robin | The Hack Store, the HackerOS system app that installs, updates and removes apps… |
| 2026-10-31 06:29:42 | [Simulacra](https://www.nuget.org/packages/Simulacra) | 0.0.2 | Niklas Wendel | Simulacra - source-generated proxies for .NET |
| 2026-10-31 06:42:30 | [OvoUi.Lang.Generator](https://www.nuget.org/packages/OvoUi.Lang.Generator) | 1.0.4 | tiouo | Source generator for strongly typed OvoUi.Lang localization resources. |
| 2026-10-31 07:08:21 | [NKaspa](https://www.nuget.org/packages/NKaspa) | 0.1.9-alpha | lifeme2027 | A .NET library for Kaspa. The public API follows NBitcoin where a Kaspa counter… |
| 2026-10-31 07:08:22 | [Mordex.Windows](https://www.nuget.org/packages/Mordex.Windows) | 6.0.0 | Ehsan Enaloo | Mordex WinForms controls for .NET 10 with out-of-process designer support. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-29 06:21 UTC

New packages created between 2026-10-29 05:20 UTC and 2026-10-29 06:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-29T06-21-05-421996Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-29 05:46:06 | [Joinery.Dovetail.Hosting](https://www.nuget.org/packages/Joinery.Dovetail.Hosting) | 0.3.0 | David Driscoll,Rocket Surgeon… | Adds helpers to easily bootstrap an application using conventions by just using… |
| 2026-10-29 06:13:16 | [Pilz.Updating.Ui.WinForms](https://www.nuget.org/packages/Pilz.Updating.Ui.WinForms) | 5.0.1 | Pilz.Updating.Ui.WinForms | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

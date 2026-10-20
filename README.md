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

## Latest list — 2026-10-20 06:21 UTC

New packages created between 2026-10-20 05:19 UTC and 2026-10-20 06:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-20T06-21-09-056649Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-20 05:30:52 | [Facturexa.ZugferdValidator](https://www.nuget.org/packages/Facturexa.ZugferdValidator) | 7.3.0 | Zanyar Systems | Validates ZUGFeRD / Factur-X and XRechnung e-invoices offline for .NET; profile… |
| 2026-10-20 05:54:15 | [ObjectListView.WinForms](https://www.nuget.org/packages/ObjectListView.WinForms) | 3.0.1-preview | Phillip Piper,Teddy Z | A maintained fork of ObjectListView, a Windows Forms ListView control with mode… |
| 2026-10-20 06:06:29 | [Zuken.E3.Utilities.GetProjectData](https://www.nuget.org/packages/Zuken.E3.Utilities.GetProjectData) | 0.9.4 | Zuken E3 GmbH | Zuken.E3.Utilities.GetProjectData wrapper for COM api call job.GetProjectData f… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

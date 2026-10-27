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

## Latest list — 2026-10-27 17:21 UTC

New packages created between 2026-10-27 16:20 UTC and 2026-10-27 17:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-27T17-21-04-558495Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-27 16:28:45 | [JxlSharp](https://www.nuget.org/packages/JxlSharp) | 0.13.0 | Hefaistos68 | Pure C#/.NET implementation of JPEG XL (libjxl) with both a simple default-para… |
| 2026-10-27 16:46:13 | [Davydov.Revit.Templates](https://www.nuget.org/packages/Davydov.Revit.Templates) | 0.2.0 | Nikolai Davydov | dotnet new davydov-revit: a Revit 2025–2027 add-in with Nice3point SDK and Tool… |
| 2026-10-27 16:50:38 | [VirtoCommerce.AdminShell.Core](https://www.nuget.org/packages/VirtoCommerce.AdminShell.Core) | 3.1000.0 | VirtoCommerce.AdminShell.Core | Package Description |
| 2026-10-27 16:50:39 | [VirtoCommerce.AdminShell.Data](https://www.nuget.org/packages/VirtoCommerce.AdminShell.Data) | 3.1000.0 | VirtoCommerce.AdminShell.Data | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

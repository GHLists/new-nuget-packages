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

## Latest list — 2026-11-23 00:20 UTC

New packages created between 2026-11-22 23:20 UTC and 2026-11-23 00:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-23T00-20-32-627275Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-22 23:34:00 | [SuperStrong.Types.HotChocolate.V16](https://www.nuget.org/packages/SuperStrong.Types.HotChocolate.V16) | 1.0.1 | Ihor Kuzmychov (iikuzmychov) | Strong types for .NET — define once, use everywhere! |
| 2026-11-22 23:34:03 | [SuperStrong.Types.NewtonsoftJson.V13](https://www.nuget.org/packages/SuperStrong.Types.NewtonsoftJson.V13) | 1.0.1 | Ihor Kuzmychov (iikuzmychov) | Strong types for .NET — define once, use everywhere! |
| 2026-11-22 23:34:05 | [SuperStrong.Types.EntityFrameworkCore.V10](https://www.nuget.org/packages/SuperStrong.Types.EntityFrameworkCore.V10) | 1.0.1 | Ihor Kuzmychov (iikuzmychov) | Strong types for .NET — define once, use everywhere! |
| 2026-11-22 23:34:06 | [SuperStrong.Types.AspNetCore.OpenApi.V10](https://www.nuget.org/packages/SuperStrong.Types.AspNetCore.OpenApi.V10) | 1.0.1 | Ihor Kuzmychov (iikuzmychov) | Strong types for .NET — define once, use everywhere! |
| 2026-11-22 23:35:44 | [Rogski.LicenseGate](https://www.nuget.org/packages/Rogski.LicenseGate) | 0.1.0 | License Gate contributors | Check direct and transitive NuGet dependency licenses against a repository poli… |
| 2026-11-23 00:08:00 | [Validonce.AspNetCore](https://www.nuget.org/packages/Validonce.AspNetCore) | 0.0.1-placeholder | Metatoy LLC | Placeholder for validonce: write validation rules once on the server, enforce t… |
| 2026-11-23 00:08:01 | [Validonce](https://www.nuget.org/packages/Validonce) | 0.0.1-placeholder | Metatoy LLC | Placeholder for validonce: write validation rules once on the server, enforce t… |
| 2026-11-23 00:08:01 | [Validonce.Cli](https://www.nuget.org/packages/Validonce.Cli) | 0.0.1-placeholder | Metatoy LLC | Placeholder for validonce: write validation rules once on the server, enforce t… |
| 2026-11-23 00:08:02 | [Validonce.FluentValidation](https://www.nuget.org/packages/Validonce.FluentValidation) | 0.0.1-placeholder | Metatoy LLC | Placeholder for validonce: write validation rules once on the server, enforce t… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

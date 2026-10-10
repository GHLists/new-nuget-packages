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

## Latest list — 2026-10-10 02:19 UTC

New packages created between 2026-10-10 01:22 UTC and 2026-10-10 02:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-10T02-19-35-101579Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-10 01:56:59 | [CodeBrix.RustTools.MitLicenseForever](https://www.nuget.org/packages/CodeBrix.RustTools.MitLicenseForever) | 1.0.283.116 | Jeremy Ellis | A .NET library for inspecting, license-checking, building and running Rust appl… |
| 2026-10-10 01:57:26 | [CodeBrix.RustTools.Docker.MitLicenseForever](https://www.nuget.org/packages/CodeBrix.RustTools.Docker.MitLicenseForever) | 1.0.283.116 | Jeremy Ellis | A .NET library for building Rust applications inside a Linux Docker container,… |
| 2026-10-10 02:09:30 | [IPluginBase](https://www.nuget.org/packages/IPluginBase) | 0.0.4 | Jaffoo | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-26 09:19 UTC

New packages created between 2026-11-26 08:21 UTC and 2026-11-26 09:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-26T09-19-25-110469Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-26 08:23:48 | [Boyner.HelloWorld](https://www.nuget.org/packages/Boyner.HelloWorld) | 1.0.0 | Boyner | A simple Hello World package by Boyner. Adds the Boyner.HelloWorld.Greeter clas… |
| 2026-11-26 08:35:39 | [Dharmu.Security.Core](https://www.nuget.org/packages/Dharmu.Security.Core) | 0.2.0 | Dharmendra Gupta | Core contracts and ECDSA P-256 validation for signed offline software licenses… |
| 2026-11-26 08:36:43 | [Dharmu.Security.Windows](https://www.nuget.org/packages/Dharmu.Security.Windows) | 0.2.0 | Dharmendra Gupta | Windows CNG device identity, optional TPM-backed signing identity, and device-k… |
| 2026-11-26 08:37:01 | [Dharmu.Security.AspNetCore](https://www.nuget.org/packages/Dharmu.Security.AspNetCore) | 0.2.0 | Dharmendra Gupta | Offline license enforcement middleware, signed activation endpoints, revision a… |
| 2026-11-26 08:52:14 | [DeepBlue.FunctionTraceTime.Core](https://www.nuget.org/packages/DeepBlue.FunctionTraceTime.Core) | 1.0.0 | DeepBlue.FunctionTraceTime.Co… | 一个方法追踪日记 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

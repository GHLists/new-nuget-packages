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

## Latest list — 2026-11-25 00:19 UTC

New packages created between 2026-11-24 23:20 UTC and 2026-11-25 00:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-25T00-19-41-179181Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-24 23:48:30 | [Toolbelt.Blazor.Prismizor](https://www.nuget.org/packages/Toolbelt.Blazor.Prismizor) | 1.0.0 | J.Sakamoto | A syntax highlighting component for Blazor, which is a C# port of Prism.js. It… |
| 2026-11-25 00:03:34 | [sktest123](https://www.nuget.org/packages/sktest123) | 1.0.0 | Svetlana Kofman | Empty test package. |
| 2026-11-25 00:08:35 | [Azure.Functions.Cli.Workloads.Workers.Python.osx-arm64](https://www.nuget.org/packages/Azure.Functions.Cli.Workloads.Workers.Python.osx-arm64) | 4.47.0-preview | Microsoft | Azure Functions CLI content workload that ships the Python language worker. |
| 2026-11-25 00:08:42 | [Azure.Functions.Cli.Workloads.Workers.Python.win-arm64](https://www.nuget.org/packages/Azure.Functions.Cli.Workloads.Workers.Python.win-arm64) | 4.47.0-preview | Microsoft | Azure Functions CLI content workload that ships the Python language worker. |
| 2026-11-25 00:08:54 | [Microsoft.ValidationOS.SDK.Microsoft-WinVOS-Inbox-Drivers-Platform](https://www.nuget.org/packages/Microsoft.ValidationOS.SDK.Microsoft-WinVOS-Inbox-Drivers-Platform) | 10.0.26100.10068 | Microsoft | The Validation OS Modular SDK available as a set of NuGet packages for more sea… |
| 2026-11-25 00:14:14 | [TeaQL.ObjectStorage.S3](https://www.nuget.org/packages/TeaQL.ObjectStorage.S3) | 0.7.0 | TeaQL | TeaQL runtime and data services for .NET |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

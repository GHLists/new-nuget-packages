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

## Latest list — 2026-11-26 19:20 UTC

New packages created between 2026-11-26 18:19 UTC and 2026-11-26 19:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-26T19-20-07-162556Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-26 18:20:57 | [DbRelay.SqlServer](https://www.nuget.org/packages/DbRelay.SqlServer) | 0.2.0 | DbRelay contributors | SQL Server storage provider for DbRelay (Microsoft.Data.SqlClient): transaction… |
| 2026-11-26 18:30:51 | [AudioIOSharp](https://www.nuget.org/packages/AudioIOSharp) | 0.1.0 | Mike Oliphant | Real-time, allocation-free audio and MIDI I/O for .NET: ASIO, ALSA, JACK. |
| 2026-11-26 18:41:21 | [Gatewright.State.Redis](https://www.nuget.org/packages/Gatewright.State.Redis) | 1.0.0 | Pierrick Gourlain | Package Description |
| 2026-11-26 18:41:22 | [Gatewright.Core](https://www.nuget.org/packages/Gatewright.Core) | 1.0.0 | Pierrick Gourlain | Package Description |
| 2026-11-26 18:41:22 | [Gatewright.Sdk](https://www.nuget.org/packages/Gatewright.Sdk) | 1.0.0 | Pierrick Gourlain | Package Description |
| 2026-11-26 18:41:23 | [Gatewright.Testing](https://www.nuget.org/packages/Gatewright.Testing) | 1.0.0 | Pierrick Gourlain | Package Description |
| 2026-11-26 18:41:23 | [Gatewright.Exposure](https://www.nuget.org/packages/Gatewright.Exposure) | 1.0.0 | Pierrick Gourlain | Package Description |
| 2026-11-26 18:41:23 | [Gatewright.Distribution](https://www.nuget.org/packages/Gatewright.Distribution) | 1.0.0 | Pierrick Gourlain | Package Description |
| 2026-11-26 18:41:24 | [Gatewright.Templates](https://www.nuget.org/packages/Gatewright.Templates) | 1.0.0 | Pierrick Gourlain | dotnet new template for a Gatewright host: a gateway distribution with a sample… |
| 2026-11-26 18:41:24 | [Gatewright.Policies](https://www.nuget.org/packages/Gatewright.Policies) | 1.0.0 | Pierrick Gourlain | Package Description |
| 2026-11-26 18:41:24 | [Gatewright.DataPlane](https://www.nuget.org/packages/Gatewright.DataPlane) | 1.0.0 | Pierrick Gourlain | Package Description |
| 2026-11-26 18:41:25 | [Gatewright.Cli](https://www.nuget.org/packages/Gatewright.Cli) | 1.0.0 | Pierrick Gourlain | Package Description |
| 2026-11-26 18:41:25 | [Gatewright.ControlPlane](https://www.nuget.org/packages/Gatewright.ControlPlane) | 1.0.0 | Pierrick Gourlain | Package Description |
| 2026-11-26 18:41:26 | [Gatewright.Kubernetes](https://www.nuget.org/packages/Gatewright.Kubernetes) | 1.0.0 | Pierrick Gourlain | Package Description |
| 2026-11-26 18:41:26 | [Gatewright.Abstractions](https://www.nuget.org/packages/Gatewright.Abstractions) | 1.0.0 | Pierrick Gourlain | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

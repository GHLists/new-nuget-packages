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

## Latest list — 2026-11-07 19:21 UTC

New packages created between 2026-11-07 18:20 UTC and 2026-11-07 19:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-07T19-21-10-109018Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-07 18:20:47 | [BTDB.BackendActions](https://www.nuget.org/packages/BTDB.BackendActions) | 36.1.0 | Boris Letocha | Leader-scheduled, resource-limited background actions over BTDB replication and… |
| 2026-11-07 19:07:02 | [PowerCraft.OCI.Core](https://www.nuget.org/packages/PowerCraft.OCI.Core) | 0.1.1 | The Code Kitchen | Typed kernel for PowerCraft.OCI: a read-only reader of an Oracle Cloud Infrastr… |
| 2026-11-07 19:13:54 | [OasDelta.linux-arm64](https://www.nuget.org/packages/OasDelta.linux-arm64) | 1.0.1 | John Zabroski, Fluent Foundat… | OpenAPI diff and breaking-change detection: a byte-for-byte compatible C# port… |
| 2026-11-07 19:13:55 | [OasDelta.linux-x64](https://www.nuget.org/packages/OasDelta.linux-x64) | 1.0.1 | John Zabroski, Fluent Foundat… | OpenAPI diff and breaking-change detection: a byte-for-byte compatible C# port… |
| 2026-11-07 19:13:56 | [OasDelta.osx-arm64](https://www.nuget.org/packages/OasDelta.osx-arm64) | 1.0.1 | John Zabroski, Fluent Foundat… | OpenAPI diff and breaking-change detection: a byte-for-byte compatible C# port… |
| 2026-11-07 19:13:57 | [OasDelta.osx-x64](https://www.nuget.org/packages/OasDelta.osx-x64) | 1.0.1 | John Zabroski, Fluent Foundat… | OpenAPI diff and breaking-change detection: a byte-for-byte compatible C# port… |
| 2026-11-07 19:14:00 | [OasDelta](https://www.nuget.org/packages/OasDelta) | 1.0.1 | John Zabroski, Fluent Foundat… | OpenAPI diff and breaking-change detection: a byte-for-byte compatible C# port… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

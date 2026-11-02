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

## Latest list — 2026-11-02 23:21 UTC

New packages created between 2026-11-02 22:21 UTC and 2026-11-02 23:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-02T23-21-41-077215Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-02 22:32:32 | [CodeMap.Tool](https://www.nuget.org/packages/CodeMap.Tool) | 0.2.1 | CodeMap contributors | Maps C# solutions (and TypeScript / JavaScript, with Node.js) into a relationsh… |
| 2026-11-02 22:47:01 | [ShortDev.BluePrint](https://www.nuget.org/packages/ShortDev.BluePrint) | 0.1.0-alpha | ShortDevelopment | Compiler for the GTK blueprint markup language |
| 2026-11-02 22:57:02 | [Mediana.Codecs.Jpeg](https://www.nuget.org/packages/Mediana.Codecs.Jpeg) | 0.1.14 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-02 23:06:02 | [Reimaginate.Orchestrator.Exchange](https://www.nuget.org/packages/Reimaginate.Orchestrator.Exchange) | 1.1.13 | Reimaginate | Read-only Exchange Online mailbox workflow actions for Reimaginate Orchestrator. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

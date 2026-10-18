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

## Latest list — 2026-10-18 15:19 UTC

New packages created between 2026-10-18 14:19 UTC and 2026-10-18 15:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-18T15-19-25-936083Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-18 14:30:12 | [E2e4.OpenXml.Wrappers](https://www.nuget.org/packages/E2e4.OpenXml.Wrappers) | 1.0.0 | E2e4 | A Word-object-model-like API (Range, Paragraphs, Tables, Bookmarks, Comments, F… |
| 2026-10-18 14:33:10 | [CHOCore.chodatabase](https://www.nuget.org/packages/CHOCore.chodatabase) | 8.0.0 | CHOCore.chodatabase | Package Description |
| 2026-10-18 14:33:32 | [Esgo](https://www.nuget.org/packages/Esgo) | 0.1.1 | ESGO Logistics UG (haftungsbe… | Official .NET SDK for the ESGO API: matching search for empty truck runs and op… |
| 2026-10-18 14:40:40 | [Laminar](https://www.nuget.org/packages/Laminar) | 0.1.0 | Jaxel Rojas | Small, composable, operation-first resilience for .NET delegates. |
| 2026-10-18 14:59:44 | [Coworkee.Retention](https://www.nuget.org/packages/Coworkee.Retention) | 0.0.1.34 | fgilde | Retention: days to keep per kind of data (audit trail, outbox, logs, deleted re… |
| 2026-10-18 14:59:52 | [CxAgent.Plugins.Abstractions](https://www.nuget.org/packages/CxAgent.Plugins.Abstractions) | 3.0.0 | Nikolaos Protopapas | The contract a cxagent plugin implements: IPlugin, its manifest, and the job ty… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

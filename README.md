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

## Latest list — 2026-11-02 00:19 UTC

New packages created between 2026-11-01 23:20 UTC and 2026-11-02 00:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-02T00-19-31-43701Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-01 23:25:04 | [Scotec.Revit.Analyzers](https://www.nuget.org/packages/Scotec.Revit.Analyzers) | 2027.4.1 | scotec Software Solutions AB | Roslyn analyzers for Scotec.Revit. |
| 2026-11-01 23:25:04 | [Scotec.Revit.Isolation.SourceGenerator](https://www.nuget.org/packages/Scotec.Revit.Isolation.SourceGenerator) | 2027.4.1 | scotec Software Solutions AB | Source generator to support assembly load context in Revit add-ins. |
| 2026-11-01 23:29:40 | [Beardmouse.Scriptorium.Nib.Snapshot](https://www.nuget.org/packages/Beardmouse.Scriptorium.Nib.Snapshot) | 0.4.0 | Maxime Mangel | Package Description |
| 2026-11-01 23:59:06 | [Markwardt.LiveAi](https://www.nuget.org/packages/Markwardt.LiveAi) | 1.0.0 | Chris Markwardt | Runs live AI coding sessions on the Claude Code, OpenAI Codex and OpenCode (for… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

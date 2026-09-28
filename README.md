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

## Latest list — 2026-09-28 12:21 UTC

New packages created between 2026-09-28 11:23 UTC and 2026-09-28 12:21 UTC.

[Full CSV](data/new-nuget-packages-2026-09-28T12-21-49-573721Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-28 11:39:37 | [Flamoris.Mcp.Wpf](https://www.nuget.org/packages/Flamoris.Mcp.Wpf) | 1.2.0 | FLAMORIS | Shared FLAMORIS desktop MCP connection UI. |
| 2026-09-28 11:46:26 | [Fuaran.Program.Server.UI](https://www.nuget.org/packages/Fuaran.Program.Server.UI) | 0.6.0 | Fuaran | Fuaran.Program.Server.UI — the UI adapter for the server placement of the domai… |
| 2026-09-28 11:46:27 | [Fuaran.Program.UI](https://www.nuget.org/packages/Fuaran.Program.UI) | 0.6.0 | Fuaran | Fuaran.Program.UI — the UI adapter for the domain-generic bounded program core:… |
| 2026-09-28 11:59:25 | [Aprillz.MewUI.Geometry](https://www.nuget.org/packages/Aprillz.MewUI.Geometry) | 0.22.0 | Aprillz | Geometry operations for MewUI shapes. |
| 2026-09-28 11:59:27 | [Aprillz.MewUI.Markdown](https://www.nuget.org/packages/Aprillz.MewUI.Markdown) | 0.22.0 | Aprillz | Native Markdown controls for MewUI using Markdig. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

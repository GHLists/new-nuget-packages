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

## Latest list — 2026-10-18 05:21 UTC

New packages created between 2026-10-18 04:20 UTC and 2026-10-18 05:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-18T05-21-29-808562Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-18 04:59:50 | [SevenMLabs.Astrology](https://www.nuget.org/packages/SevenMLabs.Astrology) | 1.0.0 | SevenMLabs.Astrology | 7mlabs Astro SDK: offline astrology calculations, IANA birth-time conversion an… |
| 2026-10-18 05:00:14 | [ErinnTimer](https://www.nuget.org/packages/ErinnTimer) | 1.0.0 | Molth Nevin | Caller-driven timer scheduling with typed callback storage. |
| 2026-10-18 05:01:40 | [com.IvanMurzak.CodeExec](https://www.nuget.org/packages/com.IvanMurzak.CodeExec) | 0.1.0 | Ivan Murzak | Run short C# snippets inside a live host process (game engines, editors, any .N… |
| 2026-10-18 05:01:41 | [com.IvanMurzak.CodeExec.Roslyn](https://www.nuget.org/packages/com.IvanMurzak.CodeExec.Roslyn) | 0.1.0 | Ivan Murzak | Source-only Roslyn compiler for com.IvanMurzak.CodeExec. Compiles inside your p… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

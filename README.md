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

## Latest list — 2026-10-09 08:19 UTC

New packages created between 2026-10-09 07:20 UTC and 2026-10-09 08:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-09T08-19-53-583843Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-09 07:31:13 | [Universe.MemoryPack.Generator](https://www.nuget.org/packages/Universe.MemoryPack.Generator) | 1.30.0 | Cysharp,Ryan Martin | Code generator for MemoryPack. |
| 2026-10-09 07:31:52 | [Universe.MemoryPack](https://www.nuget.org/packages/Universe.MemoryPack) | 1.30.0 | Cysharp,Ryan Martin | Zero encoding extreme performance binary serializer for C#. |
| 2026-10-09 08:08:36 | [VL.MediaControls.HDE](https://www.nuget.org/packages/VL.MediaControls.HDE) | 1.0.0 | vvvv | Control your media sessions from the vvvv editor |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

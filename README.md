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

## Latest list — 2026-10-24 17:24 UTC

New packages created between 2026-10-24 16:20 UTC and 2026-10-24 17:24 UTC.

[Full CSV](data/new-nuget-packages-2026-10-24T17-24-18-349399Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-24 16:22:53 | [LeanToDotNet.Runtime](https://www.nuget.org/packages/LeanToDotNet.Runtime) | 0.3.1 | Keith Adler | The small runtime a lean2il assembly calls into: Lean's Nat and Int on BigInteg… |
| 2026-10-24 16:22:55 | [lean2il](https://www.nuget.org/packages/lean2il) | 0.3.1 | Keith Adler | Compile Lean 4 definitions to a .NET assembly, after re-checking every proof ab… |
| 2026-10-24 16:22:56 | [LeanToDotNet.Build](https://www.nuget.org/packages/LeanToDotNet.Build) | 0.3.1 | Keith Adler | Compile Lean 4 definitions into your .NET project on every build: runs lake bui… |
| 2026-10-24 16:24:52 | [OBaseRTC](https://www.nuget.org/packages/OBaseRTC) | 26.10.34 | Oesam Technology | Live video between two screens of a Blazor Server app for the OBase Framework:… |
| 2026-10-24 16:42:40 | [AnAspect.Mediator.Notification](https://www.nuget.org/packages/AnAspect.Mediator.Notification) | 1.0.0 | Pouria Riyahi | A lightweight, high-performance notification and domain-event publisher for .NE… |
| 2026-10-24 16:44:59 | [BitMagic.X16E.linux-x64](https://www.nuget.org/packages/BitMagic.X16E.linux-x64) | 0.1.74 | Yazwh0 | BitMagic's Commander X16 emulator. |
| 2026-10-24 16:44:59 | [BitMagic.X16E](https://www.nuget.org/packages/BitMagic.X16E) | 0.1.74 | Yazwh0 | BitMagic's Commander X16 emulator. |
| 2026-10-24 16:45:03 | [BitMagic.X16E.win-x64](https://www.nuget.org/packages/BitMagic.X16E.win-x64) | 0.1.74 | Yazwh0 | BitMagic's Commander X16 emulator. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

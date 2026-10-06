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

## Latest list — 2026-10-06 20:19 UTC

New packages created between 2026-10-06 19:19 UTC and 2026-10-06 20:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-06T20-19-06-78448Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-06 19:21:39 | [Natrix.Composables.Dom](https://www.nuget.org/packages/Natrix.Composables.Dom) | 0.16.0 | miroljub1995 | DOM composables for Natrix components, in the spirit of VueUse. |
| 2026-10-06 19:23:45 | [Achai.Client](https://www.nuget.org/packages/Achai.Client) | 2.0.1 | guavovic | Cliente .NET da achaí-API (CEP, logradouro, cidades, lote, consenso, coordenada… |
| 2026-10-06 19:30:07 | [CircleAI](https://www.nuget.org/packages/CircleAI) | 3.8.0 | The Geek Network | Circle AI — the on-device assistant runtime: inference, memory, skills, voice,… |
| 2026-10-06 19:33:29 | [Meridian.Brighter.Postgres](https://www.nuget.org/packages/Meridian.Brighter.Postgres) | 0.1.1 | Max Anstey | Fixes and additions for running Paramore Brighter on PostgreSQL: a distributed… |
| 2026-10-06 19:36:35 | [RG3.ClosedXML.IO](https://www.nuget.org/packages/RG3.ClosedXML.IO) | 10.1.1 | rg@rg1008.com | 1、基于 RG3.ClosedXML 二次调整依赖包，把包名从 RG3.ClosedXML.IO改成RG3.ClosedXML.IO 2、excel处理，基于… |
| 2026-10-06 19:39:13 | [TDeboutte.Common.Services.Abstractions](https://www.nuget.org/packages/TDeboutte.Common.Services.Abstractions) | 0.4.0 | Thibault Deboutte | Package Description |
| 2026-10-06 19:42:55 | [rpi](https://www.nuget.org/packages/rpi) | 20.0.0.8 | Sub Systems, Inc. | RTF to PDF Converter |
| 2026-10-06 20:02:36 | [MergeIt-RecordMergerForDataverse](https://www.nuget.org/packages/MergeIt-RecordMergerForDataverse) | 1.0.0 | AmraouiH | Merge two active Dynamics 365 / Dataverse records field by field with MergeIt f… |
| 2026-10-06 20:03:22 | [StanzaSharp.Cpu.Linux](https://www.nuget.org/packages/StanzaSharp.Cpu.Linux) | 0.3.0 | Jakob Boman | StanzaSharp plus the CPU libtorch for Linux x64 only. Use instead of StanzaShar… |
| 2026-10-06 20:03:22 | [StanzaSharp.Cpu.MacOS](https://www.nuget.org/packages/StanzaSharp.Cpu.MacOS) | 0.3.0 | Jakob Boman | StanzaSharp plus the CPU libtorch for macOS on Apple Silicon (arm64) only. Use… |
| 2026-10-06 20:03:23 | [StanzaSharp.Cpu.Windows](https://www.nuget.org/packages/StanzaSharp.Cpu.Windows) | 0.3.0 | Jakob Boman | StanzaSharp plus the CPU libtorch for Windows x64 only. Use instead of StanzaSh… |
| 2026-10-06 20:03:23 | [StanzaSharp.Cpu.WindowsArm64](https://www.nuget.org/packages/StanzaSharp.Cpu.WindowsArm64) | 0.3.0 | Jakob Boman | StanzaSharp plus the CPU libtorch for Windows on Arm64 only. TorchSharp-cpu has… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-14 23:21 UTC

New packages created between 2026-11-14 22:19 UTC and 2026-11-14 23:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-14T23-21-27-031117Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-14 22:21:11 | [JalaliX](https://www.nuget.org/packages/JalaliX) | 0.1.1 | Hossein Maklavani | Jalali (Persian / Shamsi) calendar for .NET |
| 2026-11-14 22:51:51 | [Hydris.Cli](https://www.nuget.org/packages/Hydris.Cli) | 0.9.6 | neuralfog | Hydris CLI: task runner and project commands. |
| 2026-11-14 22:51:51 | [Hydris.QuickJs](https://www.nuget.org/packages/Hydris.QuickJs) | 0.9.6 | neuralfog | Embedded QuickJS server-side rendering engine for Hydris. |
| 2026-11-14 22:51:52 | [Hydris](https://www.nuget.org/packages/Hydris) | 0.9.6 | neuralfog | Server-side rendering framework for elemix, built on Native-AOT C#. |
| 2026-11-14 22:51:52 | [Hydris.Generators](https://www.nuget.org/packages/Hydris.Generators) | 0.9.6 | neuralfog | Source generators for Hydris (ViewData). |
| 2026-11-14 22:54:09 | [Wireloom.Dds.Cpp.Generator](https://www.nuget.org/packages/Wireloom.Dds.Cpp.Generator) | 1.1.0 | Wireloom.Dds.Cpp | Native AOT C++ IDL generator and CMake build integration for Wireloom. |
| 2026-11-14 22:54:37 | [Nullean.Snapshots.PublicApi](https://www.nuget.org/packages/Nullean.Snapshots.PublicApi) | 0.13.0 | Nullean and contributors | Public API snapshots for Nullean.Snapshots: an assembly's API stored as a .api… |
| 2026-11-14 23:05:39 | [Electrical.AI.Learning](https://www.nuget.org/packages/Electrical.AI.Learning) | 1.4.0 | Gravicode Studios (Kang Fadhi… | Machine learning for Electrical.Net: load forecasting (gradient boosting, neura… |
| 2026-11-14 23:05:40 | [Electrical.Pmu](https://www.nuget.org/packages/Electrical.Pmu) | 1.4.0 | Gravicode Studios (Kang Fadhi… | Synchrophasors for Electrical.Net: IEEE C37.118.2 data/configuration/header/com… |
| 2026-11-14 23:05:48 | [Electrical.DigitalTwin.ThreeD.Avalonia](https://www.nuget.org/packages/Electrical.DigitalTwin.ThreeD.Avalonia) | 1.4.0 | Gravicode Studios (Kang Fadhi… | Avalonia control for the Electrical.Net 3D digital twin: hosts a ThreeNet scene… |
| 2026-11-14 23:05:56 | [Electrical.DigitalTwin.ThreeD](https://www.nuget.org/packages/Electrical.DigitalTwin.ThreeD) | 1.4.0 | Gravicode Studios (Kang Fadhi… | 3D digital twin for Electrical.Net: procedural substation and feeder scenes (bu… |
| 2026-11-14 23:13:29 | [BlockCodeEditor.Commands](https://www.nuget.org/packages/BlockCodeEditor.Commands) | 0.2.0 | Thomas Volden | The block code editor's command contract and program tree in .NET, for hosts th… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

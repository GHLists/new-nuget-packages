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

## Latest list — 2026-11-04 21:21 UTC

New packages created between 2026-11-04 20:19 UTC and 2026-11-04 21:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-04T21-21-21-492019Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-04 20:26:34 | [TrueTechSoftware.MauiMasonry](https://www.nuget.org/packages/TrueTechSoftware.MauiMasonry) | 0.1.0 | True Tech Software | A lightweight, performant .NET MAUI control for building Pinterest-style stagge… |
| 2026-11-04 20:26:35 | [TrueTechSoftware.MauiMasonry.Core](https://www.nuget.org/packages/TrueTechSoftware.MauiMasonry.Core) | 0.1.0 | True Tech Software | Core contracts and deterministic layout calculation engine for MauiMasonry stag… |
| 2026-11-04 20:30:31 | [Pmad.AI.DiffGuard](https://www.nuget.org/packages/Pmad.AI.DiffGuard) | 0.0.3 | Julien Etelain | Git diff security, supply-chain, blast-radius, and cross-model LLM judge CLI gu… |
| 2026-11-04 20:48:02 | [Suwageval.AgentSdk](https://www.nuget.org/packages/Suwageval.AgentSdk) | 0.1.0 | Piotr Gugnowski | Everything a .NET agent under test needs for Suwageval, an evaluation server fo… |
| 2026-11-04 20:56:08 | [PluginUI.NPlug](https://www.nuget.org/packages/PluginUI.NPlug) | 0.2.0 | asm8086 | Hosts PluginUI editors in NPlug (VST3) plug-ins: IAudioPluginView adapter and p… |
| 2026-11-04 20:56:08 | [PluginUI](https://www.nuget.org/packages/PluginUI) | 0.2.0 | asm8086 | Win32 + Direct2D user interface toolkit for audio plug-in editors (VST3...), Na… |
| 2026-11-04 20:56:08 | [PluginUI.Design](https://www.nuget.org/packages/PluginUI.Design) | 0.2.0 | asm8086 | PluginUI designs (.pluginui): document model, AOT-safe runtime loader, C# code… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

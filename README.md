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

## Latest list — 2026-11-07 04:19 UTC

New packages created between 2026-11-07 03:20 UTC and 2026-11-07 04:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-07T04-19-57-520743Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-07 03:25:05 | [Dflat.Edi.Identity](https://www.nuget.org/packages/Dflat.Edi.Identity) | 1.7.2.89 | Dflat | Plugins EDI du module Identity : purge planifiée des jetons d'appareil (DeviceT… |
| 2026-11-07 03:31:51 | [PluginUI.Host.Vst2](https://www.nuget.org/packages/PluginUI.Host.Vst2) | 0.3.0 | asm8086 | VST 2.4 plug-in hosting for PluginUI.Host: scanning (shell plug-ins included),… |
| 2026-11-07 03:31:52 | [PluginUI.Host.Windows](https://www.nuget.org/packages/PluginUI.Host.Windows) | 0.3.0 | asm8086 | Windows audio and MIDI devices for PluginUI.Host: ASIO, WASAPI output and input… |
| 2026-11-07 03:31:52 | [PluginUI.Host](https://www.nuget.org/packages/PluginUI.Host) | 0.3.0 | asm8086 | Audio plug-in host for .NET: loads VST3 plug-ins (files, or an NPlug factory in… |
| 2026-11-07 03:31:53 | [PluginUI.Desktop](https://www.nuget.org/packages/PluginUI.Desktop) | 0.3.0 | asm8086 | Desktop applications with PluginUI: application object, JSON settings, recent f… |
| 2026-11-07 03:38:47 | [Haytham.Runtime](https://www.nuget.org/packages/Haytham.Runtime) | 0.1.0 | CairnPack | Embeddable runtime for Haytham modules: module lifecycle, events, managed tasks… |
| 2026-11-07 03:40:27 | [ActualLab.Rpc.TypeScript](https://www.nuget.org/packages/ActualLab.Rpc.TypeScript) | 15.1.11 | Actual Chat, Inc. | ActualLab.Rpc.TypeScript - generates TypeScript contracts (interfaces, DTOs, se… |
| 2026-11-07 03:40:28 | [ActualLab.Rpc.TypeScript.Generator](https://www.nuget.org/packages/ActualLab.Rpc.TypeScript.Generator) | 15.1.11 | Actual Chat, Inc. | ActualLab.Rpc.TypeScript.Generator - an MSBuild target generating TypeScript co… |
| 2026-11-07 03:44:13 | [AuditLoggingPipeline.Core](https://www.nuget.org/packages/AuditLoggingPipeline.Core) | 0.2.0 | Troy Crowe | Shared delivery engine for the AuditLoggingPipeline plugins: bounded channel, r… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

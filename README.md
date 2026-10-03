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

## Latest list — 2026-10-03 00:18 UTC

New packages created between 2026-10-02 23:21 UTC and 2026-10-03 00:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-03T00-18-54-369485Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-02 23:21:58 | [ManagedCode.SkillOpt](https://www.nuget.org/packages/ManagedCode.SkillOpt) | 0.1.0 | ManagedCode | In-process text-space skill optimization using Microsoft.Extensions.AI. |
| 2026-10-02 23:28:39 | [ManagedCode.Presidio.Evaluation](https://www.nuget.org/packages/ManagedCode.Presidio.Evaluation) | 0.0.2 | ManagedCode | Presidio evidence sanitization and Microsoft.Extensions.AI response privacy eva… |
| 2026-10-02 23:29:07 | [Periphery.Ble.InTheHand](https://www.nuget.org/packages/Periphery.Ble.InTheHand) | 5.0.0 | Charles Lee | ADR-0085: joins a Periphery DeviceInfo for a Bluetooth LE device to 32feet's In… |
| 2026-10-02 23:33:28 | [Majorsilence.Forms.Essentials](https://www.nuget.org/packages/Majorsilence.Forms.Essentials) | 26.6.0 | Majorsilence | Platform capabilities that carry per-platform dependencies the Majorsilence.For… |
| 2026-10-03 00:10:05 | [NodeAec.Licensing.Lite](https://www.nuget.org/packages/NodeAec.Licensing.Lite) | 0.1.0 | Node.aec | Offline Ed25519 verification with no network for Node.aec Revit plugins (fail-c… |
| 2026-10-03 00:12:40 | [NodeAec.Templates.RevitPlugin](https://www.nuget.org/packages/NodeAec.Templates.RevitPlugin) | 0.1.0 | Node.aec | Autodesk Revit add-in template with Node.aec offline license verification built… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

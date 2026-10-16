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

## Latest list — 2026-10-16 17:19 UTC

New packages created between 2026-10-16 16:21 UTC and 2026-10-16 17:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-16T17-19-10-379995Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-16 16:33:51 | [Kaladel.Kiota.ImportExtensionFix.TypeScript](https://www.nuget.org/packages/Kaladel.Kiota.ImportExtensionFix.TypeScript) | 1.0.0 | Kaladel | Post-processes Kiota-generated TypeScript clients to strip the unnecessary ".js… |
| 2026-10-16 16:56:27 | [Paradise.Assets.Packing](https://www.nuget.org/packages/Paradise.Assets.Packing) | 0.61.0 | ParadiseEngine | Seekable, independently compressed Zstandard asset packs exposed as a read-only… |
| 2026-10-16 16:58:07 | [D365KnowledgeBase.ERParser](https://www.nuget.org/packages/D365KnowledgeBase.ERParser) | 1.0.0 | D365KnowledgeBase.ERParser | Parser for Dynamics 365 Finance and Operations Electronic Reporting configurati… |
| 2026-10-16 17:01:32 | [Luces.DI](https://www.nuget.org/packages/Luces.DI) | 1.0.0 | Anonymous | DI Tools |
| 2026-10-16 17:02:06 | [Qyl.Telemetry.Testing](https://www.nuget.org/packages/Qyl.Telemetry.Testing) | 1.0.0 | ANcpLua | Trace-isolated OTLP evidence for native MSTest tests. |
| 2026-10-16 17:04:02 | [SI.Rosetta.Aggregates.KurrentDB](https://www.nuget.org/packages/SI.Rosetta.Aggregates.KurrentDB) | 1.29.0 | SI.Rosetta.Aggregates.Kurrent… | Package Description |
| 2026-10-16 17:04:16 | [SI.Rosetta.Aggregates.MongoDB](https://www.nuget.org/packages/SI.Rosetta.Aggregates.MongoDB) | 1.29.0 | SI.Rosetta.Aggregates.MongoDB | Package Description |
| 2026-10-16 17:04:50 | [SI.Rosetta.Persistence.KurrentDB](https://www.nuget.org/packages/SI.Rosetta.Persistence.KurrentDB) | 1.29.0 | SI.Rosetta.Persistence.Kurren… | Package Description |
| 2026-10-16 17:05:30 | [SI.Rosetta.Projections.KurrentDB](https://www.nuget.org/packages/SI.Rosetta.Projections.KurrentDB) | 1.29.0 | SI.Rosetta.Projections.Kurren… | Package Description |
| 2026-10-16 17:06:09 | [SI.Rosetta.TestKit.Upcasting](https://www.nuget.org/packages/SI.Rosetta.TestKit.Upcasting) | 1.29.0 | SI.Informational.Systems | Test Kit for SI.Rosetta event upcasters |
| 2026-10-16 17:09:04 | [RippleFx.Engine.Native](https://www.nuget.org/packages/RippleFx.Engine.Native) | 1.5.0 | ConnectingTheDots | The Ripple Effect engine for RippleFx.Engine, with its Python interpreter: Wind… |
| 2026-10-16 17:09:06 | [RippleFx.Engine.Native.NoPython](https://www.nuget.org/packages/RippleFx.Engine.Native.NoPython) | 1.5.0 | ConnectingTheDots | The Ripple Effect engine for RippleFx.Engine, without Python — smaller, and pla… |
| 2026-10-16 17:09:06 | [RippleFx.Engine](https://www.nuget.org/packages/RippleFx.Engine) | 1.5.0 | ConnectingTheDots | C# bindings of the Ripple Effect engine: open a compiled campaign, play it thro… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

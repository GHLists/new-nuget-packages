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

## Latest list — 2026-11-13 00:20 UTC

New packages created between 2026-11-12 23:21 UTC and 2026-11-13 00:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-13T00-20-36-470532Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-12 23:36:23 | [Zymergi.Data](https://www.nuget.org/packages/Zymergi.Data) | 11.3.0-alpha | Oliver Yu | ADO.NET helpers for Zymergi: connection and command extensions, DbUnitOfWork, S… |
| 2026-11-12 23:39:04 | [Ai.Tlbx.Sip](https://www.nuget.org/packages/Ai.Tlbx.Sip) | 1.0.0 | TLBX | Managed SIP user agents, call control and bidirectional PCM media for Windows a… |
| 2026-11-12 23:39:05 | [Ai.Tlbx.VoiceAssistant.Sip](https://www.nuget.org/packages/Ai.Tlbx.VoiceAssistant.Sip) | 11.9.0 | TLBX | Per-call SIP PCM audio adapter for Ai.Tlbx.VoiceAssistant. |
| 2026-11-12 23:44:20 | [BinarySerializer.SourceGeneration](https://www.nuget.org/packages/BinarySerializer.SourceGeneration) | 10.2.1 | Jeff Haynes | Roslyn source generator that emits static registration metadata for BinarySeria… |
| 2026-11-12 23:59:39 | [Sondor.Cqrs](https://www.nuget.org/packages/Sondor.Cqrs) | 0.1.0 | Sondor Dev | Commands, queries and notifications dispatched in process, with an opt-in pipel… |
| 2026-11-13 00:01:29 | [IOScene](https://www.nuget.org/packages/IOScene) | 0.1.0 | mahach666 | Neutral scene model for tessellated BIM and CAD data: elements, shared geometry… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

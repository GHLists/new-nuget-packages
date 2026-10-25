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

## Latest list — 2026-10-25 05:18 UTC

New packages created between 2026-10-25 04:20 UTC and 2026-10-25 05:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-25T05-18-56-409439Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-25 04:27:29 | [HyperCodecs](https://www.nuget.org/packages/HyperCodecs) | 1.0.0 | Glenn Watson | Sound and video containers and codecs written in managed C#: no native library… |
| 2026-10-25 04:27:30 | [HyperCodecs.Platform](https://www.nuget.org/packages/HyperCodecs.Platform) | 1.0.0 | Glenn Watson | Operating system sound output and hardware video decoding for HyperCodecs: WASA… |
| 2026-10-25 04:27:32 | [HyperCodecs.Platform.Linux](https://www.nuget.org/packages/HyperCodecs.Platform.Linux) | 1.0.0 | Glenn Watson | PulseAudio (and PipeWire) sound output and VA-API hardware video decoding for H… |
| 2026-10-25 04:33:46 | [SeatsChart.Client](https://www.nuget.org/packages/SeatsChart.Client) | 0.1.1 | SeatsChart | Official SeatsChart .NET SDK for the SeatsChart seating API: seat maps, holds,… |
| 2026-10-25 04:50:38 | [Octeka.Messaging](https://www.nuget.org/packages/Octeka.Messaging) | 1.2.0 | Patrick Robichaud | In-memory registry and message routing infrastructure for the Octeka Messaging… |
| 2026-10-25 04:50:38 | [Octeka.Messaging.Abstractions](https://www.nuget.org/packages/Octeka.Messaging.Abstractions) | 1.2.0 | Patrick Robichaud | Core messaging abstractions and interfaces for the Octeka Messaging framework. |
| 2026-10-25 04:50:39 | [Octeka.Messaging.Ipc](https://www.nuget.org/packages/Octeka.Messaging.Ipc) | 1.2.0 | Patrick Robichaud | High-throughput inter-process communication (IPC) client and server messaging v… |
| 2026-10-25 04:50:39 | [Octeka.Messaging.Local](https://www.nuget.org/packages/Octeka.Messaging.Local) | 1.2.0 | Patrick Robichaud | High-performance in-memory local messenger for the Octeka Messaging framework. |
| 2026-10-25 04:50:40 | [Octeka.Messaging.Serialization.Json](https://www.nuget.org/packages/Octeka.Messaging.Serialization.Json) | 1.2.0 | Patrick Robichaud | UTF-8 JSON message serializer for the Octeka Messaging framework. |
| 2026-10-25 04:50:41 | [Octeka.Messaging.Tcp](https://www.nuget.org/packages/Octeka.Messaging.Tcp) | 1.2.0 | Patrick Robichaud | Reliable socket-based TCP client and server messaging with binary envelope fram… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

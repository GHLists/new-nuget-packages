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

## Latest list — 2026-10-11 06:21 UTC

New packages created between 2026-10-11 05:19 UTC and 2026-10-11 06:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-11T06-21-07-493663Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-11 05:21:02 | [Rulebearing.Rules](https://www.nuget.org/packages/Rulebearing.Rules) | 0.1.3 | Ben Bahrenburg | Rulebearing's framework presets as a versioned library: extends: rulebearing-ru… |
| 2026-10-11 05:22:12 | [CodeBrix.VideoEncoding.Av1.BsdLicenseForever](https://www.nuget.org/packages/CodeBrix.VideoEncoding.Av1.BsdLicenseForever) | 1.0.284.321 | Jeremy Ellis | AV1 video encoding for CodeBrix.VideoProcessing. Av1Encoder turns planar I420,… |
| 2026-10-11 05:27:01 | [NAPS2.Jpeg.Binaries](https://www.nuget.org/packages/NAPS2.Jpeg.Binaries) | 1.0.0 | Ben Olden-Cooligan | jpegli JPEG encoder binaries for NAPS2.Sdk |
| 2026-10-11 05:33:25 | [MJCZone.Realtime.Contract](https://www.nuget.org/packages/MJCZone.Realtime.Contract) | 0.1.0 | MJCZone, Inc. | Channel grammar, envelope and tenant guard for the realtime backbone. |
| 2026-10-11 05:33:25 | [MJCZone.Realtime.Tokens](https://www.nuget.org/packages/MJCZone.Realtime.Tokens) | 0.1.0 | MJCZone, Inc. | Mint Centrifugo connection and subscription JWTs (ES256), serve their JWKS, and… |
| 2026-10-11 05:33:26 | [MJCZone.Realtime.Publisher](https://www.nuget.org/packages/MJCZone.Realtime.Publisher) | 0.1.0 | MJCZone, Inc. | Publish envelopes to the realtime backbone over Centrifugo's gRPC API, with per… |
| 2026-10-11 05:33:27 | [MJCZone.Realtime.AgUi](https://www.nuget.org/packages/MJCZone.Realtime.AgUi) | 0.1.0 | MJCZone, Inc. | Publish an AG-UI agent run (from any AG-UI event source) to the realtime backbo… |
| 2026-10-11 05:33:27 | [MJCZone.Realtime.AgUi.AgentFramework](https://www.nuget.org/packages/MJCZone.Realtime.AgUi.AgentFramework) | 0.1.0 | MJCZone, Inc. | Microsoft Agent Framework as an AG-UI event source for MJCZone.Realtime.AgUi. |
| 2026-10-11 06:00:46 | [SpawnDev.AI](https://www.nuget.org/packages/SpawnDev.AI) | 1.1.0 | LostBeard | Core contracts for the SpawnDev AI stack: chat sessions, Ollama/OpenAI-compatib… |
| 2026-10-11 06:00:47 | [SpawnDev.AI.Server](https://www.nuget.org/packages/SpawnDev.AI.Server) | 1.1.0 | LostBeard | Ollama/OpenAI-compatible model server on the SpawnDev.ILGPU.ML inference engine… |
| 2026-10-11 06:05:09 | [PulseSharp.Abstractions](https://www.nuget.org/packages/PulseSharp.Abstractions) | 0.0.1-alpha | Waqas Ahmad | Contracts for PulseSharp, lightweight events and jobs for .NET. Reference this… |
| 2026-10-11 06:05:10 | [PulseSharp](https://www.nuget.org/packages/PulseSharp) | 0.0.1-alpha | Waqas Ahmad | PulseSharp: lightweight events and jobs for .NET, from the device to the cloud.… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

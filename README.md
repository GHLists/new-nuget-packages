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

## Latest list — 2026-10-16 03:21 UTC

New packages created between 2026-10-16 02:19 UTC and 2026-10-16 03:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-16T03-21-12-427862Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-16 02:30:56 | [Kable.Engine.Disruptor](https://www.nuget.org/packages/Kable.Engine.Disruptor) | 1.8.2 | Johnny | Ultra-low-latency Lock-Free SPSC RingBuffer and CPU Affinity execution engine f… |
| 2026-10-16 02:30:57 | [Kable.Generators](https://www.nuget.org/packages/Kable.Generators) | 1.8.2 | Johnny | Roslyn Source Generator for Kable declarative commands and RPC contracts. |
| 2026-10-16 02:30:58 | [Kable.Grpc](https://www.nuget.org/packages/Kable.Grpc) | 1.8.2 | Johnny | High-performance gRPC bidirectional streaming transport adapter for Kable over… |
| 2026-10-16 02:30:59 | [Kable.Melsec](https://www.nuget.org/packages/Kable.Melsec) | 1.8.2 | Kable Authors | High-performance zero-allocation Mitsubishi SLMP / MC Protocol 3E binary frame… |
| 2026-10-16 02:31:00 | [Kable.Modbus](https://www.nuget.org/packages/Kable.Modbus) | 1.8.2 | Kable Authors | High-performance zero-allocation Modbus-TCP and Modbus-RTU protocol codecs and… |
| 2026-10-16 02:31:01 | [Kable.Mqtt](https://www.nuget.org/packages/Kable.Mqtt) | 1.8.2 | Kable Authors | High-performance MQTT telemetry publisher and connection context over MQTTnet f… |
| 2026-10-16 02:31:02 | [Kable.Observability.OpenTelemetry](https://www.nuget.org/packages/Kable.Observability.OpenTelemetry) | 1.8.2 | Johnny | OpenTelemetry and System.Diagnostics.Metrics bridge adapter for Kable reactive… |
| 2026-10-16 02:31:04 | [Kable.OpcUa](https://www.nuget.org/packages/Kable.OpcUa) | 1.8.2 | Kable Authors | High-performance OPC UA client bridge and node subscription adapter over OPCFou… |
| 2026-10-16 02:31:05 | [Kable.SharedMemory](https://www.nuget.org/packages/Kable.SharedMemory) | 1.8.2 | Kable Authors | Ultra-low-latency Inter-Process Communication (IPC) and high-frequency waveform… |
| 2026-10-16 02:31:06 | [Kable.Transport.Ipc](https://www.nuget.org/packages/Kable.Transport.Ipc) | 1.8.2 | Johnny | High-performance Out-of-Process IPC transport (Named Pipes and Shared Memory) f… |
| 2026-10-16 02:31:07 | [Kable.UI.Wpf](https://www.nuget.org/packages/Kable.UI.Wpf) | 1.8.2 | Johnny | Ready-made WPF UserControls for real-time hardware communication monitoring, Wi… |
| 2026-10-16 02:32:43 | [AscUI](https://www.nuget.org/packages/AscUI) | 1.0.0 | AscUI | A Turbo Vision style console windowing framework for .NET. Reproduces the look… |
| 2026-10-16 02:33:40 | [Soenneker.OneSignal.HttpClients](https://www.nuget.org/packages/Soenneker.OneSignal.HttpClients) | 4.0.1 | Jake Soenneker | A thread-safe singleton HttpClient for OneSignal's OpenAPI integration. |
| 2026-10-16 02:33:41 | [Soenneker.OneSignal.OpenApiClient](https://www.nuget.org/packages/Soenneker.OneSignal.OpenApiClient) | 4.0.1 | Jake Soenneker | A generated OpenAPI client for OneSignal. |
| 2026-10-16 02:43:38 | [OSK.Petra.Godot.Math.Formulas](https://www.nuget.org/packages/OSK.Petra.Godot.Math.Formulas) | 0.1.0 | BlankDev117 | Provides |
| 2026-10-16 02:45:13 | [Soenneker.OneSignal.OpenApiClientUtil](https://www.nuget.org/packages/Soenneker.OneSignal.OpenApiClientUtil) | 4.0.2 | Jake Soenneker | A thread-safe utility for obtaining OneSignal's OpenApiClient singleton. |
| 2026-10-16 02:51:34 | [Authway.Client](https://www.nuget.org/packages/Authway.Client) | 0.1.0 | iyulab | Client for Authway's administration API — register applications, invite users,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

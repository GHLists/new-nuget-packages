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

## Latest list — 2026-10-02 18:19 UTC

New packages created between 2026-10-02 17:22 UTC and 2026-10-02 18:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-02T18-19-40-223413Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-02 17:23:26 | [ProtoTest.Analyzers](https://www.nuget.org/packages/ProtoTest.Analyzers) | 1.1.0 | Matthias Seys | Roslyn analyzers for ProtoTest suites: the intent-dependent mistakes the framew… |
| 2026-10-02 17:23:27 | [ProtoTest.Cli](https://www.nuget.org/packages/ProtoTest.Cli) | 1.1.0 | Matthias Seys | Command-line access to ProtoTest evidence: the failure digest, the feedback cha… |
| 2026-10-02 17:23:31 | [ProtoTest.Mcp](https://www.nuget.org/packages/ProtoTest.Mcp) | 1.1.0 | Matthias Seys | Read-only MCP server over .prototrace evidence: an agent lists runs, reads a fa… |
| 2026-10-02 17:23:33 | [ProtoTest.Traces](https://www.nuget.org/packages/ProtoTest.Traces) | 1.1.0 | Matthias Seys | Reader for .prototrace archives: the run, its tests and each test's operations… |
| 2026-10-02 17:23:34 | [ProtoTest.Aspire](https://www.nuget.org/packages/ProtoTest.Aspire) | 1.1.0 | Matthias Seys | Run an Aspire AppHost with a ProtoTest suite: the run starts it, its resources… |
| 2026-10-02 17:23:38 | [ProtoTest.Devices](https://www.nuget.org/packages/ProtoTest.Devices) | 1.1.0 | Matthias Seys | Talk to devices - simulators or hardware - from the same test context, lifecycl… |
| 2026-10-02 17:23:40 | [ProtoTest.Diagnosis](https://www.nuget.org/packages/ProtoTest.Diagnosis) | 1.1.0 | Matthias Seys | Deterministic diagnosis of a .prototrace run: the causal failure summary, its c… |
| 2026-10-02 17:23:41 | [ProtoTest.Hosting](https://www.nuget.org/packages/ProtoTest.Hosting) | 1.1.0 | Matthias Seys | Run background workers and generic hosts in-process with a ProtoTest suite. |
| 2026-10-02 17:23:56 | [ProtoTest.Web.Pages](https://www.nuget.org/packages/ProtoTest.Web.Pages) | 1.1.0 | Matthias Seys | Shared page identity and inventory for ProtoTest web integrations. |
| 2026-10-02 17:24:01 | [ProtoTest.Devices.Mqtt](https://www.nuget.org/packages/ProtoTest.Devices.Mqtt) | 1.1.0 | Matthias Seys | MQTT transport for ProtoTest.Devices: talk to devices over publish/subscribe ag… |
| 2026-10-02 17:24:03 | [ProtoTest.Devices.Mqtt.Testcontainers](https://www.nuget.org/packages/ProtoTest.Devices.Mqtt.Testcontainers) | 1.1.0 | Matthias Seys | A Mosquitto MQTT broker container owned as a run-scoped resource for ProtoTest.… |
| 2026-10-02 17:24:04 | [ProtoTest.Devices.Serial](https://www.nuget.org/packages/ProtoTest.Devices.Serial) | 1.1.0 | Matthias Seys | Serial transport for ProtoTest.Devices: talk to devices on a COM port or /dev/t… |
| 2026-10-02 17:24:08 | [ProtoTest.Devices.Tcp](https://www.nuget.org/packages/ProtoTest.Devices.Tcp) | 1.1.0 | Matthias Seys | TCP transport for ProtoTest.Devices: talk to devices over a raw socket, connect… |
| 2026-10-02 17:24:10 | [ProtoTest.Devices.WebSocket](https://www.nuget.org/packages/ProtoTest.Devices.WebSocket) | 1.1.0 | Matthias Seys | WebSocket transport for ProtoTest.Devices: talk to devices over ws:// or wss://. |
| 2026-10-02 17:24:20 | [ProtoTest.Verification](https://www.nuget.org/packages/ProtoTest.Verification) | 1.1.0 | Matthias Seys | Cross-run verification over ProtoTest reports and traces: coverage deltas, spec… |
| 2026-10-02 17:24:25 | [ProtoTest.Feedback](https://www.nuget.org/packages/ProtoTest.Feedback) | 1.1.0 | Matthias Seys | Posts a ProtoTest run's failure digest where a pull request reads it: a comment… |
| 2026-10-02 17:24:37 | [ProtoTest.Devices.WebSocket.AspNetCore](https://www.nuget.org/packages/ProtoTest.Devices.WebSocket.AspNetCore) | 1.1.0 | Matthias Seys | In-process WebSocket device connections for ProtoTest: reach an application's e… |
| 2026-10-02 17:24:39 | [ProtoTest.Messaging.MassTransit](https://www.nuget.org/packages/ProtoTest.Messaging.MassTransit) | 1.1.0 | Matthias Seys | MassTransit bridge for the ProtoTest messaging capability: publish and await me… |
| 2026-10-02 17:24:42 | [ProtoTest.WireMock](https://www.nuget.org/packages/ProtoTest.WireMock) | 1.1.0 | Matthias Seys | Fake HTTP services for ProtoTest suites, backed by WireMock.Net: per-test stubs… |
| 2026-10-02 17:44:15 | [MASS4.Attributes](https://www.nuget.org/packages/MASS4.Attributes) | 5.6.0 | Bruno Massa | Shared metadata for forms, editor tools, stable type identity and service disco… |
| 2026-10-02 17:44:17 | [TheSingularityWorkshop.FSM_Serialization](https://www.nuget.org/packages/TheSingularityWorkshop.FSM_Serialization) | 1.0.0 | Trent Best | Binary serialization infrastructure for FSM ecosystem state, MicroBundle compos… |
| 2026-10-02 17:50:46 | [TheSingularityWorkshop.MicroBundleDomain](https://www.nuget.org/packages/TheSingularityWorkshop.MicroBundleDomain) | 1.0.0 | Trent Best | Domain-side foundation for defining and composing loadable MicroBundle semantic… |
| 2026-10-02 17:53:08 | [TemporalCommunity.Templates](https://www.nuget.org/packages/TemporalCommunity.Templates) | 0.5.0 | TemporalCommunity.Templates | dotnet new templates for Temporal .NET: item templates for a workflow, an activ… |
| 2026-10-02 18:02:37 | [MsdfAtlasGen](https://www.nuget.org/packages/MsdfAtlasGen) | 1.1.0 | MsdfAtlasGen.Native contribut… | In-process MSDF/MTSDF font-atlas generation for .NET. msdf-atlas-gen and msdfge… |
| 2026-10-02 18:08:38 | [Waher.Networking.E2ee](https://www.nuget.org/packages/Waher.Networking.E2ee) | 1.0.0 | Peter Waher | Library that defines a protocol for End-to-End encrypted binary communication o… |
| 2026-10-02 18:10:25 | [Waher.Security.E2ee](https://www.nuget.org/packages/Waher.Security.E2ee) | 1.0.0 | Peter Waher | Class library containing a basic abstraction for End-to-End Encryption (E2EE) u… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-12 17:21 UTC

New packages created between 2026-10-12 16:21 UTC and 2026-10-12 17:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-12T17-21-11-376653Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-12 16:37:00 | [ClassSaver2](https://www.nuget.org/packages/ClassSaver2) | 0.1.2 | nglamdev | Fast compile-time binary serialization source generator for C#. |
| 2026-10-12 16:47:37 | [LuxMediator](https://www.nuget.org/packages/LuxMediator) | 1.0.0 | Anonymous | (●'◡'●) |
| 2026-10-12 16:53:57 | [Aspose.PSD.FOSS](https://www.nuget.org/packages/Aspose.PSD.FOSS) | 26.10.0 | Aspose | Aspose.PSD FOSS for .NET provides open-source solution for PSD and PSB file rea… |
| 2026-10-12 17:02:04 | [Ais.Net.Broadcaster](https://www.nuget.org/packages/Ais.Net.Broadcaster) | 1.0.0 | Endjin Limited | Broadcasts NMEA AIS sentences to TCP and WebSocket clients: replay a recording… |
| 2026-10-12 17:02:06 | [Ais.Net.Broadcaster.Cli](https://www.nuget.org/packages/Ais.Net.Broadcaster.Cli) | 1.0.0 | Endjin Limited | Command-line NMEA AIS broadcaster: replays a recording or relays a live feed to… |
| 2026-10-12 17:02:08 | [Ais.Net.Receiver.Benchmarks](https://www.nuget.org/packages/Ais.Net.Receiver.Benchmarks) | 1.0.0 | Ais.Net.Receiver.Benchmarks | Package Description |
| 2026-10-12 17:03:56 | [ClassSaver2Test](https://www.nuget.org/packages/ClassSaver2Test) | 1.0.0 | ClassSaver2Test | Package Description |
| 2026-10-12 17:05:26 | [VintranExternalV2.Grpc.Contracts](https://www.nuget.org/packages/VintranExternalV2.Grpc.Contracts) | 1.6.0 | Vintran Ltd | gRPC service contracts, generated stubs for VantPay, VtPass, and the shared ext… |
| 2026-10-12 17:08:22 | [VenEl.ModularMCP.ServiceNow](https://www.nuget.org/packages/VenEl.ModularMCP.ServiceNow) | 1.0.0 | VenEl | VenEl Modular MCP Plugin - VenEl.ModularMCP.ServiceNow |
| 2026-10-12 17:09:53 | [Egov.Integrations.MPay.Soap](https://www.nuget.org/packages/Egov.Integrations.MPay.Soap) | 10.0.1 | E-Governance Agency (EGA) | A reusable library that helps service providers integrate with MPay using the S… |
| 2026-10-12 17:12:24 | [Parsley.Runtime](https://www.nuget.org/packages/Parsley.Runtime) | 1.0.0 | honey the codewitch | The runtime for the Parsley parser synthesizer |
| 2026-10-12 17:12:59 | [Parsley.Generator](https://www.nuget.org/packages/Parsley.Generator) | 1.0.0 | honey the codewitch | Synthesizes a Parsley parser, lexer and evaluator into a partial class marked [… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

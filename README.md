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

## Latest list — 2026-10-02 01:20 UTC

New packages created between 2026-10-02 00:20 UTC and 2026-10-02 01:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-02T01-20-24-961472Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-02 00:38:50 | [Tamp.Conformance.Anthropic](https://www.nuget.org/packages/Tamp.Conformance.Anthropic) | 0.1.1 | Scott Singleton | Anthropic (Claude) bring-your-own-key adapter for Tamp.Conformance. A thin ICha… |
| 2026-10-02 00:38:51 | [Tamp.Conformance.Bedrock](https://www.nuget.org/packages/Tamp.Conformance.Bedrock) | 0.1.1 | Scott Singleton | AWS Bedrock bring-your-own-key adapter for Tamp.Conformance. A thin IChatComple… |
| 2026-10-02 00:38:52 | [Tamp.Conformance.OpenAiCompatible](https://www.nuget.org/packages/Tamp.Conformance.OpenAiCompatible) | 0.1.1 | Scott Singleton | OpenAI-compatible bring-your-own-key adapter for Tamp.Conformance. One thin ICh… |
| 2026-10-02 01:01:19 | [NavierStokesEquations](https://www.nuget.org/packages/NavierStokesEquations) | 1.0.0 | LUCHER4321 | N-dimensional incompressible fluid simulator based on the Navier-Stokes equatio… |
| 2026-10-02 01:10:27 | [Centra.Providers.Flotilla.Udp](https://www.nuget.org/packages/Centra.Providers.Flotilla.Udp) | 0.2.1 | Chad Bauers | High-throughput, microsecond-latency UDP datagram consensus pub/sub provider fo… |
| 2026-10-02 01:10:39 | [Centra.Providers.Flotilla.Tcp](https://www.nuget.org/packages/Centra.Providers.Flotilla.Tcp) | 0.2.1 | Chad Bauers | Connection-oriented TCP streaming consensus pub/sub provider for Centra backed… |
| 2026-10-02 01:10:40 | [Centra.Providers.Flotilla](https://www.nuget.org/packages/Centra.Providers.Flotilla) | 0.2.1 | Chad Bauers | High-throughput, microsecond-latency Raft consensus pub/sub provider for Centra… |
| 2026-10-02 01:10:41 | [Centra.Providers.Flotilla.Grpc](https://www.nuget.org/packages/Centra.Providers.Flotilla.Grpc) | 0.2.1 | Chad Bauers | HTTP/2 gRPC consensus pub/sub provider for Centra backed by Flotilla. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

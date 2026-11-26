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

## Latest list — 2026-11-26 04:19 UTC

New packages created between 2026-11-26 03:19 UTC and 2026-11-26 04:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-26T04-19-10-847707Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-26 03:27:44 | [Du.Abp.ZeroCore.EntityFrameworkCore](https://www.nuget.org/packages/Du.Abp.ZeroCore.EntityFrameworkCore) | 10.5.1 | Abp.ZeroCore.EntityFrameworkC… | Abp.ZeroCore.EntityFrameworkCore |
| 2026-11-26 03:47:58 | [SpaceCG.Standard.Wpf](https://www.nuget.org/packages/SpaceCG.Standard.Wpf) | 1.0.0 | SpaceCG.Standard.Wpf | Package Description |
| 2026-11-26 03:49:50 | [NCode.Coordination.Hosting](https://www.nuget.org/packages/NCode.Coordination.Hosting) | 0.8.0 | NCode Group | The hosting of NCode.Coordination: the host's session, opened once the composit… |
| 2026-11-26 03:51:48 | [Tuna](https://www.nuget.org/packages/Tuna) | 0.1.0 | delicioustuna | Numerical computing library for .NET 10 providing vectors, matrices, tensors, l… |
| 2026-11-26 03:52:09 | [Tuna.Differentiation](https://www.nuget.org/packages/Tuna.Differentiation) | 0.1.0 | delicioustuna | Tape-based reverse-mode automatic differentiation for scalars, vectors, matrice… |
| 2026-11-26 03:52:22 | [Tuna.Integration](https://www.nuget.org/packages/Tuna.Integration) | 0.1.0 | delicioustuna | One-dimensional, multidimensional adaptive, and quasi-Monte Carlo numerical int… |
| 2026-11-26 03:52:35 | [Tuna.NeuralNetwork](https://www.nuget.org/packages/Tuna.NeuralNetwork) | 0.1.0 | delicioustuna | Neural network building blocks (2D convolution, Mamba state-space blocks, norma… |
| 2026-11-26 03:52:48 | [Tuna.Optimization](https://www.nuget.org/packages/Tuna.Optimization) | 0.1.0 | delicioustuna | Numerical optimization algorithms (L-BFGS, SGD/Adam, proximal methods, global i… |
| 2026-11-26 03:53:02 | [Tuna.Probabilistic](https://www.nuget.org/packages/Tuna.Probabilistic) | 0.1.0 | delicioustuna | Probabilistic inference (HMC, NUTS, slice sampling, ensemble and parallel tempe… |
| 2026-11-26 03:53:15 | [Tuna.SignalProcessing](https://www.nuget.org/packages/Tuna.SignalProcessing) | 0.1.0 | delicioustuna | FFT, DCT, convolution, correlation, and discrete/continuous wavelet transforms… |
| 2026-11-26 03:53:26 | [Tuna.Statistics](https://www.nuget.org/packages/Tuna.Statistics) | 0.1.0 | delicioustuna | Statistical distributions (continuous, discrete, multivariate, and composite) w… |
| 2026-11-26 04:11:49 | [RDCore.SDK.Protocols](https://www.nuget.org/packages/RDCore.SDK.Protocols) | 0.2.0-alpha | 9562-7303 Québec inc. | The messages a client exchanges with the RDCore platform, with no dependency on… |
| 2026-11-26 04:11:50 | [CrowCast](https://www.nuget.org/packages/CrowCast) | 1.0.0 | Elysium Coding | Application-neutral gossip membership, messaging, deduplication, coordination,… |
| 2026-11-26 04:11:53 | [CrowCast.Akka](https://www.nuget.org/packages/CrowCast.Akka) | 1.0.0 | Elysium Coding | Akka.NET Cluster and Distributed PubSub backend for CrowCast. |
| 2026-11-26 04:11:55 | [CrowCast.ControlPlane](https://www.nuget.org/packages/CrowCast.ControlPlane) | 1.0.0 | Elysium Coding | gRPC ingestion, aggregation, and live query services for CrowCast observations. |
| 2026-11-26 04:11:57 | [CrowCast.ControlPlane.Client](https://www.nuget.org/packages/CrowCast.ControlPlane.Client) | 1.0.0 | Elysium Coding | Non-blocking gRPC observation reporter for CrowCast replicas. |
| 2026-11-26 04:11:59 | [CrowCast.ControlPlane.Protocol](https://www.nuget.org/packages/CrowCast.ControlPlane.Protocol) | 1.0.0 | Elysium Coding | Versioned gRPC contracts for reporting CrowCast observations to a control plane. |
| 2026-11-26 04:12:02 | [CrowCast.ControlPlane.WebUI](https://www.nuget.org/packages/CrowCast.ControlPlane.WebUI) | 1.0.0 | Elysium Coding | ZoOrce fleet dashboard for multiple CrowCast clusters and observer perspectives. |
| 2026-11-26 04:12:04 | [CrowCast.Observability](https://www.nuget.org/packages/CrowCast.Observability) | 1.0.0 | Elysium Coding | Bounded, application-neutral observation snapshots and events for CrowCast clus… |
| 2026-11-26 04:12:10 | [CrowCast.WebUI](https://www.nuget.org/packages/CrowCast.WebUI) | 1.0.0 | Elysium Coding | Optional ZoOrce dashboard for the local perspective of a CrowCast replica. |
| 2026-11-26 04:12:12 | [CrowCast.WebUI.Shell](https://www.nuget.org/packages/CrowCast.WebUI.Shell) | 1.0.0 | Elysium Coding | Shared ZoOrce shell and AG Grid/ECharts adapters for CrowCast web modules. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

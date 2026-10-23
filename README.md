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

## Latest list — 2026-10-23 22:21 UTC

New packages created between 2026-10-23 21:20 UTC and 2026-10-23 22:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-23T22-21-16-763827Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-23 21:26:39 | [RunSignal.OpenTelemetry](https://www.nuget.org/packages/RunSignal.OpenTelemetry) | 0.1.0 | Gokhan Ertogan | Adds RunSignal's workload metrics and spans to the OpenTelemetry .NET SDK with… |
| 2026-10-23 21:26:40 | [RunSignal.Hangfire](https://www.nuget.org/packages/RunSignal.Hangfire) | 0.1.0 | Gokhan Ertogan | Records every Hangfire job run as a RunSignal workload run (success, failure, c… |
| 2026-10-23 21:26:41 | [RunSignal.Core](https://www.nuget.org/packages/RunSignal.Core) | 0.1.0 | Gokhan Ertogan | Zero-dependency core of RunSignal. Records runs, items and heartbeats of backgr… |
| 2026-10-23 21:26:42 | [RunSignal.Alerting](https://www.nuget.org/packages/RunSignal.Alerting) | 0.1.0 | Gokhan Ertogan | Reads RunSignal workload manifests and computes when each alert should fire (mi… |
| 2026-10-23 21:26:43 | [RunSignal.Prometheus](https://www.nuget.org/packages/RunSignal.Prometheus) | 0.1.0 | Gokhan Ertogan | Turns RunSignal workload manifests into Prometheus alerting rules (missed, fail… |
| 2026-10-23 21:26:44 | [RunSignal.Quartz](https://www.nuget.org/packages/RunSignal.Quartz) | 0.1.0 | Gokhan Ertogan | Records every Quartz.NET job execution as a RunSignal workload run (success, fa… |
| 2026-10-23 21:26:44 | [RunSignal.Quartz4](https://www.nuget.org/packages/RunSignal.Quartz4) | 0.1.0 | Gokhan Ertogan | Records every Quartz.NET 4 job execution as a RunSignal workload run (success,… |
| 2026-10-23 21:26:45 | [RunSignal.DotNet](https://www.nuget.org/packages/RunSignal.DotNet) | 0.1.0 | Gokhan Ertogan | Registers RunSignal workloads with Microsoft.Extensions.DependencyInjection: Ad… |
| 2026-10-23 21:26:46 | [RunSignal.Cli](https://www.nuget.org/packages/RunSignal.Cli) | 0.1.0 | Gokhan Ertogan | The runsignal command: plan, diff and provision New Relic alerts, or export Pro… |
| 2026-10-23 21:26:47 | [RunSignal.NewRelic](https://www.nuget.org/packages/RunSignal.NewRelic) | 0.1.0 | Gokhan Ertogan | Turns a RunSignal workload manifest into New Relic NRQL alert conditions (misse… |
| 2026-10-23 21:35:33 | [Goo.NativeDialogs](https://www.nuget.org/packages/Goo.NativeDialogs) | 0.11.0 | Xaz | Owned native message boxes for Goo windows. |
| 2026-10-23 21:37:01 | [Idrak.CoreML](https://www.nuget.org/packages/Idrak.CoreML) | 0.4.0 | Ahmed Seada | Reserved for Apple's Neural Engine through Core ML: an exported model converted… |
| 2026-10-23 21:37:02 | [Idrak.Data](https://www.nuget.org/packages/Idrak.Data) | 0.4.0 | Ahmed Seada | Datasets for Idrak (no dependencies beyond Idrak): read JSON Lines, JSON, CSV,… |
| 2026-10-23 21:37:03 | [Idrak.Diffusion](https://www.nuget.org/packages/Idrak.Diffusion) | 0.4.0 | Ahmed Seada | Reserved for image and audio generation by denoising: UNet and DiT denoisers, n… |
| 2026-10-23 21:37:05 | [Idrak.Diffusion.Plugins](https://www.nuget.org/packages/Idrak.Diffusion.Plugins) | 0.4.0 | Ahmed Seada | Reserved for the diffusion model families as plug-ins on Idrak.Diffusion, one n… |
| 2026-10-23 21:37:06 | [Idrak.Extensions](https://www.nuget.org/packages/Idrak.Extensions) | 0.4.0 | Ahmed Seada | Reserved for extensions and helpers over the library's contracts that apps shar… |
| 2026-10-23 21:37:07 | [Idrak.Gpu](https://www.nuget.org/packages/Idrak.Gpu) | 0.4.0 | Ahmed Seada | The GPU devices of Idrak: CUDA (talks to the NVIDIA driver directly, PTX genera… |
| 2026-10-23 21:37:08 | [Idrak.HarfBuzz](https://www.nuget.org/packages/Idrak.HarfBuzz) | 0.4.0 | Ahmed Seada | Reserved for HarfBuzz as a second text shaper beside the library's own, registe… |
| 2026-10-23 21:37:10 | [Idrak.Imaging](https://www.nuget.org/packages/Idrak.Imaging) | 0.4.0 | Ahmed Seada | Images for Idrak (no dependencies beyond Idrak): PNG, JPEG, BMP and Netpbm deco… |
| 2026-10-23 21:37:12 | [Idrak.Network](https://www.nuget.org/packages/Idrak.Network) | 0.4.0 | Ahmed Seada | The real transports and the collective algorithms of an Idrak cluster (plan 23)… |
| 2026-10-23 21:37:14 | [Idrak.Reinforcement](https://www.nuget.org/packages/Idrak.Reinforcement) | 0.4.0 | Ahmed Seada | Reinforcement learning for Idrak (no dependencies beyond Idrak): the general al… |
| 2026-10-23 21:37:15 | [Idrak.Reinforcement.Plugins](https://www.nuget.org/packages/Idrak.Reinforcement.Plugins) | 0.4.0 | Ahmed Seada | The reinforcement-learning environment families for Idrak, as plug-ins on the l… |
| 2026-10-23 21:37:16 | [Idrak.Text](https://www.nuget.org/packages/Idrak.Text) | 0.4.0 | Ahmed Seada | Natural language processing for Idrak (no dependencies beyond Idrak and Idrak.D… |
| 2026-10-23 21:37:17 | [Idrak.Text.Plugins](https://www.nuget.org/packages/Idrak.Text.Plugins) | 0.4.0 | Ahmed Seada | The text model families for Idrak, as plug-ins on the library's public API (one… |
| 2026-10-23 21:37:18 | [Idrak.Video](https://www.nuget.org/packages/Idrak.Video) | 0.4.0 | Ahmed Seada | Reserved for video in and out: decoding and encoding frames, frame sampling and… |
| 2026-10-23 21:37:19 | [Idrak.Video.Plugins](https://www.nuget.org/packages/Idrak.Video.Plugins) | 0.4.0 | Ahmed Seada | Reserved for the video model families as plug-ins on Idrak.Video, one namespace… |
| 2026-10-23 21:37:21 | [Idrak.Vision](https://www.nuget.org/packages/Idrak.Vision) | 0.4.0 | Ahmed Seada | Computer vision for Idrak (no dependencies beyond Idrak and Idrak.Imaging): ima… |
| 2026-10-23 21:37:22 | [Idrak.Vision.Plugins](https://www.nuget.org/packages/Idrak.Vision.Plugins) | 0.4.0 | Ahmed Seada | The vision model families for Idrak, as plug-ins on the library's public API (o… |
| 2026-10-23 21:37:25 | [Idrak.Abstraction.Testing](https://www.nuget.org/packages/Idrak.Abstraction.Testing) | 0.4.0 | Ahmed Seada | The conformance and stress kit for Idrak's contracts: checks a device, a token… |
| 2026-10-23 21:37:27 | [Idrak.Audio.Plugins](https://www.nuget.org/packages/Idrak.Audio.Plugins) | 0.4.0 | Ahmed Seada | The speech and voice model families for Idrak, as plug-ins on the library's pub… |
| 2026-10-23 21:37:28 | [Idrak.Cluster](https://www.nuget.org/packages/Idrak.Cluster) | 0.4.0 | Ahmed Seada | A cluster of GPUs and machines simulated on one machine (plan 23): devices carv… |
| 2026-10-23 21:37:29 | [Idrak.Data.Plugins](https://www.nuget.org/packages/Idrak.Data.Plugins) | 0.4.0 | Ahmed Seada | Reserved for document formats as plug-ins on Idrak.Data, starting with Office (… |
| 2026-10-23 21:37:31 | [Idrak.Abstraction](https://www.nuget.org/packages/Idrak.Abstraction) | 0.4.0 | Ahmed Seada | The contracts Idrak is built on, each with its default implementation: devices… |
| 2026-10-23 21:37:32 | [Idrak.Audio](https://www.nuget.org/packages/Idrak.Audio) | 0.4.0 | Ahmed Seada | Sound for Idrak (no dependencies beyond Idrak): WAV, FLAC and MP3 decoding and… |
| 2026-10-23 21:38:21 | [DataStandardizer.File.iCal](https://www.nuget.org/packages/DataStandardizer.File.iCal) | 1.0.0 | matthew25187 | Data Standardizer provides implementations of various internationally recognise… |
| 2026-10-23 21:39:03 | [AetherDb.Sdk.SemanticKernel](https://www.nuget.org/packages/AetherDb.Sdk.SemanticKernel) | 0.7.0 | Aether Contributors | Semantic Kernel agent-memory provider backed by the Aether .NET SDK. Gives a Se… |
| 2026-10-23 21:44:06 | [Zippendo](https://www.nuget.org/packages/Zippendo) | 1.3.14 | Zippendo | Official C# and .NET SDK for the Zippendo shipping API: book shipments, print l… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

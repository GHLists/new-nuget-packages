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

## Latest list — 2026-10-28 03:23 UTC

New packages created between 2026-10-28 02:18 UTC and 2026-10-28 03:23 UTC.

[Full CSV](data/new-nuget-packages-2026-10-28T03-23-15-667643Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-28 02:19:58 | [JYPPX.DeploySharp.Backend.LlamaSharp](https://www.nuget.org/packages/JYPPX.DeploySharp.Backend.LlamaSharp) | 2.0.0 | Guojin Yan | LLamaSharp adapter for DeploySharp local GGUF text generation and embeddings. |
| 2026-10-28 02:19:58 | [JYPPX.DeploySharp.Backend.OnnxRuntime](https://www.nuget.org/packages/JYPPX.DeploySharp.Backend.OnnxRuntime) | 2.0.0 | Guojin Yan | Managed ONNX Runtime adapter for named-tensor DeploySharp inference without bun… |
| 2026-10-28 02:19:59 | [JYPPX.DeploySharp.Backend.OpenCV](https://www.nuget.org/packages/JYPPX.DeploySharp.Backend.OpenCV) | 2.0.0 | Guojin Yan | OpenCV DNN CPU adapter for explicit named vision tensor contracts with runtime… |
| 2026-10-28 02:20:01 | [JYPPX.DeploySharp.Backend.OpenVINO](https://www.nuget.org/packages/JYPPX.DeploySharp.Backend.OpenVINO) | 2.0.0 | Guojin Yan | Managed OpenVINO adapter for named-tensor DeploySharp inference without bundlin… |
| 2026-10-28 02:20:02 | [JYPPX.DeploySharp.Backend.TensorRT](https://www.nuget.org/packages/JYPPX.DeploySharp.Backend.TensorRT) | 2.0.0 | Guojin Yan | Managed TensorRT inference, ONNX-to-engine, CUDA/RTC execution, and caller-conf… |
| 2026-10-28 02:20:03 | [JYPPX.DeploySharp.Core](https://www.nuget.org/packages/JYPPX.DeploySharp.Core) | 2.0.0 | Guojin Yan | Dependency-free contracts, tensors, model metadata, canonical results, diagnost… |
| 2026-10-28 02:20:04 | [JYPPX.DeploySharp.Extensibility](https://www.nuget.org/packages/JYPPX.DeploySharp.Extensibility) | 2.0.0 | Guojin Yan | Manifest-driven backend plugin, runtime dependency, native probe, options schem… |
| 2026-10-28 02:20:04 | [JYPPX.DeploySharp.LLM](https://www.nuget.org/packages/JYPPX.DeploySharp.LLM) | 2.0.0 | Guojin Yan | Backend-neutral language-model workflows, generation contracts, chat prompts, a… |
| 2026-10-28 02:20:05 | [JYPPX.DeploySharp.ModelFactory](https://www.nuget.org/packages/JYPPX.DeploySharp.ModelFactory) | 2.0.0 | Guojin Yan | Validated model catalogs, versioned Release and pinned official upstream downlo… |
| 2026-10-28 02:20:06 | [JYPPX.DeploySharp.ModelPack.Json](https://www.nuget.org/packages/JYPPX.DeploySharp.ModelPack.Json) | 2.0.0 | Guojin Yan | Strict JSON manifests, integrity verification, and safe local package loading f… |
| 2026-10-28 02:20:07 | [JYPPX.DeploySharp.Multimodal](https://www.nuget.org/packages/JYPPX.DeploySharp.Multimodal) | 2.0.0 | Guojin Yan | Backend-neutral multimodal orchestration, ordered media identity, streaming, ca… |
| 2026-10-28 02:20:09 | [JYPPX.DeploySharp.Visual](https://www.nuget.org/packages/JYPPX.DeploySharp.Visual) | 2.0.0 | Guojin Yan | Image-library-neutral prepared-tensor pipelines, profiles, classification, dete… |
| 2026-10-28 02:20:10 | [JYPPX.DeploySharp.Visual.OpenCV](https://www.nuget.org/packages/JYPPX.DeploySharp.Visual.OpenCV) | 2.0.0 | Guojin Yan | OpenCV image loading and high-throughput preprocessing for DeploySharp Visual c… |
| 2026-10-28 02:20:11 | [JYPPX.DeploySharp.Visual.TensorRT](https://www.nuget.org/packages/JYPPX.DeploySharp.Visual.TensorRT) | 2.0.0 | Guojin Yan | CUDA preprocessing and TensorRT visual inference for classification, detection,… |
| 2026-10-28 02:48:52 | [cAlgoKit](https://www.nuget.org/packages/cAlgoKit) | 0.0.1 | z1long | A helper library for cTrader cBots. |
| 2026-10-28 03:00:31 | [Meziantou.Framework.Hashing](https://www.nuget.org/packages/Meziantou.Framework.Hashing) | 1.0.0 | meziantou | Fully managed hash algorithms: password hashing and key derivation (BCrypt, Arg… |
| 2026-10-28 03:10:43 | [AsyncServerCore](https://www.nuget.org/packages/AsyncServerCore) | 1.0.1 | fwt | 高性能异步 TCP 服务器框架:SAEA 网络层、模块路由、中间件管道、鉴权/加密、时间轮调度 |
| 2026-10-28 03:11:55 | [AsyncServerData](https://www.nuget.org/packages/AsyncServerData) | 1.0.1 | fwt | AsyncServerCore 的数据访问扩展:Redis 缓存与 MySQL/Oracle/SqlServer 关系库(Dapper) |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

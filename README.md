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

## Latest list — 2026-11-14 17:19 UTC

New packages created between 2026-11-14 16:21 UTC and 2026-11-14 17:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-14T17-19-05-464325Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-14 16:32:33 | [Sharplight.HuggingFace](https://www.nuget.org/packages/Sharplight.HuggingFace) | 0.1.2-alpha | Sharplight contributors | Hugging Face checkpoint importer (safetensors + config.json + tokenizer files)… |
| 2026-11-14 16:32:34 | [Sharplight.AspNetCore](https://www.nuget.org/packages/Sharplight.AspNetCore) | 0.1.2-alpha | Sharplight contributors | ASP.NET Core minimal-API endpoints exposing a Sharplight model through OpenAI-… |
| 2026-11-14 16:32:35 | [Sharplight.Templating](https://www.nuget.org/packages/Sharplight.Templating) | 0.1.2-alpha | Sharplight contributors | Jinja2-compatible template engine for chat templates. |
| 2026-11-14 16:32:35 | [Sharplight.Tokenizers](https://www.nuget.org/packages/Sharplight.Tokenizers) | 0.1.2-alpha | Sharplight contributors | Tokenizers for Sharplight: BPE, SentencePiece, WordPiece and Unigram, compatibl… |
| 2026-11-14 16:32:36 | [Sharplight.Vulkan](https://www.nuget.org/packages/Sharplight.Vulkan) | 0.1.2-alpha | Sharplight contributors | Vulkan execution provider for Sharplight. |
| 2026-11-14 16:32:37 | [Sharplight.Gguf](https://www.nuget.org/packages/Sharplight.Gguf) | 0.1.2-alpha | Sharplight contributors | GGUF importer for Sharplight: reads llama.cpp model files (all ggml quantizatio… |
| 2026-11-14 16:32:38 | [Sharplight.Package.Import](https://www.nuget.org/packages/Sharplight.Package.Import) | 0.1.2-alpha | Sharplight contributors | Builds Sharplight model packages (.slm) from any registered source format and p… |
| 2026-11-14 16:32:38 | [Sharplight.Onnx](https://www.nuget.org/packages/Sharplight.Onnx) | 0.1.2-alpha | Sharplight contributors | ONNX importer for Sharplight: a hand-rolled protobuf decoder plus an ONNX-to-IR… |
| 2026-11-14 16:32:39 | [Sharplight.Llm](https://www.nuget.org/packages/Sharplight.Llm) | 0.1.2-alpha | Sharplight contributors | LLM inference: model loading, sessions, generation loop, sampling, chat formatt… |
| 2026-11-14 16:32:40 | [Sharplight.Shaders](https://www.nuget.org/packages/Sharplight.Shaders) | 0.1.2-alpha | Sharplight contributors | Backend-neutral Slang kernel library and compiler (SPIR-V, CUDA/PTX, Metal targ… |
| 2026-11-14 16:32:41 | [Sharplight.Package](https://www.nuget.org/packages/Sharplight.Package) | 0.1.2-alpha | Sharplight contributors | Reads and writes Sharplight model packages (.slm): weights, tokenizer, metadata… |
| 2026-11-14 16:32:41 | [Sharplight.Cpu](https://www.nuget.org/packages/Sharplight.Cpu) | 0.1.2-alpha | Sharplight contributors | Multithreaded SIMD CPU execution provider for Sharplight (dequantize-on-the-fly… |
| 2026-11-14 16:32:42 | [Sharplight.Hub](https://www.nuget.org/packages/Sharplight.Hub) | 0.1.2-alpha | Sharplight contributors | Hugging Face Hub client and local model store: search, resumable verified downl… |
| 2026-11-14 16:32:43 | [Sharplight.Architectures](https://www.nuget.org/packages/Sharplight.Architectures) | 0.1.2-alpha | Sharplight contributors | Model architecture adapters: canonical model sources → Sharplight compute graph… |
| 2026-11-14 16:32:43 | [Sharplight.Core](https://www.nuget.org/packages/Sharplight.Core) | 0.1.2-alpha | Sharplight contributors | Format-agnostic tensor graph IR, model definition and execution-provider abstra… |
| 2026-11-14 16:32:44 | [Sharplight.Extensions.AI](https://www.nuget.org/packages/Sharplight.Extensions.AI) | 0.1.2-alpha | Sharplight contributors | Microsoft.Extensions.AI adapters (IChatClient) over Sharplight.Llm. |
| 2026-11-14 16:35:04 | [Heron.Plugin.BTM](https://www.nuget.org/packages/Heron.Plugin.BTM) | 0.3.0 | ornithologist-love | Prebuilt Better Task Manager plugin for Heron hosts: processes, performance, se… |
| 2026-11-14 16:37:11 | [BccCode.Privacy.Client](https://www.nuget.org/packages/BccCode.Privacy.Client) | 0.0.5 | BCC | BCC Privacy client built on BCC Platform |
| 2026-11-14 16:41:56 | [Bronskiy.Sequences](https://www.nuget.org/packages/Bronskiy.Sequences) | 1.0.0 | Bronskiy.Sequences | Provides a generator, that generates lazily evaluated sequences from functions. |
| 2026-11-14 16:41:57 | [Carbon.ConsulSecretEncryptor.Core](https://www.nuget.org/packages/Carbon.ConsulSecretEncryptor.Core) | 1.0.0 | Carbon.ConsulSecretEncryptor.… | 1.0.0 - Shared certificate resolution and RSA-OAEP/SHA256 + hybrid AES-256-GCM… |
| 2026-11-14 16:46:47 | [Vorticity.ObjectStorage](https://www.nuget.org/packages/Vorticity.ObjectStorage) | 0.13.0 | Evariops | Object stores for Vorticity's files and datasets on Amazon S3, Cloudflare R2, O… |
| 2026-11-14 16:58:30 | [Sinter.AspNetCore](https://www.nuget.org/packages/Sinter.AspNetCore) | 0.18.0 | tiaforge | Fills a sinter build's embedded-data placeholders per request: the page's API d… |
| 2026-11-14 17:05:01 | [RagnaCore.AutomationApi.Sdk](https://www.nuget.org/packages/RagnaCore.AutomationApi.Sdk) | 2.6.0 | Fenix | Plugin SDK for RagnaCore |
| 2026-11-14 17:08:13 | [FlowGovernanceManager](https://www.nuget.org/packages/FlowGovernanceManager) | 1.0.0 | Nagendra kumar Kosaraju | Identify and remediate unhealthy Power Automate flows at scale. Health scoring,… |
| 2026-11-14 17:09:00 | [RedMaple.Orchestrator.Containers.Wslc](https://www.nuget.org/packages/RedMaple.Orchestrator.Containers.Wslc) | 1.2.4 | Jerker Olofsson | Don't use this library directly, use RedMaple.Orchestrator.DockerCompose. This… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

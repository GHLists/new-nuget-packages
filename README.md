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

## Latest list — 2026-09-29 18:20 UTC

New packages created between 2026-09-29 17:19 UTC and 2026-09-29 18:20 UTC.

[Full CSV](data/new-nuget-packages-2026-09-29T18-20-08-51405Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-29 17:21:16 | [FauxData](https://www.nuget.org/packages/FauxData) | 1.0.1 | Dieter Van Broeck | Fake data generator with rule-based configuration. |
| 2026-09-29 17:25:48 | [D20Tek.BlazorComponents.Menus](https://www.nuget.org/packages/D20Tek.BlazorComponents.Menus) | 1.11.19 | DarthPedro | A Blazor component for providing a self-positioning FlyoutMenu (popover) trigge… |
| 2026-09-29 17:30:16 | [Bladehero.Telegram.Platform.Testing](https://www.nuget.org/packages/Bladehero.Telegram.Platform.Testing) | 10.1.0 | bladehero | Component tests for Telegram bots built on Bladehero.Telegram.Platform: runs th… |
| 2026-09-29 17:31:08 | [RedSkia.Licensing.Wpf](https://www.nuget.org/packages/RedSkia.Licensing.Wpf) | 1.1.0 | RedSkia | Activation window and start-up gate for WPF apps licensed through redskia.dev.… |
| 2026-09-29 17:31:09 | [RedSkia.Licensing](https://www.nuget.org/packages/RedSkia.Licensing) | 1.1.0 | RedSkia | Licence activation and offline ES256 token verification for software sold on re… |
| 2026-09-29 17:40:37 | [Idrak](https://www.nuget.org/packages/Idrak) | 0.1.0 | Ahmed Seada | Self-contained neural network library for .NET: tensors, autograd, layers and o… |
| 2026-09-29 17:40:38 | [Idrak.AspNetCore](https://www.nuget.org/packages/Idrak.AspNetCore) | 0.1.0 | Ahmed Seada | ASP.NET Core integration for Idrak: registers an InferenceEngine in dependency… |
| 2026-09-29 17:40:39 | [Idrak.Datasets](https://www.nuget.org/packages/Idrak.Datasets) | 0.1.0 | Ahmed Seada | Datasets for Idrak (no dependencies): read JSON Lines, JSON, CSV, text and Parq… |
| 2026-09-29 17:40:40 | [Idrak.Datasets.Cli](https://www.nuget.org/packages/Idrak.Datasets.Cli) | 0.1.0 | Ahmed Seada | idrak-data: inspect, count, download and assemble training datasets from Huggin… |
| 2026-09-29 17:40:42 | [Idrak.FineTuning.Cli](https://www.nuget.org/packages/Idrak.FineTuning.Cli) | 0.1.0 | Ahmed Seada | idrak-tune: fine-tune pretrained language models (LoRA / QLoRA) on any dataset… |
| 2026-09-29 17:40:44 | [Idrak.LanguageModels](https://www.nuget.org/packages/Idrak.LanguageModels) | 0.1.0 | Ahmed Seada | Language models for Idrak (no dependencies): load Llama, Qwen, Mistral and Gemm… |
| 2026-09-29 17:40:45 | [Idrak.Mcp](https://www.nuget.org/packages/Idrak.Mcp) | 0.1.0 | Ahmed Seada | Model Context Protocol for Idrak: use the tools of MCP servers in conversations… |
| 2026-09-29 17:40:46 | [Idrak.Onnx](https://www.nuget.org/packages/Idrak.Onnx) | 0.1.0 | Ahmed Seada | ONNX export for Idrak models (no dependencies): networks become .onnx files tha… |
| 2026-09-29 17:40:47 | [Idrak.Onnx.Runtime](https://www.nuget.org/packages/Idrak.Onnx.Runtime) | 0.1.0 | Ahmed Seada | Runs ONNX models (exported by Idrak.Onnx or any other tool) with ONNX Runtime a… |
| 2026-09-29 17:44:32 | [Polhem.Core](https://www.nuget.org/packages/Polhem.Core) | 1.1.0 | Polhem contributors | Base infrastructure for the Polhem framework, including collections, serializat… |
| 2026-09-29 18:06:22 | [tallyman](https://www.nuget.org/packages/tallyman) | 1.0.2 | Jaeymo | Tallyman counts lines in every file under a directory. |
| 2026-09-29 18:09:24 | [OmronEip](https://www.nuget.org/packages/OmronEip) | 0.2.4 | ImThatGuy | .NET client for Omron NX/NJ Sysmac controllers over EtherNet/IP (symbolic tag a… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

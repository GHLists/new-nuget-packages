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

## Latest list — 2026-10-30 20:19 UTC

New packages created between 2026-10-30 19:21 UTC and 2026-10-30 20:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-30T20-19-38-572595Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-30 19:31:45 | [Azure.Functions.Cli.Workloads.Workers.Python](https://www.nuget.org/packages/Azure.Functions.Cli.Workloads.Workers.Python) | 4.46.2-preview | Microsoft | Azure Functions CLI content workload that ships the Python language worker. |
| 2026-10-30 19:33:25 | [Monq.Core.GrpcClientExtensions](https://www.nuget.org/packages/Monq.Core.GrpcClientExtensions) | 0.1.0-rev-411161078… | MONQ Digital lab | Shared gRPC client registration on top of Monq.Core.MicroserviceAddressing: nam… |
| 2026-10-30 19:33:49 | [ZapSMTP](https://www.nuget.org/packages/ZapSMTP) | 0.1.0 | ZapSMTP | The official .NET library for the ZapSMTP email API: send, receive and track em… |
| 2026-10-30 19:33:50 | [ZapSMTP.Extensions.DependencyInjection](https://www.nuget.org/packages/ZapSMTP.Extensions.DependencyInjection) | 0.1.0 | ZapSMTP | Registers the ZapSMTP client with Microsoft.Extensions.DependencyInjection and… |
| 2026-10-30 19:39:21 | [Nelshh.GstSharpBundle](https://www.nuget.org/packages/Nelshh.GstSharpBundle) | 1.28.8.1 | GstSharpBundle | GStreamer C# bindings for .NET 8+ with the official GStreamer 1.28 runtime bund… |
| 2026-10-30 19:39:32 | [Nelshh.GstSharpBundle.Windows.X64](https://www.nuget.org/packages/Nelshh.GstSharpBundle.Windows.X64) | 1.28.8.1 | GstSharpBundle.Windows.X64 | GStreamer C# bindings for .NET 8+ with the official GStreamer 1.28 runtime bund… |
| 2026-10-30 19:40:42 | [FAI.Router](https://www.nuget.org/packages/FAI.Router) | 0.1.0 | MASFractal | Picks the right LLM, agent or tool for each request and checks what it delivere… |
| 2026-10-30 19:45:24 | [BuildAgent.Tool](https://www.nuget.org/packages/BuildAgent.Tool) | 2.0.0 | The-Running-Dev | Runs build-agent builds in the versioned image from the host and updates a runn… |
| 2026-10-30 19:56:42 | [BorrowedTorch.UI.Markup](https://www.nuget.org/packages/BorrowedTorch.UI.Markup) | 1.0.0 | Vladyslav Pysarenko | Builds BorrowedTorch.UI element trees from XML markup: elements by type name, t… |
| 2026-10-30 20:00:33 | [NanoByte.StructureEditor.NewtonsoftJson](https://www.nuget.org/packages/NanoByte.StructureEditor.NewtonsoftJson) | 3.0.0 | Bastian Eicher | Newtonsoft.Json serialization support for split-screen editors for data structu… |
| 2026-10-30 20:04:02 | [NetReporter.Fonts.Liberation](https://www.nuget.org/packages/NetReporter.Fonts.Liberation) | 1.3.0 | Marvin Chinchilla | Liberation Sans, Serif and Mono fonts (SIL OFL 1.1) embedded for NetReporter, m… |
| 2026-10-30 20:04:45 | [Soenneker.Blazor.Extensions.IJSRuntimes](https://www.nuget.org/packages/Soenneker.Blazor.Extensions.IJSRuntimes) | 11.0.1 | Jake Soenneker | Extension methods for IJSRuntime that add operation context to JavaScript invoc… |
| 2026-10-30 20:12:48 | [Morgana.AI.LanguageModels.Anthropic](https://www.nuget.org/packages/Morgana.AI.LanguageModels.Anthropic) | 1.0.0-beta1 | Marco De Salvo | Anthropic provider for Morgana: serves a tier on Claude models. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

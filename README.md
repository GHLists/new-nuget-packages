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

## Latest list — 2026-10-09 20:21 UTC

New packages created between 2026-10-09 19:19 UTC and 2026-10-09 20:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-09T20-21-45-328776Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-09 19:35:31 | [UiGuideAgent.Cli](https://www.nuget.org/packages/UiGuideAgent.Cli) | 0.6.0 | DomitorAI | UiGuide Agent developer tool: init, scan, bundle, doctor. |
| 2026-10-09 19:35:35 | [UiGuideAgent.Protocol](https://www.nuget.org/packages/UiGuideAgent.Protocol) | 0.6.0 | DomitorAI | UiGuide Agent protocol contracts (v1), shared by the server and the client SDKs. |
| 2026-10-09 19:35:36 | [UiGuideAgent.Companion](https://www.nuget.org/packages/UiGuideAgent.Companion) | 0.6.0 | DomitorAI | UiGuide Agent Companion: the help assistant next to any Windows application (Py… |
| 2026-10-09 19:35:36 | [UiGuideAgent.Web](https://www.nuget.org/packages/UiGuideAgent.Web) | 0.6.0 | DomitorAI | UiGuide Agent for .NET web UIs: Blazor, Razor Pages / MVC, .NET MAUI Blazor Hyb… |
| 2026-10-09 19:35:37 | [UiGuideAgent.Desktop](https://www.nuget.org/packages/UiGuideAgent.Desktop) | 0.6.0 | DomitorAI | UiGuide Agent SDK for .NET desktop applications (WPF and WinForms, .NET 8+ and… |
| 2026-10-09 19:35:38 | [UiGuideAgent.Server.Host](https://www.nuget.org/packages/UiGuideAgent.Server.Host) | 0.6.0 | DomitorAI | UiGuide Agent server, ready to run: dotnet tool install -g UiGuideAgent.Server.… |
| 2026-10-09 19:35:38 | [UiGuideAgent.Server](https://www.nuget.org/packages/UiGuideAgent.Server) | 0.6.0 | DomitorAI | UiGuide Agent server library: add the AI help agent to any ASP.NET Core applica… |
| 2026-10-09 19:36:31 | [Droidline](https://www.nuget.org/packages/Droidline) | 0.1.3 | Droidline contributors | Android automation from C# and .NET: test your apps on real phones, script the… |
| 2026-10-09 19:39:05 | [Rldc.Common](https://www.nuget.org/packages/Rldc.Common) | 0.2.0 | Rldc contributors | Shared request, response, and typed-answer contracts for the Rldc decision libr… |
| 2026-10-09 19:39:06 | [Rldc.Core](https://www.nuget.org/packages/Rldc.Core) | 0.2.0 | Rldc contributors | Decision routing and provider abstractions for applications built on Rldc. |
| 2026-10-09 19:39:08 | [Rldc.Inference](https://www.nuget.org/packages/Rldc.Inference) | 0.2.0 | Rldc contributors | Prepared ONNX and Laya GGUF inference, bundle validation, and model packing for… |
| 2026-10-09 19:39:09 | [Rldc](https://www.nuget.org/packages/Rldc) | 0.2.0 | Rldc contributors | Typed model decisions for .NET apps, with dependency-injection registration and… |
| 2026-10-09 19:39:12 | [Rldc.Maf](https://www.nuget.org/packages/Rldc.Maf) | 0.2.0 | Rldc contributors | Expose Rldc conversational inference through Microsoft.Extensions.AI and Micros… |
| 2026-10-09 19:39:13 | [Rldc.Inference.WinML](https://www.nuget.org/packages/Rldc.Inference.WinML) | 0.2.0 | Rldc contributors | Optional Windows ML execution-provider integration for Rldc ONNX inference. |
| 2026-10-09 20:01:32 | [Meziantou.Prebuilt](https://www.nuget.org/packages/Meziantou.Prebuilt) | 2.3.0 | meziantou | Lists the prebuilt tools (ffmpeg, ffprobe, zopfli, oxipng, pngout, cwebp, ...)… |
| 2026-10-09 20:03:36 | [ThinkGeo.Gpu.Native](https://www.nuget.org/packages/ThinkGeo.Gpu.Native) | 1.0.0-beta001 | ThinkGeo | Native libraries for ThinkGeo.Gpu on Windows: ANGLE, which runs the engine's Op… |
| 2026-10-09 20:09:03 | [LiteScript.Net](https://www.nuget.org/packages/LiteScript.Net) | 0.1.0 | LePtitDev | .NET wrapper of LiteScript, a little script engine to embed in applications (ob… |
| 2026-10-09 20:11:33 | [2dog.nunit](https://www.nuget.org/packages/2dog.nunit) | 4.7.2.110 | Moritz Voss | NUnit fixtures, bounded frame waits, signal expectations and deferred-deletion… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

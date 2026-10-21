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

## Latest list — 2026-10-21 07:22 UTC

New packages created between 2026-10-21 06:21 UTC and 2026-10-21 07:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-21T07-22-38-969082Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-21 06:27:35 | [MyLibery](https://www.nuget.org/packages/MyLibery) | 1.1.2.12 | jack.chang | Some useful function. |
| 2026-10-21 06:38:52 | [Blazor.AI.Core](https://www.nuget.org/packages/Blazor.AI.Core) | 1.0.0 | Gravicode Studios | Blazor.AI core runtime: multi-provider IChatClient factory (OpenAI, Azure OpenA… |
| 2026-10-21 06:38:53 | [Blazor.AI.RAG](https://www.nuget.org/packages/Blazor.AI.RAG) | 1.0.0 | Gravicode Studios | Blazor.AI retrieval-augmented generation: document ingestion (PDF, text, markdo… |
| 2026-10-21 06:38:53 | [Blazor.AI.Decision](https://www.nuget.org/packages/Blazor.AI.Decision) | 1.0.0 | Gravicode Studios | Blazor.AI decision intelligence: rules engine, DMN-style decision tables, decis… |
| 2026-10-21 06:38:54 | [Blazor.AI.Visualization](https://www.nuget.org/packages/Blazor.AI.Visualization) | 1.0.0 | Gravicode Studios | Blazor.AI visual analytics: AI dashboards, realtime, prediction and forecast ch… |
| 2026-10-21 06:38:54 | [Blazor.AI.Bio](https://www.nuget.org/packages/Blazor.AI.Bio) | 1.0.0 | Gravicode Studios | Blazor.AI biology analysis components powered by Biotech.Net: DNA sequence anal… |
| 2026-10-21 06:38:55 | [Blazor.AI.Analytics](https://www.nuget.org/packages/Blazor.AI.Analytics) | 1.0.0 | Gravicode Studios | Blazor.AI machine learning, data science and reinforcement learning workbenches… |
| 2026-10-21 06:38:55 | [Blazor.AI.Abstractions](https://www.nuget.org/packages/Blazor.AI.Abstractions) | 1.0.0 | Gravicode Studios | Blazor.AI contracts: provider options, vector index, smart-component contracts,… |
| 2026-10-21 06:38:56 | [Blazor.AI.Components](https://www.nuget.org/packages/Blazor.AI.Components) | 1.0.0 | Gravicode Studios | Blazor.AI Razor components: Smart Components (SmartPaste, SmartTextArea, SmartC… |
| 2026-10-21 06:38:56 | [Blazor.AI.Agents](https://www.nuget.org/packages/Blazor.AI.Agents) | 1.0.0 | Gravicode Studios | Blazor.AI agents: agent studio, tool calling, task board, memory viewer, debugg… |
| 2026-10-21 06:38:57 | [Blazor.AI.Templates](https://www.nuget.org/packages/Blazor.AI.Templates) | 1.0.0 | Gravicode Studios | dotnet new templates for Blazor.AI: a Blazor Web App wired with AI providers, c… |
| 2026-10-21 06:38:57 | [Blazor.AI.LocalModels](https://www.nuget.org/packages/Blazor.AI.LocalModels) | 1.0.0 | Gravicode Studios | Blazor.AI Hugging Face and local models: model hub browser, downloader, inferen… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

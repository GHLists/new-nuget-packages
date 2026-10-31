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

## Latest list — 2026-10-31 23:18 UTC

New packages created between 2026-10-31 22:18 UTC and 2026-10-31 23:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-31T23-18-57-611055Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-31 22:20:12 | [AgentDelegation](https://www.nuget.org/packages/AgentDelegation) | 0.1.1 | kamal1910 | Signed, attenuating delegation chains for AI agents: intersection authority, pr… |
| 2026-10-31 22:20:13 | [AgentDelegation.SemanticKernel](https://www.nuget.org/packages/AgentDelegation.SemanticKernel) | 0.1.1 | kamal1910 | Semantic Kernel function filter that marks every tool and sub-agent result as u… |
| 2026-10-31 22:20:14 | [AgentDelegation.AspNetCore](https://www.nuget.org/packages/AgentDelegation.AspNetCore) | 0.1.1 | kamal1910 | ASP.NET Core gateway middleware for AgentDelegation. Place it in front of tool… |
| 2026-10-31 22:28:28 | [RazorEngine.NetFramework.Roslyn](https://www.nuget.org/packages/RazorEngine.NetFramework.Roslyn) | 5.0.0 | Matthew Abbott,Ben Dornis,Mat… | RazorEngine - Roslyn compiler service: compiles templates in-process with Rosly… |
| 2026-10-31 22:33:14 | [Evolutionary](https://www.nuget.org/packages/Evolutionary) | 0.2.0 | Peter Wehrfritz | A small toolbox library for evolutionary algorithms. It provides the immutable… |
| 2026-10-31 22:43:28 | [HebrewOcrNet](https://www.nuget.org/packages/HebrewOcrNet) | 1.0.1 | StasEdward,BobLd,RapidOCR,Riv… | Hebrew OCR for .NET without Python: a C# port of the paddleocr-hebrew word pipe… |
| 2026-10-31 22:46:14 | [HotConfig](https://www.nuget.org/packages/HotConfig) | 1.0.0 | Emre Akdemir | Redis-backed Microsoft.Extensions.Configuration provider with hot reload throug… |
| 2026-10-31 22:47:16 | [BorrowedTorch.Capabilities](https://www.nuget.org/packages/BorrowedTorch.Capabilities) | 1.0.0 | Vladyslav Pysarenko | What the machine a game runs on offers, for its settings and its start: the vid… |
| 2026-10-31 22:49:15 | [Shiny.UniversalHubs.Multipeer](https://www.nuget.org/packages/Shiny.UniversalHubs.Multipeer) | 1.5.0-beta-0006 | Allan Ritchie | Shiny.UniversalHubs over Apple's MultipeerConnectivity - Apple devices host and… |
| 2026-10-31 22:49:17 | [Shiny.UniversalHubs.Nearby](https://www.nuget.org/packages/Shiny.UniversalHubs.Nearby) | 1.5.0-beta-0006 | Allan Ritchie | Shiny.UniversalHubs over Google's Nearby Connections - Android, iOS and macOS d… |
| 2026-10-31 22:49:33 | [Kgen.ExtensionManager.Abstractions](https://www.nuget.org/packages/Kgen.ExtensionManager.Abstractions) | 1.0.0 | KGen LLC | Shared extension metadata contracts. |
| 2026-10-31 22:49:34 | [Kgen.ControlCatalog.Extension.Abstractions](https://www.nuget.org/packages/Kgen.ControlCatalog.Extension.Abstractions) | 11.0.0 | KGen LLC | Avalonia extension contract for the KGen Control Catalog. |
| 2026-10-31 22:49:43 | [kgen.ControlCatalog.Extension.LiveCharts](https://www.nuget.org/packages/kgen.ControlCatalog.Extension.LiveCharts) | 0.1.0 | Frederic Forjan | LiveCharts plugin for the Avalonia ControlCatalog / KGen Flavored. |
| 2026-10-31 22:49:46 | [kgen.ControlCatalog.Extension.Mapsui](https://www.nuget.org/packages/kgen.ControlCatalog.Extension.Mapsui) | 0.1.1 | Frederic Forjan | Mapsui plugin the Avalonia ControlCatalog / KGen Flavored. |
| 2026-10-31 23:00:54 | [Hexalith.ChatBot.Client](https://www.nuget.org/packages/Hexalith.ChatBot.Client) | 1.83.0 | Hexalith Contributors | Governed chatbot module for Hexalith. |
| 2026-10-31 23:00:56 | [Hexalith.ChatBot.Contracts](https://www.nuget.org/packages/Hexalith.ChatBot.Contracts) | 1.83.0 | Hexalith Contributors | Governed chatbot module for Hexalith. |
| 2026-10-31 23:00:58 | [Hexalith.ChatBot.Testing](https://www.nuget.org/packages/Hexalith.ChatBot.Testing) | 1.83.0 | Hexalith Contributors | Governed chatbot module for Hexalith. |
| 2026-10-31 23:08:17 | [ToolUp.Facts.Presentation.Server](https://www.nuget.org/packages/ToolUp.Facts.Presentation.Server) | 0.38.0 | Andrew J. Willshire | ToolUp.Facts.Presentation Server — the render_chart and render_table AI tools:… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

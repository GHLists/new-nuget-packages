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

## Latest list — 2026-09-30 22:20 UTC

New packages created between 2026-09-30 21:19 UTC and 2026-09-30 22:20 UTC.

[Full CSV](data/new-nuget-packages-2026-09-30T22-20-21-15832Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-30 21:23:32 | [SandboxedAgents](https://www.nuget.org/packages/SandboxedAgents) | 0.2.0 | grauzone-git | Standalone sandboxed-agents for Windows. Run tools/install-command.ps1 after Nu… |
| 2026-09-30 21:32:38 | [PocketCsvReader.WebLogs](https://www.nuget.org/packages/PocketCsvReader.WebLogs) | 2.39.0 | Cédric L. Charlier | PocketCsvReader.WebLogs extends PocketCsvReader with streaming readers for Comm… |
| 2026-09-30 21:42:47 | [Itp.SimpleHL7](https://www.nuget.org/packages/Itp.SimpleHL7) | 5.0.0-preview1 | mgaffigan | Package Description |
| 2026-09-30 21:54:37 | [Novolis.Templates](https://www.nuget.org/packages/Novolis.Templates) | 2026.1.1.27 | Novolis | dotnet new template packs for Novolis solutions and projects. |
| 2026-09-30 21:55:51 | [Novolis.TemplateSmokeTest](https://www.nuget.org/packages/Novolis.TemplateSmokeTest) | 2026.1.1.22 | Novolis | Smoke test package for CI and NuGet publishing validation |
| 2026-09-30 21:56:50 | [Majo.TerminalUI](https://www.nuget.org/packages/Majo.TerminalUI) | 0.0.1 | Sweety Majo | A small terminal interaction layer for .NET console applications. |
| 2026-09-30 21:57:12 | [Novolis.ThreeD.Import.Assimp](https://www.nuget.org/packages/Novolis.ThreeD.Import.Assimp) | 2026.1.1.10 | Novolis | Assimp-based FBX, OBJ, and glTF import into Novolis.Math.Geometry meshes and Th… |
| 2026-09-30 21:57:14 | [Novolis.ThreeD.Scene](https://www.nuget.org/packages/Novolis.ThreeD.Scene) | 2026.1.1.10 | Novolis | Renderer-neutral 3D scene graph with nodes, lights, cameras, staged evaluation,… |
| 2026-09-30 21:57:31 | [Novolis.Astro.Abstractions](https://www.nuget.org/packages/Novolis.Astro.Abstractions) | 2026.1.0.22 | Novolis | Core stellar coordinates, hop/transit evaluation contracts for Novolis.Astro. |
| 2026-09-30 21:57:32 | [Novolis.Astro.Assessment](https://www.nuget.org/packages/Novolis.Astro.Assessment) | 2026.1.0.22 | Novolis | Pluggable star-system assessment scorers and deterministic SystemProfile genera… |
| 2026-09-30 21:57:33 | [Novolis.Astro.Catalog](https://www.nuget.org/packages/Novolis.Astro.Catalog) | 2026.1.0.22 | Novolis | Star system catalog store, queries, and import adapters. |
| 2026-09-30 21:57:33 | [Novolis.Cad.Blueprint](https://www.nuget.org/packages/Novolis.Cad.Blueprint) | 2026.1.0.33 | Novolis | Avalonia-free CadBlueprint companion to CadDocument — contextual walls, interio… |
| 2026-09-30 21:57:34 | [Novolis.Astro.Catalog.Data](https://www.nuget.org/packages/Novolis.Astro.Catalog.Data) | 2026.1.0.22 | Novolis | Pregenerated stellar catalog packs (Near-Sol, local HYG slice). |
| 2026-09-30 21:57:35 | [Novolis.Cad.Evaluation](https://www.nuget.org/packages/Novolis.Cad.Evaluation) | 2026.1.0.33 | Novolis | Avalonia-free staged CAD evaluation (CadDocument → meshes / phys): CadModelEval… |
| 2026-09-30 21:57:35 | [Novolis.Aspire.Hosting.Signoz](https://www.nuget.org/packages/Novolis.Aspire.Hosting.Signoz) | 2026.1.1.25 | Novolis | Aspire hosting integration for SigNoz observability (multi-container local stac… |
| 2026-09-30 21:57:35 | [Novolis.Astro.Overlay](https://www.nuget.org/packages/Novolis.Astro.Overlay) | 2026.1.0.22 | Novolis | Alias and label overlays bound to catalog system ids. |
| 2026-09-30 21:57:36 | [Novolis.Cad.Primitives](https://www.nuget.org/packages/Novolis.Cad.Primitives) | 2026.1.0.33 | Novolis | Avalonia-free CAD interchange DTOs for .cadjson / .cadphys (documents, entities… |
| 2026-09-30 21:57:36 | [Novolis.Astro.Plotting](https://www.nuget.org/packages/Novolis.Astro.Plotting) | 2026.1.0.22 | Novolis | Headless stellar path projection and SVG/TSV export. |
| 2026-09-30 21:57:37 | [Novolis.Cad.SceneBridge](https://www.nuget.org/packages/Novolis.Cad.SceneBridge) | 2026.1.0.33 | Novolis | Avalonia-free CadDocument → SceneDocument bridge: tessellate solids/walls/space… |
| 2026-09-30 21:57:37 | [Novolis.Astro.Routing](https://www.nuget.org/packages/Novolis.Astro.Routing) | 2026.1.0.22 | Novolis | Interstellar route graphs, pluggable hop cost/transit models, planner and accum… |
| 2026-09-30 21:57:38 | [Novolis.Civics.Agents](https://www.nuget.org/packages/Novolis.Civics.Agents) | 2026.1.0.17 | Novolis | Heuristic fiscal/regime agents that adjust FiscalPolicy only. |
| 2026-09-30 21:57:39 | [Novolis.Civics.Core](https://www.nuget.org/packages/Novolis.Civics.Core) | 2026.1.0.17 | Novolis | Bounded-minimum civic kernel: nation identity, fiscal intent, civic stocks, per… |
| 2026-09-30 21:57:40 | [Novolis.Civics.EconomyBridge](https://www.nuget.org/packages/Novolis.Civics.EconomyBridge) | 2026.1.0.17 | Novolis | Map Civics FiscalPolicy to Economy StatePolicy and bind NationId to State entit… |
| 2026-09-30 21:57:41 | [Novolis.Civics.Simulation](https://www.nuget.org/packages/Novolis.Civics.Simulation) | 2026.1.0.17 | Novolis | Composition root: advance civic periods over NationState. |
| 2026-09-30 21:57:42 | [Novolis.Documents](https://www.nuget.org/packages/Novolis.Documents) | 2026.1.1.28 | Novolis | Paged document model: page setup, typography, header/footer, watermark, and clo… |
| 2026-09-30 21:57:43 | [Novolis.Documents.Layout](https://www.nuget.org/packages/Novolis.Documents.Layout) | 2026.1.1.28 | Novolis | One-column pagination for PagedDocument: First/Toc/Body/Last page plans, ITextM… |
| 2026-09-30 21:57:44 | [Novolis.Documents.Skia](https://www.nuget.org/packages/Novolis.Documents.Skia) | 2026.1.1.28 | Novolis | SkiaSharp PDF writer for PagedDocument: layout measurement, tables, images, hea… |
| 2026-09-30 21:57:54 | [Novolis.Commands.Abstractions](https://www.nuget.org/packages/Novolis.Commands.Abstractions) | 2026.1.1.36 | Novolis | Contracts for Novolis command parsing, envelopes, and queueing. |
| 2026-09-30 21:57:54 | [Novolis.Chat.Abstractions](https://www.nuget.org/packages/Novolis.Chat.Abstractions) | 2026.1.2.9 | Novolis | Chat ids, frames, events, and live-state contracts. |
| 2026-09-30 21:57:55 | [Novolis.Commands.DependencyInjection](https://www.nuget.org/packages/Novolis.Commands.DependencyInjection) | 2026.1.1.36 | Novolis | Microsoft.Extensions.DependencyInjection registration for Novolis.Commands. |
| 2026-09-30 21:57:56 | [Novolis.Chat.Directory](https://www.nuget.org/packages/Novolis.Chat.Directory) | 2026.1.2.9 | Novolis | Named chat spaces and channels, rosters, devices, and SecureText group membersh… |
| 2026-09-30 21:57:57 | [Novolis.Commands.Engine](https://www.nuget.org/packages/Novolis.Commands.Engine) | 2026.1.1.36 | Novolis | Parse prompts into command envelopes without executing domain behavior. |
| 2026-09-30 21:57:57 | [Novolis.Chat.Hosting.AspNetCore](https://www.nuget.org/packages/Novolis.Chat.Hosting.AspNetCore) | 2026.1.2.9 | Novolis | ASP.NET Core SignalR orchestration for encrypted chat conversations. |
| 2026-09-30 21:57:58 | [Novolis.Commands.Expressions](https://www.nuget.org/packages/Novolis.Commands.Expressions) | 2026.1.1.36 | Novolis | Parse function-call style prompts (Name(arg, …)) into structured expression cal… |
| 2026-09-30 21:57:58 | [Novolis.Chat.Live](https://www.nuget.org/packages/Novolis.Chat.Live) | 2026.1.2.9 | Novolis | Ephemeral chat presence, typing TTL, and receipt state. |
| 2026-09-30 21:57:59 | [Novolis.Commands.Queueing](https://www.nuget.org/packages/Novolis.Commands.Queueing) | 2026.1.1.36 | Novolis | Channel-backed command queue and interrupt-aware runner. |
| 2026-09-30 21:58:00 | [Novolis.Commands.Testing](https://www.nuget.org/packages/Novolis.Commands.Testing) | 2026.1.1.36 | Novolis | Test doubles and helpers for Novolis.Commands. |
| 2026-09-30 21:58:06 | [Novolis.MSBuild.LibraryReference](https://www.nuget.org/packages/Novolis.MSBuild.LibraryReference) | 2026.1.1.12 | Novolis | MSBuild LibraryReference item that expands to ProjectReference when a local pro… |
| 2026-09-30 21:58:07 | [Novolis.Game.Humanoid](https://www.nuget.org/packages/Novolis.Game.Humanoid) | 2026.1.1.29 | Novolis | Game-facing humanoid clip banks and body masks over Novolis.Simulation.Humanoid. |
| 2026-09-30 21:58:08 | [Novolis.Game.Identity](https://www.nuget.org/packages/Novolis.Game.Identity) | 2026.1.1.29 | Novolis | In-memory pseudonymous player directory and external identity linker. |
| 2026-09-30 21:58:10 | [Novolis.Game.Identity.Abstractions](https://www.nuget.org/packages/Novolis.Game.Identity.Abstractions) | 2026.1.1.29 | Novolis | Pseudonymous player identity refs for games (no PII in platform API). |
| 2026-09-30 21:58:11 | [Novolis.Game.Identity.AspNetCore](https://www.nuget.org/packages/Novolis.Game.Identity.AspNetCore) | 2026.1.1.29 | Novolis | Map ASP.NET claims to pseudonymous PlayerRef without platform PII storage. |
| 2026-09-30 21:58:12 | [Novolis.Game.MenuFlows](https://www.nuget.org/packages/Novolis.Game.MenuFlows) | 2026.1.1.29 | Novolis | UI-agnostic game screen stack and menu navigation. |
| 2026-09-30 21:58:12 | [Novolis.CodeGen.Bindings](https://www.nuget.org/packages/Novolis.CodeGen.Bindings) | 2026.1.2.47 | Novolis | Manifest fragments, merge plans, and binding codegen orchestration. |
| 2026-09-30 21:58:13 | [Novolis.Geopolitics.Conflict](https://www.nuget.org/packages/Novolis.Geopolitics.Conflict) | 2026.1.0.26 | Novolis | Territorial conflict resolution: frontier discovery, staging bonuses, and per-d… |
| 2026-09-30 21:58:13 | [Novolis.Game.Multiplayer.Abstractions](https://www.nuget.org/packages/Novolis.Game.Multiplayer.Abstractions) | 2026.1.1.29 | Novolis | Lobby and session abstractions for multiplayer games. |
| 2026-09-30 21:58:13 | [Novolis.CodeGen.Bindings.Roslyn](https://www.nuget.org/packages/Novolis.CodeGen.Bindings.Roslyn) | 2026.1.2.47 | Novolis | Roslyn hook host, emit writer, and compilation unit comparison for binding code… |
| 2026-09-30 21:58:14 | [Novolis.Game.Multiplayer.AspNetCore](https://www.nuget.org/packages/Novolis.Game.Multiplayer.AspNetCore) | 2026.1.1.29 | Novolis | SignalR hub bases and DTOs for game lobbies. |
| 2026-09-30 21:58:14 | [Novolis.Geopolitics.Core](https://www.nuget.org/packages/Novolis.Geopolitics.Core) | 2026.1.0.26 | Novolis | Geopolitics kernel: polities, provinces, relations, treaties, wars, and civic/f… |
| 2026-09-30 21:58:14 | [Novolis.CodeGen.Pipeline](https://www.nuget.org/packages/Novolis.CodeGen.Pipeline) | 2026.1.2.47 | Novolis | Linear step pipeline kernel with fingerprinted skip/cache and result.json. |
| 2026-09-30 21:58:15 | [Novolis.Game.Packaging.Inno](https://www.nuget.org/packages/Novolis.Game.Packaging.Inno) | 2026.1.1.29 | Novolis | Inno Setup script generation helpers for Windows game installers. |
| 2026-09-30 21:58:16 | [Novolis.CodeGen.Reflection](https://www.nuget.org/packages/Novolis.CodeGen.Reflection) | 2026.1.2.47 | Novolis | Type and reflection display helpers (friendly names, display names). |
| 2026-09-30 21:58:16 | [Novolis.Geopolitics.Diplomacy](https://www.nuget.org/packages/Novolis.Geopolitics.Diplomacy) | 2026.1.0.26 | Novolis | Treaty and supranational-organization lifecycle: bilateral/multilateral instrum… |
| 2026-09-30 21:58:17 | [Novolis.CodeGen.Reflection.ClassDiagram](https://www.nuget.org/packages/Novolis.CodeGen.Reflection.ClassDiagram) | 2026.1.2.47 | Novolis | Build Mermaid classDiagram text from assembly reflection. |
| 2026-09-30 21:58:18 | [Novolis.CodeGen.Reflection.Dump](https://www.nuget.org/packages/Novolis.CodeGen.Reflection.Dump) | 2026.1.2.47 | Novolis | Dump objects as C# initialization code for tests and debugging. |
| 2026-09-30 21:58:19 | [Novolis.Game.Procedural](https://www.nuget.org/packages/Novolis.Game.Procedural) | 2026.1.1.29 | Novolis | Seeded procedural tools for games: noise/FBM terrain, infinite chunk streaming,… |
| 2026-09-30 21:58:20 | [Novolis.Geopolitics.PolicyAgents](https://www.nuget.org/packages/Novolis.Geopolitics.PolicyAgents) | 2026.1.0.26 | Novolis | Deterministic heuristic policy agent: fiscal-policy adjustment, diplomacy propo… |
| 2026-09-30 21:58:20 | [Novolis.CodeGen.Xml](https://www.nuget.org/packages/Novolis.CodeGen.Xml) | 2026.1.2.47 | Novolis | XmlSchemaSet loading and SchemaGraph IR for XSD-driven code generation. |
| 2026-09-30 21:58:21 | [Novolis.Geopolitics.Scenarios](https://www.nuget.org/packages/Novolis.Geopolitics.Scenarios) | 2026.1.0.26 | Novolis | Original fiction world seed: procedural generator, seed DTOs/loader, default em… |
| 2026-09-30 21:58:21 | [Novolis.CodeGen.Xsd](https://www.nuget.org/packages/Novolis.CodeGen.Xsd) | 2026.1.2.47 | Novolis | SchemaGraph → Roslyn SyntaxFactory emit profiles (Wire XmlSerializer, Lean reco… |
| 2026-09-30 21:58:22 | [Novolis.Geopolitics.Simulation](https://www.nuget.org/packages/Novolis.Geopolitics.Simulation) | 2026.1.0.26 | Novolis | Composition root: day/month simulation tick wiring conflict, diplomacy, trade,… |
| 2026-09-30 21:58:23 | [Novolis.Geopolitics.Trade](https://www.nuget.org/packages/Novolis.Geopolitics.Trade) | 2026.1.0.26 | Novolis | Monthly resource clearing: domestic production/consumption, common-market pooli… |
| 2026-09-30 21:58:23 | [Novolis.Math.Arrays](https://www.nuget.org/packages/Novolis.Math.Arrays) | 2026.1.1.45 | Novolis | Volumetric dense grids and index helpers for Novolis math libraries. |
| 2026-09-30 21:58:23 | [Novolis.Mapping](https://www.nuget.org/packages/Novolis.Mapping) | 2026.1.1.7 | Novolis | DI-friendly object mapping definitions (migrated from Frank.Mapping). |
| 2026-09-30 21:58:24 | [Novolis.Markup.Html](https://www.nuget.org/packages/Novolis.Markup.Html) | 2026.1.1.55 | Novolis | Fluent HTML, CSS, JavaScript (functions/classes), and SVG builders for .NET. |
| 2026-09-30 21:58:25 | [Novolis.Math.Geometry](https://www.nuget.org/packages/Novolis.Math.Geometry) | 2026.1.1.45 | Novolis | Geometry primitives, transforms, intersections, and BVH for Novolis stack libra… |
| 2026-09-30 21:58:25 | [Novolis.Markup.Markdown](https://www.nuget.org/packages/Novolis.Markup.Markdown) | 2026.1.1.55 | Novolis | Fluent GitHub-flavored Markdown document builder for .NET. |
| 2026-09-30 21:58:26 | [Novolis.Math.Measure](https://www.nuget.org/packages/Novolis.Math.Measure) | 2026.1.1.45 | Novolis | Scalar length, size, thickness, and rect measure types (points) for Novolis lib… |
| 2026-09-30 21:58:27 | [Novolis.Markup.Markdown.Documents](https://www.nuget.org/packages/Novolis.Markup.Markdown.Documents) | 2026.1.1.55 | Novolis | Map Novolis.Markup.Markdown documents to Novolis.Documents PagedDocument and ex… |
| 2026-09-30 21:58:27 | [Novolis.Manuscript](https://www.nuget.org/packages/Novolis.Manuscript) | 2026.1.1.36 | Novolis | Manuscript workspace catalog, chapter metadata, and diagnostics (no PDF/audio). |
| 2026-09-30 21:58:27 | [Novolis.Logging.Agent](https://www.nuget.org/packages/Novolis.Logging.Agent) | 2026.1.6.25 | Novolis | Agent Surface host for Novolis remote logging (snapshot tail, subscribe, setlev… |
| 2026-09-30 21:58:27 | [Novolis.Math.Topology](https://www.nuget.org/packages/Novolis.Math.Topology) | 2026.1.1.45 | Novolis | Connectivity primitives (polygon, face, edge) for Novolis math libraries. |
| 2026-09-30 21:58:28 | [Novolis.Markup.Markdown.Mermaid.Rendering](https://www.nuget.org/packages/Novolis.Markup.Markdown.Mermaid.Rendering) | 2026.1.1.55 | Novolis | Markdown HTML rendering with headless Mermaid SVG diagrams. |
| 2026-09-30 21:58:28 | [Novolis.Logging.Contracts](https://www.nuget.org/packages/Novolis.Logging.Contracts) | 2026.1.6.25 | Novolis | Remote log wire DTOs and logging scope stack bridge for multi-sink hosts. |
| 2026-09-30 21:58:28 | [Novolis.Manuscript.Editorial](https://www.nuget.org/packages/Novolis.Manuscript.Editorial) | 2026.1.1.36 | Novolis | Deterministic manuscript editorial detectors: lexicon, AI-slop patterns, and na… |
| 2026-09-30 21:58:29 | [Novolis.Logging.Core](https://www.nuget.org/packages/Novolis.Logging.Core) | 2026.1.6.25 | Novolis | In-process remote log hub, ring buffer, and ILogger provider for Novolis loggin… |
| 2026-09-30 21:58:29 | [Novolis.Markup.Markdown.Rendering](https://www.nuget.org/packages/Novolis.Markup.Markdown.Rendering) | 2026.1.1.55 | Novolis | HTML document export for Markdown source (Novolis.Markup.Markdown). PDF via Nov… |
| 2026-09-30 21:58:29 | [Novolis.Manuscript.Export.Audio](https://www.nuget.org/packages/Novolis.Manuscript.Export.Audio) | 2026.1.1.36 | Novolis | Manuscript speech planning, voice-map YAML, audiobook pipeline, and preview. |
| 2026-09-30 21:58:30 | [Novolis.Logging.Diagnostics](https://www.nuget.org/packages/Novolis.Logging.Diagnostics) | 2026.1.6.25 | Novolis | Bounded app-private diagnostic journal and ILogger provider for mobile and desk… |
| 2026-09-30 21:58:30 | [Novolis.Markup.Mermaid](https://www.nuget.org/packages/Novolis.Markup.Mermaid) | 2026.1.1.55 | Novolis | Fluent Mermaid diagram syntax builder and parser for .NET (flowchart, sequence,… |
| 2026-09-30 21:58:31 | [Novolis.Manuscript.Export.Markdown](https://www.nuget.org/packages/Novolis.Manuscript.Export.Markdown) | 2026.1.1.36 | Novolis | Manuscript Markdown/HTML export via Novolis.Markup.Markdown (Parse + MarkdownTo… |
| 2026-09-30 21:58:31 | [Novolis.Logging.Faster](https://www.nuget.org/packages/Novolis.Logging.Faster) | 2026.1.6.25 | Novolis | Microsoft FASTER FasterLog durable sink for Novolis remote logging. |
| 2026-09-30 21:58:32 | [Novolis.Markup.Mermaid.Rendering](https://www.nuget.org/packages/Novolis.Markup.Mermaid.Rendering) | 2026.1.1.55 | Novolis | Headless Mermaid diagram export to SVG (Mermaider) and PNG (Svg.Skia) for Novol… |
| 2026-09-30 21:58:32 | [Novolis.Manuscript.Export.Pdf](https://www.nuget.org/packages/Novolis.Manuscript.Export.Pdf) | 2026.1.1.36 | Novolis | Manuscript PDF export via Novolis.Documents + Documents.Skia with Markdown/HTML… |
| 2026-09-30 21:58:32 | [Novolis.Logging.Transports](https://www.nuget.org/packages/Novolis.Logging.Transports) | 2026.1.6.25 | Novolis | HTTP ingest/SSE and LocalIpc hosts for Novolis remote logging. |
| 2026-09-30 21:58:33 | [Novolis.Manuscript.IO](https://www.nuget.org/packages/Novolis.Manuscript.IO) | 2026.1.1.36 | Novolis | Manuscript tree surgery, working-copy helpers, and git/GitHub façades. |
| 2026-09-30 21:58:33 | [Novolis.IO.Git](https://www.nuget.org/packages/Novolis.IO.Git) | 2026.1.1.34 | Novolis | Process-based Git: status, history/graph, stash, diff, branches, and multi-repo… |
| 2026-09-30 21:58:34 | [Novolis.Scheduling](https://www.nuget.org/packages/Novolis.Scheduling) | 2026.1.1.7 | Novolis | Cron job registration and scheduling (migrated from Frank.CronJobs). |
| 2026-09-30 21:58:34 | [Novolis.Manuscript.LegacyBooks](https://www.nuget.org/packages/Novolis.Manuscript.LegacyBooks) | 2026.1.1.36 | Novolis | Legacy content/series and content/books adapter that returns NMP/1 ManuscriptSn… |
| 2026-09-30 21:58:35 | [Novolis.IO.GitHub](https://www.nuget.org/packages/Novolis.IO.GitHub) | 2026.1.1.34 | Novolis | GitHub OAuth device flow and sparse content/ repository mirror (Pull + Save/Com… |
| 2026-09-30 21:58:35 | [Novolis.Scheduling.Cron](https://www.nuget.org/packages/Novolis.Scheduling.Cron) | 2026.1.1.7 | Novolis | Cron expression parsing and next-occurrence calculation (MIT, from Frank.CronJo… |
| 2026-09-30 21:58:35 | [Novolis.Manuscript.Metrics](https://www.nuget.org/packages/Novolis.Manuscript.Metrics) | 2026.1.1.36 | Novolis | Manuscript word-count, TODO metrics, and character-slice reports for NMP book t… |
| 2026-09-30 21:58:36 | [Novolis.IO.Indexing](https://www.nuget.org/packages/Novolis.IO.Indexing) | 2026.1.1.34 | Novolis | In-memory, format-agnostic content index: entries, aliases, open facets, and di… |
| 2026-09-30 21:58:36 | [Novolis.Manuscript.Protocol](https://www.nuget.org/packages/Novolis.Manuscript.Protocol) | 2026.1.1.36 | Novolis | NMP/1 typed manuscript protocol: workspace discovery, catalog, metadata, and di… |
| 2026-09-30 21:58:37 | [Novolis.IO.Mobile.Android](https://www.nuget.org/packages/Novolis.IO.Mobile.Android) | 2026.1.1.34 | Novolis | Host-side Android Debug Bridge (ADB protocol via AdvancedSharpAdbClient): devic… |
| 2026-09-30 21:58:38 | [Novolis.Manuscript.References](https://www.nuget.org/packages/Novolis.Manuscript.References) | 2026.1.1.36 | Novolis | Domain-aware manuscript reference library built on Novolis.IO.Indexing (cards,… |
| 2026-09-30 21:58:39 | [Novolis.IO.Paths](https://www.nuget.org/packages/Novolis.IO.Paths) | 2026.1.1.34 | Novolis | Workspace root discovery helpers with caller-supplied markers. |
| 2026-09-30 21:58:40 | [Novolis.IO.Processes](https://www.nuget.org/packages/Novolis.IO.Processes) | 2026.1.1.34 | Novolis | Concurrent process job queue with process-tree cancellation. |
| 2026-09-30 21:58:41 | [Novolis.IO.Recovery](https://www.nuget.org/packages/Novolis.IO.Recovery) | 2026.1.1.34 | Novolis | Content-hash draft recovery snapshots under a configurable root. |
| 2026-09-30 21:58:41 | [Novolis.Pdf.Abstractions](https://www.nuget.org/packages/Novolis.Pdf.Abstractions) | 2026.1.1.10 | Novolis | UI-neutral contracts and records for Novolis PDF reading. |
| 2026-09-30 21:58:42 | [Novolis.MachineLearning.Algorithms](https://www.nuget.org/packages/Novolis.MachineLearning.Algorithms) | 2026.1.1.38 | Novolis | Classic ML.NET trainers plus typed Features<T> Naive Bayes (Gaussian/Bernoulli)… |
| 2026-09-30 21:58:42 | [Novolis.IO.Watching](https://www.nuget.org/packages/Novolis.IO.Watching) | 2026.1.1.34 | Novolis | Single-file FileSystemWatcher helpers with optional debounce. |
| 2026-09-30 21:58:42 | [Novolis.Pdf.Core](https://www.nuget.org/packages/Novolis.Pdf.Core) | 2026.1.1.10 | Novolis | Reader lifetime, limits, lazy object access, and orchestration for Novolis PDF. |
| 2026-09-30 21:58:43 | [Novolis.MachineLearning.AutoMl](https://www.nuget.org/packages/Novolis.MachineLearning.AutoMl) | 2026.1.1.38 | Novolis | ML.NET AutoML experiment helpers, metrics formatting, and satellite trainer pac… |
| 2026-09-30 21:58:44 | [Novolis.Pdf.Documents](https://www.nuget.org/packages/Novolis.Pdf.Documents) | 2026.1.1.10 | Novolis | Local recent-document, reading-position, and cache records for Novolis PDF host… |
| 2026-09-30 21:58:44 | [Novolis.IO.Workspace](https://www.nuget.org/packages/Novolis.IO.Workspace) | 2026.1.1.34 | Novolis | Typed directory-root workspace abstraction with explicit file I/O capabilities. |
| 2026-09-30 21:58:45 | [Novolis.MachineLearning.Core](https://www.nuget.org/packages/Novolis.MachineLearning.Core) | 2026.1.1.38 | Novolis | Core IO and path helpers for Novolis machine learning packages. |
| 2026-09-30 21:58:45 | [Novolis.Pdf.Parsing](https://www.nuget.org/packages/Novolis.Pdf.Parsing) | 2026.1.1.10 | Novolis | Ground-up PDF syntax, cross-reference, indirect-object, and stream parsing. |
| 2026-09-30 21:58:45 | [Novolis.IO.Workspace.Abstractions](https://www.nuget.org/packages/Novolis.IO.Workspace.Abstractions) | 2026.1.1.34 | Novolis | Typed directory-root workspace abstraction. |
| 2026-09-30 21:58:46 | [Novolis.Maui.Agent](https://www.nuget.org/packages/Novolis.Maui.Agent) | 2026.1.1.28 | Novolis | In-process MAUI UI agent host: LocalIpc ui.* protocol, tree dump, screenshot, c… |
| 2026-09-30 21:58:46 | [Novolis.MachineLearning.Dump](https://www.nuget.org/packages/Novolis.MachineLearning.Dump) | 2026.1.1.38 | Novolis | Persist neural snapshots as CodeGen dump C# fixtures and ML.NET models as zip f… |
| 2026-09-30 21:58:46 | [Novolis.Pdf.Platform](https://www.nuget.org/packages/Novolis.Pdf.Platform) | 2026.1.1.10 | Novolis | Platform-neutral activation, document source, and local storage contracts for N… |
| 2026-09-30 21:58:46 | [Novolis.IO.Workspace.Testing](https://www.nuget.org/packages/Novolis.IO.Workspace.Testing) | 2026.1.1.34 | Novolis | In-memory IFileWorkspace for unit tests. |
| 2026-09-30 21:58:47 | [Novolis.Maui.Agent.Protocol](https://www.nuget.org/packages/Novolis.Maui.Agent.Protocol) | 2026.1.1.28 | Novolis | MessagePack DTOs, LocalIpc helpers, and client for the MAUI UI agent protocol (… |
| 2026-09-30 21:58:47 | [Novolis.Pdf.Rendering](https://www.nuget.org/packages/Novolis.Pdf.Rendering) | 2026.1.1.10 | Novolis | Host-neutral page graphics, transforms, and render-target contracts for Novolis… |
| 2026-09-30 21:58:47 | [Novolis.MachineLearning.Llm.Abstractions](https://www.nuget.org/packages/Novolis.MachineLearning.Llm.Abstractions) | 2026.1.1.38 | Novolis | Provider-neutral contracts for local and remote language model chat generation. |
| 2026-09-30 21:58:48 | [Novolis.Pdf.Rendering.Skia](https://www.nuget.org/packages/Novolis.Pdf.Rendering.Skia) | 2026.1.1.10 | Novolis | Contained Skia raster adapter for Novolis PDF page rendering. |
| 2026-09-30 21:58:48 | [Novolis.Maui.GraphicalProfile](https://www.nuget.org/packages/Novolis.Maui.GraphicalProfile) | 2026.1.1.28 | Novolis | Required Novolis graphical profile for MAUI hosts: Merglyph palette, typography… |
| 2026-09-30 21:58:48 | [Novolis.MachineLearning.Neural](https://www.nuget.org/packages/Novolis.MachineLearning.Neural) | 2026.1.1.38 | Novolis | Dense feedforward neural network implementation with training, mutation, and JS… |
| 2026-09-30 21:58:49 | [Novolis.Economy.Abstractions](https://www.nuget.org/packages/Novolis.Economy.Abstractions) | 2026.1.0.52 | Novolis | Model-neutral economic capability contracts and actor boundary records. |
| 2026-09-30 21:58:49 | [Novolis.Pdf.Text](https://www.nuget.org/packages/Novolis.Pdf.Text) | 2026.1.1.10 | Novolis | PDF text spans, search, selection geometry, and navigation extraction. |
| 2026-09-30 21:58:49 | [Novolis.Maui.Markdown](https://www.nuget.org/packages/Novolis.Maui.Markdown) | 2026.1.1.28 | Novolis | MAUI Markdown viewer: Novolis.Markup HTML + Mermaid SVG in a locked-down WebVie… |
| 2026-09-30 21:58:51 | [Novolis.Maui.Mermaid](https://www.nuget.org/packages/Novolis.Maui.Mermaid) | 2026.1.1.28 | Novolis | MAUI Mermaid diagram view: render Mermaid source (or Novolis.Markup.Mermaid bui… |
| 2026-09-30 21:58:53 | [Novolis.Economy.Accounting](https://www.nuget.org/packages/Novolis.Economy.Accounting) | 2026.1.0.52 | Novolis | Read-only financial projections and diagnostics over Core economic state, with… |
| 2026-09-30 21:58:53 | [Novolis.MachineLearning.Neural.Abstractions](https://www.nuget.org/packages/Novolis.MachineLearning.Neural.Abstractions) | 2026.1.1.38 | Novolis | Contracts and DTOs for dense neural networks and snapshot serialization. |
| 2026-09-30 21:58:53 | [Novolis.Maui.PdfViewer](https://www.nuget.org/packages/Novolis.Maui.PdfViewer) | 2026.1.1.28 | Novolis | Local Novolis PDF viewer control for MAUI Windows and Android hosts. |
| 2026-09-30 21:58:54 | [Novolis.Economy.Agents](https://www.nuget.org/packages/Novolis.Economy.Agents) | 2026.1.0.52 | Novolis | Simulation-independent rules-based and fuzzable economic actor policies. |
| 2026-09-30 21:58:55 | [Novolis.MachineLearning.SharpMind](https://www.nuget.org/packages/Novolis.MachineLearning.SharpMind) | 2026.1.1.38 | Novolis | Optional SharpMind-backed local LLM chat adapter for Novolis machine learning p… |
| 2026-09-30 21:58:55 | [Novolis.Maui.WebView](https://www.nuget.org/packages/Novolis.Maui.WebView) | 2026.1.1.28 | Novolis | Locked-down MAUI WebView for locally rendered HTML (CSP, navigation policy). Av… |
| 2026-09-30 21:58:55 | [Novolis.Physics](https://www.nuget.org/packages/Novolis.Physics) | 2026.1.1.47 | Novolis | Force-first simulation stack for games and tools — one install for all Novolis.… |
| 2026-09-30 21:58:55 | [Novolis.Economy.Core](https://www.nuget.org/packages/Novolis.Economy.Core) | 2026.1.0.52 | Novolis | Bounded-minimum economic authority: immutable EconomyState, authoritative posit… |
| 2026-09-30 21:58:56 | [Novolis.Physics.Abstractions](https://www.nuget.org/packages/Novolis.Physics.Abstractions) | 2026.1.1.47 | Novolis | Force models, static world queries, and integration contracts for Novolis.Physi… |
| 2026-09-30 21:58:56 | [Novolis.Economy.Finance](https://www.nuget.org/packages/Novolis.Economy.Finance) | 2026.1.0.52 | Novolis | Inter-firm term loans, interest accrual, and default hooks for Novolis economic… |
| 2026-09-30 21:58:57 | [Novolis.Physics.Aerodynamics](https://www.nuget.org/packages/Novolis.Physics.Aerodynamics) | 2026.1.1.47 | Novolis | Atmosphere density hooks and simple lift/drag force models. |
| 2026-09-30 21:58:57 | [Novolis.Messaging](https://www.nuget.org/packages/Novolis.Messaging) | 2026.1.1.45 | Novolis | In-process pulse messaging (PulseFlow) over channels with DI. |
| 2026-09-30 21:58:58 | [Novolis.Economy.Logistics](https://www.nuget.org/packages/Novolis.Economy.Logistics) | 2026.1.0.52 | Novolis | Hub/corridor transport network, itinerary planning, and multi-leg shipments sch… |
| 2026-09-30 21:58:58 | [Novolis.Physics.Astro](https://www.nuget.org/packages/Novolis.Physics.Astro) | 2026.1.1.47 | Novolis | Astronomical unit conversions (ly/pc/AU) to SI meters for physics bridging. |
| 2026-09-30 21:58:58 | [Novolis.Messaging.Abstractions](https://www.nuget.org/packages/Novolis.Messaging.Abstractions) | 2026.1.1.45 | Novolis | Message contracts above channels (Frank.Messaging.Abstractions migration). |
| 2026-09-30 21:58:59 | [Novolis.Economy.Markets](https://www.nuget.org/packages/Novolis.Economy.Markets) | 2026.1.0.52 | Novolis | Market estimate and imperfect-information stubs for Novolis economic simulation. |
| 2026-09-30 21:58:59 | [Novolis.Physics.Ballistics](https://www.nuget.org/packages/Novolis.Physics.Ballistics) | 2026.1.1.47 | Novolis | Projectile drag helpers and static-world ray/sweep queries. |
| 2026-09-30 21:59:00 | [Novolis.Economy.Models.DeterministicBounded](https://www.nuget.org/packages/Novolis.Economy.Models.DeterministicBounded) | 2026.1.0.52 | Novolis | Host-neutral finite deterministic economic model for regression and teaching. |
| 2026-09-30 21:59:00 | [Novolis.Physics.Cloth](https://www.nuget.org/packages/Novolis.Physics.Cloth) | 2026.1.1.47 | Novolis | Cloth / fabric simulation: particle sheets, strain limits, blade and blast cutt… |
| 2026-09-30 21:59:00 | [Novolis.Messaging.Channels](https://www.nuget.org/packages/Novolis.Messaging.Channels) | 2026.1.1.45 | Novolis | System.Threading.Channels registration for Microsoft.Extensions.DependencyInjec… |
| 2026-09-30 21:59:00 | [AxaFrance.WebEngine.Cli](https://www.nuget.org/packages/AxaFrance.WebEngine.Cli) | 3.26.273.2-preview | AxaFrance, Huaxing YUAN | WebEngine CLI and local daemon for persistent Selenium browser automation sessi… |
| 2026-09-30 21:59:01 | [Novolis.Economy.Models.SmallOpenRegionalTrade](https://www.nuget.org/packages/Novolis.Economy.Models.SmallOpenRegionalTrade) | 2026.1.0.52 | Novolis | Host-neutral small open regional trade economic model and named scenarios. |
| 2026-09-30 21:59:01 | [Novolis.Physics.Collision.Simple](https://www.nuget.org/packages/Novolis.Physics.Collision.Simple) | 2026.1.1.47 | Novolis | Static triangle mesh with BVH and query-only IStaticWorld implementation. |
| 2026-09-30 21:59:02 | [Novolis.Messaging.Coordination.Abstractions](https://www.nuget.org/packages/Novolis.Messaging.Coordination.Abstractions) | 2026.1.1.45 | Novolis | Distributed host coordination ports (presence, tick leadership, token denylist,… |
| 2026-09-30 21:59:02 | [Novolis.Economy.Population](https://www.nuget.org/packages/Novolis.Economy.Population) | 2026.1.0.52 | Novolis | Consumer cohort and preference stubs for Novolis economic simulation. |
| 2026-09-30 21:59:02 | [Novolis.Physics.Gravity](https://www.nuget.org/packages/Novolis.Physics.Gravity) | 2026.1.1.47 | Novolis | Point and spherical gravity force models for Novolis.Physics. |
| 2026-09-30 21:59:03 | [Novolis.Messaging.Coordination.InMemory](https://www.nuget.org/packages/Novolis.Messaging.Coordination.InMemory) | 2026.1.1.45 | Novolis | In-process coordination implementations for single-host and tests. |
| 2026-09-30 21:59:03 | [Novolis.Economy.Primitives](https://www.nuget.org/packages/Novolis.Economy.Primitives) | 2026.1.0.52 | Novolis | Small BCL-only vocabulary for economic identities, quantities, positions, and m… |
| 2026-09-30 21:59:03 | [Novolis.Windows.Audio](https://www.nuget.org/packages/Novolis.Windows.Audio) | 2026.1.1.14 | Novolis | Windows WASAPI loopback capture for interactive session hosts. |
| 2026-09-30 21:59:04 | [Novolis.Physics.Joints](https://www.nuget.org/packages/Novolis.Physics.Joints) | 2026.1.1.47 | Novolis | Distance constraints between dynamic spheres for ragdolls and chains. |
| 2026-09-30 21:59:04 | [Novolis.Economy.Production](https://www.nuget.org/packages/Novolis.Economy.Production) | 2026.1.0.52 | Novolis | Product definitions, batches, facility IDs, Quantity/time ops vocabulary, and c… |
| 2026-09-30 21:59:04 | [Novolis.Messaging.Coordination.Redis](https://www.nuget.org/packages/Novolis.Messaging.Coordination.Redis) | 2026.1.1.45 | Novolis | StackExchange.Redis coordination (Garnet/Redis) with configurable key prefix. |
| 2026-09-30 21:59:05 | [Novolis.Windows.Clipboard](https://www.nuget.org/packages/Novolis.Windows.Clipboard) | 2026.1.1.14 | Novolis | Windows text clipboard access for interactive session hosts. |
| 2026-09-30 21:59:05 | [Novolis.Physics.Motion](https://www.nuget.org/packages/Novolis.Physics.Motion) | 2026.1.1.47 | Novolis | Rigid-body motion, fixed timestep helpers, and force aggregation pipeline. |
| 2026-09-30 21:59:06 | [Novolis.Economy.Simulation](https://www.nuget.org/packages/Novolis.Economy.Simulation) | 2026.1.0.52 | Novolis | Economic model composition and execution: clocks, phases, agents, runs, metrics… |
| 2026-09-30 21:59:06 | [Novolis.Messaging.SecureText](https://www.nuget.org/packages/Novolis.Messaging.SecureText) | 2026.1.1.45 | Novolis | Transport-neutral authenticated envelope, replay policy, and sessions for end-t… |
| 2026-09-30 21:59:06 | [Novolis.Physics.Orbits](https://www.nuget.org/packages/Novolis.Physics.Orbits) | 2026.1.1.47 | Novolis | Central-body orbital helpers, fixed-step Leapfrog, and SoA-oriented kernels. |
| 2026-09-30 21:59:06 | [Novolis.Windows.Display](https://www.nuget.org/packages/Novolis.Windows.Display) | 2026.1.1.14 | Novolis | Windows monitor topology and DPI discovery. |
| 2026-09-30 21:59:07 | [Novolis.Messaging.ServiceBus.Abstractions](https://www.nuget.org/packages/Novolis.Messaging.ServiceBus.Abstractions) | 2026.1.1.45 | Novolis | Service Bus client, sender, receiver, and admin ports. |
| 2026-09-30 21:59:08 | [Novolis.Windows.Input](https://www.nuget.org/packages/Novolis.Windows.Input) | 2026.1.1.14 | Novolis | Windows pointer and keyboard input injection primitives. |
| 2026-09-30 21:59:08 | [Novolis.Storage.Abstractions](https://www.nuget.org/packages/Novolis.Storage.Abstractions) | 2026.1.1.36 | Novolis | Entity repository and event-store contracts with AddStorage DI composition. |
| 2026-09-30 21:59:08 | [Novolis.Messaging.ServiceBus.Broker.Almost](https://www.nuget.org/packages/Novolis.Messaging.ServiceBus.Broker.Almost) | 2026.1.1.45 | Novolis | AlmostServiceBus in-process broker host for local development and tests. |
| 2026-09-30 21:59:09 | [Novolis.Testing.Appium](https://www.nuget.org/packages/Novolis.Testing.Appium) | 2026.1.1.40 | Novolis | TUnit Appium session helpers for Android and Windows MAUI hosts. |
| 2026-09-30 21:59:09 | [Novolis.Windows.Pdf](https://www.nuget.org/packages/Novolis.Windows.Pdf) | 2026.1.1.14 | Novolis | Windows user-space PDF activation and current-user file association helpers. |
| 2026-09-30 21:59:09 | [Novolis.Storage.InMemory](https://www.nuget.org/packages/Novolis.Storage.InMemory) | 2026.1.1.36 | Novolis | In-memory IRepository provider for tests and playtest profiles. |
| 2026-09-30 21:59:10 | [Novolis.Testing.Coverage](https://www.nuget.org/packages/Novolis.Testing.Coverage) | 2026.1.1.40 | Novolis | Test helpers for coverage-closing work: public API surface probes for smoke tes… |
| 2026-09-30 21:59:10 | [Novolis.Messaging.ServiceBus.Client](https://www.nuget.org/packages/Novolis.Messaging.ServiceBus.Client) | 2026.1.1.45 | Novolis | Azure.Messaging.ServiceBus adapter implementing Novolis Service Bus ports. |
| 2026-09-30 21:59:10 | [Novolis.Storage.Json](https://www.nuget.org/packages/Novolis.Storage.Json) | 2026.1.1.36 | Novolis | JSON file-per-entity IRepository provider. |
| 2026-09-30 21:59:10 | [Novolis.Windows.Sessions](https://www.nuget.org/packages/Novolis.Windows.Sessions) | 2026.1.1.14 | Novolis | Windows interactive session discovery and session identity helpers. |
| 2026-09-30 21:59:11 | [Novolis.Testing.Logging](https://www.nuget.org/packages/Novolis.Testing.Logging) | 2026.1.1.40 | Novolis | Test logging for TUnit TestContext. |
| 2026-09-30 21:59:11 | [Novolis.Storage.LiteDb](https://www.nuget.org/packages/Novolis.Storage.LiteDb) | 2026.1.1.36 | Novolis | LiteDB-backed IRepository provider. |
| 2026-09-30 21:59:11 | [Novolis.Messaging.ServiceBus.Primitives](https://www.nuget.org/packages/Novolis.Messaging.ServiceBus.Primitives) | 2026.1.1.45 | Novolis | Service Bus message envelope (IMessage<T> / Message<T>) and settle primitives. |
| 2026-09-30 21:59:12 | [Novolis.Testing.ServiceBus](https://www.nuget.org/packages/Novolis.Testing.ServiceBus) | 2026.1.1.40 | Novolis | TUnit Service Bus test host over AlmostServiceBus (Novolis Client + Broker.Almo… |
| 2026-09-30 21:59:13 | [Novolis.Storage.Sqlite](https://www.nuget.org/packages/Novolis.Storage.Sqlite) | 2026.1.1.36 | Novolis | SQLite-backed IRepository provider. |
| 2026-09-30 21:59:13 | [Novolis.Testing.TUnit](https://www.nuget.org/packages/Novolis.Testing.TUnit) | 2026.1.1.40 | Novolis | TUnit test output extensions (tables, JSON, C# dump). |
| 2026-09-30 21:59:14 | [Novolis.Testing.TestBases](https://www.nuget.org/packages/Novolis.Testing.TestBases) | 2026.1.1.40 | Novolis | Test host bases for integration tests (TUnit). |
| 2026-09-30 21:59:15 | [Novolis.Testing.TestServer](https://www.nuget.org/packages/Novolis.Testing.TestServer) | 2026.1.1.40 | Novolis | In-memory test server helpers |
| 2026-09-30 21:59:16 | [Novolis.Testing.Testcontainers](https://www.nuget.org/packages/Novolis.Testing.Testcontainers) | 2026.1.1.40 | Novolis | Testcontainers helpers |
| 2026-09-30 21:59:20 | [Novolis.Rendering](https://www.nuget.org/packages/Novolis.Rendering) | 2026.1.1.70 | Novolis | Rendering composition stack — materials, scene compile, CPU/GPU backends, prese… |
| 2026-09-30 21:59:21 | [Novolis.Rendering.Abstractions](https://www.nuget.org/packages/Novolis.Rendering.Abstractions) | 2026.1.1.70 | Novolis | Graphics-host-neutral frame buffers, cameras, and ray tracing contracts. |
| 2026-09-30 21:59:22 | [Novolis.Rendering.Backends.Cpu](https://www.nuget.org/packages/Novolis.Rendering.Backends.Cpu) | 2026.1.1.70 | Novolis | CPU path tracing backend with progressive accumulation. |
| 2026-09-30 21:59:23 | [Novolis.WorkflowEngine](https://www.nuget.org/packages/Novolis.WorkflowEngine) | 2026.1.1.8 | Novolis | Named, manually invokable workflow pipelines for .NET applications. |
| 2026-09-30 21:59:23 | [Novolis.Transports.Abstractions](https://www.nuget.org/packages/Novolis.Transports.Abstractions) | 2026.1.1.56 | Novolis | Transport-neutral connection, stream, datagram, and capability contracts. |
| 2026-09-30 21:59:24 | [Novolis.Rendering.Backends.Igpu](https://www.nuget.org/packages/Novolis.Rendering.Backends.Igpu) | 2026.1.1.70 | Novolis | ILGPU ray tracing backend (GPU compute with CPU fallback). |
| 2026-09-30 21:59:24 | [Novolis.WorkflowEngine.Abstractions](https://www.nuget.org/packages/Novolis.WorkflowEngine.Abstractions) | 2026.1.1.8 | Novolis | Contracts and execution records for Novolis workflows. |
| 2026-09-30 21:59:25 | [Novolis.Transports.Datagrams](https://www.nuget.org/packages/Novolis.Transports.Datagrams) | 2026.1.1.56 | Novolis | UDP datagram channel primitives. |
| 2026-09-30 21:59:25 | [Novolis.Rendering.Backends.TwoD.Silk](https://www.nuget.org/packages/Novolis.Rendering.Backends.TwoD.Silk) | 2026.1.1.70 | Novolis | Silk.NET OpenGL backend for Novolis.Rendering.TwoD. |
| 2026-09-30 21:59:26 | [Novolis.WorkflowEngine.Channels](https://www.nuget.org/packages/Novolis.WorkflowEngine.Channels) | 2026.1.1.8 | Novolis | System.Threading.Channels trigger adapter for Novolis workflows. |
| 2026-09-30 21:59:26 | [Novolis.Rendering.Backends.Vulkan](https://www.nuget.org/packages/Novolis.Rendering.Backends.Vulkan) | 2026.1.1.70 | Novolis | Vulkan backends: compute path tracing and interactive wireframe graphics (SPIR-… |
| 2026-09-30 21:59:26 | [Novolis.Transports.Discovery](https://www.nuget.org/packages/Novolis.Transports.Discovery) | 2026.1.1.56 | Novolis | Generic UDP discovery beacon primitives. |
| 2026-09-30 21:59:26 | [Novolis.Video.Abstractions](https://www.nuget.org/packages/Novolis.Video.Abstractions) | 2026.1.0.23 | Novolis | Platform-neutral capture, encoded-frame, encoder, and decoder contracts. |
| 2026-09-30 21:59:27 | [Novolis.Ship.Analysis](https://www.nuget.org/packages/Novolis.Ship.Analysis) | 2026.1.1.22 | Novolis | Engineering plausibility analysis for ShipDesign: mass, gravity loads, pressure… |
| 2026-09-30 21:59:27 | [Novolis.WorkflowEngine.Hosting](https://www.nuget.org/packages/Novolis.WorkflowEngine.Hosting) | 2026.1.1.8 | Novolis | Generic-host integration for Novolis workflows. |
| 2026-09-30 21:59:27 | [Novolis.Rendering.Compile](https://www.nuget.org/packages/Novolis.Rendering.Compile) | 2026.1.1.70 | Novolis | Scene compilation into flat runtime structures and BVH. |
| 2026-09-30 21:59:27 | [Novolis.Transports.Framing](https://www.nuget.org/packages/Novolis.Transports.Framing) | 2026.1.1.56 | Novolis | Length-prefixed stream framing primitives. |
| 2026-09-30 21:59:27 | [Novolis.Video.Capture.Windows](https://www.nuget.org/packages/Novolis.Video.Capture.Windows) | 2026.1.0.23 | Novolis | Windows webcam capture for Novolis.Video.Rtc (SIPSorceryMedia.Windows). |
| 2026-09-30 21:59:28 | [Novolis.Ship.Design](https://www.nuget.org/packages/Novolis.Ship.Design) | 2026.1.1.22 | Novolis | Object-first ship design model: ShipDesign graph with per-object CadDocument co… |

_Showing the first 200 of 365 packages; see the [full CSV](data/new-nuget-packages-2026-09-30T22-20-21-15832Z.csv)._

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

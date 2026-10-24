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

## Latest list — 2026-10-24 12:21 UTC

New packages created between 2026-10-24 11:21 UTC and 2026-10-24 12:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-24T12-21-45-961921Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-24 11:29:02 | [AgentCrystal](https://www.nuget.org/packages/AgentCrystal) | 0.3.2 | YELANDAOKONG | Core provider-neutral contracts for text and multimodal model access, embedding… |
| 2026-10-24 11:29:03 | [AgentCrystal.Agents](https://www.nuget.org/packages/AgentCrystal.Agents) | 0.3.2 | YELANDAOKONG | Text and multimodal model and tool loops with caller-configured limits. |
| 2026-10-24 11:29:04 | [AgentCrystal.Decorators](https://www.nuget.org/packages/AgentCrystal.Decorators) | 0.3.2 | YELANDAOKONG | Middleware wrappers that preserve current Crystal client contracts and capabili… |
| 2026-10-24 11:29:05 | [AgentCrystal.Harness](https://www.nuget.org/packages/AgentCrystal.Harness) | 0.3.2 | YELANDAOKONG | Composition of named Agents with shared caller-configured limits. |
| 2026-10-24 11:29:06 | [AgentCrystal.Pipelines](https://www.nuget.org/packages/AgentCrystal.Pipelines) | 0.3.2 | YELANDAOKONG | Generic caller-owned middleware for typed asynchronous operations and event str… |
| 2026-10-24 11:29:07 | [AgentCrystal.Tools](https://www.nuget.org/packages/AgentCrystal.Tools) | 0.3.2 | YELANDAOKONG | Text and multimodal tool registration, policy, and execution. Crystal supplies… |
| 2026-10-24 11:29:08 | [AgentCrystal.Workflows](https://www.nuget.org/packages/AgentCrystal.Workflows) | 0.3.2 | YELANDAOKONG | Caller-defined typed workflow graphs with conditional edges and bounded concurr… |
| 2026-10-24 11:29:41 | [WifiManager.MacVendors](https://www.nuget.org/packages/WifiManager.MacVendors) | 1.0.0 | exendahal | Names the manufacturer of a network adapter from its MAC address, offline, usin… |
| 2026-10-24 11:31:58 | [Tarjamot.BergamotMarkup](https://www.nuget.org/packages/Tarjamot.BergamotMarkup) | 0.1.10 | Filip Navara | Firefox's HTML translation for Tarjamot: a port of Bergamot's HTML mode, which… |
| 2026-10-24 11:32:22 | [Fable.Temporal](https://www.nuget.org/packages/Fable.Temporal) | 0.1.0 | Oliver Coad | Strongly typed Fable bindings for JavaScript Temporal, independent of compiler… |
| 2026-10-24 11:41:25 | [Eryph.Mcp.Server](https://www.nuget.org/packages/Eryph.Mcp.Server) | 0.1.1 | dbosoft | stdio MCP server for eryph: create, run and inspect catlets with the user's ery… |
| 2026-10-24 11:50:57 | [BitMagic.ClaudeBox.Cli](https://www.nuget.org/packages/BitMagic.ClaudeBox.Cli) | 0.1.1 | Yazwh0 | Named, colour-coded Claude Code sessions in Windows Terminal tabs that come bac… |
| 2026-10-24 11:53:51 | [HotChocolate.CostAnalysis.Core](https://www.nuget.org/packages/HotChocolate.CostAnalysis.Core) | 16.7.0 | ChilliCream authors and contr… | The shared implementation of the IBM GraphQL cost specification: schema indexes… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

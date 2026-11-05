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

## Latest list — 2026-11-05 19:19 UTC

New packages created between 2026-11-05 18:20 UTC and 2026-11-05 19:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-05T19-19-53-661461Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-05 18:21:12 | [Kahuna.Aspire.Client](https://www.nuget.org/packages/Kahuna.Aspire.Client) | 1.15.0 | Andres Gutierrez | .NET Aspire client integration for Kahuna: registers a KahunaClient from a conn… |
| 2026-11-05 18:21:23 | [Kahuna.Aspire.Hosting](https://www.nuget.org/packages/Kahuna.Aspire.Hosting) | 1.15.0 | Andres Gutierrez | .NET Aspire hosting integration for Kahuna: run a Kahuna node as a container re… |
| 2026-11-05 18:21:51 | [MyAgents.Runtime.Workers](https://www.nuget.org/packages/MyAgents.Runtime.Workers) | 1.0.0 | Michspirit99 | MyAgents — A .NET agent orchestration framework built on Microsoft.Extensions.A… |
| 2026-11-05 18:21:51 | [MyAgents.Memory](https://www.nuget.org/packages/MyAgents.Memory) | 1.0.0 | Michspirit99 | MyAgents — A .NET agent orchestration framework built on Microsoft.Extensions.A… |
| 2026-11-05 18:21:52 | [MyAgents.Runtime.Chat](https://www.nuget.org/packages/MyAgents.Runtime.Chat) | 1.0.0 | Michspirit99 | MyAgents — A .NET agent orchestration framework built on Microsoft.Extensions.A… |
| 2026-11-05 18:21:52 | [MyAgents.Agents](https://www.nuget.org/packages/MyAgents.Agents) | 1.0.0 | Michspirit99 | MyAgents — A .NET agent orchestration framework built on Microsoft.Extensions.A… |
| 2026-11-05 18:21:52 | [MyAgents.Generators](https://www.nuget.org/packages/MyAgents.Generators) | 1.0.0 | Michspirit99 | MyAgents source generator: compile-time [AgentTool] ITool wrappers with JSON sc… |
| 2026-11-05 18:21:53 | [MyAgents.Mcp](https://www.nuget.org/packages/MyAgents.Mcp) | 1.0.0 | Michspirit99 | MyAgents — A .NET agent orchestration framework built on Microsoft.Extensions.A… |
| 2026-11-05 18:21:53 | [MyAgents.Testing](https://www.nuget.org/packages/MyAgents.Testing) | 1.0.0 | Michspirit99 | MyAgents — A .NET agent orchestration framework built on Microsoft.Extensions.A… |
| 2026-11-05 18:21:53 | [MyAgents.Core](https://www.nuget.org/packages/MyAgents.Core) | 1.0.0 | Michspirit99 | MyAgents — A .NET agent orchestration framework built on Microsoft.Extensions.A… |
| 2026-11-05 18:21:54 | [MyAgents.Runtime.Workers.Sqlite](https://www.nuget.org/packages/MyAgents.Runtime.Workers.Sqlite) | 1.0.0 | Michspirit99 | MyAgents — A .NET agent orchestration framework built on Microsoft.Extensions.A… |
| 2026-11-05 18:27:32 | [Hexalith.McpCli](https://www.nuget.org/packages/Hexalith.McpCli) | 2.0.1 | Hexalith Contributors | Generic Hexalith EventStore gateway CLI and MCP server for decorated Contracts… |
| 2026-11-05 18:28:07 | [WebMarkupMin.AspNet.Zstd](https://www.nuget.org/packages/WebMarkupMin.AspNet.Zstd) | 2.24.0-rc1 | Andrey Taritsyn | WebMarkupMin.AspNet.Zstd contains one compressor-adapter for compression of tex… |
| 2026-11-05 18:31:56 | [JsonnetSharp](https://www.nuget.org/packages/JsonnetSharp) | 0.1.0 | HanJaeJoon | A pure C# implementation of the Jsonnet data templating language, ported from g… |
| 2026-11-05 18:38:29 | [CamusDB.Testcontainers.XunitV3](https://www.nuget.org/packages/CamusDB.Testcontainers.XunitV3) | 0.17.0 | Andres Gutierrez | xUnit.net v3 fixture for CamusDB.Testcontainers: shares one CamusDB container a… |
| 2026-11-05 18:38:47 | [CamusDB.Testcontainers.Xunit](https://www.nuget.org/packages/CamusDB.Testcontainers.Xunit) | 0.17.0 | Andres Gutierrez | xUnit.net v2 fixture for CamusDB.Testcontainers: shares one CamusDB container a… |
| 2026-11-05 18:39:14 | [CamusDB.Testcontainers](https://www.nuget.org/packages/CamusDB.Testcontainers) | 0.17.0 | Andres Gutierrez | Testcontainers module for CamusDB: starts a throwaway CamusDB server in Docker… |
| 2026-11-05 18:43:27 | [InvariantStringHelper](https://www.nuget.org/packages/InvariantStringHelper) | 1.0.0 | DevAM | Invariant-culture string interpolation that allocates only the result string: I… |
| 2026-11-05 18:45:00 | [IoTSharp.WinForms.DataVisualization](https://www.nuget.org/packages/IoTSharp.WinForms.DataVisualization) | 10.0.0 | IoTSharp | Windows Forms chart controls for .NET 10. The public System.Windows.Forms.DataV… |
| 2026-11-05 18:52:16 | [XactJobs.UI](https://www.nuget.org/packages/XactJobs.UI) | 0.2.0 | XactJobs | Dashboard UI for XactJobs background job processing library. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

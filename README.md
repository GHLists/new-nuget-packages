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

## Latest list — 2026-10-15 10:20 UTC

New packages created between 2026-10-15 09:22 UTC and 2026-10-15 10:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-15T10-20-41-12423Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-15 09:25:31 | [UKHO.ADDS.Clients.SalesCatalogueService](https://www.nuget.org/packages/UKHO.ADDS.Clients.SalesCatalogueService) | 1.1.61015 | UKHO.ADDS.Clients.SalesCatalo… | ADDS Shared Clients |
| 2026-10-15 09:25:54 | [BorrowedTorch.FabricSimulator](https://www.nuget.org/packages/BorrowedTorch.FabricSimulator) | 1.0.0 | Vladyslav Pysarenko | GPU cloth solver for MonoGame: a compute shader integrates the particles, relax… |
| 2026-10-15 09:30:13 | [Webority.Email.Outbox.AzureStorage](https://www.nuget.org/packages/Webority.Email.Outbox.AzureStorage) | 0.55.0 | Webority Technologies | Azure Blob Storage for queued email attachments: implements IEmailOutboxAttachm… |
| 2026-10-15 09:34:26 | [BorrowedTorch.RayTracing](https://www.nuget.org/packages/BorrowedTorch.RayTracing) | 1.0.0 | Vladyslav Pysarenko | Ray casting for MonoGame (compute fork): a binned-SAH BVH, per-mesh bottom-leve… |
| 2026-10-15 09:42:55 | [Robentex.Fanuc.OpcUa](https://www.nuget.org/packages/Robentex.Fanuc.OpcUa) | 1.0.0 | Robentex | Secure-by-default .NET 9 client library for FANUC OPC UA HMI Device Communicati… |
| 2026-10-15 09:54:14 | [Claustrum](https://www.nuget.org/packages/Claustrum) | 0.1.0 | Dario Orlovich | Harness-neutral coding-agent delegation: one binary that runs role-based agent… |
| 2026-10-15 10:00:26 | [ITBees.Prestashop](https://www.nuget.org/packages/ITBees.Prestashop) | 8.0.2 | ITBees | PrestaShop (8.x) Webservice API client for FAS applications: orders, order stat… |
| 2026-10-15 10:00:58 | [AgentRouter](https://www.nuget.org/packages/AgentRouter) | 1.0.0-preview-0001 | AgentRouter.Cli | Agent Router: model gateway and local control plane for coding agents. |
| 2026-10-15 10:02:13 | [MAFUtils.SqlServer](https://www.nuget.org/packages/MAFUtils.SqlServer) | 0.4.0 | Dean Chalk | Session-scoped SQL Server metadata catalogs and dependency graph tools for Micr… |
| 2026-10-15 10:04:29 | [Aiursoft.AgentKit.Evaluator](https://www.nuget.org/packages/Aiursoft.AgentKit.Evaluator) | 10.0.0 | Aiursoft | Deterministic assertion, evidence, JSON matching, and scoring primitives for ag… |
| 2026-10-15 10:04:31 | [Aiursoft.AgentKit.AgentRunner](https://www.nuget.org/packages/Aiursoft.AgentKit.AgentRunner) | 10.0.0 | Aiursoft | Provider-neutral AgentKit runtime entry points and ordered approval execution. |
| 2026-10-15 10:04:33 | [Aiursoft.AgentKit.Mcp](https://www.nuget.org/packages/Aiursoft.AgentKit.Mcp) | 10.0.0 | Aiursoft | Official MCP SDK adapters for Aiursoft.AgentKit. |
| 2026-10-15 10:04:35 | [Aiursoft.AgentKit](https://www.nuget.org/packages/Aiursoft.AgentKit) | 10.0.0 | Aiursoft | Provider-neutral contracts, messages, cloning, and transcript validation for ag… |
| 2026-10-15 10:07:24 | [com.IvanMurzak.Rql](https://www.nuget.org/packages/com.IvanMurzak.Rql) | 0.1.0 | Ivan Murzak | RQL: a compact pipeline language for AI agents to query and safely change live… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

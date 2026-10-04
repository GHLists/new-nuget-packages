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

## Latest list — 2026-10-04 01:19 UTC

New packages created between 2026-10-04 00:18 UTC and 2026-10-04 01:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-04T01-19-22-045416Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-04 00:19:23 | [Pneuma.Sdk](https://www.nuget.org/packages/Pneuma.Sdk) | 1.0.0 | Joel Christner | C# SDK for the Pneuma REST API - subject knowledge-graph ingestion, search, and… |
| 2026-10-04 00:20:11 | [Partio.Sdk](https://www.nuget.org/packages/Partio.Sdk) | 0.5.1 | Joel Christner | C# client SDK for Partio, a multi-tenant REST service for chunking, embedding,… |
| 2026-10-04 00:23:07 | [Syntrony.UoW](https://www.nuget.org/packages/Syntrony.UoW) | 1.0.0 | Syntrony Technologies Inc. | Implicit unit of work for ASP.NET Core: an action filter opens one per MVC acti… |
| 2026-10-04 00:41:37 | [Shiny.Controls.RangePickers.Shared](https://www.nuget.org/packages/Shiny.Controls.RangePickers.Shared) | 1.6.0-beta-0008 | Allan Ritchie | Host-neutral engine behind the Shiny date range, time range and date/time range… |
| 2026-10-04 00:43:18 | [Vivente.Social](https://www.nuget.org/packages/Vivente.Social) | 0.1.1-alpha | Vivente Unlimited | Reusable, app-agnostic .NET clients for publishing to and connecting social pla… |
| 2026-10-04 00:44:08 | [GAG.Ssv.Client](https://www.nuget.org/packages/GAG.Ssv.Client) | 1.0.1 | GAG | Resilient .NET client for gag.ssv: mTLS, retries with backoff, in-memory cache… |
| 2026-10-04 00:47:58 | [OneFlight](https://www.nuget.org/packages/OneFlight) | 1.0.0 | Stan Drapkin | High-performance .NET single-flight/coalescing library. Concurrent operations w… |
| 2026-10-04 00:50:53 | [VenEl.MCP.ServiceNow](https://www.nuget.org/packages/VenEl.MCP.ServiceNow) | 1.0.0 | VenEl | VenEl Core Business Logic - VenEl.MCP.ServiceNow |
| 2026-10-04 00:52:21 | [RabbitMQ.ClientKit](https://www.nuget.org/packages/RabbitMQ.ClientKit) | 1.0.0 | Colin Campbell | RabbitMQ client toolkit for typed publishing, consuming, serialization, and plu… |
| 2026-10-04 00:52:22 | [RabbitMQ.ClientKit.ChannelPooling](https://www.nuget.org/packages/RabbitMQ.ClientKit.ChannelPooling) | 1.0.0 | Colin Campbell | Channel pooling and consumer channel reuse extensions for RabbitMQ.ClientKit. |
| 2026-10-04 00:52:23 | [RabbitMQ.ClientKit.DynamicConfiguration](https://www.nuget.org/packages/RabbitMQ.ClientKit.DynamicConfiguration) | 1.0.0 | Colin Campbell | Optional dynamic and reloadable RabbitMQ configuration support for RabbitMQ.Cli… |
| 2026-10-04 01:01:53 | [SawKing.DotNetSolutionKit](https://www.nuget.org/packages/SawKing.DotNetSolutionKit) | 2.6.1 | Vladimir Savkin | A .NET 8 microservice solution template for high-load systems, proven in produc… |
| 2026-10-04 01:08:12 | [OpenBim.Ifc](https://www.nuget.org/packages/OpenBim.Ifc) | 0.1.0 | point-grey | Read, edit, validate and write IFC (STEP and ifcXML) files from .NET: the openb… |
| 2026-10-04 01:08:47 | [Idrak.Cli](https://www.nuget.org/packages/Idrak.Cli) | 0.2.0 | Ahmed Seada | idrak: one command-line tool for Idrak: check devices, chat with and serve lang… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-18 00:18 UTC

New packages created between 2026-10-17 23:21 UTC and 2026-10-18 00:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-18T00-18-43-143465Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-17 23:47:37 | [Atulin.Sqids.AspNetCore](https://www.nuget.org/packages/Atulin.Sqids.AspNetCore) | 1.0.0 | Atulin | SQID implementation made specifically for ASP.NET Core usage |
| 2026-10-18 00:00:34 | [Jakar.Json.Http](https://www.nuget.org/packages/Jakar.Json.Http) | 10.1.0 | Tyler Stegmaier | Jakar.Json for HttpClient: JakarJsonContent and GetFromJakarJsonAsync / PostAsJ… |
| 2026-10-18 00:00:36 | [Jakar.Json.SystemTextJson](https://www.nuget.org/packages/Jakar.Json.SystemTextJson) | 10.1.0 | Tyler Stegmaier | Jakar.Json inside System.Text.Json: a JsonConverterFactory that reads and write… |
| 2026-10-18 00:00:37 | [Jakar.Json.Akka](https://www.nuget.org/packages/Jakar.Json.Akka) | 10.1.0 | Tyler Stegmaier | Jakar.Json as an Akka.NET serializer: messages and persisted events of [JsonMod… |
| 2026-10-18 00:00:39 | [Jakar.Json.AwsLambda](https://www.nuget.org/packages/Jakar.Json.AwsLambda) | 10.1.0 | Tyler Stegmaier | Jakar.Json as an AWS Lambda serializer: [JsonModel] requests and responses are… |
| 2026-10-18 00:00:40 | [Jakar.Json.AzureCore](https://www.nuget.org/packages/Jakar.Json.AzureCore) | 10.1.0 | Tyler Stegmaier | Jakar.Json as an Azure SDK ObjectSerializer (Azure.Core): [JsonModel] types are… |
| 2026-10-18 00:00:41 | [Soenneker.OpenSeaChest.Binaries](https://www.nuget.org/packages/Soenneker.OpenSeaChest.Binaries) | 4.0.1 | Jake Soenneker | Native openSeaChest binaries for storage device diagnostics and management. |
| 2026-10-18 00:00:41 | [Jakar.Json.Caching](https://www.nuget.org/packages/Jakar.Json.Caching) | 10.1.0 | Tyler Stegmaier | Jakar.Json for Microsoft's caches: a HybridCache serializer factory for [JsonMo… |
| 2026-10-18 00:00:42 | [Jakar.Json.Cap](https://www.nuget.org/packages/Jakar.Json.Cap) | 10.1.0 | Tyler Stegmaier | Jakar.Json for CAP (DotNetCore.CAP): message payloads of [JsonModel] types are… |
| 2026-10-18 00:00:43 | [Jakar.Json.Cosmos](https://www.nuget.org/packages/Jakar.Json.Cosmos) | 10.1.0 | Tyler Stegmaier | Jakar.Json as the Azure Cosmos DB serializer: items of [JsonModel] types (and c… |
| 2026-10-18 00:00:47 | [Jakar.Json.Dapper](https://www.nuget.org/packages/Jakar.Json.Dapper) | 10.1.0 | Tyler Stegmaier | Jakar.Json for Dapper: type handlers that write [JsonModel] parameters (and col… |
| 2026-10-18 00:00:48 | [Jakar.Json.DurableTask](https://www.nuget.org/packages/Jakar.Json.DurableTask) | 10.1.0 | Tyler Stegmaier | Jakar.Json as the Durable Task (Durable Functions / Durable Task Scheduler) dat… |
| 2026-10-18 00:00:49 | [Jakar.Json.EasyNetQ](https://www.nuget.org/packages/Jakar.Json.EasyNetQ) | 10.1.0 | Tyler Stegmaier | Jakar.Json as the EasyNetQ (RabbitMQ) message serializer: [JsonModel] messages… |
| 2026-10-18 00:00:50 | [Jakar.Json.Elasticsearch](https://www.nuget.org/packages/Jakar.Json.Elasticsearch) | 10.1.0 | Tyler Stegmaier | Jakar.Json as the Elasticsearch .NET client's source serializer: documents (_so… |
| 2026-10-18 00:00:51 | [Jakar.Json.EntityFrameworkCore](https://www.nuget.org/packages/Jakar.Json.EntityFrameworkCore) | 10.1.0 | Tyler Stegmaier | Jakar.Json for EF Core JSON columns: a value converter and value comparer that… |
| 2026-10-18 00:00:52 | [Jakar.Json.Flurl](https://www.nuget.org/packages/Jakar.Json.Flurl) | 10.1.0 | Tyler Stegmaier | Jakar.Json as Flurl.Http's JSON serializer: request and response bodies of [Jso… |
| 2026-10-18 00:00:53 | [Jakar.Json.FusionCache](https://www.nuget.org/packages/Jakar.Json.FusionCache) | 10.1.0 | Tyler Stegmaier | Jakar.Json as FusionCache's distributed-cache serializer: [JsonModel] values (a… |
| 2026-10-18 00:00:54 | [Jakar.Json.GraphQLClient](https://www.nuget.org/packages/Jakar.Json.GraphQLClient) | 10.1.0 | Tyler Stegmaier | Jakar.Json for GraphQL.Client: response data (and variables) of [JsonModel] typ… |
| 2026-10-18 00:00:56 | [Jakar.Json.Kafka](https://www.nuget.org/packages/Jakar.Json.Kafka) | 10.1.0 | Tyler Stegmaier | Jakar.Json for Confluent.Kafka: serializers and deserializers (sync and async)… |
| 2026-10-18 00:00:57 | [Jakar.Json.Logging](https://www.nuget.org/packages/Jakar.Json.Logging) | 10.1.0 | Tyler Stegmaier | A JSON console formatter for Microsoft.Extensions.Logging that writes [JsonMode… |
| 2026-10-18 00:00:58 | [Jakar.Json.Marten](https://www.nuget.org/packages/Jakar.Json.Marten) | 10.1.0 | Tyler Stegmaier | Jakar.Json for Marten (PostgreSQL document database and event store): documents… |
| 2026-10-18 00:00:59 | [Jakar.Json.MassTransit](https://www.nuget.org/packages/Jakar.Json.MassTransit) | 10.1.0 | Tyler Stegmaier | Jakar.Json for MassTransit: messages of [JsonModel] types are written and read… |
| 2026-10-18 00:01:00 | [Jakar.Json.NServiceBus](https://www.nuget.org/packages/Jakar.Json.NServiceBus) | 10.1.0 | Tyler Stegmaier | Jakar.Json for NServiceBus: messages of [JsonModel] types are written and read… |
| 2026-10-18 00:01:01 | [Jakar.Json.OpenApi](https://www.nuget.org/packages/Jakar.Json.OpenApi) | 10.1.0 | Tyler Stegmaier | OpenAPI schemas that match Jakar.Json: [JsonModel] types are described with the… |
| 2026-10-18 00:01:02 | [Jakar.Json.OpenSearch](https://www.nuget.org/packages/Jakar.Json.OpenSearch) | 10.1.0 | Tyler Stegmaier | Jakar.Json as the OpenSearch .NET client's source serializer: documents (_sourc… |
| 2026-10-18 00:01:03 | [Jakar.Json.Orleans](https://www.nuget.org/packages/Jakar.Json.Orleans) | 10.1.0 | Tyler Stegmaier | Jakar.Json for Orleans: grain call arguments, results and state of [JsonModel]… |
| 2026-10-18 00:01:04 | [Jakar.Json.Quartz](https://www.nuget.org/packages/Jakar.Json.Quartz) | 10.1.0 | Tyler Stegmaier | Jakar.Json for Quartz.NET job data: store [JsonModel] values in a JobDataMap as… |
| 2026-10-18 00:01:06 | [Jakar.Json.Rebus](https://www.nuget.org/packages/Jakar.Json.Rebus) | 10.1.0 | Tyler Stegmaier | Jakar.Json for Rebus: message bodies of [JsonModel] types are written and read… |
| 2026-10-18 00:01:07 | [Jakar.Json.Refit](https://www.nuget.org/packages/Jakar.Json.Refit) | 10.1.0 | Tyler Stegmaier | Jakar.Json as Refit's content serializer: request and response bodies of [JsonM… |
| 2026-10-18 00:01:08 | [Jakar.Json.RestSharp](https://www.nuget.org/packages/Jakar.Json.RestSharp) | 10.1.0 | Tyler Stegmaier | Jakar.Json as RestSharp's serializer: request and response bodies of [JsonModel… |
| 2026-10-18 00:01:09 | [Jakar.Json.Serilog](https://www.nuget.org/packages/Jakar.Json.Serilog) | 10.1.0 | Tyler Stegmaier | Jakar.Json for Serilog: [JsonModel] values logged with {@Value} are destructure… |
| 2026-10-18 00:01:10 | [Jakar.Json.SignalR](https://www.nuget.org/packages/Jakar.Json.SignalR) | 10.1.0 | Tyler Stegmaier | Jakar.Json for SignalR's JSON hub protocol: hub method arguments and results of… |
| 2026-10-18 00:01:11 | [Jakar.Json.StackExchangeRedis](https://www.nuget.org/packages/Jakar.Json.StackExchangeRedis) | 10.1.0 | Tyler Stegmaier | Jakar.Json for StackExchange.Redis: store and read [JsonModel] values in Redis… |
| 2026-10-18 00:01:12 | [Jakar.Json.Temporal](https://www.nuget.org/packages/Jakar.Json.Temporal) | 10.1.0 | Tyler Stegmaier | Jakar.Json for Temporal (.NET SDK): workflow and activity arguments and results… |
| 2026-10-18 00:01:13 | [Jakar.Json.Wolverine](https://www.nuget.org/packages/Jakar.Json.Wolverine) | 10.1.0 | Tyler Stegmaier | Jakar.Json as Wolverine's message serializer: messages of [JsonModel] types are… |
| 2026-10-18 00:10:51 | [Soenneker.OpenSeaChest.Util](https://www.nuget.org/packages/Soenneker.OpenSeaChest.Util) | 4.0.4 | Jake Soenneker | A process-based utility for openSeaChest storage device diagnostics and managem… |
| 2026-10-18 00:11:37 | [LlamaLogic.Architecture](https://www.nuget.org/packages/LlamaLogic.Architecture) | 1.0.0 | LlamaLogic | Read and write the lot architecture of Maxis' The Sims 4: walls, floors, roofs,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

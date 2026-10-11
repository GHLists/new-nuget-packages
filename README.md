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

## Latest list — 2026-10-11 03:20 UTC

New packages created between 2026-10-11 02:19 UTC and 2026-10-11 03:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-11T03-20-51-43103Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-11 02:29:20 | [nugetgo.github.com.google.uuid](https://www.nuget.org/packages/nugetgo.github.com.google.uuid) | 1.6.0 | go2cs conversion | unofficial go2cs C# conversion of github.com/google/uuid v1.6.0, built on the G… |
| 2026-10-11 02:43:04 | [CSharpLoad](https://www.nuget.org/packages/CSharpLoad) | 0.1.1 | Xavier Raboteur | CSharp-first load and performance testing framework for .NET. |
| 2026-10-11 02:43:05 | [CSharpLoad.Cli](https://www.nuget.org/packages/CSharpLoad.Cli) | 0.1.1 | Xavier Raboteur | Command-line tooling for CSharpLoad reports and performance baselines. |
| 2026-10-11 02:43:05 | [CSharpLoad.Distributed](https://www.nuget.org/packages/CSharpLoad.Distributed) | 0.1.1 | Xavier Raboteur | Distributed coordinator, agent contracts and result aggregation for CSharpLoad. |
| 2026-10-11 02:43:06 | [CSharpLoad.Distributed.AspNetCore](https://www.nuget.org/packages/CSharpLoad.Distributed.AspNetCore) | 0.1.1 | Xavier Raboteur | ASP.NET Core agent host for CSharpLoad distributed execution. |
| 2026-10-11 02:43:07 | [CSharpLoad.Grpc](https://www.nuget.org/packages/CSharpLoad.Grpc) | 0.1.1 | Xavier Raboteur | gRPC load-testing steps and metrics for CSharpLoad. |
| 2026-10-11 02:43:08 | [CSharpLoad.Http](https://www.nuget.org/packages/CSharpLoad.Http) | 0.1.1 | Xavier Raboteur | HTTP protocol helpers and metrics for CSharpLoad. |
| 2026-10-11 02:43:09 | [CSharpLoad.Kafka](https://www.nuget.org/packages/CSharpLoad.Kafka) | 0.1.1 | Xavier Raboteur | Kafka load-testing steps and metrics for CSharpLoad. |
| 2026-10-11 02:43:09 | [CSharpLoad.OpenTelemetry](https://www.nuget.org/packages/CSharpLoad.OpenTelemetry) | 0.1.1 | Xavier Raboteur | OpenTelemetry tracing and metrics integration for CSharpLoad. |
| 2026-10-11 02:43:10 | [CSharpLoad.RabbitMq](https://www.nuget.org/packages/CSharpLoad.RabbitMq) | 0.1.1 | Xavier Raboteur | RabbitMQ load-testing steps and metrics for CSharpLoad. |
| 2026-10-11 02:43:11 | [CSharpLoad.Redis](https://www.nuget.org/packages/CSharpLoad.Redis) | 0.1.1 | Xavier Raboteur | Redis load-testing steps and metrics for CSharpLoad. |
| 2026-10-11 02:43:12 | [CSharpLoad.SignalR](https://www.nuget.org/packages/CSharpLoad.SignalR) | 0.1.1 | Xavier Raboteur | SignalR load-testing steps and metrics for CSharpLoad. |
| 2026-10-11 02:43:13 | [CSharpLoad.Sql](https://www.nuget.org/packages/CSharpLoad.Sql) | 0.1.1 | Xavier Raboteur | ADO.NET SQL load-testing steps and metrics for CSharpLoad. |
| 2026-10-11 02:43:14 | [CSharpLoad.Templates](https://www.nuget.org/packages/CSharpLoad.Templates) | 0.1.1 | Xavier Raboteur | dotnet new templates for CSharpLoad load-testing projects. |
| 2026-10-11 02:43:14 | [CSharpLoad.WebSockets](https://www.nuget.org/packages/CSharpLoad.WebSockets) | 0.1.1 | Xavier Raboteur | WebSocket load-testing steps and metrics for CSharpLoad. |
| 2026-10-11 02:55:25 | [DataMapper.Extensions](https://www.nuget.org/packages/DataMapper.Extensions) | 1.0.0 | Scotty Hudson <scotty@scottyh… | Extension methods that map IDataReader, DataTable and DataRow rows onto POCOs,… |
| 2026-10-11 03:02:06 | [HunterAhlquist.Solo.Shared](https://www.nuget.org/packages/HunterAhlquist.Solo.Shared) | 1.8.0 | Hunter Ahlquist | DTOs and the client-side seams a Solo extension's pages compile against: the ho… |
| 2026-10-11 03:02:08 | [HunterAhlquist.Solo.Extensibility](https://www.nuget.org/packages/HunterAhlquist.Solo.Extensibility) | 1.8.0 | Hunter Ahlquist | The contract a Solo extension's server half compiles against: the entry point,… |
| 2026-10-11 03:15:26 | [Floci.Testcontainers.Core](https://www.nuget.org/packages/Floci.Testcontainers.Core) | 1.0.0 | Floci and its contributors | Shared core of the Floci Testcontainers modules for .NET: the cloud descriptor,… |
| 2026-10-11 03:15:27 | [Floci.Testcontainers.Aws](https://www.nuget.org/packages/Floci.Testcontainers.Aws) | 1.0.0 | Floci and its contributors | A Testcontainers for .NET module for Floci, the free, open-source local AWS emu… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

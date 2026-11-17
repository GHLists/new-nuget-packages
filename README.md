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

## Latest list — 2026-11-17 07:20 UTC

New packages created between 2026-11-17 06:19 UTC and 2026-11-17 07:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-17T07-20-31-074484Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-17 06:22:29 | [Gnar.Enver.Extensions.Options](https://www.nuget.org/packages/Gnar.Enver.Extensions.Options) | 2.0.0 | Gnar Software LLC | Microsoft.Extensions.Options integration for Enver.Binding. Binds [EnvBindable]… |
| 2026-11-17 06:22:30 | [Gnar.Enver.Extensions](https://www.nuget.org/packages/Gnar.Enver.Extensions) | 2.0.0 | Gnar Software LLC | Everything for using Enver in an app built on Microsoft.Extensions: load .env f… |
| 2026-11-17 06:38:19 | [AutoRegisterDependency.Core](https://www.nuget.org/packages/AutoRegisterDependency.Core) | 1.0.0 | tengfei8771 | Attribute-driven dependency injection on top of Autofac. Mark a class with [Com… |
| 2026-11-17 06:38:27 | [AutoRegisterDependency.Extension.Interception](https://www.nuget.org/packages/AutoRegisterDependency.Extension.Interception) | 1.0.0 | tengfei8771 | Castle DynamicProxy based method interception for AutoRegisterDependency. Deriv… |
| 2026-11-17 06:38:29 | [AutoRegisterDependency.Extension.Quartz.Abstractions](https://www.nuget.org/packages/AutoRegisterDependency.Extension.Quartz.Abstractions) | 1.0.0 | tengfei8771 | Shared Quartz integration abstractions for AutoRegisterDependency: the [Job] at… |
| 2026-11-17 06:38:32 | [AutoRegisterDependency.Extension.Configuration](https://www.nuget.org/packages/AutoRegisterDependency.Extension.Configuration) | 1.0.0 | tengfei8771 | [Configuration] / [Bean] / [Value] / [ConfigurationProperties] / [Profile] for… |
| 2026-11-17 06:38:35 | [AutoRegisterDependency.Extension.EventBus](https://www.nuget.org/packages/AutoRegisterDependency.Extension.EventBus) | 1.0.0 | tengfei8771 | In-process event bus for AutoRegisterDependency. Publish/subscribe with auto-di… |
| 2026-11-17 06:38:37 | [AutoRegisterDependency.Extension.AggregateService](https://www.nuget.org/packages/AutoRegisterDependency.Extension.AggregateService) | 1.0.0 | tengfei8771 | Aggregate several registered services behind one interface for AutoRegisterDepe… |
| 2026-11-17 06:38:40 | [AutoRegisterDependency.Extension.Transactional](https://www.nuget.org/packages/AutoRegisterDependency.Extension.Transactional) | 1.0.0 | tengfei8771 | Declarative transactions for AutoRegisterDependency. Mark a class or method wit… |
| 2026-11-17 06:38:42 | [AutoRegisterDependency.Extension.Quartz3](https://www.nuget.org/packages/AutoRegisterDependency.Extension.Quartz3) | 1.0.0 | tengfei8771 | Quartz.NET 3.x scheduling for AutoRegisterDependency, targeting netstandard2.0… |
| 2026-11-17 06:38:45 | [AutoRegisterDependency.Extension.Quartz4](https://www.nuget.org/packages/AutoRegisterDependency.Extension.Quartz4) | 1.0.0 | tengfei8771 | Quartz.NET 4.x scheduling for AutoRegisterDependency, targeting net10.0 — the o… |
| 2026-11-17 06:49:08 | [Vedhaai.MCPWatch](https://www.nuget.org/packages/Vedhaai.MCPWatch) | 0.1.0 | vedhaai | MCPWatch security guard for MCP servers written in C# or VB.NET, on .NET Framew… |
| 2026-11-17 06:51:10 | [Haukcode.Rdm](https://www.nuget.org/packages/Haukcode.Rdm) | 6.0.152 | Hakan Lindestaf | Transport-independent ANSI E1.20 RDM library for .NET (.NET8+): packet building… |
| 2026-11-17 06:55:10 | [UvA.GLASS.Analyzers](https://www.nuget.org/packages/UvA.GLASS.Analyzers) | 0.1.0 | UvA.GLASS.Analyzers | Package Description |
| 2026-11-17 07:10:02 | [LCS.BuildTools](https://www.nuget.org/packages/LCS.BuildTools) | 26.11.10 | McHarnyPEP | Dotnet tool for various build tasks |
| 2026-11-17 07:10:10 | [Transmitly.Client](https://www.nuget.org/packages/Transmitly.Client) | 1.0.0 | Swift Nodes LLC | Dependency-free .NET client for the Transmitly email API |
| 2026-11-17 07:12:05 | [AiraysSdk](https://www.nuget.org/packages/AiraysSdk) | 1.0.1 | R. Tuğrul Altın | Airays Ticket Hotel API SDK for external integrations. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

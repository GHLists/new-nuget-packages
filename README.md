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

## Latest list — 2026-11-08 14:21 UTC

New packages created between 2026-11-08 13:19 UTC and 2026-11-08 14:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-08T14-21-25-159804Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-08 13:44:15 | [EventFlux.Saga](https://www.nuget.org/packages/EventFlux.Saga) | 1.0.0 | kadirkdr | Lightweight, free saga/process-manager pattern for EventFlux: in-process-first… |
| 2026-11-08 13:44:34 | [EventFlux.Saga.Generators](https://www.nuget.org/packages/EventFlux.Saga.Generators) | 1.0.0 | kadirkdr | Compile-time saga state generation for EventFlux.Saga: turns a [SagaStateSet] e… |
| 2026-11-08 13:44:53 | [EventFlux.Saga.Testing](https://www.nuget.org/packages/EventFlux.Saga.Testing) | 1.0.0 | kadirkdr | Given/When/Then test harness for EventFlux.Saga: unit-test saga state machines… |
| 2026-11-08 13:45:07 | [EventFlux.Saga.EfCore](https://www.nuget.org/packages/EventFlux.Saga.EfCore) | 1.0.0 | kadirkdr | Entity Framework Core persistence for EventFlux.Saga, built on EfCore.Repositor… |
| 2026-11-08 13:45:23 | [EventFlux.Saga.Inspector.EfCore](https://www.nuget.org/packages/EventFlux.Saga.Inspector.EfCore) | 1.0.0 | kadirkdr | Durable Entity Framework Core timeline store for the EventFlux.Saga inspector,… |
| 2026-11-08 13:45:39 | [EventFlux.Saga.RabbitFlow](https://www.nuget.org/packages/EventFlux.Saga.RabbitFlow) | 1.0.0 | kadirkdr | RabbitMQ transport adapter for EventFlux.Saga on top of EventFlux.RabbitFlow: s… |
| 2026-11-08 13:45:57 | [EventFlux.Saga.RedisFlow](https://www.nuget.org/packages/EventFlux.Saga.RedisFlow) | 1.0.0 | kadirkdr | Redis Streams transport adapter for EventFlux.Saga on top of EventFlux.RedisFlo… |
| 2026-11-08 14:01:13 | [EventFlux.Saga.Inspector](https://www.nuget.org/packages/EventFlux.Saga.Inspector) | 1.0.0 | kadirkdr | Built-in observability for EventFlux.Saga: records every saga transition in a t… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

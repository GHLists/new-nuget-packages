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

## Latest list — 2026-11-08 03:20 UTC

New packages created between 2026-11-08 02:21 UTC and 2026-11-08 03:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-08T03-20-28-87117Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-08 02:26:43 | [SankhyaAPI.Client.Testing](https://www.nuget.org/packages/SankhyaAPI.Client.Testing) | 6.0.0 | samueldias21 | Servidor fake do Sankhya (WireMock) e utilitários de teste para integrações com… |
| 2026-11-08 02:41:30 | [DbTest.MSTest](https://www.nuget.org/packages/DbTest.MSTest) | 0.2.0 | dbaitest | MSTest integration for DbTest: a base class that shares one container per engin… |
| 2026-11-08 02:53:24 | [T.Molodoy.SharpExtensions.R3](https://www.nuget.org/packages/T.Molodoy.SharpExtensions.R3) | 0.0.1 | T. Molodoy | RxJava-style Single and Completable types and extension operators for R3, with… |
| 2026-11-08 03:11:38 | [Signingflow](https://www.nuget.org/packages/Signingflow) | 0.1.0 | Signingflow | Signingflow API client for sending a document, reading envelope status, and ver… |
| 2026-11-08 03:14:25 | [RealtimeStack.Plugins.Logging](https://www.nuget.org/packages/RealtimeStack.Plugins.Logging) | 2.0.3-beta | RealtimeStack Contributors | Shared provider-neutral error handling and registration for RealtimeStack loggi… |
| 2026-11-08 03:14:26 | [RealtimeStack.Plugins.Bugsnag](https://www.nuget.org/packages/RealtimeStack.Plugins.Bugsnag) | 2.0.3-beta | RealtimeStack Contributors | Bugsnag error reporting adapter for RealtimeStack.Plugins.Logging. |
| 2026-11-08 03:14:27 | [RealtimeStack.Plugins.Serilog](https://www.nuget.org/packages/RealtimeStack.Plugins.Serilog) | 2.0.3-beta | RealtimeStack Contributors | Serilog error reporting adapter for RealtimeStack.Plugins.Logging. |
| 2026-11-08 03:14:29 | [RealtimeStack.Plugins.Log4net](https://www.nuget.org/packages/RealtimeStack.Plugins.Log4net) | 2.0.3-beta | RealtimeStack Contributors | Log4net error reporting adapter for RealtimeStack.Plugins.Logging. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

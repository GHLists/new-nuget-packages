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

## Latest list — 2026-10-15 12:19 UTC

New packages created between 2026-10-15 11:20 UTC and 2026-10-15 12:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-15T12-19-42-100572Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-15 11:21:54 | [Sipral.Maui](https://www.nuget.org/packages/Sipral.Maui) | 1.2.0 | Sytek | Sipral - Session Initiation Protocol Rust Audio Layer. The .NET binding for .NE… |
| 2026-10-15 11:23:19 | [Minos.NET.DependencyInjection](https://www.nuget.org/packages/Minos.NET.DependencyInjection) | 1.0.1 | Marcel Roozekrans | Registers Minos.NET's IDecisionClient in a .NET host, as a default client or as… |
| 2026-10-15 11:23:20 | [Minos.NET.Caching](https://www.nuget.org/packages/Minos.NET.Caching) | 1.0.1 | Marcel Roozekrans | A caching stage for Minos.NET's decision client pipeline: a repeated question s… |
| 2026-10-15 11:23:21 | [Minos.NET.OpenAI](https://www.nuget.org/packages/Minos.NET.OpenAI) | 1.0.1 | Marcel Roozekrans | OpenAI's Decisions API, POST /v1/decisions, for Minos.NET's IDecisionClient: GP… |
| 2026-10-15 11:23:21 | [Minos.NET](https://www.nuget.org/packages/Minos.NET) | 1.0.1 | Marcel Roozekrans | Typed, source-generated decision questions for .NET, provider-neutral: the ques… |
| 2026-10-15 11:23:22 | [Minos.NET.RateLimiting](https://www.nuget.org/packages/Minos.NET.RateLimiting) | 1.0.1 | Marcel Roozekrans | A rate-limiting stage for Minos.NET's decision client pipeline, over System.Thr… |
| 2026-10-15 11:23:22 | [Minos.NET.SystemOne](https://www.nuget.org/packages/Minos.NET.SystemOne) | 1.0.1 | Marcel Roozekrans | The /v1/systemone protocol for Minos.NET: TypeSafe's Jev API, OpenRouter, vLLM… |
| 2026-10-15 11:37:13 | [Sendway.Client](https://www.nuget.org/packages/Sendway.Client) | 0.1.0 | iyulab | Client for Sendway: send email, SMS and app push, read a message's outcome with… |
| 2026-10-15 11:45:27 | [AppWeaver.GuardClauses](https://www.nuget.org/packages/AppWeaver.GuardClauses) | 1.0.0 | Team AppWeaver | Domain-focused guard clauses for AppWeaver. Provides static validation methods… |
| 2026-10-15 11:50:42 | [Integrious.Umbraco.SaneDatabaseAvailabilityCheck](https://www.nuget.org/packages/Integrious.Umbraco.SaneDatabaseAvailabilityCheck) | 1.0.0 | Integrious | Replaces Umbraco's default boot-time database availability check, which gives u… |
| 2026-10-15 11:55:48 | [Laraue.Apps.Feedback.Internal.Contracts](https://www.nuget.org/packages/Laraue.Apps.Feedback.Internal.Contracts) | 0.0.1 | Belyansky Ilya | Package Description |
| 2026-10-15 11:57:07 | [DbApimaticSDK](https://www.nuget.org/packages/DbApimaticSDK) | 0.0.1 | Muhammad Rafay | Sample SDKs for DB by APIMatic |
| 2026-10-15 12:04:13 | [DropbApimaticSDK](https://www.nuget.org/packages/DropbApimaticSDK) | 0.0.2 | Muhammad Rafay | Sample SDKs for DB by APIMatic |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

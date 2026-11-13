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

## Latest list — 2026-11-13 20:21 UTC

New packages created between 2026-11-13 19:21 UTC and 2026-11-13 20:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-13T20-21-23-829117Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-13 19:32:12 | [AuthCallout.Core](https://www.nuget.org/packages/AuthCallout.Core) | 0.1.3 | Ryan Anthony | Decision core of nats-auth-callout-service: claims access, claim matching and g… |
| 2026-11-13 19:32:12 | [AuthCallout.Contracts](https://www.nuget.org/packages/AuthCallout.Contracts) | 0.1.3 | Ryan Anthony | Shared contracts for nats-auth-callout-service: AppSlug KV bucket, key and scop… |
| 2026-11-13 19:32:13 | [AuthCallout.Identity](https://www.nuget.org/packages/AuthCallout.Identity) | 0.1.3 | Ryan Anthony | Identity primitives for nats-auth-callout-service: verify the signed Callout-Id… |
| 2026-11-13 19:32:59 | [Sigill.Sdk.Policy](https://www.nuget.org/packages/Sigill.Sdk.Policy) | 0.14.0 | Sigill | The official Cedar policy core (cedar-policy 4.14.0) as one pinned WebAssembly… |
| 2026-11-13 19:47:14 | [IntentSharp.Specialist](https://www.nuget.org/packages/IntentSharp.Specialist) | 1.1.0 | C2Consultants LLC | Models defined per intent for C# and .NET, so one application can use several m… |
| 2026-11-13 19:52:39 | [TechTeaStudio.Mcp](https://www.nuget.org/packages/TechTeaStudio.Mcp) | 0.1.0 | Ronald Ryan | Studio conventions for Model Context Protocol servers built on the official C#… |
| 2026-11-13 19:52:41 | [TechTeaStudio.Mcp.Testing](https://www.nuget.org/packages/TechTeaStudio.Mcp.Testing) | 0.1.0 | Ronald Ryan | Contract checks for Model Context Protocol servers, run from any test framework… |
| 2026-11-13 20:03:14 | [VNS.Harbor](https://www.nuget.org/packages/VNS.Harbor) | 18.0.0 | VNS | VNS Harbor in Umbraco: log in from the Harbor admin, and sync settings and data… |
| 2026-11-13 20:09:58 | [VersionFlow.Core](https://www.nuget.org/packages/VersionFlow.Core) | 1.0.0 | Bradley Ables | Strongly typed configuration-driven service and method version routing. |
| 2026-11-13 20:10:21 | [VersionFlow.Extensions.Cqrs](https://www.nuget.org/packages/VersionFlow.Extensions.Cqrs) | 1.0.0 | Bradley Ables | Dependency-free typed CQRS handler contracts for direct application operations. |
| 2026-11-13 20:10:43 | [VersionFlow.Extensions.DI](https://www.nuget.org/packages/VersionFlow.Extensions.DI) | 1.0.0 | Bradley Ables | Attribute-based Microsoft DI registration with native ServiceLifetime support. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

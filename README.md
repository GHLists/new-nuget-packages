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

## Latest list — 2026-10-17 12:20 UTC

New packages created between 2026-10-17 11:19 UTC and 2026-10-17 12:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-17T12-20-30-857359Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-17 11:24:54 | [aweXpect.Xml](https://www.nuget.org/packages/aweXpect.Xml) | 0.1.1 | aweXpect | Expectations for XML for aweXpect. |
| 2026-10-17 11:25:57 | [Vericairn.Daemon](https://www.nuget.org/packages/Vericairn.Daemon) | 0.7.1 | Jason Furr | The Vericairn daemon host: one process owns one open estate and serves the vers… |
| 2026-10-17 11:25:58 | [Vericairn.Mcp](https://www.nuget.org/packages/Vericairn.Mcp) | 0.7.1 | Jason Furr | A Model Context Protocol server over the Vericairn API: a client adapter that e… |
| 2026-10-17 11:25:59 | [Vericairn.Protocol](https://www.nuget.org/packages/Vericairn.Protocol) | 0.7.1 | Jason Furr | The versioned Vericairn API contract: operations, requests, responses, state la… |
| 2026-10-17 11:26:00 | [Vericairn.Records](https://www.nuget.org/packages/Vericairn.Records) | 0.7.1 | Jason Furr | Vericairn record format: canonical JSON, identifiers, hashing, validation and e… |
| 2026-10-17 11:26:01 | [Vericairn.Runtime](https://www.nuget.org/packages/Vericairn.Runtime) | 0.7.1 | Jason Furr | Vericairn runtime: the live store, content-addressed objects, storage profiles,… |
| 2026-10-17 11:26:02 | [Vericairn.Sdk](https://www.nuget.org/packages/Vericairn.Sdk) | 0.7.1 | Jason Furr | The typed client of the Vericairn API over a local socket, a named pipe or pinn… |
| 2026-10-17 11:32:40 | [SyntaxCircus.Maui.AgeAssurance](https://www.nuget.org/packages/SyntaxCircus.Maui.AgeAssurance) | 0.1.0 | Syntax Circus LLC | Platform age signals for MAUI apps on iOS (Apple Declared Age Range) and Androi… |
| 2026-10-17 11:38:01 | [LMSupply.Decider](https://www.nuget.org/packages/LMSupply.Decider) | 0.125.0 | iyulab | Typed decisions for .NET from a local model: give a state and named questions (… |
| 2026-10-17 11:42:47 | [RoarUI](https://www.nuget.org/packages/RoarUI) | 1.0.0 | Blazor School | RoarUI is a Blazor component library for .NET 10 built on WebAwesome, with stro… |
| 2026-10-17 11:46:14 | [aweXpect.Logging](https://www.nuget.org/packages/aweXpect.Logging) | 0.1.1 | aweXpect | Expectations for logging with Microsoft.Extensions.Logging for aweXpect. |
| 2026-10-17 11:54:21 | [JamesTryand.DotnetCqrs.Retention](https://www.nuget.org/packages/JamesTryand.DotnetCqrs.Retention) | 0.31.0 | James Tryand | Governed erasure for dotnetcqrs, opt-in: a request to erase a data subject is h… |
| 2026-10-17 11:54:30 | [SharpDeps.Cli](https://www.nuget.org/packages/SharpDeps.Cli) | 0.2.0 | SharpDeps.Cli | Explicit trusted indexing and saved graph queries for SharpDeps. |
| 2026-10-17 11:54:31 | [SharpDeps.Mcp](https://www.nuget.org/packages/SharpDeps.Mcp) | 0.2.0 | SharpDeps.Mcp | Optional stdio adapter for SharpDeps saved Query and explicitly trusted updates. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

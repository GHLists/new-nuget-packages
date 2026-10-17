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

## Latest list — 2026-10-17 01:19 UTC

New packages created between 2026-10-17 00:20 UTC and 2026-10-17 01:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-17T01-19-25-084583Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-17 00:57:17 | [Tharga.Team.Email](https://www.nuget.org/packages/Tharga.Team.Email) | 3.29.0 | Daniel Bohlin | E-mail for Tharga Team — reading over IMAP, sending over SMTP and MIME handling… |
| 2026-10-17 00:58:52 | [Snail.Sdk](https://www.nuget.org/packages/Snail.Sdk) | 0.1.0 | orldev | The base MSBuild SDK of every Snail library and server: the build rules, the an… |
| 2026-10-17 00:58:53 | [Snail.Sdk.Analyzers](https://www.nuget.org/packages/Snail.Sdk.Analyzers) | 0.1.0 | orldev | The owner's code rules as Roslyn analyzers: unpack long LINQ chains, create bef… |
| 2026-10-17 00:58:54 | [Snail.Sdk.Library](https://www.nuget.org/packages/Snail.Sdk.Library) | 0.1.0 | orldev | The MSBuild SDK of a Snail library: Snail.Sdk, plus the public API kept in Publ… |
| 2026-10-17 00:58:56 | [Snail.Sdk.Mcp](https://www.nuget.org/packages/Snail.Sdk.Mcp) | 0.1.0 | orldev | The MSBuild SDK of a Snail MCP server: Snail.Sdk, plus a dotnet tool of the Mcp… |
| 2026-10-17 00:58:57 | [Snail.Sdk.Mcp.Hosting](https://www.nuget.org/packages/Snail.Sdk.Mcp.Hosting) | 0.1.0 | orldev | What every Snail MCP server starts from: the empty host with log lines on stder… |
| 2026-10-17 00:58:58 | [Snail.Sdk.Mcp.Http](https://www.nuget.org/packages/Snail.Sdk.Mcp.Http) | 0.1.0 | orldev | One Snail MCP server for every session of the machine: the empty web host on a… |
| 2026-10-17 00:59:00 | [Snail.Sdk.Mcp.Testing](https://www.nuget.org/packages/Snail.Sdk.Mcp.Testing) | 0.1.0 | orldev | Starts a Snail MCP server under test the way a client starts it — the dll besid… |
| 2026-10-17 00:59:01 | [Snail.Sdk.Templates](https://www.nuget.org/packages/Snail.Sdk.Templates) | 0.1.0 | orldev | The templates of a Snail library (dotnet new s3l-lib) and a Snail MCP server (d… |
| 2026-10-17 01:08:30 | [EmberLlm](https://www.nuget.org/packages/EmberLlm) | 0.1.0 | Michael Smith | A .NET client for local LLM servers (LM Studio, Ollama, llama.cpp, vLLM), built… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

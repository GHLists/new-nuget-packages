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

## Latest list — 2026-11-19 01:19 UTC

New packages created between 2026-11-19 00:20 UTC and 2026-11-19 01:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-19T01-19-21-049965Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-19 00:30:39 | [Vercuski.Vertical_Slice-Clean_Architecture.Templates](https://www.nuget.org/packages/Vercuski.Vertical_Slice-Clean_Architecture.Templates) | 1.1.1 | Scott Vercuski | A .NET 10 Minimal API solution template that organizes features as vertical sli… |
| 2026-11-19 00:41:33 | [Okta.OAuth2](https://www.nuget.org/packages/Okta.OAuth2) | 0.2.0 | Okta | OAuth2 and OIDC authentication flows for the Okta .NET SDK: Authorization Code… |
| 2026-11-19 00:48:53 | [MyGeminiWebMcp.linux-x64](https://www.nuget.org/packages/MyGeminiWebMcp.linux-x64) | 0.1.0-beta | kimvi | MCP server for Gemini Web: multi-account pool with automatic failover, conversa… |
| 2026-11-19 00:48:55 | [MyGeminiWebMcp.osx-arm64](https://www.nuget.org/packages/MyGeminiWebMcp.osx-arm64) | 0.1.0-beta | kimvi | MCP server for Gemini Web: multi-account pool with automatic failover, conversa… |
| 2026-11-19 00:48:57 | [MyGeminiWebMcp.win-x64](https://www.nuget.org/packages/MyGeminiWebMcp.win-x64) | 0.1.0-beta | kimvi | MCP server for Gemini Web: multi-account pool with automatic failover, conversa… |
| 2026-11-19 00:50:28 | [MyGeminiWebMcp](https://www.nuget.org/packages/MyGeminiWebMcp) | 0.1.0-beta | kimvi | MCP server for Gemini Web: multi-account pool with automatic failover, conversa… |
| 2026-11-19 00:51:34 | [BinkyLabs.OpenApi.Arazzo.Tool](https://www.nuget.org/packages/BinkyLabs.OpenApi.Arazzo.Tool) | 1.0.0 | BinkyLabs | OpenAPI Arazzo CLI - Validate Arazzo documents |
| 2026-11-19 00:51:35 | [BinkyLabs.OpenApi.Arazzo](https://www.nuget.org/packages/BinkyLabs.OpenApi.Arazzo) | 1.0.0 | BinkyLabs | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

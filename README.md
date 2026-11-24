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

## Latest list — 2026-11-24 17:19 UTC

New packages created between 2026-11-24 16:19 UTC and 2026-11-24 17:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-24T17-19-46-444841Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-24 16:23:03 | [Skarp.win-x64](https://www.nuget.org/packages/Skarp.win-x64) | 0.1.0 | Sir Phillip Tubell | skarp: C# code health metrics (cyclomatic, cognitive, NPath, nesting, lines, st… |
| 2026-11-24 16:23:06 | [Skarp.linux-x64](https://www.nuget.org/packages/Skarp.linux-x64) | 0.1.0 | Sir Phillip Tubell | skarp: C# code health metrics (cyclomatic, cognitive, NPath, nesting, lines, st… |
| 2026-11-24 16:23:08 | [Skarp.any](https://www.nuget.org/packages/Skarp.any) | 0.1.0 | Sir Phillip Tubell | skarp: C# code health metrics (cyclomatic, cognitive, NPath, nesting, lines, st… |
| 2026-11-24 16:23:09 | [Skarp](https://www.nuget.org/packages/Skarp) | 0.1.0 | Sir Phillip Tubell | skarp: C# code health metrics (cyclomatic, cognitive, NPath, nesting, lines, st… |
| 2026-11-24 16:36:31 | [Styml](https://www.nuget.org/packages/Styml) | 0.1.0 | Sébastien Ros | The System.Text.Json API, for YAML. A YAML 1.2 reader, writer, document model a… |
| 2026-11-24 17:07:03 | [AiProxy.Mcp.Sdk](https://www.nuget.org/packages/AiProxy.Mcp.Sdk) | 1.0.0 | Aurora | MCP SDK: message_signed transport authentication — ES256 request signer for cli… |
| 2026-11-24 17:07:04 | [AiProxy.Mcp.Sdk.AspNetCore](https://www.nuget.org/packages/AiProxy.Mcp.Sdk.AspNetCore) | 1.0.0 | Aurora | ASP.NET Core middleware for message_signed MCP endpoints: verifies Mcp-Message-… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

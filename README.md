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

## Latest list — 2026-10-07 00:20 UTC

New packages created between 2026-10-06 23:21 UTC and 2026-10-07 00:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-07T00-20-47-650314Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-06 23:25:37 | [Vestigium.Helpers.LogParser.Har](https://www.nuget.org/packages/Vestigium.Helpers.LogParser.Har) | 1.0.0 | Vestigium.Helpers.LogParser.H… | Package Description |
| 2026-10-06 23:27:18 | [NGB.Platform.Attachments](https://www.nuget.org/packages/NGB.Platform.Attachments) | 3.1.0 | NGB Platform | NGB Platform Attachments capability. |
| 2026-10-06 23:27:19 | [NGB.Platform.Notes](https://www.nuget.org/packages/NGB.Platform.Notes) | 3.1.0 | NGB Platform | NGB Platform Notes capability. |
| 2026-10-06 23:27:20 | [NGB.Platform.Attachments.MinIO](https://www.nuget.org/packages/NGB.Platform.Attachments.MinIO) | 3.1.0 | NGB Platform | NGB Platform Attachments.MinIO capability. |
| 2026-10-06 23:43:23 | [Salt.Api](https://www.nuget.org/packages/Salt.Api) | 1.0.10 | Panoramic Data Limited | A typed, read-only-by-option .NET client for the Salt Project REST API (rest_ch… |
| 2026-10-06 23:43:25 | [CSharpEssentials.AspNetCore.OpenApi](https://www.nuget.org/packages/CSharpEssentials.AspNetCore.OpenApi) | 5.0.0 | senrecep | Microsoft.AspNetCore.OpenApi integration for the CSharpEssentials enum conventi… |
| 2026-10-06 23:43:27 | [CSharpEssentials.AspNetCore.Swashbuckle](https://www.nuget.org/packages/CSharpEssentials.AspNetCore.Swashbuckle) | 5.0.0 | senrecep | Swashbuckle (Swagger) integration for CSharpEssentials.AspNetCore: versioned Sw… |
| 2026-10-06 23:43:40 | [Vestigium.Helpers.LogParser.Url](https://www.nuget.org/packages/Vestigium.Helpers.LogParser.Url) | 1.0.0 | Vestigium.Helpers.LogParser.U… | Package Description |
| 2026-10-06 23:45:12 | [Microsoft.CopyOnWrite](https://www.nuget.org/packages/Microsoft.CopyOnWrite) | 0.5.1 | Microsoft | A .NET library that encapsulates OS and filesystem differences for creating Cop… |
| 2026-10-06 23:50:33 | [Ten99.Aria.Mcp.Ado](https://www.nuget.org/packages/Ten99.Aria.Mcp.Ado) | 1.0.693 | 1099 Ventures Inc | ARIA's native C# Azure DevOps MCP server — multi-org, lean responses, registry-… |
| 2026-10-06 23:50:34 | [Ten99.Aria.Mcp.Codecks](https://www.nuget.org/packages/Ten99.Aria.Mcp.Codecks) | 1.0.693 | 1099 Ventures Inc | Model Context Protocol (MCP) server for Codecks project management: cards, deck… |
| 2026-10-06 23:50:36 | [Ten99.Aria.Mcp.Email.Imap](https://www.nuget.org/packages/Ten99.Aria.Mcp.Email.Imap) | 1.0.693 | 1099 Ventures Inc | ARIA's IMAP/SMTP (MailKit) email MCP server — read/filter/triage a mailbox over… |
| 2026-10-06 23:50:38 | [Ten99.Aria.Mcp.Email.O365](https://www.nuget.org/packages/Ten99.Aria.Mcp.Email.O365) | 1.0.693 | 1099 Ventures Inc | ARIA's Microsoft 365 (Outlook/Graph) email MCP server — read/filter/triage a ma… |
| 2026-10-06 23:50:41 | [Ten99.Aria.Mcp.LocalFiles](https://www.nuget.org/packages/Ten99.Aria.Mcp.LocalFiles) | 1.0.693 | 1099 Ventures Inc | Model Context Protocol (MCP) server for local filesystem operations: read, writ… |
| 2026-10-06 23:50:42 | [Ten99.Aria.Common](https://www.nuget.org/packages/Ten99.Aria.Common) | 1.0.693 | 1099 Ventures Inc | Dependency-light generic primitives shared by the ARIA projects and MCP servers… |
| 2026-10-06 23:50:44 | [Ten99.Aria.Hosting.Mcp.Core](https://www.nuget.org/packages/Ten99.Aria.Hosting.Mcp.Core) | 1.0.693 | 1099 Ventures Inc | Reusable host for running a Model Context Protocol (MCP) server over stdio: a o… |
| 2026-10-07 00:06:34 | [Ilmek.Skills](https://www.nuget.org/packages/Ilmek.Skills) | 0.1.0 | AimTune | Agent Skills for ilmek — load SKILL.md folders, expose them to a model with pro… |
| 2026-10-07 00:06:36 | [Ilmek.Mcp](https://www.nuget.org/packages/Ilmek.Mcp) | 0.1.0 | AimTune | MCP for ilmek — consume Model Context Protocol servers as replay-safe tools, re… |
| 2026-10-07 00:06:37 | [Ilmek.A2A](https://www.nuget.org/packages/Ilmek.A2A) | 0.1.0 | AimTune | A2A for ilmek — call Agent2Agent agents from a graph, replay-safe, with human-i… |
| 2026-10-07 00:06:44 | [ElephantSqlDb.Data](https://www.nuget.org/packages/ElephantSqlDb.Data) | 1.0.189 | ElephantSqlDB, Inc: DevOps | Client API needed to interact with the ElephantSqlDB cloud database storage ser… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

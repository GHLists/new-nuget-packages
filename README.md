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

## Latest list — 2026-10-04 03:21 UTC

New packages created between 2026-10-04 02:21 UTC and 2026-10-04 03:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-04T03-21-24-351087Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-04 02:34:09 | [Authio.Client](https://www.nuget.org/packages/Authio.Client) | 0.1.0 | Leonardo Almeida | The Authio client for .NET without any ASP.NET Core dependency: discovery, ever… |
| 2026-10-04 02:34:47 | [Authio.AspNetCore](https://www.nuget.org/packages/Authio.AspNetCore) | 0.1.0 | Leonardo Almeida | Protect an ASP.NET Core API with Authio: JWT bearer validation from the realm's… |
| 2026-10-04 02:35:09 | [Authio.AspNetCore.Bff](https://www.nuget.org/packages/Authio.AspNetCore.Bff) | 0.1.0 | Leonardo Almeida | Backend-for-Frontend for Authio: lets a browser SPA (React, Angular, Vue...) si… |
| 2026-10-04 02:35:31 | [Authio.Mcp.AspNetCore](https://www.nuget.org/packages/Authio.Mcp.AspNetCore) | 0.1.0 | Leonardo Almeida | Protects an ASP.NET Core MCP server (OAuth 2.1 resource server) with Authio: JW… |
| 2026-10-04 02:58:15 | [Soenneker.Devto.HttpClients](https://www.nuget.org/packages/Soenneker.Devto.HttpClients) | 4.0.1 | Jake Soenneker | A thread-safe singleton HttpClient for Devto's OpenAPI integration. |
| 2026-10-04 02:58:52 | [Soenneker.Devto.OpenApiClient](https://www.nuget.org/packages/Soenneker.Devto.OpenApiClient) | 4.0.1 | Jake Soenneker | A generated OpenAPI client for DEV.to. |
| 2026-10-04 03:04:32 | [Soenneker.Devto.OpenApiClientUtil](https://www.nuget.org/packages/Soenneker.Devto.OpenApiClientUtil) | 4.0.1 | Jake Soenneker | A thread-safe utility for obtaining Devto's OpenApiClient singleton. |
| 2026-10-04 03:09:49 | [Meziantou.Framework.NodeJs](https://www.nuget.org/packages/Meziantou.Framework.NodeJs) | 1.0.0 | meziantou | Run JavaScript and call Node.js modules (local files or npm packages) from .NET… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

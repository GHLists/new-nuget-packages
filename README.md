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

## Latest list — 2026-10-26 07:19 UTC

New packages created between 2026-10-26 06:21 UTC and 2026-10-26 07:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-26T07-19-58-492184Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-26 06:32:40 | [dotnet-fdg](https://www.nuget.org/packages/dotnet-fdg) | 0.1.0 | tianvan | Applies the Framework Design Guidelines analyzers' automatic fixes to C# projec… |
| 2026-10-26 06:32:41 | [FrameworkDesignGuidelines.Analyzers](https://www.nuget.org/packages/FrameworkDesignGuidelines.Analyzers) | 0.1.0 | tianvan | Roslyn analyzers and per-profile analyzer configuration distilled from Framewor… |
| 2026-10-26 06:59:10 | [BusinessCentralDeploymentTool](https://www.nuget.org/packages/BusinessCentralDeploymentTool) | 1.0.0 | Maksym Kravchenko | Local MCP server that deploys Business Central per-tenant extensions, inspects… |
| 2026-10-26 07:02:56 | [Dotnetstore.Security.Tool](https://www.nuget.org/packages/Dotnetstore.Security.Tool) | 1.0.0 | Hans Sjödin | Command-line tool that generates keys and secrets for Dotnetstore.Security and… |
| 2026-10-26 07:02:56 | [Dotnetstore.Security](https://www.nuget.org/packages/Dotnetstore.Security) | 1.0.0 | Hans Sjödin | Common functions to secure the app |
| 2026-10-26 07:02:57 | [Dotnetstore.Security.AspNetCore](https://www.nuget.org/packages/Dotnetstore.Security.AspNetCore) | 1.0.0 | Hans Sjödin | ASP.NET Core JWT bearer authentication for Dotnetstore.Security |
| 2026-10-26 07:11:05 | [Workhorse](https://www.nuget.org/packages/Workhorse) | 0.10.0 | Stablemates | The Workhorse client and worker for .NET: a durable task queue on PostgreSQL. |
| 2026-10-26 07:11:06 | [Workhorse.Hosting](https://www.nuget.org/packages/Workhorse.Hosting) | 0.10.0 | Stablemates | Dependency injection, options, the hosted worker, and health checks for Workhor… |
| 2026-10-26 07:11:07 | [Workhorse.EntityFrameworkCore](https://www.nuget.org/packages/Workhorse.EntityFrameworkCore) | 0.10.0 | Stablemates | Gives Workhorse the Npgsql connection and the transaction of an EF Core DbConte… |
| 2026-10-26 07:11:08 | [Workhorse.AspNetCore](https://www.nuget.org/packages/Workhorse.AspNetCore) | 0.10.0 | Stablemates | The embedded Workhorse dashboard backend for ASP.NET Core. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

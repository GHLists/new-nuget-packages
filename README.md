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

## Latest list — 2026-10-24 11:21 UTC

New packages created between 2026-10-24 10:21 UTC and 2026-10-24 11:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-24T11-21-55-053645Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-24 10:33:08 | [Snk.Net.Forms](https://www.nuget.org/packages/Snk.Net.Forms) | 10.4.0 | SNK | SNK .NET Forms - a UI-free form engine: versioned JSON form definitions, condit… |
| 2026-10-24 10:33:22 | [Snk.Net.Server](https://www.nuget.org/packages/Snk.Net.Server) | 10.4.0 | SNK | SNK .NET Server Library |
| 2026-10-24 10:40:06 | [Mentis.AI.Contracts](https://www.nuget.org/packages/Mentis.AI.Contracts) | 1.0.0 | Mentis.AI Contributors | gRPC contract (proto files and generated C# client/server stubs) of the Mentis.… |
| 2026-10-24 10:52:49 | [SjolystInnovation.AppKit.Consent](https://www.nuget.org/packages/SjolystInnovation.AppKit.Consent) | 1.0.0 | Sjølyst Innovation AS | A pseudonymous, append-only log of the cookie consent choices a site's banner s… |
| 2026-10-24 10:57:45 | [EfMigrationPack.Cli](https://www.nuget.org/packages/EfMigrationPack.Cli) | 1.0.3 | Paul Oliver | Command-line tool for packing EF Core migrations: "dotnet ef-pack pack" packs m… |
| 2026-10-24 11:12:32 | [ThinkBase.AI.MPP](https://www.nuget.org/packages/ThinkBase.AI.MPP) | 1.0.2 | ThinkBase.AI | The server side of the Machine Payments Protocol (MPP) for ASP.NET Core MCP ser… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

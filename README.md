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

## Latest list — 2026-11-01 19:21 UTC

New packages created between 2026-11-01 18:18 UTC and 2026-11-01 19:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-01T19-21-21-654272Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-01 18:32:17 | [G4.WebDriver.Remote.Sap](https://www.nuget.org/packages/G4.WebDriver.Remote.Sap) | 2026.11.1.14 | G4™ API Community | The G4.WebDriver.Remote.Sap package is the client for the SAP GUI WebDriver ser… |
| 2026-11-01 18:32:45 | [Labcoat.Vitest](https://www.nuget.org/packages/Labcoat.Vitest) | 1.2.0 | Erik Lieben | Vitest runner for Labcoat: lists and runs the Vitest tests of your JavaScript /… |
| 2026-11-01 18:34:13 | [SyntaxCircus.Markdown](https://www.nuget.org/packages/SyntaxCircus.Markdown) | 0.1.0 | Syntax Circus LLC | Safe-by-default Markdown to HTML for user- and CMS-authored content: raw HTML d… |
| 2026-11-01 18:48:10 | [EveShipFit.DogmaEngine](https://www.nuget.org/packages/EveShipFit.DogmaEngine) | 14.0.0 | EVEShipFit Team | Library to calculate statistics for EVE Online ship fits |
| 2026-11-01 18:54:42 | [EvolvDB.CLI](https://www.nuget.org/packages/EvolvDB.CLI) | 0.1.0 | EvolvDB Team | Command-line interface tool for EvolvDB database migrations and seeding. |
| 2026-11-01 18:54:43 | [EvolvDB.PostgreSQL](https://www.nuget.org/packages/EvolvDB.PostgreSQL) | 0.1.0 | EvolvDB Team | PostgreSQL database provider for EvolvDB using Npgsql. |
| 2026-11-01 18:54:43 | [EvolvDB.SqlServer](https://www.nuget.org/packages/EvolvDB.SqlServer) | 0.1.0 | EvolvDB Team | SQL Server database provider for EvolvDB using Microsoft.Data.SqlClient. |
| 2026-11-01 18:54:44 | [EvolvDB.Core](https://www.nuget.org/packages/EvolvDB.Core) | 0.1.0 | EvolvDB Team | Core abstractions, SQL parser, and migration engine for EvolvDB. |
| 2026-11-01 18:57:02 | [Corfedo.Work.Conformance](https://www.nuget.org/packages/Corfedo.Work.Conformance) | 0.1.0 | Wojciech Wentland | Conformance suite for Corfedo Work store providers, on xUnit v3: a provider's o… |
| 2026-11-01 18:57:17 | [ManagedCode.GrokSharpSDK](https://www.nuget.org/packages/ManagedCode.GrokSharpSDK) | 1.0.70.1 | ManagedCode | CLI-first .NET SDK for the official Grok Build coding agent. |
| 2026-11-01 18:57:18 | [ManagedCode.GrokSharpSDK.Extensions.AI](https://www.nuget.org/packages/ManagedCode.GrokSharpSDK.Extensions.AI) | 1.0.70.1 | ManagedCode | Microsoft.Extensions.AI IChatClient adapter for the Grok Build agent CLI. |
| 2026-11-01 19:02:47 | [Corfedo.Work.EntityFrameworkCore](https://www.nuget.org/packages/Corfedo.Work.EntityFrameworkCore) | 0.1.0 | Wojciech Wentland | Entity Framework Core adapter for Corfedo Work: maps lease and reconciliation f… |
| 2026-11-01 19:02:48 | [Corfedo.Work](https://www.nuget.org/packages/Corfedo.Work) | 0.1.0 | Wojciech Wentland | Background jobs, cron schedules and leases for .NET that live in your database… |
| 2026-11-01 19:02:49 | [Corfedo.Work.PostgreSql](https://www.nuget.org/packages/Corfedo.Work.PostgreSql) | 0.1.0 | Wojciech Wentland | PostgreSQL store for Corfedo Work, over Npgsql: background jobs, cron schedules… |
| 2026-11-01 19:02:50 | [Corfedo.Work.InMemory](https://www.nuget.org/packages/Corfedo.Work.InMemory) | 0.1.0 | Wojciech Wentland | In-memory store provider for Corfedo Work, with a controllable clock, for tests… |
| 2026-11-01 19:08:49 | [BlazorHMR](https://www.nuget.org/packages/BlazorHMR) | 0.1.14-pre-6ad356fb | Marco van den Oever | Hot reload for Blazor WebAssembly apps that applies (almost) any change while t… |
| 2026-11-01 19:08:49 | [BlazorHMR.Photino](https://www.nuget.org/packages/BlazorHMR.Photino) | 0.1.14-pre-6ad356fb | Marco van den Oever | Package Description |
| 2026-11-01 19:08:50 | [BlazorHMR.PhotinoX](https://www.nuget.org/packages/BlazorHMR.PhotinoX) | 0.1.14-pre-6ad356fb | Marco van den Oever | Package Description |
| 2026-11-01 19:08:50 | [BlazorHMR.Protocol](https://www.nuget.org/packages/BlazorHMR.Protocol) | 0.1.14-pre-6ad356fb | Marco van den Oever | The wire protocol shared by the BlazorHMR client and server. |
| 2026-11-01 19:08:51 | [BlazorHMR.Server](https://www.nuget.org/packages/BlazorHMR.Server) | 0.1.14-pre-6ad356fb | Marco van den Oever | The server side of BlazorHMR, as a .NET tool (blazor-hmr): watches a Blazor Web… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

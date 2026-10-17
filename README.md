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

## Latest list — 2026-10-17 17:22 UTC

New packages created between 2026-10-17 16:19 UTC and 2026-10-17 17:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-17T17-22-07-618882Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-17 16:29:24 | [PictureSharp.Heif](https://www.nuget.org/packages/PictureSharp.Heif) | 0.5.0 | Artur Pelzak | HEIC/HEIF format plugin for PictureSharp, written entirely in C#. No native dep… |
| 2026-10-17 16:36:58 | [Xapi.Core](https://www.nuget.org/packages/Xapi.Core) | 0.2.0 | Nurullah Türkoğlu | Experience API (xAPI 2.0, IEEE 9274.1.1, and 1.0.3) models for .NET: strict JSO… |
| 2026-10-17 16:36:58 | [Xapi.Client](https://www.nuget.org/packages/Xapi.Client) | 0.2.0 | Nurullah Türkoğlu | Experience API (xAPI 2.0, IEEE 9274.1.1, and 1.0.3) client for .NET: Statements… |
| 2026-10-17 16:36:59 | [Xapi.Lrs.PostgreSql](https://www.nuget.org/packages/Xapi.Lrs.PostgreSql) | 0.2.0 | Nurullah Türkoğlu | PostgreSQL storage for the Xapi.Lrs Learning Record Store: UsePostgreSql(connec… |
| 2026-10-17 16:36:59 | [Xapi.Lrs.Sqlite](https://www.nuget.org/packages/Xapi.Lrs.Sqlite) | 0.2.0 | Nurullah Türkoğlu | SQLite storage for the Xapi.Lrs Learning Record Store: UseSqlite(connectionStri… |
| 2026-10-17 16:36:59 | [Xapi.Client.Outbox](https://www.nuget.org/packages/Xapi.Client.Outbox) | 0.2.0 | Nurullah Türkoğlu | Durable outbox for Experience API (xAPI 2.0 and 1.0.3) statements on top of Xap… |
| 2026-10-17 16:37:00 | [Xapi.Lrs](https://www.nuget.org/packages/Xapi.Lrs) | 0.2.0 | Nurullah Türkoğlu | An embeddable xAPI Learning Record Store (xAPI 2.0, IEEE 9274.1.1, and 1.0.3) f… |
| 2026-10-17 16:44:49 | [Starlings.Tokenizers](https://www.nuget.org/packages/Starlings.Tokenizers) | 0.3.0 | StarlingHq | Managed .NET tokenizer for Hugging Face tokenizer.json files (format 1.0): Unig… |
| 2026-10-17 16:46:07 | [SimplArchive.Cli](https://www.nuget.org/packages/SimplArchive.Cli) | 0.47.0 | saconsole | saconsole — administrative CLI for a SimplArchive installation: sign in, provis… |
| 2026-10-17 17:03:23 | [NetAmpowering.AspNet](https://www.nuget.org/packages/NetAmpowering.AspNet) | 1.0.0 | Gaetan Delpierre | Zero-config OpenTelemetry APM for classic ASP.NET (WebForms and MVC 5) on .NET… |
| 2026-10-17 17:06:07 | [NetAmpowering.AspNet.Mvc](https://www.nuget.org/packages/NetAmpowering.AspNet.Mvc) | 1.0.0 | Gaetan Delpierre | ASP.NET MVC 5 action tracing for the NetAmpowering APM. Registers a global filt… |
| 2026-10-17 17:07:58 | [NetAmpowering.AspNet.WebApi](https://www.nuget.org/packages/NetAmpowering.AspNet.WebApi) | 1.0.0 | Gaetan Delpierre | ASP.NET Web API 2 action tracing for the NetAmpowering APM (.NET Framework 4.7.… |
| 2026-10-17 17:08:39 | [NetAmpowering.AspNetCore](https://www.nuget.org/packages/NetAmpowering.AspNetCore) | 1.0.0 | Gaetan Delpierre | Codeless OpenTelemetry APM for ASP.NET Core (.NET 8) Web APIs, controllers and… |
| 2026-10-17 17:09:25 | [NetAmpowering.Coverage](https://www.nuget.org/packages/NetAmpowering.Coverage) | 1.0.0 | Gaetan Delpierre | Fody IL weaver that instruments every .NET method at compile time for productio… |
| 2026-10-17 17:09:59 | [NetAmpowering.Coverage.AspNet](https://www.nuget.org/packages/NetAmpowering.Coverage.AspNet) | 1.0.0 | Gaetan Delpierre | Starts NetAmpowering production code coverage in classic ASP.NET (.NET Framewor… |
| 2026-10-17 17:10:35 | [NetAmpowering.Coverage.Core](https://www.nuget.org/packages/NetAmpowering.Coverage.Core) | 1.0.0 | Gaetan Delpierre | Host-agnostic runtime registry for NetAmpowering production code coverage (nets… |
| 2026-10-17 17:11:10 | [NetAmpowering.Coverage.Runtime](https://www.nuget.org/packages/NetAmpowering.Coverage.Runtime) | 1.0.0 | Gaetan Delpierre | Runtime registry and OpenTelemetry/Prometheus exporter for production code cove… |
| 2026-10-17 17:11:44 | [NetAmpowering.Observability](https://www.nuget.org/packages/NetAmpowering.Observability) | 1.0.0 | Gaetan Delpierre | Codeless OpenTelemetry instrumentation for Blazor Server. Automatic tracing for… |
| 2026-10-17 17:12:33 | [NetAmpowering.Observability.Core](https://www.nuget.org/packages/NetAmpowering.Observability.Core) | 1.0.0 | Gaetan Delpierre | Host-agnostic core of the NetAmpowering APM (netstandard2.0, usable from .NET F… |
| 2026-10-17 17:13:06 | [NetAmpowering.Observability.EntityFramework6](https://www.nuget.org/packages/NetAmpowering.Observability.EntityFramework6) | 1.0.0 | Gaetan Delpierre | OpenTelemetry tracing for Entity Framework 6 (.NET Framework 4.7.2+ and .NET 8)… |
| 2026-10-17 17:13:27 | [NetAlign](https://www.nuget.org/packages/NetAlign) | 1.0.0 | NetAlign | Alignment analyzer and code fixer for dotnet format. |
| 2026-10-17 17:14:10 | [NetAmpowering.Observability.NHibernate](https://www.nuget.org/packages/NetAmpowering.Observability.NHibernate) | 1.0.0 | Gaetan Delpierre | OpenTelemetry tracing for NHibernate 5.5+ (.NET Framework 4.7.2+ and .NET 8): o… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

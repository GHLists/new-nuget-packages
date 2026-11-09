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

## Latest list — 2026-11-09 02:21 UTC

New packages created between 2026-11-09 01:21 UTC and 2026-11-09 02:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-09T02-21-15-936937Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-09 01:41:16 | [Laranet](https://www.nuget.org/packages/Laranet) | 0.1.0 | TheJavaZ | A Laravel-inspired toolkit for .NET, bringing expressive APIs, developer-friend… |
| 2026-11-09 01:41:17 | [Laranet.AspNetCore](https://www.nuget.org/packages/Laranet.AspNetCore) | 0.1.0 | TheJavaZ | ASP.NET Core integration for Laranet.Data pagination responses. |
| 2026-11-09 01:41:18 | [Laranet.Cli](https://www.nuget.org/packages/Laranet.Cli) | 0.1.0 | TheJavaZ | Command-line tool for generating Laranet application code. |
| 2026-11-09 01:41:19 | [Laranet.Data](https://www.nuget.org/packages/Laranet.Data) | 0.1.0 | TheJavaZ | Provider-neutral IQueryable search, sorting, and pagination utilities for Laran… |
| 2026-11-09 01:41:20 | [Laranet.EntityFrameworkCore](https://www.nuget.org/packages/Laranet.EntityFrameworkCore) | 0.1.0 | TheJavaZ | Entity Framework Core integration for Laranet.Data asynchronous query execution. |
| 2026-11-09 01:48:21 | [Bear.Cache](https://www.nuget.org/packages/Bear.Cache) | 1.0.1 | Ada Xiong | This Cache project includes some cache classes, help classes, etc. |
| 2026-11-09 01:56:11 | [Atalog.Sdk](https://www.nuget.org/packages/Atalog.Sdk) | 0.1.1 | Caio Gualberto | Sends errors, logs, metrics and traces from .NET apps to a self-hosted Atalog i… |
| 2026-11-09 02:03:39 | [Trax.Api.Console.Terminal](https://www.nuget.org/packages/Trax.Api.Console.Terminal) | 1.69.0 | Theauxm | trax-console, the Trax .NET operations console in a terminal: runs, dead letter… |
| 2026-11-09 02:03:40 | [Trax.StateMachine.Client](https://www.nuget.org/packages/Trax.StateMachine.Client) | 1.69.0 | Theauxm,mark-keaton | Drive a Trax state machine a host serves from .NET: Blazor, MAUI, Avalonia, WPF… |
| 2026-11-09 02:03:42 | [Trax.Client](https://www.nuget.org/packages/Trax.Client) | 1.69.0 | Theauxm,mark-keaton | Send a Trax host's persisted GraphQL documents from .NET: a document by the id… |
| 2026-11-09 02:03:44 | [Trax.StateMachine.Gherkin](https://www.nuget.org/packages/Trax.StateMachine.Gherkin) | 1.69.0 | Theauxm,mark-keaton | Derive Trax .NET state machines from Gherkin features and a glossary: each mach… |
| 2026-11-09 02:03:45 | [Trax.StateMachine.Gherkin.Reqnroll](https://www.nuget.org/packages/Trax.StateMachine.Gherkin.Reqnroll) | 1.69.0 | Theauxm,mark-keaton | Reqnroll bindings that run Trax .NET features against a host in the test proces… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

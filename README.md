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

## Latest list — 2026-10-21 23:18 UTC

New packages created between 2026-10-21 22:20 UTC and 2026-10-21 23:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-21T23-18-55-11669Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-21 22:22:53 | [rmg.UpdateClient](https://www.nuget.org/packages/rmg.UpdateClient) | 3.7.61021.1 | Jonathan Dewalt | Startup update check and updater bootstrap for rmg WPF applications that update… |
| 2026-10-21 22:24:58 | [Respire.RateLimiting](https://www.nuget.org/packages/Respire.RateLimiting) | 0.11.0 | Tom Hurst | Redis-backed named and partitioned ASP.NET Core rate limiting policies. |
| 2026-10-21 22:24:59 | [Respire.Gcp](https://www.nuget.org/packages/Respire.Gcp) | 0.11.0 | Tom Hurst | Google Cloud Memorystore IAM credential provider for Respire. |
| 2026-10-21 22:25:24 | [Respire.Templates](https://www.nuget.org/packages/Respire.Templates) | 0.11.0 | Tom Hurst | Project templates for applications using Respire and Redis. |
| 2026-10-21 22:25:36 | [Respire.Testing.StackExchangeCompat](https://www.nuget.org/packages/Respire.Testing.StackExchangeCompat) | 0.11.0 | Tom Hurst | In-memory test fixtures for the supported StackExchange.Redis compatibility sub… |
| 2026-10-21 22:50:45 | [StructuredConcurrency](https://www.nuget.org/packages/StructuredConcurrency) | 0.1.0 | Gokhan Ertogan | Structured concurrency for .NET: child tasks run inside a scope that completes… |
| 2026-10-21 22:51:41 | [Basic.Reference.Assemblies.Net481](https://www.nuget.org/packages/Basic.Reference.Assemblies.Net481) | 1.8.13 | jaredpar | This package provides reference assemblies for use with Roslyn Compilation obje… |
| 2026-10-21 22:51:58 | [Sudzekai.WebOs.Core](https://www.nuget.org/packages/Sudzekai.WebOs.Core) | 1.0.0 | Sudzekai | Sudzekai WebOS plugin core types, descriptors, and utilities. |
| 2026-10-21 22:51:58 | [Sudzekai.WebOs.Hosting](https://www.nuget.org/packages/Sudzekai.WebOs.Hosting) | 1.0.0 | Sudzekai | Sudzekai WebOS plugin host infrastructure for ASP.NET Core applications. |
| 2026-10-21 22:51:59 | [Sudzekai.WebOs.Plugin](https://www.nuget.org/packages/Sudzekai.WebOs.Plugin) | 1.0.0 | Sudzekai | Sudzekai WebOS plugin builder and SDK for creating native plugins. |
| 2026-10-21 22:56:25 | [OwlDomain.SDL3.Image.Native](https://www.nuget.org/packages/OwlDomain.SDL3.Image.Native) | 3.4.8 | OwlDomain | Native libraries for SDL3_Image. |
| 2026-10-21 23:01:45 | [SocialPoster.Posting](https://www.nuget.org/packages/SocialPoster.Posting) | 0.5.0 | Isaac Levin | Post text and media to X, Bluesky, LinkedIn, Mastodon and Threads from any .NET… |
| 2026-10-21 23:02:20 | [SocialPoster.Core](https://www.nuget.org/packages/SocialPoster.Core) | 0.5.0 | Isaac Levin | Reusable SocialPoster app services: SQLite storage, contacts, scheduling and th… |
| 2026-10-21 23:02:33 | [Riddler.Uxid](https://www.nuget.org/packages/Riddler.Uxid) | 1.0.0 | John Thornton | Prefixed, K-sortable identifiers a person can read: random, deterministic and m… |
| 2026-10-21 23:02:40 | [SocialPoster.Components](https://www.nuget.org/packages/SocialPoster.Components) | 0.5.0 | Isaac Levin | Embeddable SocialPoster Blazor components and routed UI for interactive server… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

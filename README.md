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

## Latest list — 2026-10-03 17:19 UTC

New packages created between 2026-10-03 16:21 UTC and 2026-10-03 17:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-03T17-19-52-268566Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-03 16:36:39 | [SunamoWshShortcut](https://www.nuget.org/packages/SunamoWshShortcut) | 26.10.3.1 | www.sunamo.cz | Package Description |
| 2026-10-03 16:39:42 | [Swevo.AutoAuth.Analyzers](https://www.nuget.org/packages/Swevo.AutoAuth.Analyzers) | 1.0.0 | Justin Bannister | Roslyn analyzers for insecure AutoAuth/OpenIddict configuration patterns. |
| 2026-10-03 16:51:24 | [Config233](https://www.nuget.org/packages/Config233) | 0.2.0 | neko233-com | Atomic configuration snapshots, JSON/TSV readers, typed indexes and cross-table… |
| 2026-10-03 16:53:25 | [Ioc233](https://www.nuget.org/packages/Ioc233) | 0.2.0 | neko233-com | Explicit-instance dependency injection and deterministic startup lifecycle for… |
| 2026-10-03 16:54:45 | [Rpc233](https://www.nuget.org/packages/Rpc233) | 0.2.0 | neko233-com | Bounded binary HTTP RPC, method dispatch, deadlines and cancellation for C# gam… |
| 2026-10-03 16:55:40 | [ByteMsg233.Server](https://www.nuget.org/packages/ByteMsg233.Server) | 1.1.0 | neko233-com | Bounded ByteMsg233 binary serialization runtime for C# game servers, with Go wi… |
| 2026-10-03 16:57:03 | [ByteMsg233.Unity](https://www.nuget.org/packages/ByteMsg233.Unity) | 1.1.0 | neko233-com | ByteMsg233 binary serialization runtime for Unity and C#, with reusable buffers… |
| 2026-10-03 17:14:31 | [SRF.Gpt.Testing](https://www.nuget.org/packages/SRF.Gpt.Testing) | 0.8.0 | John P Kosh | Test support for SRF.Gpt consumers: scripted fake chat, embedding, image and sp… |
| 2026-10-03 17:14:32 | [SRF.Gpt.Azure](https://www.nuget.org/packages/SRF.Gpt.Azure) | 0.8.0 | John P Kosh | Azure OpenAI profiles for SRF.Gpt: the unified /openai/v1/ endpoint with Micros… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

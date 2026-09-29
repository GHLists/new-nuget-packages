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

## Latest list — 2026-09-29 20:20 UTC

New packages created between 2026-09-29 19:20 UTC and 2026-09-29 20:20 UTC.

[Full CSV](data/new-nuget-packages-2026-09-29T20-20-54-116578Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-29 19:25:10 | [Causalia.AzureServiceBus](https://www.nuget.org/packages/Causalia.AzureServiceBus) | 2.3.0 | Causalia contributors | Deterministic Azure Service Bus delivery and settlement semantics for Causalia. |
| 2026-09-29 19:45:10 | [Akay.To.Azure.Identity](https://www.nuget.org/packages/Akay.To.Azure.Identity) | 1.0.1 | A.Caballero | Shared Azure credential selection for Akay.To integrations |
| 2026-09-29 19:53:44 | [Appouse.Safetalk.Redis](https://www.nuget.org/packages/Appouse.Safetalk.Redis) | 1.1.0 | Appouse | Distributed replay protection for Appouse.Safetalk: an IHmacReplayCache backed… |
| 2026-09-29 19:59:22 | [CORE.IBGE](https://www.nuget.org/packages/CORE.IBGE) | 4.95.0 | CORE.IBGE | Package Description |
| 2026-09-29 20:07:21 | [SaveState.DependencyInjection](https://www.nuget.org/packages/SaveState.DependencyInjection) | 0.1.0 | SaveState contributors | Microsoft.Extensions.DependencyInjection integration for SaveState. |
| 2026-09-29 20:07:24 | [SaveState.Generator](https://www.nuget.org/packages/SaveState.Generator) | 0.1.0 | SaveState contributors | Project-agnostic state + save/load framework: incremental source generator for… |
| 2026-09-29 20:07:27 | [SaveState.Godot](https://www.nuget.org/packages/SaveState.Godot) | 0.1.0 | SaveState contributors | Godot 4 adapter for SaveState: user:// save store, Godot output logger, and a r… |
| 2026-09-29 20:07:30 | [SaveState.Policy](https://www.nuget.org/packages/SaveState.Policy) | 0.1.0 | SaveState contributors | Project-agnostic state + save/load framework: incremental source generator for… |
| 2026-09-29 20:07:33 | [SaveState.Runtime](https://www.nuget.org/packages/SaveState.Runtime) | 0.1.0 | SaveState contributors | Project-agnostic state + save/load framework: incremental source generator for… |
| 2026-09-29 20:07:36 | [SaveState.Shared](https://www.nuget.org/packages/SaveState.Shared) | 0.1.0 | SaveState contributors | Project-agnostic state + save/load framework: incremental source generator for… |
| 2026-09-29 20:07:42 | [CService.Library.MultiThreadManager](https://www.nuget.org/packages/CService.Library.MultiThreadManager) | 1.0.0 | Carlos Eduardo Sponchiado | Process items concurrently in .NET with a bounded queue, dynamic concurrency, o… |
| 2026-09-29 20:14:17 | [AvroSharp.Tool](https://www.nuget.org/packages/AvroSharp.Tool) | 0.2.0 | zcsizmadia | The avrosharp command-line tool: C# types and serializers from Apache Avro™ sch… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

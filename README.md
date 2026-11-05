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

## Latest list — 2026-11-05 22:20 UTC

New packages created between 2026-11-05 21:19 UTC and 2026-11-05 22:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-05T22-20-47-623728Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-05 21:22:28 | [Jeff.Sdk](https://www.nuget.org/packages/Jeff.Sdk) | 1.4.0 | Casperaki Multimedia Solution… | The Jeff SDK for .NET: call Jeff's decision functions, route, escalate and run… |
| 2026-11-05 21:24:22 | [Cosmos.OpenTelemetry.Hosting](https://www.nuget.org/packages/Cosmos.OpenTelemetry.Hosting) | 0.2.0 | Cosmos | Configuración OpenTelemetry y Serilog de las APIs y workers de los bounded cont… |
| 2026-11-05 21:35:23 | [SimpleJsonRpc](https://www.nuget.org/packages/SimpleJsonRpc) | 1.0.0 | Rokas | A standalone mostly correct .NET Stream based JSON-RPC 2.0 protocol implementat… |
| 2026-11-05 21:40:12 | [AnoiMessagingCenter](https://www.nuget.org/packages/AnoiMessagingCenter) | 1.0.0 | Anoi | Allocation-conscious, weak-reference messaging center for .NET 10+. |
| 2026-11-05 21:57:53 | [XUnit_IngeniousGenerator](https://www.nuget.org/packages/XUnit_IngeniousGenerator) | 0.1.0 | Yuji Kanda | C#のコードから、xUnitのテストコードをRoslynだけで決定的に生成します（LLM不要）。TEST001でテストの不足を警告し、クイックフィックスで生成… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

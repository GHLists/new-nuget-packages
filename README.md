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

## Latest list — 2026-11-13 09:20 UTC

New packages created between 2026-11-13 08:18 UTC and 2026-11-13 09:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-13T09-20-52-917904Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-13 08:22:41 | [TradeWize.SDK](https://www.nuget.org/packages/TradeWize.SDK) | 2.0.0 | TradeWize | TradeWize SDK — TradeWize Console için robot geliştirme kütüphanesi: Robot taba… |
| 2026-11-13 08:37:13 | [Ranvier](https://www.nuget.org/packages/Ranvier) | 0.2.0 | shayanhabibi | Fine-grained reactive computation for .NET: signals, memos and effects on an ex… |
| 2026-11-13 08:37:14 | [Ranvier.CSharp](https://www.nuget.org/packages/Ranvier.CSharp) | 0.2.0 | shayanhabibi | C# entry points for Ranvier: delegate-based factories and extension methods. |
| 2026-11-13 08:37:15 | [Ranvier.Traced](https://www.nuget.org/packages/Ranvier.Traced) | 0.2.0 | shayanhabibi | The traced build of Ranvier: the same assembly, namespaces and version, with th… |
| 2026-11-13 08:37:16 | [Ranvier.CSharp.Traced](https://www.nuget.org/packages/Ranvier.CSharp.Traced) | 0.2.0 | shayanhabibi | The traced build of Ranvier.CSharp: C# entry points for Ranvier, with the traci… |
| 2026-11-13 08:37:16 | [Ranvier.Elmish](https://www.nuget.org/packages/Ranvier.Elmish) | 0.2.0 | shayanhabibi | An Elmish-style model-view-update bridge for Ranvier: a model held in a signal,… |
| 2026-11-13 08:37:17 | [Ranvier.Elmish.Traced](https://www.nuget.org/packages/Ranvier.Elmish.Traced) | 0.2.0 | shayanhabibi | The traced build of Ranvier.Elmish: the model-view-update bridge for Ranvier. D… |
| 2026-11-13 08:37:18 | [Ranvier.Query](https://www.nuget.org/packages/Ranvier.Query) | 0.2.0 | shayanhabibi | Typed reactive queries and mutation reconciliation for partially loaded applica… |
| 2026-11-13 08:37:19 | [Ranvier.Query.Traced](https://www.nuget.org/packages/Ranvier.Query.Traced) | 0.2.0 | shayanhabibi | Typed reactive queries and mutation reconciliation for partially loaded applica… |
| 2026-11-13 08:37:20 | [Ranvier.Wire](https://www.nuget.org/packages/Ranvier.Wire) | 0.2.0 | shayanhabibi | The JSON wire codec of Ranvier's transports: the same wire text on .NET (includ… |
| 2026-11-13 08:37:24 | [Ranvier.Wire.Traced](https://www.nuget.org/packages/Ranvier.Wire.Traced) | 0.2.0 | shayanhabibi | The JSON wire codec of Ranvier's transports: the same wire text on .NET (includ… |
| 2026-11-13 08:56:50 | [ConfigFerret](https://www.nuget.org/packages/ConfigFerret) | 0.1.0 | RT | Config provenance tracer: answers "why is this value 42?" by tracing every effe… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

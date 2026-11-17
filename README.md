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

## Latest list — 2026-11-17 02:20 UTC

New packages created between 2026-11-17 01:19 UTC and 2026-11-17 02:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-17T02-20-05-356505Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-17 01:22:32 | [GameEventScript.Syntax](https://www.nuget.org/packages/GameEventScript.Syntax) | 0.5.0 | Stephan Schlöpke | GES lexer, parser and single-source validator, plus GES and GESA syntax highlig… |
| 2026-11-17 01:22:40 | [GameEventScript.Generator](https://www.nuget.org/packages/GameEventScript.Generator) | 0.5.0 | Stephan Schlöpke | Game Event Script schema code generator: computes the generation layout of .ges… |
| 2026-11-17 01:45:57 | [RyanZhang.MemoryHelper.Core](https://www.nuget.org/packages/RyanZhang.MemoryHelper.Core) | 1.0.0 | Ryan Zhang | SM-2 spaced repetition scheduler and ISrsItem abstraction used by MemoryHelper… |
| 2026-11-17 01:54:36 | [Hmz.Core.Realtime](https://www.nuget.org/packages/Hmz.Core.Realtime) | 0.1.0 | Hmz | Reusable realtime delivery engine for Hmz backends on ASP.NET Core: a best-effo… |
| 2026-11-17 01:54:37 | [Hmz.Core.Realtime.Abstractions](https://www.nuget.org/packages/Hmz.Core.Realtime.Abstractions) | 0.1.0 | Hmz | Contracts of the Hmz realtime engine: the best-effort publisher, audiences, pre… |
| 2026-11-17 01:59:43 | [Azure.Connectors.Sdk](https://www.nuget.org/packages/Azure.Connectors.Sdk) | 1.0.0 | Microsoft | Lightweight SDK for building typed connectors for Azure |
| 2026-11-17 02:01:34 | [Great.Parts.Cel](https://www.nuget.org/packages/Great.Parts.Cel) | 1.0.0 | The Great.Parts Authors | Common Expression Language (CEL) for .NET 10 and .NET 11: compile and evaluate… |
| 2026-11-17 02:01:35 | [Great.Parts.Cel.Protobuf](https://www.nuget.org/packages/Great.Parts.Cel.Protobuf) | 1.0.0 | The Great.Parts Authors | Protocol Buffers support for Great.Parts.Cel: use protobuf messages and well-kn… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

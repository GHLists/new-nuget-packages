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

## Latest list — 2026-11-22 04:20 UTC

New packages created between 2026-11-22 03:19 UTC and 2026-11-22 04:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-22T04-20-17-380056Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-22 03:20:13 | [Erdigo.Core](https://www.nuget.org/packages/Erdigo.Core) | 1.0.0 | Ziorentia | The integration-v1 wire format, strict JSON and Noise handshakes used by the Er… |
| 2026-11-22 03:20:14 | [Erdigo.Send](https://www.nuget.org/packages/Erdigo.Send) | 1.0.0 | Ziorentia | Writes pins, markers, notes, photos and tracks to a paired Erdigo receiver, and… |
| 2026-11-22 03:20:15 | [Erdigo.Sdk](https://www.nuget.org/packages/Erdigo.Sdk) | 1.0.0 | Ziorentia | Writes pins, markers, notes, photos and tracks to an Erdigo receiver on the loc… |
| 2026-11-22 03:20:16 | [Erdigo.MockReceiver](https://www.nuget.org/packages/Erdigo.MockReceiver) | 1.0.0 | Ziorentia | An in-memory stand-in for the receiver side of integration-v1, for developing a… |
| 2026-11-22 03:39:40 | [Cangming.Logs.App](https://www.nuget.org/packages/Cangming.Logs.App) | 0.1.9.1122 | Fangyu,lukan@xknife.net,Asong… | 日志应用层：面板数据源与支持包。 |
| 2026-11-22 03:39:49 | [Cangming.Logs.Serilog](https://www.nuget.org/packages/Cangming.Logs.Serilog) | 0.1.9.1122 | Fangyu,lukan@xknife.net,Asong… | 当使用 Serilog 作为日志基础时，提供对日志相关契约的薄适配实现。 |
| 2026-11-22 03:39:52 | [Cangming.Logs.Testing](https://www.nuget.org/packages/Cangming.Logs.Testing) | 0.1.9.1122 | Fangyu,lukan@xknife.net,Asong… | 为插件测试提供 ILogService 的内存捕获实现与日志条目断言，只依赖 Contracts，不依赖具体日志框架与测试框架。 |
| 2026-11-22 03:54:13 | [BlazorPowerPack](https://www.nuget.org/packages/BlazorPowerPack) | 1.0.0 | Jeremy Burman and Gemini | Packs standalone Blazor WebAssembly + Fluent UI apps into compressed binary bun… |
| 2026-11-22 04:15:55 | [Chondrite.Compile](https://www.nuget.org/packages/Chondrite.Compile) | 0.9.0-alpha01 | LEAP 71 | Deterministic Chondrite schema compiler with automatic MSBuild integration and… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

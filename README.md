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

## Latest list — 2026-11-22 13:18 UTC

New packages created between 2026-11-22 12:20 UTC and 2026-11-22 13:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-22T13-18-52-272157Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-22 12:30:06 | [Sundew.Xaml.Optimizers.Wpf](https://www.nuget.org/packages/Sundew.Xaml.Optimizers.Wpf) | 3.0.0-u20261122-122… | Kim Hugener-Ohlsen | Various Xaml optimizers: - ThemeOptimizer - StaticToDynamicResourceOptimizer -… |
| 2026-11-22 12:31:13 | [ToucanHub.Sdk.Json](https://www.nuget.org/packages/ToucanHub.Sdk.Json) | 1.0.1 | Christian Bourbier | Sdk Json |
| 2026-11-22 12:31:14 | [ToucanHub.Sdk.Query](https://www.nuget.org/packages/ToucanHub.Sdk.Query) | 1.0.1 | Christian Bourbier | Sdk Query |
| 2026-11-22 12:34:21 | [Sundew.Xaml.Optimizer.BuildTask](https://www.nuget.org/packages/Sundew.Xaml.Optimizer.BuildTask) | 3.0.0-u20261122-123… | Kim Hugener-Ohlsen | A framework for creating Xaml optimizers for WPF, Avalonia, Maui, WinUI, UWP an… |
| 2026-11-22 12:34:57 | [MathHelperLab5](https://www.nuget.org/packages/MathHelperLab5) | 1.0.0 | MathHelperLab5 | Package Description |
| 2026-11-22 12:43:04 | [Isud.Tm](https://www.nuget.org/packages/Isud.Tm) | 1.0.0 | 优标宝开放平台 | 优标宝商标数据开放 API 的 .NET SDK（零第三方运行时依赖，契约驱动）。支持商标/外观检索、档案列表、报告、用量、请求日志与 MCP。 |
| 2026-11-22 12:47:39 | [Pycom.Media.Client](https://www.nuget.org/packages/Pycom.Media.Client) | 0.1.0 | Pycom | Strongly typed client for the Pycom Enterprise Media Platform runtime API. |
| 2026-11-22 12:48:07 | [Nextended.Aspire.Hosting.SigNoz](https://www.nuget.org/packages/Nextended.Aspire.Hosting.SigNoz) | 10.1.68 | fgilde | SigNoz for .NET Aspire — ClickHouse, the SigNoz OpenTelemetry collector and Sig… |
| 2026-11-22 12:58:40 | [Blaizio.Syntax.Languages](https://www.nuget.org/packages/Blaizio.Syntax.Languages) | 0.3.6 | Blaizio | More languages for Blaizio.Syntax and the Blaizio Code Block: Python, Java, Go,… |
| 2026-11-22 12:58:41 | [Blaizio.Syntax](https://www.nuget.org/packages/Blaizio.Syntax) | 0.3.6 | Blaizio | Syntax highlighting for Blazor, in C#: SyntaxText splits code into runs of one… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

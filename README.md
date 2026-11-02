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

## Latest list — 2026-11-02 06:19 UTC

New packages created between 2026-11-02 05:18 UTC and 2026-11-02 06:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-02T06-19-35-509154Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-02 05:21:15 | [victor-wiki.TransformersSharp](https://www.nuget.org/packages/victor-wiki.TransformersSharp) | 1.0.0 | victor-wiki | C# implementation of huggingface-transformers. |
| 2026-11-02 05:24:01 | [Raven.LocalAI.Agent.Console.Template](https://www.nuget.org/packages/Raven.LocalAI.Agent.Console.Template) | 1.0.0 | Raven | A dotnet new template for a LocalAI-backed Microsoft Agent Framework console ap… |
| 2026-11-02 05:27:34 | [Webority.Social.Azure](https://www.nuget.org/packages/Webority.Social.Azure) | 0.9.0 | Webority Technologies | Azure Key Vault secret store and Azure Blob media for the Webority social libra… |
| 2026-11-02 05:28:25 | [Johnwikix.ScottPlot.Avalonia](https://www.nuget.org/packages/Johnwikix.ScottPlot.Avalonia) | 5.1.60.3 | Scott Harden | User controls for displaying interactive plots in Avalonia applications |
| 2026-11-02 05:28:30 | [Johnwikix.ScottPlot.Avalonia.D3D12](https://www.nuget.org/packages/Johnwikix.ScottPlot.Avalonia.D3D12) | 5.1.60.3 | ScottPlot contributors | Optional hardware D3D12 full-Figure backend for the cross-platform AvaPlot cont… |
| 2026-11-02 05:46:45 | [QinSoft.LtpaToken](https://www.nuget.org/packages/QinSoft.LtpaToken) | 1.0.0 | QinSoft.LtpaToken | Package Description |
| 2026-11-02 05:58:30 | [Soenneker.Incident.OpenApiClientUtil](https://www.nuget.org/packages/Soenneker.Incident.OpenApiClientUtil) | 11.0.2 | Jake Soenneker | A thread-safe utility for obtaining Incident's OpenApiClient singleton. |
| 2026-11-02 06:02:23 | [XingGui.QingNiao.Log](https://www.nuget.org/packages/XingGui.QingNiao.Log) | 1.0.1 | XingGui | 星轨所至，数据有痕。“蓬山此去无多路，青鸟殷勤为探看”，QingNiao取意于此。在星轨的宇宙里，数据是散落的星辰，而QingNiao是那只穿梭于星辰之间的信… |
| 2026-11-02 06:04:11 | [UmbracoPrism.MobileBundle](https://www.nuget.org/packages/UmbracoPrism.MobileBundle) | 7.1.0 | Jonny Muir | A dotnet tool that generates a Prism mobile app bundle (Capacitor iOS and Andro… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

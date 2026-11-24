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

## Latest list — 2026-11-24 05:21 UTC

New packages created between 2026-11-24 04:20 UTC and 2026-11-24 05:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-24T05-21-02-683969Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-24 04:29:10 | [Ethereum.LeanPq](https://www.nuget.org/packages/Ethereum.LeanPq) | 0.17.0 | leanEthereum | .NET bindings for leanXMSS and leanSPHINCS post-quantum signatures, their leanV… |
| 2026-11-24 04:44:36 | [PlcSimulator.Lite.OpcUa](https://www.nuget.org/packages/PlcSimulator.Lite.OpcUa) | 2.2.15 | UseThink | ZL.PlcSimulator 的 OPC UA 协议扩展（可选；不引用则不引入 OPC UA 的 18 个依赖） |
| 2026-11-24 05:00:57 | [Umbraco.Community.UfmLabelPreview](https://www.nuget.org/packages/Umbraco.Community.UfmLabelPreview) | 1.0.0 | Nathaniel Nunes | Live preview of block labels (Umbraco Flavored Markdown) while configuring Bloc… |
| 2026-11-24 05:09:53 | [Msfp.Describe](https://www.nuget.org/packages/Msfp.Describe) | 0.8.0-preview | The MSFP contributors | MSFP's copies from media files: the media type from a file's first bytes, ffpro… |
| 2026-11-24 05:13:13 | [LYBox.Plugin.Shared.Web](https://www.nuget.org/packages/LYBox.Plugin.Shared.Web) | 2.4.0 | LYBoxPlugin | Web SDK for LYBox Avalonia Web plugins: WebView control, embedded Kestrel stati… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

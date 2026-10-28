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

## Latest list — 2026-10-28 06:20 UTC

New packages created between 2026-10-28 05:20 UTC and 2026-10-28 06:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-28T06-20-11-699501Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-28 05:28:55 | [Monet.Mayday.Help](https://www.nuget.org/packages/Monet.Mayday.Help) | 1.0.0 | Monet | MayDay-Helper |
| 2026-10-28 05:29:34 | [BrotherRaster](https://www.nuget.org/packages/BrotherRaster) | 0.1.0 | Matt Jarvis | Drive Brother QL and P-touch (PT) label printers over the network: raster encod… |
| 2026-10-28 05:29:39 | [BrotherRaster.Cli](https://www.nuget.org/packages/BrotherRaster.Cli) | 0.1.0 | Matt Jarvis | Command-line tool for Brother QL and P-touch label printers on the network: rea… |
| 2026-10-28 05:29:39 | [BrotherRaster.Skia](https://www.nuget.org/packages/BrotherRaster.Skia) | 0.1.0 | Matt Jarvis | SkiaSharp helpers for BrotherRaster: draw a label on a canvas sized for a QL ro… |
| 2026-10-28 05:53:54 | [Aslier.DeepseekWebChatWrapper](https://www.nuget.org/packages/Aslier.DeepseekWebChatWrapper) | 0.0.1 | Aslier | A .NET implementation for calling DeepSeek's web chat |
| 2026-10-28 05:55:10 | [EbInterface.Net.Mcp](https://www.nuget.org/packages/EbInterface.Net.Mcp) | 0.1.0-alpha | Harald Rohan | Lokaler MCP-Server (Model Context Protocol) für EbInterface.Net: ebInterface-Re… |
| 2026-10-28 05:55:11 | [EbInterface.Net](https://www.nuget.org/packages/EbInterface.Net) | 0.1.0-alpha | Harald Rohan | Unabhängige .NET-Implementierung des österreichischen E-Rechnungsstandards ebIn… |
| 2026-10-28 06:00:58 | [NetWinI18n](https://www.nuget.org/packages/NetWinI18n) | 2.0.2 | ShengbiYang | JSON-based multilingual localization library for WinForms applications. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

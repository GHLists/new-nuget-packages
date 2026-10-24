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

## Latest list — 2026-10-24 07:18 UTC

New packages created between 2026-10-24 06:20 UTC and 2026-10-24 07:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-24T07-18-58-209233Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-24 06:34:22 | [ThreeYPay.SDK](https://www.nuget.org/packages/ThreeYPay.SDK) | 1.1.0 | 3YPay Team | 3ypay (汇联支付) C# SDK - 统一支付、查询、退款、转账、分账等 |
| 2026-10-24 06:36:18 | [TKCode.StreamMark.Theme.AtomUI](https://www.nuget.org/packages/TKCode.StreamMark.Theme.AtomUI) | 0.1.0 | StreamMark contributors | Maps StreamMark Md.* resources onto AtomUI design tokens, so Markdown follows t… |
| 2026-10-24 06:36:18 | [TKCode.StreamMark.Avalonia](https://www.nuget.org/packages/TKCode.StreamMark.Avalonia) | 0.1.0 | StreamMark contributors | StreamMark Avalonia controls: self-drawn Markdown blocks, virtualizing transcri… |
| 2026-10-24 06:36:18 | [TKCode.StreamMark.Core](https://www.nuget.org/packages/TKCode.StreamMark.Core) | 0.1.0 | StreamMark contributors | StreamMark core: streaming Markdown source buffer, incomplete-markdown repair,… |
| 2026-10-24 06:36:19 | [TKCode.StreamMark.Mermaid](https://www.nuget.org/packages/TKCode.StreamMark.Mermaid) | 0.1.0 | StreamMark contributors | Mermaid diagram rendering for StreamMark (Mermaider + Svg.Skia), no browser req… |
| 2026-10-24 06:36:19 | [TKCode.StreamMark.RaTeX](https://www.nuget.org/packages/TKCode.StreamMark.RaTeX) | 0.1.0 | StreamMark contributors | LaTeX math rendering for StreamMark via the RaTeX native engine (KaTeX-compatib… |
| 2026-10-24 06:36:19 | [TKCode.StreamMark.Highlighting.TextMate](https://www.nuget.org/packages/TKCode.StreamMark.Highlighting.TextMate) | 0.1.0 | StreamMark contributors | TextMate-based incremental syntax highlighting for StreamMark code blocks. |
| 2026-10-24 06:37:33 | [Kekincai.JiebaNet.Segmenter](https://www.nuget.org/packages/Kekincai.JiebaNet.Segmenter) | 1.0.0 | andersc,kekincai | Chinese text segmentation for .NET 10 with embedded dictionaries and no third-p… |
| 2026-10-24 06:37:34 | [Kekincai.JiebaNet.Analyser](https://www.nuget.org/packages/Kekincai.JiebaNet.Analyser) | 1.0.0 | andersc,kekincai | TF-IDF and TextRank keyword extraction for .NET 10. |
| 2026-10-24 06:38:19 | [XCode.SonnetDB](https://www.nuget.org/packages/XCode.SonnetDB) | 11.25.2026.1024 | 新生命开发团队 | Provides embedded and remote SonnetDB driver integration, SQL dialect and autom… |
| 2026-10-24 06:57:24 | [DataOil.Client](https://www.nuget.org/packages/DataOil.Client) | 0.2.2 | MaxDragon Technology | The Data Oil client for .NET: one statement over rows, vectors, keywords and re… |
| 2026-10-24 06:57:26 | [SwedishTestSsn.Client](https://www.nuget.org/packages/SwedishTestSsn.Client) | 2.0.0 | Ferenyl | Client for getting Swedish social security numbers for testing from Skatteverke… |
| 2026-10-24 06:57:51 | [DataOil.EntityFrameworkCore](https://www.nuget.org/packages/DataOil.EntityFrameworkCore) | 0.1.4 | MaxDragon Technology | The Entity Framework Core provider for Data Oil. It learns each database's sche… |
| 2026-10-24 06:58:14 | [DataOil.LINQPad](https://www.nuget.org/packages/DataOil.LINQPad) | 0.1.5 | MaxDragon Technology | The LINQPad 9 driver for Data Oil. Connect to a database and its types become a… |
| 2026-10-24 07:01:05 | [ZeroMayo.ppy.osu.Framework.NativeLibs](https://www.nuget.org/packages/ZeroMayo.ppy.osu.Framework.NativeLibs) | 26.0.0 | ppy Pty Ltd | Native libraries for osu!framework |
| 2026-10-24 07:02:53 | [Goo.AppHost](https://www.nuget.org/packages/Goo.AppHost) | 0.15.0 | Xaz | Optional desktop activation and single-instance hosting for Goo. |
| 2026-10-24 07:10:30 | [Joy.AbpUi.Domain.Shared](https://www.nuget.org/packages/Joy.AbpUi.Domain.Shared) | 1.0.0 | Joy | ABP localization module providing UI and Menus resources for joy-abpui-angular.… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

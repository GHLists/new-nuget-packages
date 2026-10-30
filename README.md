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

## Latest list — 2026-10-30 17:21 UTC

New packages created between 2026-10-30 16:21 UTC and 2026-10-30 17:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-30T17-21-17-272861Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-30 16:21:17 | [Photon.Core.EventBus](https://www.nuget.org/packages/Photon.Core.EventBus) | 1.0.0.8 | putoo | 事件总线 |
| 2026-10-30 16:21:38 | [Photon.Core.Http](https://www.nuget.org/packages/Photon.Core.Http) | 1.0.0.8 | putoo | HTTP请求组件 |
| 2026-10-30 16:21:49 | [Hopper.Fintech.Flights](https://www.nuget.org/packages/Hopper.Fintech.Flights) | 0.1.0 | Hopper | Client for the HTS Fintech Flights APIs (Cancel For Any Reason and Disruption G… |
| 2026-10-30 16:22:08 | [GroupDocs.Parser.Net48](https://www.nuget.org/packages/GroupDocs.Parser.Net48) | 26.10.0 | Aspose | Runtime assemblies for GroupDocs.Parser targeting .NET Framework 4.8.0. Install… |
| 2026-10-30 16:30:34 | [Rulealize.RuleSet.Chess](https://www.nuget.org/packages/Rulealize.RuleSet.Chess) | 1.0.0 | Reny | Chess, with castling, en passant and promotion. A Rulealize rule set. |
| 2026-10-30 16:37:15 | [Rulealize.RuleSet.Minesweeper](https://www.nuget.org/packages/Rulealize.RuleSet.Minesweeper) | 1.0.0 | Reny | Minesweeper on a 9 × 9 board with ten mines, laid after the first cell is opene… |
| 2026-10-30 16:39:45 | [Parlot.Explorer](https://www.nuget.org/packages/Parlot.Explorer) | 2.1.0 | Sebastien Ros | Local parser diagnostics and replay explorer for Parlot generated parsers. |
| 2026-10-30 16:42:01 | [Doppelganger](https://www.nuget.org/packages/Doppelganger) | 0.0.1 | Niklas Wendel | Doppelganger - an opinionated, source-generated mocking library for .NET, built… |
| 2026-10-30 16:42:34 | [Bimwright.Dwg.Server](https://www.nuget.org/packages/Bimwright.Dwg.Server) | 2.1.1 | Khoa Le | MCP gateway for AutoCAD 2022-2027 DWG workflows: text reading, translation rewr… |
| 2026-10-30 16:46:22 | [Rulealize.RuleSet.PackingList](https://www.nuget.org/packages/Rulealize.RuleSet.PackingList) | 1.0.0 | Reny | What to take, and what is in the bag already: items added as they come to mind… |
| 2026-10-30 16:55:43 | [Rulealize.RuleSet.Reversi](https://www.nuget.org/packages/Rulealize.RuleSet.Reversi) | 1.0.0 | Reny | Reversi for two players on an 8 × 8 board, with passing when no disc can be pla… |
| 2026-10-30 17:01:55 | [Rulealize.RuleSet.Scoreboard](https://www.nuget.org/packages/Rulealize.RuleSet.Scoreboard) | 1.0.0 | Reny | Points for each player, round after round, and who is ahead. A Rulealize rule s… |
| 2026-10-30 17:09:36 | [Gurux.DLMS.AMI.Http](https://www.nuget.org/packages/Gurux.DLMS.AMI.Http) | 4.1.2610.3001 | Gurux Ltd | Lightweight HTTP response validation and JSON request helpers for Gurux DLMS AM… |
| 2026-10-30 17:11:42 | [CppPinyin](https://www.nuget.org/packages/CppPinyin) | 2.0.0 | CppPinyin | C# binding for cpp-pinyin2 (Mandarin and Cantonese) over its C ABI. The native… |
| 2026-10-30 17:12:50 | [OvoUi.Platform.NoAOT](https://www.nuget.org/packages/OvoUi.Platform.NoAOT) | 1.0.3 | tiouo | Optional Windows Jump List and reflection-based composition materials. Requires… |
| 2026-10-30 17:12:51 | [OvoUi.Lang](https://www.nuget.org/packages/OvoUi.Lang) | 1.0.3 | tiouo | Reactive, strongly typed Avalonia localization with configurable resource paths… |
| 2026-10-30 17:12:53 | [OvoUi.DataGrid](https://www.nuget.org/packages/OvoUi.DataGrid) | 1.0.3 | tiouo | Optional OvoUi DataGrid theme. Requires the managed runtime; Native AOT is not… |
| 2026-10-30 17:15:50 | [Rulealize.RuleSet.SplitBill](https://www.nuget.org/packages/Rulealize.RuleSet.SplitBill) | 1.0.0 | Reny | Who paid for what on a trip or a night out, and what each one pays or gets back… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

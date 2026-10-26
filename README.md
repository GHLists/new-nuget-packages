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

## Latest list — 2026-10-26 06:21 UTC

New packages created between 2026-10-26 05:21 UTC and 2026-10-26 06:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-26T06-21-02-027909Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-26 05:23:01 | [EsUtil.Feature.ColumnPacking.Core](https://www.nuget.org/packages/EsUtil.Feature.ColumnPacking.Core) | 0.1.0 | tomokuni | 複数のアイテムを複数列へ配置し、最大列高さを最小化する UI 非依存のレイアウト計算層（貪欲法・動的計画法・二分探索）。 |
| 2026-10-26 05:23:02 | [EsUtil.Feature.Loupe.Core](https://www.nuget.org/packages/EsUtil.Feature.Loupe.Core) | 0.1.0 | tomokuni | ルーペ（選択範囲の拡大表示）の UI 非依存の計算層。 |
| 2026-10-26 05:23:04 | [EsUtil.Feature.Loupe.Presenter](https://www.nuget.org/packages/EsUtil.Feature.Loupe.Presenter) | 0.1.0 | tomokuni | ルーペの外観・描画計画・ラベル計画を単一所有する UI 非依存の提示層。 |
| 2026-10-26 05:23:05 | [EsUtil.Feature.Marquee.Core](https://www.nuget.org/packages/EsUtil.Feature.Marquee.Core) | 0.1.0 | tomokuni | マーキー選択（ドラッグ矩形の選択・移動・リサイズ）の UI 非依存の計算層。 |
| 2026-10-26 05:23:06 | [EsUtil.Feature.Marquee.Presenter](https://www.nuget.org/packages/EsUtil.Feature.Marquee.Presenter) | 0.1.0 | tomokuni | マーキーの外観・描画手順を単一所有する UI 非依存の提示層。 |
| 2026-10-26 05:23:07 | [EsUtil.Feature.Thumbnail.Core](https://www.nuget.org/packages/EsUtil.Feature.Thumbnail.Core) | 0.1.0 | tomokuni | サムネイル一覧（折り返し配置・選択・可視範囲）の UI 非依存の計算層。 |
| 2026-10-26 05:23:08 | [EsUtil.Feature.Thumbnail.Presenter](https://www.nuget.org/packages/EsUtil.Feature.Thumbnail.Presenter) | 0.1.0 | tomokuni | サムネイルの外観・影・描画計画・ラベル計画を単一所有する UI 非依存の提示層。 |
| 2026-10-26 05:23:09 | [EsUtil.Feature.ZenHan.Core](https://www.nuget.org/packages/EsUtil.Feature.ZenHan.Core) | 0.1.0 | tomokuni | 全角・半角・ひらがな・カタカナ・記号の相互変換（CSV から生成した定義を不変リストで保持する）。 |
| 2026-10-26 05:23:10 | [EsUtil.Platform.Core](https://www.nuget.org/packages/EsUtil.Platform.Core) | 0.1.0 | tomokuni | UI フレームワーク非依存の共通基盤（キーと入力・幾何・座標変換・画像・OS サービス抽象）。 |
| 2026-10-26 05:23:12 | [EsUtil.Platform.Core.Windows](https://www.nuget.org/packages/EsUtil.Platform.Core.Windows) | 0.1.0 | tomokuni | System.Drawing.Bitmap と EsUtil.Platform.Core の画像型を相互変換する Windows 専用の拡張。 |
| 2026-10-26 05:23:13 | [EsUtil.Ui.WinForms.Loupe](https://www.nuget.org/packages/EsUtil.Ui.WinForms.Loupe) | 0.1.0 | tomokuni | ルーペの WinForms 版コントロール。 |
| 2026-10-26 05:23:14 | [EsUtil.Ui.WinForms.Marquee](https://www.nuget.org/packages/EsUtil.Ui.WinForms.Marquee) | 0.1.0 | tomokuni | マーキーの WinForms 版コントロール。 |
| 2026-10-26 05:23:15 | [EsUtil.Ui.WinForms.Thumbnail](https://www.nuget.org/packages/EsUtil.Ui.WinForms.Thumbnail) | 0.1.0 | tomokuni | サムネイル一覧の WinForms 版コントロール。 |
| 2026-10-26 05:23:16 | [EsUtil.Ui.WinUI3.ColorComboBox](https://www.nuget.org/packages/EsUtil.Ui.WinUI3.ColorComboBox) | 0.1.0 | tomokuni | 色選択の WinUI 3 版コントロール。 |
| 2026-10-26 05:23:17 | [EsUtil.Ui.WinUI3.ColumnPacking](https://www.nuget.org/packages/EsUtil.Ui.WinUI3.ColumnPacking) | 0.1.0 | tomokuni | 縦方向のマルチカラム配置を行う WinUI 3 のパネル（最大列高さを最小化するレイアウト計算は EsUtil.Feature.ColumnPacking.C… |
| 2026-10-26 05:23:18 | [EsUtil.Ui.WinUI3.Loupe](https://www.nuget.org/packages/EsUtil.Ui.WinUI3.Loupe) | 0.1.0 | tomokuni | ルーペの WinUI 3 版コントロール。 |
| 2026-10-26 05:23:20 | [EsUtil.Ui.WinUI3.Marquee](https://www.nuget.org/packages/EsUtil.Ui.WinUI3.Marquee) | 0.1.0 | tomokuni | マーキーの WinUI 3 版コントロール。 |
| 2026-10-26 05:23:21 | [EsUtil.Ui.WinUI3.Thumbnail](https://www.nuget.org/packages/EsUtil.Ui.WinUI3.Thumbnail) | 0.1.0 | tomokuni | サムネイル一覧の WinUI 3 版コントロール。 |
| 2026-10-26 05:23:22 | [EsUtil.Ui.AvaloniaUI.ColorComboBox](https://www.nuget.org/packages/EsUtil.Ui.AvaloniaUI.ColorComboBox) | 0.1.0 | tomokuni | Avalonia UI の色選択コントロール（色名の解決・入力の検証・不透明度の編集）。 |
| 2026-10-26 05:23:23 | [EsUtil.Ui.AvaloniaUI.Loupe](https://www.nuget.org/packages/EsUtil.Ui.AvaloniaUI.Loupe) | 0.1.0 | tomokuni | ルーペの Avalonia UI 版コントロール。 |
| 2026-10-26 05:23:25 | [EsUtil.Ui.AvaloniaUI.Marquee](https://www.nuget.org/packages/EsUtil.Ui.AvaloniaUI.Marquee) | 0.1.0 | tomokuni | マーキーの Avalonia UI 版コントロール。 |
| 2026-10-26 05:23:26 | [EsUtil.Ui.AvaloniaUI.Thumbnail](https://www.nuget.org/packages/EsUtil.Ui.AvaloniaUI.Thumbnail) | 0.1.0 | tomokuni | サムネイル一覧の Avalonia UI 版コントロール。 |
| 2026-10-26 05:23:27 | [EsUtil.Ui.MewUI.ColorComboBox](https://www.nuget.org/packages/EsUtil.Ui.MewUI.ColorComboBox) | 0.1.0 | tomokuni | MewUI の色選択コントロール（色名の一覧・入力の検証・カラーピッカー）。 |
| 2026-10-26 05:23:28 | [EsUtil.Ui.MewUI.Loupe](https://www.nuget.org/packages/EsUtil.Ui.MewUI.Loupe) | 0.1.0 | tomokuni | ルーペの MewUI 版コントロール。 |
| 2026-10-26 05:23:29 | [EsUtil.Ui.MewUI.Marquee](https://www.nuget.org/packages/EsUtil.Ui.MewUI.Marquee) | 0.1.0 | tomokuni | マーキーの MewUI 版コントロール。 |
| 2026-10-26 05:23:31 | [EsUtil.Ui.MewUI.Thumbnail](https://www.nuget.org/packages/EsUtil.Ui.MewUI.Thumbnail) | 0.1.0 | tomokuni | サムネイル一覧の MewUI 版コントロール。 |
| 2026-10-26 05:28:26 | [Tint](https://www.nuget.org/packages/Tint) | 0.0.1 | Sébastien Ros | TextMate syntax colorization for .NET: VS Code grammars and themes compiled by… |
| 2026-10-26 05:28:27 | [Tint.Grammars](https://www.nuget.org/packages/Tint.Grammars) | 0.0.1 | Sébastien Ros | The TextMate grammars of Visual Studio Code, compiled for Tint: one class per g… |
| 2026-10-26 05:28:29 | [Tint.Grammars.Sources](https://www.nuget.org/packages/Tint.Grammars.Sources) | 0.0.1 | Sébastien Ros | The TextMate grammar files of Visual Studio Code (JSON and plist, with their ma… |
| 2026-10-26 05:28:30 | [Tint.Themes](https://www.nuget.org/packages/Tint.Themes) | 0.0.1 | Sébastien Ros | The color themes of Visual Studio Code, compiled for Tint: one class per theme,… |
| 2026-10-26 05:28:31 | [Tint.Themes.Sources](https://www.nuget.org/packages/Tint.Themes.Sources) | 0.0.1 | Sébastien Ros | The color theme files of Visual Studio Code (with their includes and manifest)… |
| 2026-10-26 05:44:20 | [NCache.DistributedLock](https://www.nuget.org/packages/NCache.DistributedLock) | 5.3.800 | Alachisoft | NCache integration for Distributed Lock. |
| 2026-10-26 05:49:44 | [Octeka.Ui.Wpf.DrillDownMenu](https://www.nuget.org/packages/Octeka.Ui.Wpf.DrillDownMenu) | 1.0.0 | Patrick Robichaud | Hierarchical, in-place transition drill-down menu control for modern WPF applic… |
| 2026-10-26 05:49:53 | [NextLevel.Maintenance](https://www.nuget.org/packages/NextLevel.Maintenance) | 1.0.0 | NextLevel | Maintenance contracts shared by games (NextLevel.GameStarter) and the admin: th… |
| 2026-10-26 05:58:15 | [EsUtil.Ui.AvaloniaUI.Interop](https://www.nuget.org/packages/EsUtil.Ui.AvaloniaUI.Interop) | 0.1.0 | tomokuni | Avalonia UI と EsUtil の型（キー・幾何・色・ウィンドウ状態・画像）を相互変換するブリッジ。 |
| 2026-10-26 05:58:17 | [EsUtil.Ui.MewUI.Interop](https://www.nuget.org/packages/EsUtil.Ui.MewUI.Interop) | 0.1.0 | tomokuni | MewUI と EsUtil の型（キー・幾何・色・ウィンドウ状態・画像）を相互変換するブリッジ。 |
| 2026-10-26 05:58:18 | [EsUtil.Ui.WinForms.Interop](https://www.nuget.org/packages/EsUtil.Ui.WinForms.Interop) | 0.1.0 | tomokuni | WinForms と EsUtil の型（キー・幾何・色・ウィンドウ状態・画像）を相互変換するブリッジ。 |
| 2026-10-26 05:58:19 | [EsUtil.Ui.WinUI3.Interop](https://www.nuget.org/packages/EsUtil.Ui.WinUI3.Interop) | 0.1.0 | tomokuni | WinUI 3 と EsUtil の型（キー・幾何・色・ウィンドウ状態・画像）を相互変換するブリッジ。 |
| 2026-10-26 05:59:30 | [Astrea.Components](https://www.nuget.org/packages/Astrea.Components) | 0.8.0 | Astrea contributors | Astrea Blazor UI components for .NET 6: Tree and ResourceTable. |
| 2026-10-26 06:13:13 | [EdiMorph.Abstractions](https://www.nuget.org/packages/EdiMorph.Abstractions) | 0.1.0 | Tural Suleymani, suleymani.2r… | Contracts for specification requests, diagnostics, and rule handlers. |
| 2026-10-26 06:13:15 | [EdiMorph.Specifications](https://www.nuget.org/packages/EdiMorph.Specifications) | 0.1.0 | Tural Suleymani, suleymani.2r… | Catalog, resolver, and compiler that produce an immutable EDI specification. |
| 2026-10-26 06:13:17 | [EdiMorph.Specifications.X12](https://www.nuget.org/packages/EdiMorph.Specifications.X12) | 0.1.0 | Tural Suleymani, suleymani.2r… | X12 004010 rule documents, syntax handlers, and the typed 204 transaction. |
| 2026-10-26 06:13:22 | [EdiMorph.X12](https://www.nuget.org/packages/EdiMorph.X12) | 0.1.0 | Tural Suleymani, suleymani.2r… | X12 reader for a compiled 004010 204 interchange. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

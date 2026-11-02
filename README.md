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

## Latest list — 2026-11-02 16:20 UTC

New packages created between 2026-11-02 15:18 UTC and 2026-11-02 16:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-02T16-20-46-330053Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-02 15:21:37 | [EsUtil.Ui.AvaloniaUI.ColorSelector](https://www.nuget.org/packages/EsUtil.Ui.AvaloniaUI.ColorSelector) | 0.4.0 | tomokuni | Avalonia UI の色選択コントロール（色名の解決・入力の検証・不透明度の編集）。 |
| 2026-11-02 15:21:41 | [EsUtil.Ui.MewUI.ColorSelector](https://www.nuget.org/packages/EsUtil.Ui.MewUI.ColorSelector) | 0.4.0 | tomokuni | MewUI の色選択コントロール（色名の一覧・入力の検証・カラーピッカー）。 |
| 2026-11-02 15:21:49 | [EsUtil.Ui.WinUI3.ColorSelector](https://www.nuget.org/packages/EsUtil.Ui.WinUI3.ColorSelector) | 0.4.0 | tomokuni | 色選択の WinUI 3 版コントロール。 |
| 2026-11-02 15:26:53 | [FIAP.TechChallenge.Billing.Application.Messaging](https://www.nuget.org/packages/FIAP.TechChallenge.Billing.Application.Messaging) | 0.1.0 | FIAP.TechChallenge.Billing.Ap… | Package Description |
| 2026-11-02 15:32:02 | [Telerik.UI.for.Blazor.DatAInsightsComposer](https://www.nuget.org/packages/Telerik.UI.for.Blazor.DatAInsightsComposer) | 15.2.0 | Progress Software Corporation | Telerik UI for Blazor DatAInsightsComposer provides AI-powered dynamic generati… |
| 2026-11-02 15:32:50 | [TimerWheel](https://www.nuget.org/packages/TimerWheel) | 0.1.0 | Mark Hammond | A caller-driven hashed timing wheel for .NET, allocation-free once warm: O(1) c… |
| 2026-11-02 15:42:04 | [Aegirax.Integration](https://www.nuget.org/packages/Aegirax.Integration) | 0.1.0 | Aegirax | Integración de APIs con Aegirax: roles en OpenAPI (x-required-roles), versión d… |
| 2026-11-02 15:47:03 | [ITBees.Recordings](https://www.nuget.org/packages/ITBees.Recordings) | 8.0.4 | ITBees | Continuous camera recording on Linux devices with MediaMTX: installs and superv… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

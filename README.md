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

## Latest list — 2026-11-02 17:22 UTC

New packages created between 2026-11-02 16:20 UTC and 2026-11-02 17:22 UTC.

[Full CSV](data/new-nuget-packages-2026-11-02T17-22-04-822689Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-02 16:21:15 | [IT.Tangdao.Wpf](https://www.nuget.org/packages/IT.Tangdao.Wpf) | 1.0.0 | liuxin | Package Description |
| 2026-11-02 16:46:52 | [LogicBuilder.App.Maui.Business](https://www.nuget.org/packages/LogicBuilder.App.Maui.Business) | 1.0.1 | BlaiseD | Consolidates MAUI flow metadata structures into a shared library. |
| 2026-11-02 16:53:03 | [Hateoas.AspNetCore.OpenApi](https://www.nuget.org/packages/Hateoas.AspNetCore.OpenApi) | 2.2.0 | Yahya Erdogan | Microsoft.AspNetCore.OpenApi support for Hateoas: documents HAL "_links" as wri… |
| 2026-11-02 17:03:44 | [LogicBuilder.App.Maui.Utils](https://www.nuget.org/packages/LogicBuilder.App.Maui.Utils) | 1.0.1 | BlaiseD | Consolidates MAUI flow functions into a shared library. |
| 2026-11-02 17:12:20 | [VS_Builder.WinUI3Controls](https://www.nuget.org/packages/VS_Builder.WinUI3Controls) | 1.0.6 | Microsoft | A highly customizable WinUI 3 custom button component that enables structural p… |
| 2026-11-02 17:12:34 | [Shirasagi0012.SmoothScroll.Avalonia](https://www.nuget.org/packages/Shirasagi0012.SmoothScroll.Avalonia) | 12.0.0.1 | SmoothScroll.Avalonia.Controls | A fork adding features needed for Material3Expressive.Avalonia; Scrolling, pann… |
| 2026-11-02 17:12:49 | [Shirasagi0012.SmoothScroll.Avalonia.Interaction](https://www.nuget.org/packages/Shirasagi0012.SmoothScroll.Avalonia.Interaction) | 12.0.0.1 | SmoothScroll.Avalonia.Interac… | A fork adding features needed for Material3Expressive.Avalonia; InteractionTrac… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

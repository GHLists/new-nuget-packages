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

## Latest list — 2026-11-15 05:20 UTC

New packages created between 2026-11-15 04:19 UTC and 2026-11-15 05:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-15T05-20-49-994434Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-15 04:25:22 | [Lers.PdfSharp](https://www.nuget.org/packages/Lers.PdfSharp) | 2.0.0 | Stefan Steiger and Contributo… | PdfSharp for .NET Core PdfSharpCore is a partial port of PdfSharp.Xamarin for .… |
| 2026-11-15 04:28:53 | [Microsoft.Mxc.Sdk.Nvx.Runtime](https://www.nuget.org/packages/Microsoft.Mxc.Sdk.Nvx.Runtime) | 1.1.0 | Microsoft | Windows x64 NVX MicroVM runtime assets for Microsoft.Mxc.Sdk. |
| 2026-11-15 04:37:31 | [ReactiveUI.Primitives.Blazor.Reactive](https://www.nuget.org/packages/ReactiveUI.Primitives.Blazor.Reactive) | 10.0.0 | ReactiveUI Association Inc | Blazor integration helpers for ReactiveUI.Primitives, recompiled against System… |
| 2026-11-15 04:37:37 | [ReactiveUI.Primitives.Maui.Reactive](https://www.nuget.org/packages/ReactiveUI.Primitives.Maui.Reactive) | 10.0.0 | ReactiveUI Association Inc | MAUI dispatcher scheduler for ReactiveUI.Primitives, recompiled against System.… |
| 2026-11-15 04:46:44 | [Rechunk.Keys.AzureKeyVault](https://www.nuget.org/packages/Rechunk.Keys.AzureKeyVault) | 0.2.1 | Challa Ravindranath | Wraps Rechunk scope keys with a key that stays in Azure Key Vault. |
| 2026-11-15 04:51:46 | [MultiConnect.SDK](https://www.nuget.org/packages/MultiConnect.SDK) | 2026.1115.619 | MultiConnect | MultiConnect SDK for .NET: multiplayer networking, rooms and matchmaking, deter… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

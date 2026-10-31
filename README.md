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

## Latest list — 2026-10-31 00:20 UTC

New packages created between 2026-10-30 23:20 UTC and 2026-10-31 00:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-31T00-20-53-10515Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-30 23:43:31 | [Bit.BlazorUI.AI](https://www.nuget.org/packages/Bit.BlazorUI.AI) | 11.0.0-pre-15 | bit platform | Bit.BlazorUI.AI |
| 2026-10-30 23:43:32 | [Bit.BbScanner.Maui](https://www.nuget.org/packages/Bit.BbScanner.Maui) | 11.0.0-pre-15 | bit platform | Bit.BbScanner.Maui |
| 2026-10-30 23:43:33 | [Bit.Bheadless.Testing](https://www.nuget.org/packages/Bit.Bheadless.Testing) | 11.0.0-pre-15 | bit platform | Accessibility test tooling for Razor components, built on bUnit: a WAI-ARIA rul… |
| 2026-10-31 00:03:27 | [CascadiaUI](https://www.nuget.org/packages/CascadiaUI) | 0.1.0 | Simone Bortolin | A Fluent × macOS theme for Avalonia 12: neutral light/dark palettes, a customis… |
| 2026-10-31 00:13:55 | [Superroute.SLocker.Customer](https://www.nuget.org/packages/Superroute.SLocker.Customer) | 0.2.0 | Superroute | sLocker for customers: locker pickups, locker locations, locker storage, the lo… |
| 2026-10-31 00:13:55 | [Superroute.SLocker.UI](https://www.nuget.org/packages/Superroute.SLocker.UI) | 0.2.0 | Superroute | sLocker UI kit for .NET: the pickup list and the locker map as view models on t… |
| 2026-10-31 00:13:56 | [Superroute.SLocker.WinForms](https://www.nuget.org/packages/Superroute.SLocker.WinForms) | 0.2.0 | Superroute | sLocker UI kit for Windows Forms: the PickupList and LockerMap controls, drawn… |
| 2026-10-31 00:13:56 | [Superroute.SLocker.Wpf](https://www.nuget.org/packages/Superroute.SLocker.Wpf) | 0.2.0 | Superroute | sLocker UI kit for WPF: the PickupList and LockerMap controls, drawn by the sAp… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

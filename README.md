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

## Latest list — 2026-10-23 09:22 UTC

New packages created between 2026-10-23 08:21 UTC and 2026-10-23 09:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-23T09-22-20-520308Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-23 08:21:22 | [LocalizationRuntime](https://www.nuget.org/packages/LocalizationRuntime) | 0.1.0 | FlyingEyeOrg | 编译期固化多语言资源的 .NET 本地化运行时：运行时零文件 IO，按 CultureInfo 链回退取值。 |
| 2026-10-23 08:21:24 | [LocalizationRuntime.Generator](https://www.nuget.org/packages/LocalizationRuntime.Generator) | 0.1.0 | FlyingEyeOrg | LocalizationRuntime 的 Roslyn 增量生成器：把 Localization/*.json 编译成常量数组。 |
| 2026-10-23 08:28:27 | [UVision.Client](https://www.nuget.org/packages/UVision.Client) | 0.4.0 | iyulab | Typed HTTP client for the U-Vision judgment engine, generated from its OpenAPI… |
| 2026-10-23 08:32:19 | [Bathos.Platform](https://www.nuget.org/packages/Bathos.Platform) | 1.0.0 | Bathos Labs | Toolkit-independent native capability contracts and atomic staged file publicat… |
| 2026-10-23 08:32:20 | [Bathos.Platform.Linux](https://www.nuget.org/packages/Bathos.Platform.Linux) | 1.0.0 | Bathos Labs | Experimental Linux native capabilities for .NET 10: statx regular-file inspecti… |
| 2026-10-23 08:32:20 | [Bathos.Platform.MacOS](https://www.nuget.org/packages/Bathos.Platform.MacOS) | 1.0.0 | Bathos Labs | macOS native capabilities for .NET 10: atomic file rename and replacement, regu… |
| 2026-10-23 08:32:21 | [Bathos.Platform.Windows](https://www.nuget.org/packages/Bathos.Platform.Windows) | 1.0.0 | Bathos Labs | Windows native capabilities for .NET 10: atomic file rename and replacement, re… |
| 2026-10-23 08:45:44 | [ShellIcons.Avalonia](https://www.nuget.org/packages/ShellIcons.Avalonia) | 0.2.0-alpha | shellui-dev | Lucide-derived icons for Avalonia, drawn straight to the DrawingContext. Typed… |
| 2026-10-23 08:45:47 | [ShellIcons.Maui](https://www.nuget.org/packages/ShellIcons.Maui) | 0.2.0-alpha | shellui-dev | Lucide-derived icons for .NET MAUI as native Path shapes. Typed controls, an Ic… |
| 2026-10-23 08:47:07 | [TTT.Azure.Vault.ConfigurationBuilder](https://www.nuget.org/packages/TTT.Azure.Vault.ConfigurationBuilder) | 1.0.0 | TTT.Azure.Vault.Configuration… | Package Description |
| 2026-10-23 08:54:56 | [MeroMiti](https://www.nuget.org/packages/MeroMiti) | 1.0.0 | Inline Tech Solution | Universal Bikram Sambat (B.S.) Nepali calendar engine and date converter for .N… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

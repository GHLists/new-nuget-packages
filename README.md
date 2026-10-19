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

## Latest list — 2026-10-19 13:20 UTC

New packages created between 2026-10-19 12:20 UTC and 2026-10-19 13:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-19T13-20-23-403716Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-19 12:28:20 | [Umbraco.AI.TypeSafe](https://www.nuget.org/packages/Umbraco.AI.TypeSafe) | 18.0.0 | Umbraco | TypeSafe AI provider for Umbraco AI |
| 2026-10-19 12:30:30 | [XxmiLang.Core](https://www.nuget.org/packages/XxmiLang.Core) | 0.1.1 | xxmi-lang contributors | The shared definitions of the xxmi-lang .NET library: diagnostics, locations, e… |
| 2026-10-19 12:30:32 | [XxmiLang.Native.linux-arm64](https://www.nuget.org/packages/XxmiLang.Native.linux-arm64) | 0.1.1 | xxmi-lang contributors | The xxmi command-line tool and language server for linux-arm64, for the XxmiLan… |
| 2026-10-19 12:30:35 | [XxmiLang.Native.linux-x64](https://www.nuget.org/packages/XxmiLang.Native.linux-x64) | 0.1.1 | xxmi-lang contributors | The xxmi command-line tool and language server for linux-x64, for the XxmiLang… |
| 2026-10-19 12:30:37 | [XxmiLang.Native.osx-arm64](https://www.nuget.org/packages/XxmiLang.Native.osx-arm64) | 0.1.1 | xxmi-lang contributors | The xxmi command-line tool and language server for osx-arm64, for the XxmiLang… |
| 2026-10-19 12:30:39 | [XxmiLang.Native.osx-x64](https://www.nuget.org/packages/XxmiLang.Native.osx-x64) | 0.1.1 | xxmi-lang contributors | The xxmi command-line tool and language server for osx-x64, for the XxmiLang pa… |
| 2026-10-19 12:30:42 | [XxmiLang.Native.win-arm64](https://www.nuget.org/packages/XxmiLang.Native.win-arm64) | 0.1.1 | xxmi-lang contributors | The xxmi command-line tool and language server for win-arm64, for the XxmiLang… |
| 2026-10-19 12:30:44 | [XxmiLang.Native.win-x64](https://www.nuget.org/packages/XxmiLang.Native.win-x64) | 0.1.1 | xxmi-lang contributors | The xxmi command-line tool and language server for win-x64, for the XxmiLang pa… |
| 2026-10-19 12:30:45 | [XxmiLang](https://www.nuget.org/packages/XxmiLang) | 0.1.1 | xxmi-lang contributors | Typed .NET client for the xxmi-lang tooling: lint and analyse XXMI / 3DMigoto m… |
| 2026-10-19 12:31:50 | [Sintef.Scoop.Utilities.Framework](https://www.nuget.org/packages/Sintef.Scoop.Utilities.Framework) | 2.0.6 | SINTEF Mathematics and Cybern… | Package Description |
| 2026-10-19 12:33:47 | [AscendantWare.PSIpenta.COM](https://www.nuget.org/packages/AscendantWare.PSIpenta.COM) | 1.0.1 | AscendantWare.PSIpenta.COM | Eine moderne C#-Wrapper-Bibliothek für die PSIpenta COM-Schnittstelle, die eine… |
| 2026-10-19 12:43:39 | [LogiPluginApi](https://www.nuget.org/packages/LogiPluginApi) | 6.4.2.3567 | Logitech | Logi Plugin API for developing Logi Plugin Service plugins. |
| 2026-10-19 13:04:45 | [ChohyoPdf](https://www.nuget.org/packages/ChohyoPdf) | 0.1.0 | Ringoacid | MIT ライセンスの PDF 生成ライブラリ。日本語テキスト（TrueType サブセット埋め込み・禁則処理）、表、画像、図形、自動折り返し・自動改ページに対… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

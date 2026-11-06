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

## Latest list — 2026-11-06 00:19 UTC

New packages created between 2026-11-05 23:20 UTC and 2026-11-06 00:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-06T00-19-26-249278Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-05 23:31:31 | [DotCruz.Shared.Observability](https://www.nuget.org/packages/DotCruz.Shared.Observability) | 1.0.0 | Matheus Felipe @matheusfsc28 | Biblioteca compartilhada de observabilidade do ecossistema DotCruz: OpenTelemet… |
| 2026-11-05 23:36:04 | [Logfire.Fleet.Core.Native](https://www.nuget.org/packages/Logfire.Fleet.Core.Native) | 0.2.0 | Pydantic | The shared OpAMP client core for Logfire.Fleet.Client, compiled for each platfo… |
| 2026-11-05 23:36:05 | [Logfire.Fleet.Client](https://www.nuget.org/packages/Logfire.Fleet.Client) | 0.2.0 | Pydantic | An OpAMP client for .NET, on the shared OpAMP core (Rust, as a native library) |
| 2026-11-05 23:36:07 | [Logfire.Fleet.Extensions.Hosting](https://www.nuget.org/packages/Logfire.Fleet.Extensions.Hosting) | 0.2.0 | Pydantic | An OpenTelemetry .NET SDK set up in code (services.AddOpenTelemetry()) under an… |
| 2026-11-05 23:36:08 | [Logfire.Fleet.AutoInstrumentation](https://www.nuget.org/packages/Logfire.Fleet.AutoInstrumentation) | 0.2.0 | Pydantic | A plugin for OpenTelemetry .NET automatic instrumentation: the SDK under an OpA… |
| 2026-11-05 23:39:36 | [MediaToolkit.Vnc.Native.win-x64](https://www.nuget.org/packages/MediaToolkit.Vnc.Native.win-x64) | 0.9.15.2 | Rukhlov | libvncserver 0.9.15 shared native library for Windows x64: no TLS, Win32 thread… |
| 2026-11-05 23:41:51 | [BeeneticToolkit.Text](https://www.nuget.org/packages/BeeneticToolkit.Text) | 0.13.0 | Beenetic Studios | Text checks for player-entered text in games: a bad-word filter for names, stat… |
| 2026-11-05 23:42:49 | [Umbraco.Community.BackofficeTidy](https://www.nuget.org/packages/Umbraco.Community.BackofficeTidy) | 18.0.0 | Pascal Meyer | Hide Umbraco backoffice extensions by alias, per environment and user group, fr… |
| 2026-11-06 00:00:20 | [cints.CmdStarter](https://www.nuget.org/packages/cints.CmdStarter) | 1.0.0 | Jonathan Boivin, Norbert Ormá… | Turns plain C# classes and methods into a System.CommandLine command tree, with… |
| 2026-11-06 00:01:41 | [cints.CmdStarter.Hosting](https://www.nuget.org/packages/cints.CmdStarter.Hosting) | 1.0.0 | Jonathan Boivin, Norbert Ormá… | Generic Host (Microsoft.Extensions.Hosting) integration for CmdStarter. |
| 2026-11-06 00:05:27 | [ZipConvertCustomerBarCode.Drawing](https://www.nuget.org/packages/ZipConvertCustomerBarCode.Drawing) | 2.0.0 | cssho | カスタマバーコードを System.Drawing の Bitmap として描画する(Windows のみ) |
| 2026-11-06 00:05:28 | [ZipConvertCustomerBarCode](https://www.nuget.org/packages/ZipConvertCustomerBarCode) | 2.0.0 | cssho | 郵便番号・住所から日本郵便のカスタマバーコードを生成する(描画ライブラリ非依存) |
| 2026-11-06 00:05:29 | [ZipConvertCustomerBarCode.SkiaSharp](https://www.nuget.org/packages/ZipConvertCustomerBarCode.SkiaSharp) | 2.0.0 | cssho | カスタマバーコードを SkiaSharp で描画する(クロスプラットフォーム) |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

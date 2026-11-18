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

## Latest list — 2026-11-18 13:21 UTC

New packages created between 2026-11-18 12:19 UTC and 2026-11-18 13:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-18T13-21-57-076464Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-18 12:20:05 | [JaAddress](https://www.nuget.org/packages/JaAddress) | 0.3.0 | k14a | 日本の住所文字列を都道府県・市区町村・町字・丁目・番地に分けて正規化する .NET ライブラリ。geolonia/normalize-japanese-add… |
| 2026-11-18 12:20:06 | [JaAddress.DataBuilder](https://www.nuget.org/packages/JaAddress.DataBuilder) | 0.3.0 | k14a | JaAddress が使う住所データ（Geolonia 住所データ v2）を取得してローカルに保存する dotnet tool。 |
| 2026-11-18 12:20:49 | [Jakar.Collections](https://www.nuget.org/packages/Jakar.Collections) | 10.1.0 | Tyler Stegmaier | Observable, concurrent and pooled collections: ObservableCollection, Concurrent… |
| 2026-11-18 12:26:31 | [Ubiquiti.AirOs](https://www.nuget.org/packages/Ubiquiti.AirOs) | 1.0.0 | Ubiquiti.AirOs | .NET client library for managing Ubiquiti airOS devices over SSH: read and chan… |
| 2026-11-18 12:34:04 | [Retrace.Exit](https://www.nuget.org/packages/Retrace.Exit) | 0.1.0 | Aykut Mayali | Scan a .NET solution for Stackify Retrace usage and draft an OpenTelemetry migr… |
| 2026-11-18 12:38:00 | [Abblix.OIDC](https://www.nuget.org/packages/Abblix.OIDC) | 3.0.0 | Abblix LLP | The OAuth 2.0 and OpenID Connect vocabulary shared by Abblix OIDC Server and it… |
| 2026-11-18 12:38:04 | [Abblix.OIDC.Server.SharedSignals](https://www.nuget.org/packages/Abblix.OIDC.Server.SharedSignals) | 3.0.0 | Abblix LLP | Runs an Abblix Shared Signals transmitter on a multi-tenant Abblix OIDC Server:… |
| 2026-11-18 13:00:36 | [Burgr.Templates.Onion](https://www.nuget.org/packages/Burgr.Templates.Onion) | 1.10.0 | Damien Lechat | Burgr's complete template set: an ASP.NET Core API in onion architecture (Domai… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

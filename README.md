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

## Latest list — 2026-10-01 20:19 UTC

New packages created between 2026-10-01 19:19 UTC and 2026-10-01 20:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-01T20-19-23-04484Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-01 19:37:53 | [Brazilian.PrimitivesTypes.EntityFrameworkCore.PostgreSql](https://www.nuget.org/packages/Brazilian.PrimitivesTypes.EntityFrameworkCore.PostgreSql) | 1.3.0 | Rodrigo de Oliveira | Entity Framework Core PostgreSQL/Npgsql integration for Brazilian.PrimitivesTyp… |
| 2026-10-01 19:39:24 | [TextMagic](https://www.nuget.org/packages/TextMagic) | 1.0.1 | Shafqat Ahmed | Deterministic text layout without AI: turns answers, summaries and reports into… |
| 2026-10-01 19:42:10 | [Carbon.Cose](https://www.nuget.org/packages/Carbon.Cose) | 0.1.0 | Carbon.Cose | Package Description |
| 2026-10-01 19:44:14 | [Frostlake.FSharp](https://www.nuget.org/packages/Frostlake.FSharp) | 0.2.0 | MLorek | F# driver for Frostlake over its HTTP protocol: a pipeline query API, typed row… |
| 2026-10-01 19:45:25 | [Webority.QrCode](https://www.nuget.org/packages/Webority.QrCode) | 0.18.0 | Webority Technologies | Dependency-free QR code encoder: byte mode (UTF-8), versions 1 to 40, all eight… |
| 2026-10-01 19:55:28 | [ConfigDirector.ServerSdk.Testing](https://www.nuget.org/packages/ConfigDirector.ServerSdk.Testing) | 1.6.0 | ConfigDirector | Testing tools for the ConfigDirector server SDK: a real client over an in-memor… |
| 2026-10-01 19:59:05 | [udpping](https://www.nuget.org/packages/udpping) | 0.0.2 | Lee Harding | A `gping`-style latency grapher that probes over plain UDP echo (RFC 862) inste… |
| 2026-10-01 20:00:00 | [ConfigDirector.ServerSdk.AspNetCore.Testing](https://www.nuget.org/packages/ConfigDirector.ServerSdk.AspNetCore.Testing) | 1.6.0 | ConfigDirector | Registers a ConfigDirector test client with an ASP.NET Core application under t… |
| 2026-10-01 20:06:45 | [Tamp.Go](https://www.nuget.org/packages/Tamp.Go) | 0.1.0 | Scott Singleton | Wrapper for the go CLI — the Go toolchain build driver. Typed verb surface (Bui… |
| 2026-10-01 20:10:56 | [Gebze.Hamaliye](https://www.nuget.org/packages/Gebze.Hamaliye) | 1.0.0 | Erol ILHAN | Gebze Uygun Hamaliye - nakliyat cost calculator for Gebze, Kocaeli. Official si… |
| 2026-10-01 20:12:24 | [TKWF.Ext.MFA](https://www.nuget.org/packages/TKWF.Ext.MFA) | 0.1.0 | LoongBa.cn 龙爸出品 | TKWF 扩展：多因素认证（TOTP RFC 6238 自研 + 短信验证码双方法；绑定/解绑 + 挑战-验证流 + 尝试频控 + 恢复码；独立扩展零依赖——… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-19 05:20 UTC

New packages created between 2026-10-19 04:20 UTC and 2026-10-19 05:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-19T05-20-13-157722Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-19 04:22:05 | [Dora.Dapper.Dm](https://www.nuget.org/packages/Dora.Dapper.Dm) | 1.0.2 | Hwx | Dora.Dapper 达梦数据库驱动适配包 |
| 2026-10-19 04:23:16 | [Dora.Dapper.PostgreSql](https://www.nuget.org/packages/Dora.Dapper.PostgreSql) | 1.0.2 | Hwx | Dora.Dapper PostgreSQL 数据库驱动适配包 |
| 2026-10-19 04:24:07 | [KeyboardCore](https://www.nuget.org/packages/KeyboardCore) | 1.0.0 | Xioa_nu | Shared floating on-screen keyboard for WPF and Windows Forms, with numeric and… |
| 2026-10-19 04:32:21 | [ScanAndPay](https://www.nuget.org/packages/ScanAndPay) | 0.0.1 | Scan & Pay | Official Scan & Pay .NET SDK: accept PayTo PayID payments with QR code-based in… |
| 2026-10-19 04:53:18 | [SqlNative](https://www.nuget.org/packages/SqlNative) | 1.0.0 | Peyman Jahanbazi | Package Description |
| 2026-10-19 04:53:19 | [SqlNative.Core](https://www.nuget.org/packages/SqlNative.Core) | 1.0.0 | Peyman | Core helpers for SqlNative: engine identifier helpers, CLR type mappers, and th… |
| 2026-10-19 04:53:21 | [SqlNative.ModelGenerator](https://www.nuget.org/packages/SqlNative.ModelGenerator) | 1.0.0 | Peyman Jahanbazi | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

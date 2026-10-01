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

## Latest list — 2026-10-01 01:21 UTC

New packages created between 2026-10-01 00:22 UTC and 2026-10-01 01:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-01T01-21-42-012154Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-01 00:49:43 | [Smartstore.FFmpeg.Source](https://www.nuget.org/packages/Smartstore.FFmpeg.Source) | 9.0.2.1 | FFmpeg developers; SmartStore… | Complete corresponding sources, licenses, build scripts and per-RID configurati… |
| 2026-10-01 00:50:11 | [Defarm.Sdk](https://www.nuget.org/packages/Defarm.Sdk) | 0.1.0 | DeFarm | Official .NET SDK for the DeFarm partner API: ingestion (JSON rows, PNIB helper… |
| 2026-10-01 00:54:33 | [Webority.Security.Razor](https://www.nuget.org/packages/Webority.Security.Razor) | 0.12.0 | Webority Technologies | The browser half of Webority.Security.AspNetCore for Razor websites: public-for… |
| 2026-10-01 01:01:56 | [FullDevToolKit](https://www.nuget.org/packages/FullDevToolKit) | 1.0.0 | Carlos Fonteles | Library fundations for building applications, like websites, desktop and mobile… |
| 2026-10-01 01:15:09 | [Smartstore.wkhtmltopdf.Native.linux-arm64](https://www.nuget.org/packages/Smartstore.wkhtmltopdf.Native.linux-arm64) | 0.12.6.1 | SmartStore AG | Unmodified wkhtmltopdf 0.12.6.1 executable with patched Qt for Linux ARM64, fro… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

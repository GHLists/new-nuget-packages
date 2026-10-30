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

## Latest list — 2026-10-30 07:21 UTC

New packages created between 2026-10-30 06:19 UTC and 2026-10-30 07:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-30T07-21-25-019819Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-30 06:31:22 | [NewLife.Cube.Vue](https://www.nuget.org/packages/NewLife.Cube.Vue) | 1.0.2026.1030 | 新生命开发团队 | 魔方Vue前端皮肤包，基于Vue3+Element Plus，提供开箱即用的管理后台前端。支持动态菜单、字段元数据驱动的列表和表单、CRUD操作、OAuth登… |
| 2026-10-30 06:38:55 | [Sdcb.SimdCodecs.Bmp](https://www.nuget.org/packages/Sdcb.SimdCodecs.Bmp) | 1.1.0 | sdcb | Pure-managed BMP / DIB decoder and encoder for .NET, SIMD-accelerated (AVX2 / S… |
| 2026-10-30 06:38:59 | [Sdcb.SimdCodecs.Ico](https://www.nuget.org/packages/Sdcb.SimdCodecs.Ico) | 1.1.0 | sdcb | Pure-managed Windows icon (ICO) and cursor (CUR) decoder and encoder for .NET.… |
| 2026-10-30 06:56:17 | [RelayWA.Sdk](https://www.nuget.org/packages/RelayWA.Sdk) | 0.1.0 | RelayWA SDK contributors | Server-side RelayWA .NET SDK for WhatsApp messaging, session management, and we… |
| 2026-10-30 07:01:23 | [Corvus.Regex.Ecma262.CodeGeneration.Sources](https://www.nuget.org/packages/Corvus.Regex.Ecma262.CodeGeneration.Sources) | 1.0.9 | Endjin Limited | The Corvus.Regex.Ecma262 emitter as source: a code generator takes it to write… |
| 2026-10-30 07:07:07 | [Alcifra.Cli](https://www.nuget.org/packages/Alcifra.Cli) | 0.55.0 | saconsole | alcifra — administrative CLI for an Alcifra installation: sign in, provision te… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

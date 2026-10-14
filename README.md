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

## Latest list — 2026-10-14 07:21 UTC

New packages created between 2026-10-14 06:20 UTC and 2026-10-14 07:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-14T07-21-08-497818Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-14 06:22:46 | [ChsBuffer.SkiaSharp.Static.osx-x64](https://www.nuget.org/packages/ChsBuffer.SkiaSharp.Static.osx-x64) | 4.153.1 | ChsBuffer | SkiaSharp static library |
| 2026-10-14 06:22:52 | [ChsBuffer.SkiaSharp.Static.osx-arm64](https://www.nuget.org/packages/ChsBuffer.SkiaSharp.Static.osx-arm64) | 4.153.1 | ChsBuffer | SkiaSharp static library |
| 2026-10-14 06:26:48 | [ChsBuffer.Avalonia.Native.Static.osx-arm64](https://www.nuget.org/packages/ChsBuffer.Avalonia.Native.Static.osx-arm64) | 12.1.3 | ChsBuffer | AvaloniaNative static library for macOS NativeAOT |
| 2026-10-14 06:26:50 | [ChsBuffer.Avalonia.Native.Static.osx-x64](https://www.nuget.org/packages/ChsBuffer.Avalonia.Native.Static.osx-x64) | 12.1.3 | ChsBuffer | AvaloniaNative static library for macOS NativeAOT |
| 2026-10-14 06:26:57 | [ChsBuffer.SkiaSharp.Static](https://www.nuget.org/packages/ChsBuffer.SkiaSharp.Static) | 4.153.1 | ChsBuffer | Static SkiaSharp libraries for NativeAOT on all supported RIDs. |
| 2026-10-14 06:26:59 | [ChsBuffer.Avalonia.Native.Static](https://www.nuget.org/packages/ChsBuffer.Avalonia.Native.Static) | 12.1.3 | ChsBuffer | Static Avalonia.Native libraries for NativeAOT on all supported RIDs. |
| 2026-10-14 06:27:01 | [ChsBuffer.Angle.Static](https://www.nuget.org/packages/ChsBuffer.Angle.Static) | 2.1.27548.20260419 | ChsBuffer | Static Angle libraries for NativeAOT on all supported RIDs. |
| 2026-10-14 06:31:29 | [CodeBrix.WebGpu.Skia.MitLicenseForever](https://www.nuget.org/packages/CodeBrix.WebGpu.Skia.MitLicenseForever) | 1.0.287.390 | Jeremy Ellis | WebGPU rendering straight into SkiaSharp surfaces. Give it an SKSurface, an SKC… |
| 2026-10-14 06:31:48 | [CodeBrix.WebGpu.Graphics.MitLicenseForever](https://www.nuget.org/packages/CodeBrix.WebGpu.Graphics.MitLicenseForever) | 1.0.287.390 | Jeremy Ellis | A friendly graphics layer over WebGPU for .NET: one context object owning (or s… |
| 2026-10-14 07:04:33 | [IkeMtz.AspNetCore.OpenApi](https://www.nuget.org/packages/IkeMtz.AspNetCore.OpenApi) | 10.0.12-dev | Microsoft | Provides APIs for annotating route handler endpoints in ASP.NET Core with OpenA… |
| 2026-10-14 07:07:48 | [IdIot.Mqtt.Cloud](https://www.nuget.org/packages/IdIot.Mqtt.Cloud) | 1.3.3 | IdIot | Облачная сторона IdIot MQTT: несколько брокеров одновременно, реестр устройств… |
| 2026-10-14 07:07:51 | [IdIot.Mqtt.Cloud.Postgres](https://www.nuget.org/packages/IdIot.Mqtt.Cloud.Postgres) | 1.3.3 | IdIot | Хранилище облачного Hub IdIot MQTT на PostgreSQL и EF Core поверх существующего… |
| 2026-10-14 07:07:54 | [IdIot.Mqtt.Core](https://www.nuget.org/packages/IdIot.Mqtt.Core) | 1.3.3 | IdIot | Общая основа библиотек IdIot MQTT: wire-протокол v1, типизированные контракты,… |
| 2026-10-14 07:07:56 | [IdIot.Mqtt.Device](https://www.nuget.org/packages/IdIot.Mqtt.Device) | 1.3.3 | IdIot | Сторона устройства IdIot MQTT: один брокер, восстановление связи и подписок, во… |
| 2026-10-14 07:07:58 | [IdIot.Mqtt.Device.Sqlite](https://www.nuget.org/packages/IdIot.Mqtt.Device.Sqlite) | 1.3.3 | IdIot | Хранилище устройства IdIot MQTT на SQLite и EF Core поверх существующего DbCont… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-30 21:21 UTC

New packages created between 2026-10-30 20:19 UTC and 2026-10-30 21:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-30T21-21-23-639992Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-30 20:21:52 | [MonoChestnut.Data](https://www.nuget.org/packages/MonoChestnut.Data) | 0.1.0 | YvesShen | MonoChestnut 游戏引擎的游戏配置模型：数据类、JSON 读写（多态实体用 $type 区分）和带出错位置的校验。不依赖 MonoGame，供引擎和… |
| 2026-10-30 20:22:12 | [MonoChestnut.Rom](https://www.nuget.org/packages/MonoChestnut.Rom) | 0.1.0 | YvesShen | MonoChestnut 游戏引擎的 rom 格式：把配置和资源打包成压缩（Brotli）、加密（AES-256-GCM）、签名（ECDSA P-256）的单… |
| 2026-10-30 20:30:11 | [Decionis](https://www.nuget.org/packages/Decionis) | 0.3.0 | Decionis | Enterprise Decision Protocol SDK for policy-enforced .NET automation and verifi… |
| 2026-10-30 20:45:11 | [StrictSharp](https://www.nuget.org/packages/StrictSharp) | 1.0.22 | Felipe Alves | Library for code analisys to performance |
| 2026-10-30 21:00:02 | [T-mp.dotnet.Logging.Extensions.TestLogging](https://www.nuget.org/packages/T-mp.dotnet.Logging.Extensions.TestLogging) | 0.3.1-pre002 | T-mp.dotnet.Logging.Extension… | Logging Erweiterungen für Tests |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

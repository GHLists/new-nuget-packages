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

## Latest list — 2026-11-24 03:18 UTC

New packages created between 2026-11-24 02:21 UTC and 2026-11-24 03:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-24T03-18-57-945831Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-24 02:25:25 | [PortraitGeometry.EyeLine](https://www.nuget.org/packages/PortraitGeometry.EyeLine) | 0.1.0 | js-upup | Compute a portrait leveling rotation from two eye landmarks. Source-only C# con… |
| 2026-11-24 02:34:48 | [HandlerR](https://www.nuget.org/packages/HandlerR) | 1.0.0 | HandlerR Contributors | In-process message dispatcher: requests, notifications, streaming, pipeline beh… |
| 2026-11-24 02:35:21 | [HandlerR.Contracts](https://www.nuget.org/packages/HandlerR.Contracts) | 1.0.0 | HandlerR Contributors | Contracts package for requests, responses, and notifications. |
| 2026-11-24 02:35:35 | [HandlerR.FluentValidation](https://www.nuget.org/packages/HandlerR.FluentValidation) | 1.0.0 | HandlerR Contributors | Optional FluentValidation adapter for HandlerR. Implemented in-house; does not… |
| 2026-11-24 02:40:30 | [UrcConverter](https://www.nuget.org/packages/UrcConverter) | 0.2.1 | CloudHolic | URC (Universal Rhythm Chart) parser, serializer, playback rate scaler, and VSRG… |
| 2026-11-24 02:42:18 | [EasyAdminBlazor.Sms](https://www.nuget.org/packages/EasyAdminBlazor.Sms) | 2.7.0 | gudufy | EasyAdminBlazor 短信发送扩展：聚合阿里云、腾讯云、SendCloud 三家短信平台，纯 HTTP 实现（各平台签名自行计算），不引用任何官方… |
| 2026-11-24 03:06:23 | [Skywithin.Backlog](https://www.nuget.org/packages/Skywithin.Backlog) | 0.1.0 | Max Vagner | A markdown backlog in your repository (backlog/items/*.md with frontmatter) and… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

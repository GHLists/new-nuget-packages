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

## Latest list — 2026-09-28 02:22 UTC

New packages created between 2026-09-28 01:20 UTC and 2026-09-28 02:22 UTC.

[Full CSV](data/new-nuget-packages-2026-09-28T02-22-40-678972Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-28 01:27:14 | [MySvz.Framework.Domain.Core](https://www.nuget.org/packages/MySvz.Framework.Domain.Core) | 6.0.5-beta2 | liang.huang | 领域模型相关基础实现 |
| 2026-09-28 01:27:16 | [MySvz.Framework.IS4.Domain](https://www.nuget.org/packages/MySvz.Framework.IS4.Domain) | 6.0.5-beta2 | liang.huang | IdentityServer4 Domain |
| 2026-09-28 01:27:21 | [MySvz.Framework.Infrastructure.IntegrationEventService](https://www.nuget.org/packages/MySvz.Framework.Infrastructure.IntegrationEventService) | 6.0.5-beta2 | liang.huang | 集成事件服务 |
| 2026-09-28 01:27:24 | [MySvz.Framework.IS4.MongoDB](https://www.nuget.org/packages/MySvz.Framework.IS4.MongoDB) | 6.0.5-beta2 | liang.huang | IdentityServer4 Mongodb仓储 |
| 2026-09-28 01:29:02 | [StrictNet.Idempotency.AspNetCore](https://www.nuget.org/packages/StrictNet.Idempotency.AspNetCore) | 1.0.0 | Josh2406 | A light-weight, high-performance idempotency middleware for .NET APIs targeting… |
| 2026-09-28 01:47:45 | [PDFtoImage.Parallel](https://www.nuget.org/packages/PDFtoImage.Parallel) | 1.0.0-preview | David Sungaila | Renders PDF files in parallel by distributing PDFium work across isolated worke… |
| 2026-09-28 02:05:26 | [Gravicode.MediaPipeNet.Models.FaceStylizer](https://www.nuget.org/packages/Gravicode.MediaPipeNet.Models.FaceStylizer) | 1.0.0 | Gravicode Studios, Kang Fadhil | Face stylizer model for MediaPipe.NET: BlazeFaceStylizer color sketch (256x256)… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

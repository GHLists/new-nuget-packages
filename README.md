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

## Latest list — 2026-10-15 20:21 UTC

New packages created between 2026-10-15 19:21 UTC and 2026-10-15 20:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-15T20-21-20-477686Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-15 19:41:56 | [DotCourier.Outbox.EntityFrameworkCore](https://www.nuget.org/packages/DotCourier.Outbox.EntityFrameworkCore) | 0.8.0 | Valossa515 | Transactional outbox for DotCourier on EF Core: notifications are stored in the… |
| 2026-10-15 19:47:39 | [Cackle.FedEx.Tracking](https://www.nuget.org/packages/Cackle.FedEx.Tracking) | 2.1.1 | Will Branch | Client for the FedEx Basic Integrated Visibility (formerly Track API) REST API:… |
| 2026-10-15 20:02:32 | [Respire.Resilience](https://www.nuget.org/packages/Respire.Resilience) | 0.9.0 | Tom Hurst | Run Respire operations through Polly v8 resilience pipelines with one command r… |
| 2026-10-15 20:02:35 | [Respire.Streaming.Dashboard](https://www.nuget.org/packages/Respire.Streaming.Dashboard) | 0.9.0 | Tom Hurst | Authorized ASP.NET Core operator dashboard for Redis streams and reliable job q… |
| 2026-10-15 20:07:30 | [DotCourier.Kafka](https://www.nuget.org/packages/DotCourier.Kafka) | 0.8.0 | Valossa515 | Delivers DotCourier's transactional outbox to Kafka: the stored events are publ… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

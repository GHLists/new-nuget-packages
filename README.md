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

## Latest list — 2026-10-06 02:20 UTC

New packages created between 2026-10-06 01:21 UTC and 2026-10-06 02:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-06T02-20-29-047353Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-06 01:59:49 | [Waybill](https://www.nuget.org/packages/Waybill) | 0.1.0-alpha | Joseleno | Transactional outbox and inbox for .NET: the event written with your data reach… |
| 2026-10-06 01:59:49 | [Waybill.Testing](https://www.nuget.org/packages/Waybill.Testing) | 0.1.0-alpha | Joseleno | Test doubles for Waybill: an in-memory outbox and inbox with assertions, so app… |
| 2026-10-06 01:59:50 | [Waybill.RabbitMQ](https://www.nuget.org/packages/Waybill.RabbitMQ) | 0.1.0-alpha | Joseleno | RabbitMQ transport for Waybill: publisher confirms, persistent messages and man… |
| 2026-10-06 01:59:51 | [Waybill.EntityFrameworkCore.PostgreSql](https://www.nuget.org/packages/Waybill.EntityFrameworkCore.PostgreSql) | 0.1.0-alpha | Joseleno | EF Core and PostgreSQL persistence for Waybill: outbox capture in the same tran… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

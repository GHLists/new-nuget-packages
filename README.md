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

## Latest list — 2026-11-01 09:21 UTC

New packages created between 2026-11-01 08:20 UTC and 2026-11-01 09:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-01T09-21-05-415194Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-01 08:42:44 | [Qryx.Expressions](https://www.nuget.org/packages/Qryx.Expressions) | 1.0.1 | Abdumannon Şamsiyev | High-performance dynamic expression tree building, AST synthesis, and compiled… |
| 2026-11-01 08:42:44 | [Qryx.OpenApi](https://www.nuget.org/packages/Qryx.OpenApi) | 1.0.0 | Abdumannon Şamsiyev | .NET 10 Microsoft.AspNetCore.OpenApi schema transformer for Qryx query DTOs. |
| 2026-11-01 08:42:45 | [Qryx.AspNetCore](https://www.nuget.org/packages/Qryx.AspNetCore) | 1.0.1 | Abdumannon Şamsiyev | ASP.NET Core Minimal APIs and MVC integration, high-performance query string mo… |
| 2026-11-01 08:42:45 | [Qryx.EntityFramework](https://www.nuget.org/packages/Qryx.EntityFramework) | 1.0.1 | Abdumannon Şamsiyev | Entity Framework Core integration for Qryx: keyset cursor pagination, projectio… |
| 2026-11-01 08:42:46 | [Qryx.Swashbuckle](https://www.nuget.org/packages/Qryx.Swashbuckle) | 1.0.0 | Abdumannon Şamsiyev | Classic Swashbuckle SwaggerGen operation and parameter filters for Qryx query D… |
| 2026-11-01 08:42:47 | [Qryx.Core](https://www.nuget.org/packages/Qryx.Core) | 1.0.1 | Abdumannon Şamsiyev | Core declarative attributes ([Filter], [Sortable]), contracts (IQryxRequest), a… |
| 2026-11-01 08:42:47 | [Qryx.SourceGenerator](https://www.nuget.org/packages/Qryx.SourceGenerator) | 1.0.0 | Abdumannon Şamsiyev | Compile-time Roslyn Incremental Source Generator for Qryx query DTOs with 0.00… |
| 2026-11-01 08:46:16 | [KitStack.Seeding](https://www.nuget.org/packages/KitStack.Seeding) | 0.1.0 | ghaith100994 | Ordered, idempotent seeding runner for .NET: seed file sources (content folder,… |
| 2026-11-01 08:46:18 | [KitStack.Seeding.Abstractions](https://www.nuget.org/packages/KitStack.Seeding.Abstractions) | 0.1.0 | ghaith100994 | Abstractions for KitStack.Seeding: ISeeder, ISeederRunner, ISeedFileSource, fai… |
| 2026-11-01 08:46:19 | [KitStack.Seeding.EntityFrameworkCore](https://www.nuget.org/packages/KitStack.Seeding.EntityFrameworkCore) | 0.1.0 | ghaith100994 | EF Core seeders for KitStack.Seeding: insert-if-empty JSON seeders, additive na… |
| 2026-11-01 08:53:02 | [Dora.Shared.Repository](https://www.nuget.org/packages/Dora.Shared.Repository) | 1.0.1 | Hwx | Package Description |
| 2026-11-01 08:53:32 | [Dora.Shared.Auth](https://www.nuget.org/packages/Dora.Shared.Auth) | 1.0.1 | Hwx | Package Description |
| 2026-11-01 08:54:01 | [Dora.Shared.Redis](https://www.nuget.org/packages/Dora.Shared.Redis) | 1.0.1 | Hwx | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

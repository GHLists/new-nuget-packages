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

## Latest list — 2026-10-07 08:20 UTC

New packages created between 2026-10-07 07:20 UTC and 2026-10-07 08:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-07T08-20-52-219279Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-07 07:23:41 | [Inheto](https://www.nuget.org/packages/Inheto) | 1.0.0 | alt160 | A .NET-native, low-allocation binary serializer with shared and circular refere… |
| 2026-10-07 07:26:24 | [JorgeCostaMacia.Http.ForwardedHeaders](https://www.nuget.org/packages/JorgeCostaMacia.Http.ForwardedHeaders) | 4.1.0 | JorgeCostaMacia | Default forwarded-headers policy for a service behind a reverse proxy on the sa… |
| 2026-10-07 07:47:44 | [Orbyss.Foundation.Authentication.Core](https://www.nuget.org/packages/Orbyss.Foundation.Authentication.Core) | 0.3.0 | Orbyss | Provider-neutral validated account identity and authentication protocol constan… |
| 2026-10-07 07:47:48 | [Orbyss.Foundation.Collections.Core](https://www.nuget.org/packages/Orbyss.Foundation.Collections.Core) | 0.3.0 | Orbyss | Owned ordered collection values with structural equality. |
| 2026-10-07 07:47:52 | [Orbyss.Foundation.Execution](https://www.nuget.org/packages/Orbyss.Foundation.Execution) | 0.3.0 | Orbyss | TimeProvider-backed monotonic operation deadlines and shell registration. |
| 2026-10-07 07:47:53 | [Orbyss.Foundation.Execution.Core](https://www.nuget.org/packages/Orbyss.Foundation.Execution.Core) | 0.3.0 | Orbyss | Provider-neutral monotonic operation deadline contracts. |
| 2026-10-07 07:47:58 | [Orbyss.Foundation.PostgreSql](https://www.nuget.org/packages/Orbyss.Foundation.PostgreSql) | 0.3.0 | Orbyss | Shell-owned PostgreSQL datasources, nonpooled EF context units and native deadl… |
| 2026-10-07 07:48:04 | [Orbyss.Foundation.Web.ProblemDetails.Core](https://www.nuget.org/packages/Orbyss.Foundation.Web.ProblemDetails.Core) | 0.3.0 | Orbyss | Framework-neutral bounded problem definitions and application mapping contracts. |
| 2026-10-07 07:54:16 | [WrapPro](https://www.nuget.org/packages/WrapPro) | 1.0.0 | Winnigames2024 | WrapPro |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

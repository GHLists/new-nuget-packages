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

## Latest list — 2026-10-23 13:23 UTC

New packages created between 2026-10-23 12:20 UTC and 2026-10-23 13:23 UTC.

[Full CSV](data/new-nuget-packages-2026-10-23T13-23-52-099249Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-23 12:38:03 | [WordReplace.Core](https://www.nuget.org/packages/WordReplace.Core) | 1.0.0 | WordReplace.Core | Package Description |
| 2026-10-23 12:41:19 | [Hexalith.Parties.Aspire](https://www.nuget.org/packages/Hexalith.Parties.Aspire) | 1.6.0 | Hexalith Contributors | Aspire composition helper for the Hexalith Parties domain service. The server i… |
| 2026-10-23 12:53:41 | [SyZero.AI](https://www.nuget.org/packages/SyZero.AI) | 10.0.0 | HaitaoJin | Package Description |
| 2026-10-23 12:53:54 | [Octeka.Networking.Http.Rest](https://www.nuget.org/packages/Octeka.Networking.Http.Rest) | 2.0.0 | Patrick Robichaud | High-performance, zero-allocation, resilient REST client framework for modern .… |
| 2026-10-23 12:53:56 | [Octeka.Networking.Http.Rest.Extensions.ActivitySource](https://www.nuget.org/packages/Octeka.Networking.Http.Rest.Extensions.ActivitySource) | 2.0.0 | Patrick Robichaud | OpenTelemetry and System.Diagnostics.ActivitySource observability extensions fo… |
| 2026-10-23 12:53:56 | [Octeka.Networking.Http.Rest.Abstractions](https://www.nuget.org/packages/Octeka.Networking.Http.Rest.Abstractions) | 2.0.0 | Patrick Robichaud | Core abstractions, interfaces, and contracts for the Octeka.Networking.Http.Res… |
| 2026-10-23 12:53:57 | [Octeka.Networking.Http.Rest.QueryString](https://www.nuget.org/packages/Octeka.Networking.Http.Rest.QueryString) | 2.0.0 | Patrick Robichaud | High-performance, allocation-free query string builder and parameter serializer… |
| 2026-10-23 12:53:57 | [SyZero.Notifications](https://www.nuget.org/packages/SyZero.Notifications) | 10.0.0 | HaitaoJin | SyZero 统一通知编排，支持邮件、短信及可扩展通道。 |
| 2026-10-23 12:53:57 | [Octeka.Networking.Http.Rest.QueryString.Abstractions](https://www.nuget.org/packages/Octeka.Networking.Http.Rest.QueryString.Abstractions) | 2.0.0 | Patrick Robichaud | Abstractions and interfaces for query string builders and converters in Octeka.… |
| 2026-10-23 13:03:43 | [Transferetto.Cli](https://www.nuget.org/packages/Transferetto.Cli) | 2.0.2 | Transferetto.Cli | Command-line file and object transfers through Transferetto endpoints. |
| 2026-10-23 13:17:25 | [Engobe.Core](https://www.nuget.org/packages/Engobe.Core) | 2.0.0 | Marcel Kummerow | Core engine of the Engobe static site generator (build, serve, scaffold, deploy… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

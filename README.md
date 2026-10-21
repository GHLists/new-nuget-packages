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

## Latest list — 2026-10-21 02:20 UTC

New packages created between 2026-10-21 01:20 UTC and 2026-10-21 02:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-21T02-20-20-239233Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-21 01:23:59 | [Inertia.Net.Templates](https://www.nuget.org/packages/Inertia.Net.Templates) | 1.4.0 | Inertia.Net contributors | dotnet new templates for Inertia.js v3 apps on ASP.NET Core with Inertia.Net: R… |
| 2026-10-21 01:55:10 | [HYS.Core.MassTransit](https://www.nuget.org/packages/HYS.Core.MassTransit) | 3.1.0 | HYS | HYS.Core MassTransit 消息基础设施模块，提供 RabbitMQ + EF Core Transactional Outbox 集成 |
| 2026-10-21 01:55:38 | [HYS.Core.OpenTelemetry](https://www.nuget.org/packages/HYS.Core.OpenTelemetry) | 3.1.0 | yyl | OpenTelemetry 可观测性基础设施，支持 Traces、Metrics、Logs 三大支柱 |
| 2026-10-21 01:59:24 | [CCP.RoleAccessScanner](https://www.nuget.org/packages/CCP.RoleAccessScanner) | 1.0.0 | CCP Team | Scan and log ASP.NET Core controller/action/role info to centralized database. |
| 2026-10-21 02:05:56 | [Authsignal.Maui](https://www.nuget.org/packages/Authsignal.Maui) | 0.1.0 | Authsignal | Authsignal SDK for .NET MAUI. Wraps the Authsignal iOS and Android SDKs. |
| 2026-10-21 02:05:58 | [Authsignal.Maui.Binding.iOS](https://www.nuget.org/packages/Authsignal.Maui.Binding.iOS) | 0.1.0 | Authsignal | Native iOS binding used by Authsignal.Maui. Reference Authsignal.Maui instead. |
| 2026-10-21 02:06:01 | [Authsignal.Maui.Binding.Android](https://www.nuget.org/packages/Authsignal.Maui.Binding.Android) | 0.1.0 | Authsignal | Native Android binding used by Authsignal.Maui. Reference Authsignal.Maui inste… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

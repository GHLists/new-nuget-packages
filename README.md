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

## Latest list — 2026-11-13 18:19 UTC

New packages created between 2026-11-13 17:20 UTC and 2026-11-13 18:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-13T18-19-14-058512Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-13 17:22:05 | [AWS.OCI.Builder](https://www.nuget.org/packages/AWS.OCI.Builder) | 0.5.0 | Amazon Web Services | A .NET library for building OCI container images programmatically — overlay loc… |
| 2026-11-13 17:35:26 | [Umbraco.Community.ModelAliases](https://www.nuget.org/packages/Umbraco.Community.ModelAliases) | 1.0.0 | Matt Bliss | Generates a constants class of property aliases for every Umbraco Models Builde… |
| 2026-11-13 17:46:04 | [FclEx.Kafka](https://www.nuget.org/packages/FclEx.Kafka) | 2.4.8 | huoshan12345 | Kafka consumer helpers with explicit offset commits, JSON deserializers, header… |
| 2026-11-13 17:46:05 | [FclEx.RabbitMQ](https://www.nuget.org/packages/FclEx.RabbitMQ) | 2.4.8 | huoshan12345 | RabbitMQ publishers, consumers, and conversion routers with automatic quorum to… |
| 2026-11-13 17:59:03 | [Harp.Behavior.App](https://www.nuget.org/packages/Harp.Behavior.App) | 3.4.0 | harp-tech | App for configuring and testing Harp Behavior devices. |
| 2026-11-13 17:59:46 | [SvdGenerator](https://www.nuget.org/packages/SvdGenerator) | 1.0.0 | Thomas Legrand | Generates typed C++ peripheral headers for ARM Cortex-M targets from a CMSIS-SV… |
| 2026-11-13 18:01:42 | [Sondor.Observability](https://www.nuget.org/packages/Sondor.Observability) | 0.1.0 | Sondor Dev | OpenTelemetry for services, configured from configuration: tracing, metrics and… |
| 2026-11-13 18:04:22 | [Sang.Service.TallyIntegration](https://www.nuget.org/packages/Sang.Service.TallyIntegration) | 1.0.1 | Sang.Service.TallyIntegration | A typical library application designed to Integrate Tally |
| 2026-11-13 18:08:42 | [DevelApp.ErpLight.Plugin.Finance](https://www.nuget.org/packages/DevelApp.ErpLight.Plugin.Finance) | 1.0.0 | DevelApp.ai | Finance module plugin for ErpLight ERP system. Provides invoice management, pay… |
| 2026-11-13 18:08:42 | [DevelApp.ErpLight.Plugin.Inventory](https://www.nuget.org/packages/DevelApp.ErpLight.Plugin.Inventory) | 1.0.0 | DevelApp.ai | Inventory management plugin for ErpLight ERP system. Provides stock tracking, p… |
| 2026-11-13 18:08:43 | [DevelApp.ErpLight.Plugin.Orders](https://www.nuget.org/packages/DevelApp.ErpLight.Plugin.Orders) | 1.0.0 | DevelApp.ai | Orders management plugin for ErpLight ERP system. Provides order lifecycle mana… |
| 2026-11-13 18:08:43 | [DevelApp.ErpLight.Plugin.Products](https://www.nuget.org/packages/DevelApp.ErpLight.Plugin.Products) | 1.0.0 | DevelApp.ai | Products catalog plugin for ErpLight ERP system. Provides product catalog manag… |
| 2026-11-13 18:08:44 | [DevelApp.ErpLight.SharedKernel](https://www.nuget.org/packages/DevelApp.ErpLight.SharedKernel) | 1.0.0 | DevelApp.ai | Shared kernel for ErpLight plugin system providing common domain events, interf… |
| 2026-11-13 18:09:48 | [Anarchy.Toolkit.Build.Cli](https://www.nuget.org/packages/Anarchy.Toolkit.Build.Cli) | 1.0.0 | Leandro M. Medeiros | Command-line foundations for Anarchy solutions: starter solution scaffolding, b… |
| 2026-11-13 18:09:49 | [Anarchy.Toolkit.Build.Cli.Tool](https://www.nuget.org/packages/Anarchy.Toolkit.Build.Cli.Tool) | 1.0.0 | Leandro M. Medeiros | The anarchy-toolkit command: bootstrap Anarchy-based .NET solutions and scaffol… |
| 2026-11-13 18:11:41 | [PhotoMapStudio.Tiles](https://www.nuget.org/packages/PhotoMapStudio.Tiles) | 0.1.0 | scottlz0310 | 地図タイル（ラスター・ベクター MVT・PMTiles）の取得・キャッシュ・レート制御・デコード。描画には依存しない。 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-16 19:20 UTC

New packages created between 2026-10-16 18:19 UTC and 2026-10-16 19:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-16T19-20-35-277934Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-16 18:21:44 | [CData.OracleHCM.EntityFrameworkCore10](https://www.nuget.org/packages/CData.OracleHCM.EntityFrameworkCore10) | 26.0.9770 | CData Software, Inc. | Enables you to use standard drivers to connect to Oracle Fusion Cloud HCM objec… |
| 2026-10-16 18:22:46 | [TSpec.Architecture.CSharp](https://www.nuget.org/packages/TSpec.Architecture.CSharp) | 1.0.0 | Joakim Sigvald | Architecture rules on the code of a TSpec build: each project's source files an… |
| 2026-10-16 18:23:19 | [WoW2.Sdk.Beta.Be.Testing](https://www.nuget.org/packages/WoW2.Sdk.Beta.Be.Testing) | 10.0.67-beta | WoW Two | WoW Two be sdk test helpers (beta-forever mono-lib) — assertions, fakes, Verify… |
| 2026-10-16 18:23:22 | [WoW2.Sdk.Beta.Be.Data.Abstractions](https://www.nuget.org/packages/WoW2.Sdk.Beta.Be.Data.Abstractions) | 10.0.67-beta | WoW Two | WoW Two be sdk data abstractions (beta-forever) — BCL-only entity/repository co… |
| 2026-10-16 18:23:24 | [WoW2.Sdk.Beta.Be.Data.Migrations.Cli](https://www.nuget.org/packages/WoW2.Sdk.Beta.Be.Data.Migrations.Cli) | 10.0.67-beta | WoW Two | Web-free SQL migrator CLI (`wow-migrate`) over the WoW Two be sdk bespoke migra… |
| 2026-10-16 18:24:02 | [CData.SAPBusinessWarehouse](https://www.nuget.org/packages/CData.SAPBusinessWarehouse) | 26.0.9770 | CData Software, Inc. | The CData SAP Business Warehouse Data Provider allows you to connect to SAP Bus… |
| 2026-10-16 18:24:03 | [CData.SAPBusinessWarehouse.EntityFrameworkCore8](https://www.nuget.org/packages/CData.SAPBusinessWarehouse.EntityFrameworkCore8) | 26.0.9770 | CData Software, Inc. | The CData SAP Business Warehouse Data Provider allows you to connect to SAP Bus… |
| 2026-10-16 18:24:05 | [CData.SAPBusinessWarehouse.EntityFrameworkCore10](https://www.nuget.org/packages/CData.SAPBusinessWarehouse.EntityFrameworkCore10) | 26.0.9770 | CData Software, Inc. | The CData SAP Business Warehouse Data Provider allows you to connect to SAP Bus… |
| 2026-10-16 18:25:50 | [CData.Square.EntityFrameworkCore10](https://www.nuget.org/packages/CData.Square.EntityFrameworkCore10) | 26.0.9770 | CData Software, Inc. | Enables you to use standard drivers to access the Square Connect API |
| 2026-10-16 18:39:01 | [UnicoreSoftwareSolutions.Base.Data](https://www.nuget.org/packages/UnicoreSoftwareSolutions.Base.Data) | 1.0.0 | Unicore Software Solutions | Package Description |
| 2026-10-16 18:45:22 | [BorrowedTorch.UIDPGenerator](https://www.nuget.org/packages/BorrowedTorch.UIDPGenerator) | 1.0.0 | Pysarenko Vladyslav | Generates BorrowedTorch.UI dependency properties and style classes from .dpg fi… |
| 2026-10-16 18:50:02 | [UnicoreSoftwareSolutions.Base.Business](https://www.nuget.org/packages/UnicoreSoftwareSolutions.Base.Business) | 1.0.0 | Unicore Software Solutions | Package Description |
| 2026-10-16 19:07:42 | [AkkaFsiMcpServer](https://www.nuget.org/packages/AkkaFsiMcpServer) | 1.4.2 | AkkaFsiMcpServer | Package Description |
| 2026-10-16 19:08:16 | [AkkaFsiMcpServer.ProcSupervisorHost](https://www.nuget.org/packages/AkkaFsiMcpServer.ProcSupervisorHost) | 1.571.101.400-win34 | AkkaFsiMcpServer.ProcSupervis… | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

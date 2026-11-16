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

## Latest list — 2026-11-16 14:20 UTC

New packages created between 2026-11-16 13:19 UTC and 2026-11-16 14:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-16T14-20-01-829604Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-16 13:25:18 | [Cratis.Grip.Kits](https://www.nuget.org/packages/Cratis.Grip.Kits) | 1.0.0 | Cratis | The build kit format of Cratis Studio builders: the build-kit.yaml manifest sch… |
| 2026-11-16 13:25:18 | [Cratis.Grip.Contract](https://www.nuget.org/packages/Cratis.Grip.Contract) | 1.0.0 | Cratis | The build contract between Cratis Studio and a builder: the build order Studio… |
| 2026-11-16 13:33:04 | [FluentPropagation](https://www.nuget.org/packages/FluentPropagation) | 1.0.0 | FluentPropagation | Package Description |
| 2026-11-16 13:37:18 | [AbpConnections.HttpApi](https://www.nuget.org/packages/AbpConnections.HttpApi) | 0.8.2 | AbpGuard contributors | AbpConnections.HttpApi: connections over HTTP under api/connections. Kinds, a s… |
| 2026-11-16 13:37:18 | [AbpConnections](https://www.nuget.org/packages/AbpConnections) | 0.8.2 | AbpGuard contributors | AbpConnections: connections to outside systems for an ABP app on .NET 10 and EF… |
| 2026-11-16 13:56:25 | [Solhigson.Admin](https://www.nuget.org/packages/Solhigson.Admin) | 10.0.0 | Solhigson | Admin screens for Solhigson apps as Razor components, rendered on the server. A… |
| 2026-11-16 13:59:35 | [Meziantou.Framework.Pdf.JavaScript](https://www.nuget.org/packages/Meziantou.Framework.Pdf.JavaScript) | 1.0.0 | meziantou | Runs the scripts of the interactive forms of Meziantou.Framework.Pdf in a sandb… |
| 2026-11-16 14:01:06 | [Microsoft.FluentUI.AspNetCore.Components.Charts](https://www.nuget.org/packages/Microsoft.FluentUI.AspNetCore.Components.Charts) | 5.1.0 | Microsoft | A set of Blazor components wrapping an extended version of the Fluent UI Chart… |
| 2026-11-16 14:02:52 | [Hmz.Core.Mcp](https://www.nuget.org/packages/Hmz.Core.Mcp) | 0.1.0 | Hmz | Exposes Minimal API endpoints as permission-filtered MCP tools by re-dispatchin… |
| 2026-11-16 14:02:53 | [Hmz.Core.Notifications](https://www.nuget.org/packages/Hmz.Core.Notifications) | 0.1.0 | Hmz | In-app notification engine for Hmz backends on EF Core and PostgreSQL: deduplic… |
| 2026-11-16 14:02:54 | [Hmz.Core.Notifications.Abstractions](https://www.nuget.org/packages/Hmz.Core.Notifications.Abstractions) | 0.1.0 | Hmz | Contracts of the Hmz in-app notification engine: notification types, audience r… |
| 2026-11-16 14:06:27 | [GroupDocs.Search.Net100](https://www.nuget.org/packages/GroupDocs.Search.Net100) | 26.11.0 | Aspose | Runtime assemblies for GroupDocs.Search targeting .NET 10.0. Install directly o… |
| 2026-11-16 14:07:33 | [GroupDocs.Search.Net462](https://www.nuget.org/packages/GroupDocs.Search.Net462) | 26.11.0 | Aspose | Runtime assemblies for GroupDocs.Search targeting .NET Framework 4.6.2. Install… |
| 2026-11-16 14:08:18 | [GroupDocs.Search.Net48](https://www.nuget.org/packages/GroupDocs.Search.Net48) | 26.11.0 | Aspose | Runtime assemblies for GroupDocs.Search targeting .NET Framework 4.8. Install d… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

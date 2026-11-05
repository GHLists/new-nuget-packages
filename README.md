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

## Latest list — 2026-11-05 11:20 UTC

New packages created between 2026-11-05 10:21 UTC and 2026-11-05 11:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-05T11-20-10-930325Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-05 10:24:31 | [DataverseStorageCostReducer](https://www.nuget.org/packages/DataverseStorageCostReducer) | 1.0.0 | Apoorv Gupta | Cut Microsoft Dataverse storage costs by 20% to 60%. Audit storage bloat, Paret… |
| 2026-11-05 10:25:02 | [EffectivePermissionsInspector](https://www.nuget.org/packages/EffectivePermissionsInspector) | 1.0.0 | Apoorv Gupta | Diagnose 'Why Can't John Edit This Record?' in Microsoft Dataverse across Secur… |
| 2026-11-05 10:27:52 | [TCIS.MCP.Docs](https://www.nuget.org/packages/TCIS.MCP.Docs) | 1.0.9 | TCIS Core Community and Contr… | TCIS Core Framework is an application framework for building modular, multi-ten… |
| 2026-11-05 10:28:57 | [Likvido.Http](https://www.nuget.org/packages/Likvido.Http) | 1.0.0 | Likvido.Http | HTTP client helpers for Likvido services, including a guard for server-side fet… |
| 2026-11-05 10:29:34 | [QueryKrafter.Core](https://www.nuget.org/packages/QueryKrafter.Core) | 1.0.0 | Matt Gordon | The QueryKrafter rule model, shared by the browser and the server: jQuery Query… |
| 2026-11-05 10:29:41 | [QueryKrafter.Components](https://www.nuget.org/packages/QueryKrafter.Components) | 1.0.0 | Matt Gordon | The QueryKrafter query builder component, for Blazor Server, Blazor WebAssembly… |
| 2026-11-05 10:32:09 | [Cratis.Arc.Neo4j.Testing](https://www.nuget.org/packages/Cratis.Arc.Neo4j.Testing) | 22.168.0 | Cratis | Testing utilities for Cratis Arc applications that read a Neo4j graph: substitu… |
| 2026-11-05 10:32:10 | [Cratis.Arc.Neo4j](https://www.nuget.org/packages/Cratis.Arc.Neo4j) | 22.168.0 | Cratis | Tenant-aware Neo4j graph access for Cratis Arc: pooled drivers, graph database… |
| 2026-11-05 10:37:34 | [BIMPlugins.UI](https://www.nuget.org/packages/BIMPlugins.UI) | 1.0.4 | Samir Shibliev | Fluent extension methods to build the Autodesk Revit ribbon: panels, push, pull… |
| 2026-11-05 10:42:54 | [LoomEditor.Avalonia](https://www.nuget.org/packages/LoomEditor.Avalonia) | 0.5.0 | LoomEditor contributors | LoomEditor: a native, Native AOT-compatible code editor control for Avalonia, p… |
| 2026-11-05 10:48:17 | [En16931](https://www.nuget.org/packages/En16931) | 0.1.0 | Jonas Fassbender | .NET implementation of the EN16931:2017 data model and the two mandatory syntax… |
| 2026-11-05 10:59:00 | [LeoSouzaDev.Comex.GeneradorRelatorio](https://www.nuget.org/packages/LeoSouzaDev.Comex.GeneradorRelatorio) | 1.0.0 | SeuNomeRealOuUsuario | Biblioteca de classes desacoplada para exportação de relatórios em CSV para o e… |
| 2026-11-05 11:02:26 | [PlatformHeads.Mac](https://www.nuget.org/packages/PlatformHeads.Mac) | 0.14.0 | https://github.com/SimonCropp… | The macOS tray of an app with one head per platform: a status item in the menu… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

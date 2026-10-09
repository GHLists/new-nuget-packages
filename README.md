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

## Latest list — 2026-10-09 05:18 UTC

New packages created between 2026-10-09 04:18 UTC and 2026-10-09 05:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-09T05-18-42-899726Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-09 04:28:37 | [LumoAuth](https://www.nuget.org/packages/LumoAuth) | 1.0.0 | LumoAuth | The official LumoAuth SDK for .NET: RBAC, Zanzibar and ABAC authorization check… |
| 2026-10-09 04:28:48 | [LumoAuth.AspNetCore](https://www.nuget.org/packages/LumoAuth.AspNetCore) | 1.0.0 | LumoAuth | ASP.NET Core integration for the LumoAuth SDK: dependency injection from config… |
| 2026-10-09 04:28:51 | [NSail.Messaging.Sse](https://www.nuget.org/packages/NSail.Messaging.Sse) | 0.1.65 | Leonardo Porro,Emmanuel Arias | NSail.Messaging.Sse, part of NSail Stack: a .NET modular-monolith framework (me… |
| 2026-10-09 04:42:59 | [DotNetCore.AiguilleUnit.Serialization](https://www.nuget.org/packages/DotNetCore.AiguilleUnit.Serialization) | 1.3.0 | DotNetCore.AiguilleUnit.Seria… | DotNetCore AiguilleUnit Serialization unit library |
| 2026-10-09 04:43:03 | [DotNetCore.AiguilleUnit.Serialization.NewtonsoftJson](https://www.nuget.org/packages/DotNetCore.AiguilleUnit.Serialization.NewtonsoftJson) | 1.3.0 | DotNetCore.AiguilleUnit.Seria… | DotNetCore AiguilleUnit Newtonsoft.Json serialization support |
| 2026-10-09 04:44:50 | [PluginExtension.Common](https://www.nuget.org/packages/PluginExtension.Common) | 1.0.0 | Xanvil | 插件包管理：浏览/安装/卸载基于Nuget包格式的插件包 |
| 2026-10-09 05:00:44 | [Cratis.Screenplay.Contracts](https://www.nuget.org/packages/Cratis.Screenplay.Contracts) | 4.103.0 | all contributors | Machine-readable Screenplay language and tool contract, independent of an MCP c… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

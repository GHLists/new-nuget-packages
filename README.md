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

## Latest list — 2026-10-24 08:20 UTC

New packages created between 2026-10-24 07:18 UTC and 2026-10-24 08:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-24T08-20-13-059721Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-24 07:28:48 | [Davish.JustBdd](https://www.nuget.org/packages/Davish.JustBdd) | 0.2.0 | David Chen | Given / When / Then scenarios as plain C# lambdas: a lazy step chain that recor… |
| 2026-10-24 07:28:49 | [Davish.JustBdd.XunitV3](https://www.nuget.org/packages/Davish.JustBdd.XunitV3) | 0.2.0 | David Chen | xUnit v3 integration for Davish.JustBdd: xUnit assertions that chain after Then… |
| 2026-10-24 07:28:49 | [Davish.JustBdd.Tool](https://www.nuget.org/packages/Davish.JustBdd.Tool) | 0.2.0 | David Chen | Renders the CTRF files of several test projects (dotnet test --report-xunit-ctr… |
| 2026-10-24 07:29:30 | [AIGuiders.DotNetWorkspace.Core](https://www.nuget.org/packages/AIGuiders.DotNetWorkspace.Core) | 0.1.1 | Dmitry Karataev,AIGuiders | Solution/project graph IR (.slnx/.sln/.csproj/.fsproj) for federation hosts (Ro… |
| 2026-10-24 07:44:53 | [OceanBaseConnector](https://www.nuget.org/packages/OceanBaseConnector) | 0.1.0 | OceanBaseConnector contributo… | Experimental managed ADO.NET provider for OceanBase MySQL and Oracle compatibil… |
| 2026-10-24 07:44:54 | [OceanBaseConnector.DependencyInjection](https://www.nuget.org/packages/OceanBaseConnector.DependencyInjection) | 0.1.0 | OceanBaseConnector contributo… | Dependency injection integration for the unified OceanBase ADO.NET provider. |
| 2026-10-24 07:46:35 | [Byta.Browser](https://www.nuget.org/packages/Byta.Browser) | 0.2.0 | Hub-Game-develop | 把 Byta.GL 的同一套 API 转发给浏览器的 WebGL2：AnyCPU、无需 OpenGL 驱动，Windows/macOS/Linux 只要有浏览… |
| 2026-10-24 07:51:07 | [NanoServer](https://www.nuget.org/packages/NanoServer) | 1.0.0 | cnefan31 | 零依赖的轻量 .NET Web 能力库：路由、中间件、静态文件、JWT/SSRF 防护、WebSocket、结构化日志、每请求 DI 作用域，支持 .NET… |
| 2026-10-24 07:52:16 | [Esatto.Umbraco.Backoffice.NavigationOrder](https://www.nuget.org/packages/Esatto.Umbraco.Backoffice.NavigationOrder) | 1.0.0 | Carl Schéle | Drag the Umbraco backoffice sections and each section's tabs into the order you… |
| 2026-10-24 08:13:10 | [PowerCraft.Word.Core](https://www.nuget.org/packages/PowerCraft.Word.Core) | 0.1.0 | The Code Kitchen | Typed kernel for PowerCraft.Word: renders Markdown into a themed Word document… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

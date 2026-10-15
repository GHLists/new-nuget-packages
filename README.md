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

## Latest list — 2026-10-15 02:19 UTC

New packages created between 2026-10-15 01:22 UTC and 2026-10-15 02:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-15T02-19-57-566052Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-15 01:30:30 | [Net4x.DatabaseEditor](https://www.nuget.org/packages/Net4x.DatabaseEditor) | 1.0.0.26285 | DatabaseEditor | Package Description |
| 2026-10-15 01:31:34 | [Net4x.TrayBrowserLib](https://www.nuget.org/packages/Net4x.TrayBrowserLib) | 1.0.0.26285 | TrayBrowserLib | Package Description |
| 2026-10-15 01:31:36 | [Net4x.WcfLibrary](https://www.nuget.org/packages/Net4x.WcfLibrary) | 1.0.0.26284 | WcfLibrary | Package Description |
| 2026-10-15 01:31:44 | [Net4x.WrapperGeneratorLibrary](https://www.nuget.org/packages/Net4x.WrapperGeneratorLibrary) | 1.2.0.26286 | WrapperGeneratorLibrary | Package Description |
| 2026-10-15 01:38:50 | [CSEPDI.SmartRoadPython](https://www.nuget.org/packages/CSEPDI.SmartRoadPython) | 1.0.26.1014 | CSEPDI | 智能道路设计算法（Cython 编译 .pyd 产物 + Python 运行期依赖，源码不外泄） |
| 2026-10-15 01:38:59 | [WeDonekRpc.EmitMapper](https://www.nuget.org/packages/WeDonekRpc.EmitMapper) | 1.0.0 | WeDonekRpc.EmitMapper | Package Description |
| 2026-10-15 01:45:09 | [Iyu.MainServer.OpenIdConnect](https://www.nuget.org/packages/Iyu.MainServer.OpenIdConnect) | 0.39.0 | iyulab | iyu-framework-v5: OData + GraphQL runtime framework for .NET 10. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

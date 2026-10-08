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

## Latest list — 2026-10-08 06:19 UTC

New packages created between 2026-10-08 05:20 UTC and 2026-10-08 06:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-08T06-19-43-840948Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-08 05:21:17 | [Jazmin.AspNetCore](https://www.nuget.org/packages/Jazmin.AspNetCore) | 1.2.0 | SmithSoft Pty Ltd | ASP.NET Core endpoints for JAZMIN (.jzm) files: MapJazminFiles serves a file's… |
| 2026-10-08 05:28:45 | [DotNetCore.AiguilleUnit.Chinese](https://www.nuget.org/packages/DotNetCore.AiguilleUnit.Chinese) | 1.2.0 | DotNetCore.AiguilleUnit.Chine… | DotNetCore AiguilleUnit Chinese unit library |
| 2026-10-08 05:28:51 | [DotNetCore.AiguilleUnit.Geo](https://www.nuget.org/packages/DotNetCore.AiguilleUnit.Geo) | 1.2.0 | DotNetCore.AiguilleUnit.Geo | DotNetCore AiguilleUnit geodetic and navigational unit library |
| 2026-10-08 05:28:54 | [DotNetCore.AiguilleUnit.Imperial](https://www.nuget.org/packages/DotNetCore.AiguilleUnit.Imperial) | 1.2.0 | DotNetCore.AiguilleUnit.Imper… | DotNetCore AiguilleUnit Imperial unit library |
| 2026-10-08 05:28:56 | [DotNetCore.AiguilleUnit.Science](https://www.nuget.org/packages/DotNetCore.AiguilleUnit.Science) | 1.2.0 | DotNetCore.AiguilleUnit.Scien… | DotNetCore AiguilleUnit scientific unit library |
| 2026-10-08 05:34:01 | [PocketCsvReader.Json](https://www.nuget.org/packages/PocketCsvReader.Json) | 2.43.0 | Cédric L. Charlier | PocketCsvReader.Json is a lightweight streaming JSON document reader that expos… |
| 2026-10-08 05:34:30 | [BrowserShell.WebView.Wpf](https://www.nuget.org/packages/BrowserShell.WebView.Wpf) | 2.0.0 | FlyingEyeOrg | BrowserShell：在 WindowChromeKit 的 ChromeWindow 上承载 WebView2 的桌面 Web 外壳类库。提供窗口创建与… |
| 2026-10-08 05:37:29 | [Carbon.Data.Sql.Mocking](https://www.nuget.org/packages/Carbon.Data.Sql.Mocking) | 0.1.0 | Carbon.Data.Sql.Mocking | An in-memory MySQL fake for testing queries without a server. |
| 2026-10-08 05:42:12 | [Jtext103.CFET2.Things.UniversalModbusThing](https://www.nuget.org/packages/Jtext103.CFET2.Things.UniversalModbusThing) | 2.2.1 | Jtext103 | Configuration-driven Modbus RTU/TCP Thing for CFET2. |
| 2026-10-08 05:57:33 | [RepoDb.Sqlite.Ahtola](https://www.nuget.org/packages/RepoDb.Sqlite.Ahtola) | 0.0.1-alpha1 | RepoDb.Sqlite.Ahtola | A hybrid .NET ORM library for Ahtola, a pure managed SQLite-compatible engine (… |
| 2026-10-08 05:58:08 | [RepoDb.Sqlite.Turso](https://www.nuget.org/packages/RepoDb.Sqlite.Turso) | 0.0.1-alpha1 | RepoDb.Sqlite.Turso | A hybrid .NET ORM library for Turso (using Turso.Data.Sqlite.Provider). |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

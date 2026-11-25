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

## Latest list — 2026-11-25 10:22 UTC

New packages created between 2026-11-25 09:20 UTC and 2026-11-25 10:22 UTC.

[Full CSV](data/new-nuget-packages-2026-11-25T10-22-00-488395Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-25 09:25:35 | [Mzying2001.MonkeySharp.CefSharp87.x64](https://www.nuget.org/packages/Mzying2001.MonkeySharp.CefSharp87.x64) | 5.0.0 | Mzying2001 | CefSharp 87.1.132 host adapter for MonkeySharp userscripts. Install the matchin… |
| 2026-11-25 09:25:37 | [Mzying2001.MonkeySharp.CefSharp87.x86](https://www.nuget.org/packages/Mzying2001.MonkeySharp.CefSharp87.x86) | 5.0.0 | Mzying2001 | CefSharp 87.1.132 host adapter for MonkeySharp userscripts. Install the matchin… |
| 2026-11-25 09:50:35 | [Flowtex.DataAccess.Abstractions](https://www.nuget.org/packages/Flowtex.DataAccess.Abstractions) | 1.1.0 | Flowtex | Application-layer abstractions for Flowtex.DataAccess. Has no EF Core dependenc… |
| 2026-11-25 10:01:48 | [Eagle.Mes.Abstractions](https://www.nuget.org/packages/Eagle.Mes.Abstractions) | 1.0.0 | Eagle MES | MES 通用抽象层：数据库配置与提供器抽象，缓存 / ClickHouse / 邮件 / MongoDB / 本地化 / 数据库连接工厂契约及配套 DTO。零… |
| 2026-11-25 10:07:24 | [BlueRaiz.AI.Contracts](https://www.nuget.org/packages/BlueRaiz.AI.Contracts) | 0.4.0 | BlueRaiz | Request and response types of the BlueRaiz AI assistant platform API, shared by… |
| 2026-11-25 10:07:25 | [BlueRaiz.AI.SDK](https://www.nuget.org/packages/BlueRaiz.AI.SDK) | 0.4.0 | BlueRaiz | .NET client for the BlueRaiz AI assistant platform: chat with streaming, per-us… |
| 2026-11-25 10:07:27 | [BlueRaiz.AI.Components.Blazor](https://www.nuget.org/packages/BlueRaiz.AI.Components.Blazor) | 0.4.0 | BlueRaiz | Blazor in-app assistant for the BlueRaiz AI assistant platform: one component,… |
| 2026-11-25 10:13:27 | [Plugin.Maui.UITestHelpers.Repl](https://www.nuget.org/packages/Plugin.Maui.UITestHelpers.Repl) | 1.0.0 | jfversluis | Plugin.Maui.UITestHelpers.Repl adds an interactive REPL (read-eval-print loop)… |
| 2026-11-25 10:13:39 | [Beep.Office.Linq](https://www.nuget.org/packages/Beep.Office.Linq) | 1.0.1 | Beep.Office.Linq | Package Description |
| 2026-11-25 10:13:40 | [Beep.Office.Features](https://www.nuget.org/packages/Beep.Office.Features) | 1.0.1 | Beep.Office.Features | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

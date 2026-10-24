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

## Latest list — 2026-10-24 13:20 UTC

New packages created between 2026-10-24 12:21 UTC and 2026-10-24 13:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-24T13-20-08-840518Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-24 12:50:52 | [HeimdallFramework.Rendering](https://www.nuget.org/packages/HeimdallFramework.Rendering) | 4.0.0 | Bradley Ables | Server-side HTML rendering primitives and FluentHtml builders for Heimdall. |
| 2026-10-24 13:02:36 | [CSharpScript.Extension.Common](https://www.nuget.org/packages/CSharpScript.Extension.Common) | 0.0.5 | Xanvil | 脚本设置、引用解析、NuGet / COM 与 Runner 协议等共享能力。 |
| 2026-10-24 13:02:51 | [CSharpScript.Extension.Globals](https://www.nuget.org/packages/CSharpScript.Extension.Globals) | 0.0.5 | Xanvil | 脚本 Globals 契约（ICsxGlobalObject 等），供宿主与分析侧共享。 |
| 2026-10-24 13:03:06 | [CSharpScript.Extension.Host](https://www.nuget.org/packages/CSharpScript.Extension.Host) | 0.0.5 | Xanvil | 在宿主应用内嵌入 C# 脚本（.acsx 进程内 / .csx 经 dotnet-csx 工具）。 |
| 2026-10-24 13:04:09 | [CSharpScript.Extension.Runner](https://www.nuget.org/packages/CSharpScript.Extension.Runner) | 0.0.5 | Xanvil | 进程外 Runner（dotnet tool 命令 dotnet-csx，仅 net8.0）；供 Host 与编辑器扩展启动 .csx。 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

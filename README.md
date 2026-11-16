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

## Latest list — 2026-11-16 03:21 UTC

New packages created between 2026-11-16 02:21 UTC and 2026-11-16 03:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-16T03-21-03-681134Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-16 02:24:15 | [StreamBus](https://www.nuget.org/packages/StreamBus) | 0.5.1 | Nirav Patel | A modern .NET client for RabbitMQ Streams. Publish and consume typed messages,… |
| 2026-11-16 02:27:00 | [ProofStudio.Plugins.AddProject](https://www.nuget.org/packages/ProofStudio.Plugins.AddProject) | 0.5.4-beta | Cormier Solutions LLC | Embeddable four-step ZIP project upload, source job configuration, variable set… |
| 2026-11-16 02:30:04 | [Millia2d](https://www.nuget.org/packages/Millia2d) | 0.5.0 | Costin Andrei Patea | A game engine focused on high-performance of large numbers of actors. |
| 2026-11-16 02:43:59 | [Shashu.Sdk](https://www.nuget.org/packages/Shashu.Sdk) | 1.0.0 | Trustgate AI LLC | .NET client for SHASHU by Trustgate AI, a self-hosted AI security gateway. Poin… |
| 2026-11-16 02:47:37 | [Tubatools.AiXamlCard](https://www.nuget.org/packages/Tubatools.AiXamlCard) | 1.0.2 | 图吧工具箱 | 给 AI 助手增加原生 XAML 卡片：助手直接写 WinUI 界面并动态编译 C# 代码后置，卡片作为一条消息出现在对话里。 |
| 2026-11-16 02:47:39 | [Tubatools.AutoStart](https://www.nuget.org/packages/Tubatools.AutoStart) | 1.0.2 | 图吧工具箱 | 在设置页添加「开机自启」开关：登录 Windows 时以管理员权限启动图吧工具箱，不弹 UAC |
| 2026-11-16 03:06:31 | [Jakar.ErrorOr](https://www.nuget.org/packages/Jakar.ErrorOr) | 10.1.0 | Tyler Stegmaier | RFC 7807-style errors and results: Error, Errors, Alert and ErrorOrResult<T>. |
| 2026-11-16 03:06:58 | [Jakar.Files](https://www.nuget.org/packages/Jakar.Files) | 10.1.0 | Tyler Stegmaier | Files, directories, file watchers, embedded resources, INI configuration and pr… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

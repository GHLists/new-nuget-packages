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

## Latest list — 2026-10-10 14:19 UTC

New packages created between 2026-10-10 13:21 UTC and 2026-10-10 14:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-10T14-19-54-756301Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-10 13:21:34 | [JsonGuard](https://www.nuget.org/packages/JsonGuard) | 0.1.0 | JsonGuard | An efficient, allocation free JSON validation library for System.Text.Json, bas… |
| 2026-10-10 13:23:59 | [NCXUtilityStandard.ArubaMail](https://www.nuget.org/packages/NCXUtilityStandard.ArubaMail) | 1.20.2026.1 | NeocodeX Srl | Utility Libraries per Mail aruba |
| 2026-10-10 13:26:10 | [ExtendedArithmetic.GenericMatrix](https://www.nuget.org/packages/ExtendedArithmetic.GenericMatrix) | 3000.0.0.283 | Adam White | A generic Matrix numeric type. Supports: Scalar arithmetic, vector arithmetic,… |
| 2026-10-10 13:34:34 | [CodeWF.Avalonia.Log](https://www.nuget.org/packages/CodeWF.Avalonia.Log) | 12.1.4.1 | 沙漠尽头的狼 | 面向 Avalonia 的日志查看控件与桌面通知：基于轻量日志核心展示实时日志、级别过滤与界面友好内容，适合桌面应用内嵌日志观察台。Avalonia log… |
| 2026-10-10 13:47:58 | [LibGit2CS](https://www.nuget.org/packages/LibGit2CS) | 0.1.5-dev | LibGit2CS | A managed C# port of libgit2. |
| 2026-10-10 13:51:27 | [KofTwentyTwo.AppKit.Updates](https://www.nuget.org/packages/KofTwentyTwo.AppKit.Updates) | 0.1.0 | James Maes | Velopack self-update for KofTwentyTwo Windows apps: startup hook handling, a ne… |
| 2026-10-10 13:51:28 | [KofTwentyTwo.AppKit.WinUI](https://www.nuget.org/packages/KofTwentyTwo.AppKit.WinUI) | 0.1.0 | James Maes | WinUI 3 shell pieces for KofTwentyTwo Windows apps: branded splash overlay, Abo… |
| 2026-10-10 13:51:28 | [KofTwentyTwo.AppKit](https://www.nuget.org/packages/KofTwentyTwo.AppKit) | 0.1.0 | James Maes | UI-framework-free foundation for KofTwentyTwo Windows apps: app identity, per-u… |
| 2026-10-10 13:51:29 | [KofTwentyTwo.AppKit.Wpf](https://www.nuget.org/packages/KofTwentyTwo.AppKit.Wpf) | 0.1.0 | James Maes | WPF shell pieces for KofTwentyTwo Windows apps: branded splash overlay, About w… |
| 2026-10-10 14:00:32 | [LoupixDeck.PluginTool](https://www.nuget.org/packages/LoupixDeck.PluginTool) | 1.31.1 | RadiatorTwo | Command line tool for LoupixDeck plugin development: scaffolds a plugin against… |
| 2026-10-10 14:00:33 | [LoupixDeck.PluginTool.linux-x64](https://www.nuget.org/packages/LoupixDeck.PluginTool.linux-x64) | 1.31.1 | RadiatorTwo | Command line tool for LoupixDeck plugin development: scaffolds a plugin against… |
| 2026-10-10 14:00:34 | [LoupixDeck.PluginTool.osx-arm64](https://www.nuget.org/packages/LoupixDeck.PluginTool.osx-arm64) | 1.31.1 | RadiatorTwo | Command line tool for LoupixDeck plugin development: scaffolds a plugin against… |
| 2026-10-10 14:00:34 | [LoupixDeck.PluginTool.osx-x64](https://www.nuget.org/packages/LoupixDeck.PluginTool.osx-x64) | 1.31.1 | RadiatorTwo | Command line tool for LoupixDeck plugin development: scaffolds a plugin against… |
| 2026-10-10 14:00:35 | [LoupixDeck.PluginTool.win-x64](https://www.nuget.org/packages/LoupixDeck.PluginTool.win-x64) | 1.31.1 | RadiatorTwo | Command line tool for LoupixDeck plugin development: scaffolds a plugin against… |
| 2026-10-10 14:12:58 | [Zongsoft.Externals.Etcd](https://www.nuget.org/packages/Zongsoft.Externals.Etcd) | 0.1.0 | Zongsoft Studio(zongsoft@qq.c… | This is a library about Etcd SDK. |
| 2026-10-10 14:13:42 | [Zongsoft.Externals.OpenXml](https://www.nuget.org/packages/Zongsoft.Externals.OpenXml) | 0.3.0 | Zongsoft Studio(zongsoft@qq.c… | This is a library about OpenXml SDK. |
| 2026-10-10 14:14:52 | [Zongsoft.Upgrading.Upgrader](https://www.nuget.org/packages/Zongsoft.Upgrading.Upgrader) | 0.1.0 | Zongsoft Studio(zongsoft@qq.c… | This is a upgrader for automatic upgrading. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

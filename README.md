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

## Latest list — 2026-11-07 16:18 UTC

New packages created between 2026-11-07 15:21 UTC and 2026-11-07 16:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-07T16-18-29-560628Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-07 15:27:36 | [TelegramBotForge.AspNetCore](https://www.nuget.org/packages/TelegramBotForge.AspNetCore) | 0.1.0 | VAXA99 | Webhook mode for TelegramBotForge bots on ASP.NET Core: maps the endpoint that… |
| 2026-11-07 15:27:37 | [TelegramBotForge](https://www.nuget.org/packages/TelegramBotForge) | 0.1.0 | VAXA99 | Build Telegram bots quickly with MVC: controllers with attribute routes for com… |
| 2026-11-07 15:36:54 | [RuneDotNet](https://www.nuget.org/packages/RuneDotNet) | 0.1.0 | Geevo | C# bindings for Rune, the Rust UI framework, for NativeAOT apps. Rune is linked… |
| 2026-11-07 15:41:16 | [ZkLink.Extensions.DependencyInjection](https://www.nuget.org/packages/ZkLink.Extensions.DependencyInjection) | 1.0.1 | Aleksandr Pavlov | Microsoft.Extensions.DependencyInjection registration and host-owned lifetime f… |
| 2026-11-07 15:41:17 | [ZkLink.Analyzers](https://www.nuget.org/packages/ZkLink.Analyzers) | 1.0.1 | Aleksandr Pavlov | Roslyn analyzers for secure and asynchronous ZkLink usage. |
| 2026-11-07 16:00:27 | [McpMsSqlServer](https://www.nuget.org/packages/McpMsSqlServer) | 0.1.2 | McpMsSqlServer | MCP server for MS SQL Server, installed as a dotnet tool |
| 2026-11-07 16:02:51 | [Pushizo.Maui.Android.Binding](https://www.nuget.org/packages/Pushizo.Maui.Android.Binding) | 0.2.0 | Pushizo | Pushizo Android SDK (com.pushizo:pushizo-android) için .NET Android binding'i.… |
| 2026-11-07 16:02:53 | [Pushizo.Maui](https://www.nuget.org/packages/Pushizo.Maui) | 0.2.0 | Pushizo | Pushizo .NET MAUI SDK: push bildirimleri, in-app mesajlar, bildirim kutusu, kul… |
| 2026-11-07 16:02:56 | [Pushizo.Maui.iOS.Binding](https://www.nuget.org/packages/Pushizo.Maui.iOS.Binding) | 0.2.0 | Pushizo | Pushizo iOS SDK'sı için .NET iOS binding'i (@objc Swift cephesi). Doğrudan deği… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

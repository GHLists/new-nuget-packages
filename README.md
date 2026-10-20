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

## Latest list — 2026-10-20 20:21 UTC

New packages created between 2026-10-20 19:22 UTC and 2026-10-20 20:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-20T20-21-23-44667Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-20 19:25:47 | [IsWiX.WindowsInstaller](https://www.nuget.org/packages/IsWiX.WindowsInstaller) | 0.1.3 | IsWiX LLC | Read and write Windows Installer (.msi) databases without msi.dll. A managed re… |
| 2026-10-20 19:27:47 | [AgentConnector](https://www.nuget.org/packages/AgentConnector) | 0.1.0 | AgentConnector | Native, embeddable ASP.NET Core connector runtime. |
| 2026-10-20 19:34:09 | [Plugin.Maui.Spine.Controls.Charts](https://www.nuget.org/packages/Plugin.Maui.Spine.Controls.Charts) | 0.1.17 | Jonatan Söderberg | Small charts for dashboards in .NET MAUI: RingChart (a share as a ring, clockwi… |
| 2026-10-20 19:34:12 | [Stellaegis.Primitives.Hosting](https://www.nuget.org/packages/Stellaegis.Primitives.Hosting) | 5.0.0 | FRi | Stellaegis primitives for an application assembled by a host, with or without A… |
| 2026-10-20 19:51:07 | [BeaconSDK](https://www.nuget.org/packages/BeaconSDK) | 0.1.0 | Tavstal | A .NET library for building Minecraft launchers. Handles Microsoft authenticati… |
| 2026-10-20 19:52:54 | [Sight.Logging.Extensions](https://www.nuget.org/packages/Sight.Logging.Extensions) | 0.1.0 | Arthur Ferre | Bridge between Microsoft.Extensions.Logging and Sight.Logging. |
| 2026-10-20 19:59:21 | [Alcove](https://www.nuget.org/packages/Alcove) | 0.0.1-alpha | Adam Schiavone | Alcove: install plugins from NuGet feeds and load them into isolated cells (Ass… |
| 2026-10-20 19:59:22 | [Alcove.Autofac](https://www.nuget.org/packages/Alcove.Autofac) | 0.0.1-alpha | Adam Schiavone | Autofac add-on for Alcove: builder.AddPlugins(), constructor injection for exte… |
| 2026-10-20 19:59:23 | [Alcove.DependencyInjection](https://www.nuget.org/packages/Alcove.DependencyInjection) | 0.0.1-alpha | Adam Schiavone | Microsoft.Extensions.DependencyInjection add-on for Alcove: services.AddPlugins… |
| 2026-10-20 19:59:23 | [Alcove.Abstractions](https://www.nuget.org/packages/Alcove.Abstractions) | 0.0.1-alpha | Adam Schiavone | The plugin-facing API of Alcove: IPlugin, IPluginContext, IExtensionRegistrar,… |
| 2026-10-20 19:59:24 | [Alcove.Wpf](https://www.nuget.org/packages/Alcove.Wpf) | 0.0.1-alpha | Adam Schiavone | WPF add-on for Alcove: options.UseWpf(app) pre-loads plugins' XAML assemblies,… |
| 2026-10-20 19:59:25 | [Alcove.Sdk](https://www.nuget.org/packages/Alcove.Sdk) | 0.0.1-alpha | Adam Schiavone | Build support for Alcove plugins: sets the plugin PackageType, generates the pl… |
| 2026-10-20 20:03:25 | [Sight.Tweening](https://www.nuget.org/packages/Sight.Tweening) | 1.0.0 | Arthur Ferre | Standalone C# library to make animations with tweens. |
| 2026-10-20 20:03:52 | [SqlNative.AspNetCore](https://www.nuget.org/packages/SqlNative.AspNetCore) | 0.3.1 | Peyman Jahanbazi | ASP.NET Core integration for SqlNative. Provides DI extension methods to regist… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

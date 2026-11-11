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

## Latest list — 2026-11-11 10:21 UTC

New packages created between 2026-11-11 09:19 UTC and 2026-11-11 10:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-11T10-21-51-36255Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-11 09:21:27 | [SilverHamu.Client](https://www.nuget.org/packages/SilverHamu.Client) | 0.2.0 | dhq_boiler and contributors | .NET client for the silverhamu TCP service with binary keys and values, durable… |
| 2026-11-11 09:25:01 | [Altium.Designer.HotReload](https://www.nuget.org/packages/Altium.Designer.HotReload) | 1.0.0 | Altium | Hot reload for Altium Designer extensions in Debug builds: rebuild your C# and… |
| 2026-11-11 09:26:30 | [IOViewer](https://www.nuget.org/packages/IOViewer) | 0.1.0 | mahach666 | Fast, pure managed .NET library and CLI tool for generating standalone, zero-de… |
| 2026-11-11 09:26:32 | [IOViewer.Cli](https://www.nuget.org/packages/IOViewer.Cli) | 0.1.0 | mahach666 | Command line tool for generating standalone, zero-dependency interactive 3D Web… |
| 2026-11-11 09:28:22 | [SingleStore.AgentFramework](https://www.nuget.org/packages/SingleStore.AgentFramework) | 0.1.0 | SingleStore Inc. | SingleStore integrations for Microsoft Agent Framework. |
| 2026-11-11 09:38:04 | [Cike.Auth.Caching](https://www.nuget.org/packages/Cike.Auth.Caching) | 1.0.1 | Lemon.Li | Package Description |
| 2026-11-11 09:39:58 | [Ariadne.NET.Cli](https://www.nuget.org/packages/Ariadne.NET.Cli) | 0.7.1 | Marcel Roozekrans | The ariadne command: checks a .NET solution against its Ariadne.NET architectur… |
| 2026-11-11 09:39:59 | [Ariadne.NET.Testing](https://www.nuget.org/packages/Ariadne.NET.Testing) | 0.7.1 | Marcel Roozekrans | Checks a .NET solution against its Ariadne.NET architecture rule packs from a u… |
| 2026-11-11 09:42:25 | [WiseAuth](https://www.nuget.org/packages/WiseAuth) | 1.0.0 | Andrew Boyd | A lightweight ASP.NET Core authorization library that uses power-of-two bit-fla… |
| 2026-11-11 09:45:21 | [SimdYolo](https://www.nuget.org/packages/SimdYolo) | 0.11.3 | SimdYolo | Managed FP32 YOLO detection, segmentation and pose inference with SIMD, Vulkan… |
| 2026-11-11 09:45:22 | [SimdYolo.Training](https://www.nuget.org/packages/SimdYolo.Training) | 0.11.3 | SimdYolo.Training | Pure managed YOLOv8/v9/v10/YOLO11/YOLO26 detection-head fine-tuning with CPU SI… |
| 2026-11-11 09:47:08 | [Dosai](https://www.nuget.org/packages/Dosai) | 5.0.0 | Team AppThreat <cloud@appthre… | OWASP Dosai (Dotnet Source and Assembly Inspector) inspects .NET source code, a… |
| 2026-11-11 09:50:34 | [Rst.Ssh](https://www.nuget.org/packages/Rst.Ssh) | 0.1.0 | RST | An embeddable SSH-2 and SFTP server for .NET. A complete, self-contained SSH/SF… |
| 2026-11-11 09:53:07 | [Altium.Designer.Extension.Templates](https://www.nuget.org/packages/Altium.Designer.Extension.Templates) | 1.0.0 | Altium | dotnet new templates for Altium Designer extensions (.NET 8 or .NET 10, as the… |
| 2026-11-11 10:01:34 | [Routeables.Abstraction](https://www.nuget.org/packages/Routeables.Abstraction) | 2.1.0 | Cédric Boutin | The contracts of Routeables: IRouter, IRouteable, RouteableArgs, the attributes… |
| 2026-11-11 10:02:22 | [Routeables.Blazor](https://www.nuget.org/packages/Routeables.Blazor) | 2.1.0 | Cédric Boutin | Routeables for Blazor: view-model-first routing, routed components, regions, di… |
| 2026-11-11 10:03:15 | [Routeables.Templates](https://www.nuget.org/packages/Routeables.Templates) | 2.1.0 | Routeables.Templates | dotnet new templates for Routeables: an Avalonia, a .NET MAUI, an Uno Platform,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

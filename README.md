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

## Latest list — 2026-11-23 09:21 UTC

New packages created between 2026-11-23 08:19 UTC and 2026-11-23 09:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-23T09-21-06-617505Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-23 08:19:44 | [CodeBrix.WebPlatform.WebGpu.Graphics.ApacheLicenseForever](https://www.nuget.org/packages/CodeBrix.WebPlatform.WebGpu.Graphics.ApacheLicenseForever) | 1.0.327.498 | Jeremy Ellis | 2D and 3D graphics through WebGPU for the browser frontend of a CodeBrix.WebPla… |
| 2026-11-23 08:28:13 | [SwartBerg.Mediator.AzureServiceBus](https://www.nuget.org/packages/SwartBerg.Mediator.AzureServiceBus) | 4.1.0 | SwartBerg Studio | Azure Service Bus transport for SwartBerg.Mediator: IMediator.Publish sends not… |
| 2026-11-23 08:29:49 | [SomaFrameQDWpf](https://www.nuget.org/packages/SomaFrameQDWpf) | 0.9.0 | Dmitriy Novikov, Tim Jones, a… | SomaFrameQD is an application shell similar in concept to the Visual Studio She… |
| 2026-11-23 08:30:56 | [SomaFrameQD.Modules.CodeCompiler](https://www.nuget.org/packages/SomaFrameQD.Modules.CodeCompiler) | 0.9.0 | Dmitriy Novikov, Tim Jones, a… | CodeCompiler module for SomaFrameQD, providing C# code compilation using Roslyn. |
| 2026-11-23 08:31:26 | [SomaFrameQD.Modules.Output](https://www.nuget.org/packages/SomaFrameQD.Modules.Output) | 0.9.0 | Dmitriy Novikov, Tim Jones, a… | Output module for SomaFrameQD, providing a buffered output tool pane. |
| 2026-11-23 08:31:57 | [SomaFrameQD.Modules.PropertyGrid](https://www.nuget.org/packages/SomaFrameQD.Modules.PropertyGrid) | 0.9.0 | Dmitriy Novikov, Tim Jones, a… | PropertyGrid module for SomaFrameQD, utilising the PropertyGrid control from th… |
| 2026-11-23 08:32:46 | [SomaFrameQD.Modules.GraphEditor](https://www.nuget.org/packages/SomaFrameQD.Modules.GraphEditor) | 0.9.0 | Dmitriy Novikov, Tim Jones, a… | GraphEditor module for SomaFrameQD, providing UI controls to edit a graph of co… |
| 2026-11-23 08:33:08 | [SomaFrameQD.Modules.ErrorList](https://www.nuget.org/packages/SomaFrameQD.Modules.ErrorList) | 0.9.0 | Dmitriy Novikov, Tim Jones, a… | ErrorList module for SomaFrameQD, providing a tool window to display messages,… |
| 2026-11-23 08:33:32 | [SomaFrameQD.Modules.CodeEditor](https://www.nuget.org/packages/SomaFrameQD.Modules.CodeEditor) | 0.9.0 | Dmitriy Novikov, Tim Jones, a… | CodeEditor module for SomaFrameQD, providing a syntax-highlighted code editor u… |
| 2026-11-23 08:33:54 | [SomaFrameQD.Modules.Inspector](https://www.nuget.org/packages/SomaFrameQD.Modules.Inspector) | 0.9.0 | Dmitriy Novikov, Tim Jones, a… | Inspector module for SomaFrameQD, providing a flexible PropertyGrid-esque tool… |
| 2026-11-23 08:42:29 | [M.Simple.Container](https://www.nuget.org/packages/M.Simple.Container) | 1.0.0.1 | Mr.Sunny | A lightweight .NET dependency injection container with assembly scanning and st… |
| 2026-11-23 08:51:10 | [SonnetDB.Quartz](https://www.nuget.org/packages/SonnetDB.Quartz) | 5.2.0 | maikebing | 适用于 Quartz.NET 3.18 的 SonnetDB 持久化调度存储。 |
| 2026-11-23 09:03:54 | [Krypton.Toolkit.Suite.Extended.Software.Updater.Core.Canary](https://www.nuget.org/packages/Krypton.Toolkit.Suite.Extended.Software.Updater.Core.Canary) | 120.26.11.327-beta | Peter Wagner (A.K.A Wagnerp)… | An extension to the Standard Toolkit, which supports .NET Framework 4.7.2 - 4.8… |
| 2026-11-23 09:10:13 | [xStatic.AI](https://www.nuget.org/packages/xStatic.AI) | 17.3.0 | Sam Mullins | Optional AI add-on for xStatic for Umbraco 17+, providing Microsoft.Extensions.… |
| 2026-11-23 09:10:14 | [xStatic.Cloudflare](https://www.nuget.org/packages/xStatic.Cloudflare) | 17.3.0 | Sam Mullins | Cloudflare Pages Direct Upload and Cloudflare R2 deployers and post-generation… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

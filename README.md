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

## Latest list — 2026-10-05 14:19 UTC

New packages created between 2026-10-05 13:22 UTC and 2026-10-05 14:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-05T14-19-59-308378Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-05 13:33:54 | [PaspanCodeGraphMcp](https://www.nuget.org/packages/PaspanCodeGraphMcp) | 0.2.5 | ToCSharp | Read-only MCP server for C# and C++ code analysis by AI agents: declarations, t… |
| 2026-10-05 13:36:18 | [NeoRuneExtended.Sdk](https://www.nuget.org/packages/NeoRuneExtended.Sdk) | 0.4.0 | thororen | Write Minecraft Dungeons II mods in C#, with the game's own UI. This MSBuild pr… |
| 2026-10-05 13:36:20 | [NeoRuneExtended.Tool](https://www.nuget.org/packages/NeoRuneExtended.Tool) | 0.4.0 | thororen | The NeoRuneExtended command line: read mod logs (neorunex log), check your setu… |
| 2026-10-05 13:36:21 | [NeoRuneExtended.Templates](https://www.nuget.org/packages/NeoRuneExtended.Templates) | 0.4.0 | thororen | dotnet new templates for NeoRuneExtended mods for Minecraft Dungeons II: dotnet… |
| 2026-10-05 13:38:02 | [KeelMatrix.NuGetReady](https://www.nuget.org/packages/KeelMatrix.NuGetReady) | 0.1.0 | KeelMatrix | Rehearse a NuGet release from the exact built artifacts and prove clean isolate… |
| 2026-10-05 13:39:39 | [Cornerstone.Automation.Presentation](https://www.nuget.org/packages/Cornerstone.Automation.Presentation) | 3.0.277.17112 | Bobby Cannon | Shared .NET 10 framework for desktop and cross-platform apps: process bootstrap… |
| 2026-10-05 13:39:42 | [Cornerstone.Presentation](https://www.nuget.org/packages/Cornerstone.Presentation) | 3.0.277.17112 | Bobby Cannon | Shared .NET 10 framework for desktop and cross-platform apps: process bootstrap… |
| 2026-10-05 13:39:43 | [Cornerstone.Templates](https://www.nuget.org/packages/Cornerstone.Templates) | 3.0.277.17112 | Bobby Cannon | Project templates for Cornerstone: a basic desktop host, Keystone (Bus : State… |
| 2026-10-05 13:41:16 | [StdUnit.Tags.LinuxFs.ProcInfo](https://www.nuget.org/packages/StdUnit.Tags.LinuxFs.ProcInfo) | 0.16.0 | StdUnit.Tags.LinuxFs.ProcInfo | Package Description |
| 2026-10-05 13:42:45 | [LanDX.DotNet.Templates](https://www.nuget.org/packages/LanDX.DotNet.Templates) | 1.0.0 | LanDX | LanDX .NET project templates. |
| 2026-10-05 13:58:39 | [iPlus.Avalonia.Markup](https://www.nuget.org/packages/iPlus.Avalonia.Markup) | 12.2.901 | iPlus | iPlus fork of Avalonia - a cross-platform UI framework for .NET providing a fle… |
| 2026-10-05 14:05:03 | [PocArquitetura.HttpResilienceDefaults](https://www.nuget.org/packages/PocArquitetura.HttpResilienceDefaults) | 0.21.17 | Rodrigo Oliveira | Defaults compartilhados para configuração de HttpClient resiliente, timeouts, r… |
| 2026-10-05 14:05:04 | [PocArquitetura.ApplicationDefaults](https://www.nuget.org/packages/PocArquitetura.ApplicationDefaults) | 0.21.17 | Rodrigo Oliveira | Defaults de camada Application para validação e pipeline behaviors baseados em… |
| 2026-10-05 14:05:05 | [PocArquitetura.ApiDefaults](https://www.nuget.org/packages/PocArquitetura.ApiDefaults) | 0.21.17 | Rodrigo Oliveira | Defaults compartilhados para APIs ASP.NET Core: autenticação JWT, Swagger/OpenA… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

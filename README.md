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

## Latest list — 2026-11-04 13:19 UTC

New packages created between 2026-11-04 12:21 UTC and 2026-11-04 13:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-04T13-19-41-944297Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-04 12:22:45 | [ThunderID.AspNetCore](https://www.nuget.org/packages/ThunderID.AspNetCore) | 0.1.0 | Pasindu Balasooriya | Sign users in to ASP.NET Core apps with ThunderID, protect APIs with ThunderID… |
| 2026-11-04 12:26:06 | [Inertia.Net.EntityFrameworkCore](https://www.nuget.org/packages/Inertia.Net.EntityFrameworkCore) | 1.6.2 | Inertia.Net contributors | Entity Framework Core pagination for Inertia.Net (not Native AOT compatible). |
| 2026-11-04 12:28:29 | [zzzzv.SPMRating](https://www.nuget.org/packages/zzzzv.SPMRating) | 1.2.0 | zzzzv | Unofficial C# port of SPM Rating, an osu!mania difficulty model (4K / 6K / 7K). |
| 2026-11-04 12:30:43 | [OpenSceneGraph.Net.Rendering.OpenGL](https://www.nuget.org/packages/OpenSceneGraph.Net.Rendering.OpenGL) | 0.1.0 | Gravicode Studios (Kang Fadhi… | OpenGL 3.3 / OpenGL ES 3.0 renderer for OpenSceneGraph.Net render lists: Blinn-… |
| 2026-11-04 12:30:44 | [OpenSceneGraph.Net.Cli](https://www.nuget.org/packages/OpenSceneGraph.Net.Cli) | 0.1.0 | Gravicode Studios (Kang Fadhi… | osgnet — command line tool for OpenSceneGraph.Net: inspect, convert, optimize,… |
| 2026-11-04 12:30:45 | [OpenSceneGraph.Net](https://www.nuget.org/packages/OpenSceneGraph.Net) | 0.1.0 | Gravicode Studios (Kang Fadhi… | .NET 10 scene graph modelled on OpenSceneGraph: nodes, transforms, LOD, paging,… |
| 2026-11-04 12:30:46 | [OpenSceneGraph.Net.Templates](https://www.nuget.org/packages/OpenSceneGraph.Net.Templates) | 0.1.0 | Gravicode Studios (Kang Fadhi… | dotnet new templates for OpenSceneGraph.Net: console (native osgViewer / offscr… |
| 2026-11-04 12:30:46 | [OpenSceneGraph.Net.Blazor](https://www.nuget.org/packages/OpenSceneGraph.Net.Blazor) | 0.1.0 | Gravicode Studios (Kang Fadhi… | Blazor component (OsgCanvas) that runs an OpenSceneGraph.Net viewer in .NET and… |
| 2026-11-04 12:30:48 | [OpenSceneGraph.Net.Native](https://www.nuget.org/packages/OpenSceneGraph.Net.Native) | 0.1.0 | Gravicode Studios (Kang Fadhi… | Native OpenSceneGraph 3.6.5 runtime for OpenSceneGraph.Net: reads/writes every… |
| 2026-11-04 12:30:48 | [OpenSceneGraph.Net.Avalonia](https://www.nuget.org/packages/OpenSceneGraph.Net.Avalonia) | 0.1.0 | Gravicode Studios (Kang Fadhi… | Avalonia UI control (OsgView) that hosts an OpenSceneGraph.Net viewer with the… |
| 2026-11-04 12:33:02 | [Locally.Aspire.Client](https://www.nuget.org/packages/Locally.Aspire.Client) | 0.1.0 | Locally Build | Signs an Aspire app's Azure clients in to Locally: under `locally run`, every A… |
| 2026-11-04 12:33:02 | [Locally.Aspire.Hosting](https://www.nuget.org/packages/Locally.Aspire.Hosting) | 0.1.0 | Locally Build | Runs an Aspire AppHost's Azure resources in Locally: under `locally run`, `aspi… |
| 2026-11-04 12:33:03 | [NkkinXlsx](https://www.nuget.org/packages/NkkinXlsx) | 0.1.0 | Nkkin | A lightweight, dependency-free .NET 10 library for creating and reading XLSX wo… |
| 2026-11-04 12:40:08 | [WorldRef](https://www.nuget.org/packages/WorldRef) | 1.1.1 | worldref contributors | Every country in Arabic, English, or both: names, nationalities, dial codes, ph… |
| 2026-11-04 12:56:16 | [VstAudio](https://www.nuget.org/packages/VstAudio) | 0.0.1 | 115dkk | Reserved name for the .NET bindings of vst-audio, an isolated-process VST2/VST3… |
| 2026-11-04 13:09:31 | [Webority.Mentions](https://www.nuget.org/packages/Webority.Mentions) | 0.129.0 | Webority Technologies | Reads the mention values a Webority mention box posts (@[Label](id)): the disti… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

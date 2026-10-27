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

## Latest list — 2026-10-27 13:21 UTC

New packages created between 2026-10-27 12:18 UTC and 2026-10-27 13:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-27T13-21-33-125329Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-27 12:20:35 | [Fizzy.ImageViewer.Cuda11](https://www.nuget.org/packages/Fizzy.ImageViewer.Cuda11) | 1.3.0 | Fizzy.ImageViewer.Cuda | Optional CUDA image display and pixel queries with consumer-owned execution sco… |
| 2026-10-27 12:21:06 | [NacreCraft.WebApp](https://www.nuget.org/packages/NacreCraft.WebApp) | 0.2.4 | NacreCraftDev | Desktop and command line client for NacreCraft accounts. |
| 2026-10-27 12:24:44 | [KeyTD.Manat](https://www.nuget.org/packages/KeyTD.Manat) | 0.1.0 | KeyTD | One API for Azerbaijani online payment providers: Kapital Bank, Azericard, Payr… |
| 2026-10-27 12:27:08 | [Fizzy.ImageViewer.Cuda12](https://www.nuget.org/packages/Fizzy.ImageViewer.Cuda12) | 1.3.0 | Fizzy.ImageViewer.Cuda | Optional CUDA image display and pixel queries with consumer-owned execution sco… |
| 2026-10-27 12:27:15 | [JSNet.Runtime](https://www.nuget.org/packages/JSNet.Runtime) | 0.1.1 | Gravicode Studios (Kang Fadhi… | JS.Net runtime support: console, JSON, Math, Promise, Date, fetch, timers, Java… |
| 2026-10-27 12:27:17 | [JSNet.AI](https://www.nuget.org/packages/JSNet.AI) | 0.1.1 | Gravicode Studios (Kang Fadhi… | JS.Net AI-native features: `ai function` and `prompt` declarations backed by Mi… |
| 2026-10-27 12:27:19 | [JSNet.Sdk](https://www.nuget.org/packages/JSNet.Sdk) | 0.1.1 | Gravicode Studios (Kang Fadhi… | MSBuild project SDK for JS.Net: <Project Sdk="JSNet.Sdk/0.1.1"> compiles .jsn f… |
| 2026-10-27 12:27:20 | [JSNet.Cli](https://www.nuget.org/packages/JSNet.Cli) | 0.1.1 | Gravicode Studios (Kang Fadhi… | The jsnet command-line tool: compile, run, check, emit and format JS.Net code,… |
| 2026-10-27 12:27:21 | [JSNet.Templates](https://www.nuget.org/packages/JSNet.Templates) | 0.1.1 | Gravicode Studios (Kang Fadhi… | dotnet new templates for JS.Net: console (jsnet), classlib, webapi, web, blazor… |
| 2026-10-27 12:33:02 | [Fizzy.ImageViewer.Cuda13](https://www.nuget.org/packages/Fizzy.ImageViewer.Cuda13) | 1.3.0 | Fizzy.ImageViewer.Cuda | Optional CUDA image display and pixel queries with consumer-owned execution sco… |
| 2026-10-27 12:47:32 | [Superroute.SMap](https://www.nuget.org/packages/Superroute.SMap) | 1.0.0 | Goodneo Solutions | Maps from Superroute's sMap service: options, tokens, nearest node, styles, lay… |
| 2026-10-27 12:47:34 | [Superroute.SMap.WinForms](https://www.nuget.org/packages/Superroute.SMap.WinForms) | 1.0.0 | Goodneo Solutions | Maps from Superroute's sMap service in a WinForms control: vector basemaps in f… |
| 2026-10-27 12:47:35 | [Superroute.SMap.Wpf](https://www.nuget.org/packages/Superroute.SMap.Wpf) | 1.0.0 | Goodneo Solutions | Maps from Superroute's sMap service in a WPF control: vector basemaps in five c… |
| 2026-10-27 12:53:44 | [Nethermind.OpenVM.Runtime](https://www.nuget.org/packages/Nethermind.OpenVM.Runtime) | 2.1.0.56 | Nethermind | OpenVM zkVM accelerators for the Nethermind guest for OpenVM |
| 2026-10-27 12:57:38 | [AppWeaver.ProblemDetails](https://www.nuget.org/packages/AppWeaver.ProblemDetails) | 1.0.0 | Team AppWeaver | ProblemDetails utilities for AppWeaver: options and factories to map exceptions… |
| 2026-10-27 13:03:33 | [NCache.Dapper](https://www.nuget.org/packages/NCache.Dapper) | 5.3.800 | Alachisoft | NCache extension for Dapper providing distributed caching of database queries. |
| 2026-10-27 13:05:32 | [GriffinClient](https://www.nuget.org/packages/GriffinClient) | 1.0.0 | Tuomas Hietanen | Griffin banking-as-a-service client: onboarding (legal persons, claims, verific… |
| 2026-10-27 13:05:35 | [CritterWatch.Aspire](https://www.nuget.org/packages/CritterWatch.Aspire) | 1.1.0 | JasperFx Software, LLC | .NET Aspire hosting integration for CritterWatch: AddCritterWatch() for the con… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

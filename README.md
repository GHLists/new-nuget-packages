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

## Latest list — 2026-11-18 20:21 UTC

New packages created between 2026-11-18 19:21 UTC and 2026-11-18 20:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-18T20-21-34-451145Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-18 19:28:05 | [Singulink.CodeAnalysis.Analyzers](https://www.nuget.org/packages/Singulink.CodeAnalysis.Analyzers) | 0.5.0 | Singulink | Roslyn analyzers that check code against the Singulink.CodeAnalysis attributes,… |
| 2026-11-18 19:28:09 | [Singulink.CodeAnalysis](https://www.nuget.org/packages/Singulink.CodeAnalysis) | 0.5.0 | Singulink | Attributes that mark types and members for the Singulink.CodeAnalysis analyzers… |
| 2026-11-18 19:29:04 | [REDcat.OpenVoiceSharp](https://www.nuget.org/packages/REDcat.OpenVoiceSharp) | 1.0.4 | realcoloride, MrREDcat | OpenVoiceSharp - Agnostic C# VoIP/Voice Chat Library using Opus. |
| 2026-11-18 19:30:43 | [Waring.Maui.Carbon](https://www.nuget.org/packages/Waring.Maui.Carbon) | 0.1.0 | Joshua Waring | An unofficial .NET MAUI implementation of the Carbon Design System (v11): four… |
| 2026-11-18 19:35:02 | [mcp-sonarqube.linux-x64](https://www.nuget.org/packages/mcp-sonarqube.linux-x64) | 1.3.0 | Marko Lahma | Model Context Protocol server for SonarQube Cloud - projects, quality gates, is… |
| 2026-11-18 19:35:04 | [mcp-sonarqube.linux-arm64](https://www.nuget.org/packages/mcp-sonarqube.linux-arm64) | 1.3.0 | Marko Lahma | Model Context Protocol server for SonarQube Cloud - projects, quality gates, is… |
| 2026-11-18 19:35:05 | [mcp-sonarqube.win-x64](https://www.nuget.org/packages/mcp-sonarqube.win-x64) | 1.3.0 | Marko Lahma | Model Context Protocol server for SonarQube Cloud - projects, quality gates, is… |
| 2026-11-18 19:35:06 | [mcp-sonarqube.win-arm64](https://www.nuget.org/packages/mcp-sonarqube.win-arm64) | 1.3.0 | Marko Lahma | Model Context Protocol server for SonarQube Cloud - projects, quality gates, is… |
| 2026-11-18 19:35:06 | [JTigerNova.Tiffany](https://www.nuget.org/packages/JTigerNova.Tiffany) | 1.0.0 | JTiger Nova | Tiffany, the client SDK for the JTiger Nova platform apis. Targets jtigernova A… |
| 2026-11-18 19:35:08 | [mcp-sonarqube.osx-arm64](https://www.nuget.org/packages/mcp-sonarqube.osx-arm64) | 1.3.0 | Marko Lahma | Model Context Protocol server for SonarQube Cloud - projects, quality gates, is… |
| 2026-11-18 19:35:09 | [mcp-sonarqube.any](https://www.nuget.org/packages/mcp-sonarqube.any) | 1.3.0 | Marko Lahma | Model Context Protocol server for SonarQube Cloud - projects, quality gates, is… |
| 2026-11-18 19:39:37 | [Uniform.MatrixRtc.Hosting](https://www.nuget.org/packages/Uniform.MatrixRtc.Hosting) | 0.1.52 | Uniform.MatrixRtc.Hosting | Runs the Uniform.MatrixRtc.Authorization service in an ASP.NET host: settings i… |
| 2026-11-18 19:39:42 | [Uniform.MatrixRtc.Protocol](https://www.nuget.org/packages/Uniform.MatrixRtc.Protocol) | 0.1.52 | Uniform.MatrixRtc.Protocol | LiveKit's signalling messages, access tokens and their grants, and the MatrixRT… |
| 2026-11-18 19:39:46 | [Uniform.MatrixRtc.Authorization](https://www.nuget.org/packages/Uniform.MatrixRtc.Authorization) | 0.1.52 | Uniform.MatrixRtc.Authorizati… | A MatrixRTC authorization service compatible with lk-jwt-service: verifies Matr… |
| 2026-11-18 19:39:47 | [Uniform.MatrixRtc](https://www.nuget.org/packages/Uniform.MatrixRtc) | 0.1.52 | Uniform.MatrixRtc | A LiveKit client in pure C#: signalling, publishing and subscribing over WebRTC… |
| 2026-11-18 19:49:40 | [Channing.Arce.Client](https://www.nuget.org/packages/Channing.Arce.Client) | 1.0.1 | ChanningMou (牟成贵) | Arce adaptive routing lossless compression engine. |
| 2026-11-18 19:56:22 | [JordiAragonZaragoza.SharedKernel.Hosting](https://www.nuget.org/packages/JordiAragonZaragoza.SharedKernel.Hosting) | 12.1.1 | Jordi Aragon Zaragoza | A simple package to implement the building blocks to follow DDD principles and… |
| 2026-11-18 20:01:43 | [Channing.Arce.Tool](https://www.nuget.org/packages/Channing.Arce.Tool) | 1.0.1 | ChanningMou (牟成贵) | Arce 压缩引擎命令行工具（与 Channing.Arce.Client 配套） |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

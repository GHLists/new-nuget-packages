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

## Latest list — 2026-11-02 02:18 UTC

New packages created between 2026-11-02 01:19 UTC and 2026-11-02 02:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-02T02-18-55-388767Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-02 01:46:49 | [Gsharp.NET.Sdk.Compiler.linux-x64](https://www.nuget.org/packages/Gsharp.NET.Sdk.Compiler.linux-x64) | 0.5.460-g21e3f30fa3 | David Obando | ReadyToRun G# compiler for linux-x64. Gsharp.NET.Sdk restores it with PackageDo… |
| 2026-11-02 01:46:50 | [Gsharp.NET.Sdk.Compiler.linux-arm64](https://www.nuget.org/packages/Gsharp.NET.Sdk.Compiler.linux-arm64) | 0.5.460-g21e3f30fa3 | David Obando | ReadyToRun G# compiler for linux-arm64. Gsharp.NET.Sdk restores it with Package… |
| 2026-11-02 01:46:51 | [Gsharp.NET.Sdk.Compiler.win-x64](https://www.nuget.org/packages/Gsharp.NET.Sdk.Compiler.win-x64) | 0.5.460-g21e3f30fa3 | David Obando | ReadyToRun G# compiler for win-x64. Gsharp.NET.Sdk restores it with PackageDown… |
| 2026-11-02 01:46:52 | [Gsharp.NET.Sdk.Compiler.win-arm64](https://www.nuget.org/packages/Gsharp.NET.Sdk.Compiler.win-arm64) | 0.5.460-g21e3f30fa3 | David Obando | ReadyToRun G# compiler for win-arm64. Gsharp.NET.Sdk restores it with PackageDo… |
| 2026-11-02 01:46:54 | [Gsharp.NET.Sdk.Compiler.osx-x64](https://www.nuget.org/packages/Gsharp.NET.Sdk.Compiler.osx-x64) | 0.5.460-g21e3f30fa3 | David Obando | ReadyToRun G# compiler for osx-x64. Gsharp.NET.Sdk restores it with PackageDown… |
| 2026-11-02 01:46:55 | [Gsharp.NET.Sdk.Compiler.osx-arm64](https://www.nuget.org/packages/Gsharp.NET.Sdk.Compiler.osx-arm64) | 0.5.460-g21e3f30fa3 | David Obando | ReadyToRun G# compiler for osx-arm64. Gsharp.NET.Sdk restores it with PackageDo… |
| 2026-11-02 01:51:58 | [Trevol](https://www.nuget.org/packages/Trevol) | 0.1.0 | Joshua Montclair (Trevol) | SDK de .NET para la API de Trevol (facturación electrónica y demás documentos a… |
| 2026-11-02 01:57:45 | [GoSaveTool](https://www.nuget.org/packages/GoSaveTool) | 1.0.0 | GoSaveTool | Parse, convert, shift and repair SRT and WebVTT subtitles; word, character and… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

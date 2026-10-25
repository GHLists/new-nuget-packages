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

## Latest list — 2026-10-25 17:21 UTC

New packages created between 2026-10-25 16:20 UTC and 2026-10-25 17:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-25T17-21-08-245053Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-25 16:24:56 | [Istok.WebGPU.Native.Linux](https://www.nuget.org/packages/Istok.WebGPU.Native.Linux) | 0.0.5-preview | zvasya | Native WebGPU runtime (Google Dawn) for Linux (x64, arm64): libwebgpu_dawn.so,… |
| 2026-10-25 16:24:58 | [Istok.WebGPU.Native.macOS](https://www.nuget.org/packages/Istok.WebGPU.Native.macOS) | 0.0.5-preview | zvasya | Native WebGPU runtime (Google Dawn) for macOS (universal arm64 + x64): libwebgp… |
| 2026-10-25 16:25:00 | [Istok.WebGPU.Native.Win32](https://www.nuget.org/packages/Istok.WebGPU.Native.Win32) | 0.0.5-preview | zvasya | Native WebGPU runtime (Google Dawn) for Windows (x64, x86, arm64): webgpu_dawn.… |
| 2026-10-25 16:28:09 | [Adiakys.FeelingLucky](https://www.nuget.org/packages/Adiakys.FeelingLucky) | 0.3.0 | FeelingLucky | Multiplayer blackjack and Texas Hold'em tables for the feeling-lucky library, a… |
| 2026-10-25 16:31:10 | [Dotnetstore.BaseModel](https://www.nuget.org/packages/Dotnetstore.BaseModel) | 0.1.0 | Hans Sjödin | Common base models |
| 2026-10-25 16:31:21 | [Workes.ConsoleSystem.Godot.Logging](https://www.nuget.org/packages/Workes.ConsoleSystem.Godot.Logging) | 1.0.0 | Workes | Optional Godot 4.7.2 C# logger adapter for Workes.ConsoleSystem. |
| 2026-10-25 16:35:39 | [Octeka.Settings](https://www.nuget.org/packages/Octeka.Settings) | 1.0.0 | Patrick Robichaud (operating… | High-level, bidirectional, scoped application settings and state persistence fr… |
| 2026-10-25 16:35:40 | [Octeka.Settings.Abstractions](https://www.nuget.org/packages/Octeka.Settings.Abstractions) | 1.0.0 | Patrick Robichaud (operating… | Core abstractions, interfaces, scope taxonomy, and secret attributes for Octeka… |
| 2026-10-25 16:35:41 | [Octeka.Settings.Extensions.Configuration](https://www.nuget.org/packages/Octeka.Settings.Extensions.Configuration) | 1.0.0 | Patrick Robichaud (operating… | Octeka.Configuration integration extensions for feeding configuration into Octe… |
| 2026-10-25 16:35:41 | [Octeka.Settings.Stores.SecretService](https://www.nuget.org/packages/Octeka.Settings.Stores.SecretService) | 1.0.0 | Patrick Robichaud (operating… | Linux FreeDesktop Secret Service secret store backend provider for Octeka.Setti… |
| 2026-10-25 16:35:42 | [Octeka.Settings.Stores.WindowsCredentialManager](https://www.nuget.org/packages/Octeka.Settings.Stores.WindowsCredentialManager) | 1.0.0 | Patrick Robichaud (operating… | Windows Credential Manager secret store backend provider for Octeka.Settings vi… |
| 2026-10-25 16:36:50 | [Nite.Templates](https://www.nuget.org/packages/Nite.Templates) | 0.6.0 | Tim McQueen | dotnet new templates for Nite: a React single-page app (nite-spa) and Razor Pag… |
| 2026-10-25 16:51:38 | [Nullable.Extended.Mcp](https://www.nuget.org/packages/Nullable.Extended.Mcp) | 1.18.0 | Nullable.Extended.Mcp | MCP server to find, review and justify null-forgiving operators in large C# cod… |
| 2026-10-25 17:00:07 | [WinToAws.Cli](https://www.nuget.org/packages/WinToAws.Cli) | 1.0.0 | VENKATESHWAR REDDY VURUMALLA | Command-line tool for the WinToAws library: analyse a Windows application and g… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-09-29 19:20 UTC

New packages created between 2026-09-29 18:20 UTC and 2026-09-29 19:20 UTC.

[Full CSV](data/new-nuget-packages-2026-09-29T19-20-22-720316Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-29 18:31:30 | [GitExtensions.SonetaHarfa](https://www.nuget.org/packages/GitExtensions.SonetaHarfa) | 1.0.0 | Soneta Harfa | Soneta Harfa: Git — zmiany schematu business.xml, stan roboczy vs HEAD, opis co… |
| 2026-09-29 18:46:08 | [CodeTranspiler.Managed](https://www.nuget.org/packages/CodeTranspiler.Managed) | 0.4.1 | Tarek Wasfy and contributors | Dependency-free managed code transpiler with semantic IR, fragment fallback rou… |
| 2026-09-29 18:47:58 | [KUKULCAN.SharedKernel.Auth](https://www.nuget.org/packages/KUKULCAN.SharedKernel.Auth) | 1.0.0 | Kukulcán Software Designer | Provides authentication and authorization components for the KUKULCAN architect… |
| 2026-09-29 18:49:15 | [GameEventScript.Tool](https://www.nuget.org/packages/GameEventScript.Tool) | 0.3.0 | Stephan Schlöpke | Command-line entry point for Game Event Script. |
| 2026-09-29 18:49:17 | [GameEventScript.Tool.Aot.win-x64](https://www.nuget.org/packages/GameEventScript.Tool.Aot.win-x64) | 0.3.0 | Stephan Schlöpke | Command-line entry point for Game Event Script. |
| 2026-09-29 18:49:19 | [GameEventScript.Tool.Aot.win-arm64](https://www.nuget.org/packages/GameEventScript.Tool.Aot.win-arm64) | 0.3.0 | Stephan Schlöpke | Command-line entry point for Game Event Script. |
| 2026-09-29 18:49:20 | [GameEventScript.Tool.Aot.linux-x64](https://www.nuget.org/packages/GameEventScript.Tool.Aot.linux-x64) | 0.3.0 | Stephan Schlöpke | Command-line entry point for Game Event Script. |
| 2026-09-29 18:49:22 | [GameEventScript.Tool.Aot.linux-arm64](https://www.nuget.org/packages/GameEventScript.Tool.Aot.linux-arm64) | 0.3.0 | Stephan Schlöpke | Command-line entry point for Game Event Script. |
| 2026-09-29 18:49:23 | [GameEventScript.Tool.Aot.osx-x64](https://www.nuget.org/packages/GameEventScript.Tool.Aot.osx-x64) | 0.3.0 | Stephan Schlöpke | Command-line entry point for Game Event Script. |
| 2026-09-29 18:49:25 | [GameEventScript.Tool.Aot.osx-arm64](https://www.nuget.org/packages/GameEventScript.Tool.Aot.osx-arm64) | 0.3.0 | Stephan Schlöpke | Command-line entry point for Game Event Script. |
| 2026-09-29 18:49:26 | [GameEventScript.Tool.Aot](https://www.nuget.org/packages/GameEventScript.Tool.Aot) | 0.3.0 | Stephan Schlöpke | Command-line entry point for Game Event Script. |
| 2026-09-29 18:57:09 | [Raukeld.Anvil](https://www.nuget.org/packages/Raukeld.Anvil) | 0.1.0 | Anvil contributors | Server-rendered .NET application framework built on ASP.NET Core and Razor. |
| 2026-09-29 18:57:30 | [Raukeld.Anvil.Razor](https://www.nuget.org/packages/Raukeld.Anvil.Razor) | 0.1.0 | Anvil contributors | Razor components and browser runtime for the Anvil server-rendered framework. |
| 2026-09-29 18:58:23 | [Raukeld.Anvil.Cli](https://www.nuget.org/packages/Raukeld.Anvil.Cli) | 0.1.0 | Anvil contributors | CLI tools for Anvil applications. |
| 2026-09-29 19:03:16 | [Appouse.Safetalk.Core](https://www.nuget.org/packages/Appouse.Safetalk.Core) | 1.0.0 | Appouse | Core primitives of Appouse.Safetalk: request canonicalization and HMAC-SHA256 s… |
| 2026-09-29 19:03:17 | [Appouse.Safetalk.Abstractions](https://www.nuget.org/packages/Appouse.Safetalk.Abstractions) | 1.0.0 | Appouse | Dependency-free contracts of Appouse.Safetalk (IHmacSignatureService, IHmacSecr… |
| 2026-09-29 19:03:18 | [Appouse.Safetalk.Client](https://www.nuget.org/packages/Appouse.Safetalk.Client) | 1.0.0 | Appouse | HttpClient integration for Appouse.Safetalk: a DelegatingHandler that signs out… |
| 2026-09-29 19:03:19 | [Appouse.Safetalk.Server](https://www.nuget.org/packages/Appouse.Safetalk.Server) | 1.0.0 | Appouse | ASP.NET Core integration for Appouse.Safetalk: a middleware that verifies HMAC-… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

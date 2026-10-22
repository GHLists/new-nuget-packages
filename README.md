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

## Latest list — 2026-10-22 18:19 UTC

New packages created between 2026-10-22 17:19 UTC and 2026-10-22 18:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-22T18-19-31-328563Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-22 17:19:56 | [Tapline.Wasm](https://www.nuget.org/packages/Tapline.Wasm) | 0.1.0 | Mark Hammond | Tapline's WebAssembly, run by Wasmtime: a data provider's folds, finalizers and… |
| 2026-10-22 17:20:24 | [Tapline.Client.Opaque](https://www.nuget.org/packages/Tapline.Client.Opaque) | 0.1.0 | Mark Hammond | A .NET client's password sign-in to Tapline by OPAQUE (RFC 9807), the password… |
| 2026-10-22 17:21:08 | [Tapline.Client](https://www.nuget.org/packages/Tapline.Client) | 0.1.0 | Mark Hammond | Tapline's core and its .NET client: shared state fanned out to many clients, pr… |
| 2026-10-22 17:33:48 | [Runic.Translations](https://www.nuget.org/packages/Runic.Translations) | 0.8.0 | RunicArtifex | Runtime contracts for compiled Runic Translations. |
| 2026-10-22 17:33:48 | [Runic.Translations.Build](https://www.nuget.org/packages/Runic.Translations.Build) | 0.8.0 | RunicArtifex | Deterministic MSBuild integration for Runic.Translations translation artifacts. |
| 2026-10-22 17:33:49 | [Runic.Translations.CommandLine](https://www.nuget.org/packages/Runic.Translations.CommandLine) | 0.8.0 | RunicArtifex | Translates Runic.CommandLine help, errors and faults with Runic Translations, w… |
| 2026-10-22 17:33:49 | [Runic.Translations.Tooling](https://www.nuget.org/packages/Runic.Translations.Tooling) | 0.8.0 | RunicArtifex | MF2 compiler, interchange, and transactional authoring facade for Runic Transla… |
| 2026-10-22 17:33:50 | [Runic.Translations.Wpf](https://www.nuget.org/packages/Runic.Translations.Wpf) | 0.8.0 | RunicArtifex | WPF inline and document rendering for compiled RMF2 messages. |
| 2026-10-22 17:33:51 | [Runic.Translations.Templates](https://www.nuget.org/packages/Runic.Translations.Templates) | 0.8.0 | RunicArtifex | .NET project and item templates for Runic Translations. |
| 2026-10-22 17:33:51 | [dotnet-runic-translations](https://www.nuget.org/packages/dotnet-runic-translations) | 0.8.0 | RunicArtifex | Deterministic validation and generation tool for Runic Translations. |
| 2026-10-22 17:38:50 | [Scarlet.AspNetCore.Components.WebView.Win32Aot](https://www.nuget.org/packages/Scarlet.AspNetCore.Components.WebView.Win32Aot) | 1.2.1 | ScarletKuro | Build native Win32 apps with Blazor and WebView2, NativeAOT and trimming friend… |
| 2026-10-22 18:03:48 | [Aurix.Server](https://www.nuget.org/packages/Aurix.Server) | 1.8.1 | Aurix contributors | Server-side (game backend) SDK for the Aurix voice platform REST API: token iss… |
| 2026-10-22 18:05:20 | [Lowline](https://www.nuget.org/packages/Lowline) | 0.1.0 | iyulab | A form engine that learns from the records people confirm: suggestions for a fo… |
| 2026-10-22 18:05:20 | [Lowline.Sqlite](https://www.nuget.org/packages/Lowline.Sqlite) | 0.1.0 | iyulab | A SQLite store for the Lowline engine: the settled records and the tuning of ea… |
| 2026-10-22 18:05:21 | [Lowline.AspNetCore](https://www.nuget.org/packages/Lowline.AspNetCore) | 0.1.0 | iyulab | ASP.NET Core endpoints for the Lowline engine: AddLowline and MapLowline put a… |
| 2026-10-22 18:09:26 | [RateLimitEngine.AspNetCore](https://www.nuget.org/packages/RateLimitEngine.AspNetCore) | 1.0.1 | Peyman Salimi | ASP.NET Core middleware integration for RateLimitEngine with in-memory and Redi… |
| 2026-10-22 18:09:26 | [RateLimitEngine.Core](https://www.nuget.org/packages/RateLimitEngine.Core) | 1.0.1 | Peyman Salimi | Core abstractions, models, timing, observability, and contracts for RateLimitEn… |
| 2026-10-22 18:09:27 | [RateLimitEngine.Algorithms](https://www.nuget.org/packages/RateLimitEngine.Algorithms) | 1.0.1 | Peyman Salimi | In-memory rate limiting algorithms for RateLimitEngine, including Fixed Window,… |
| 2026-10-22 18:09:28 | [RateLimitEngine.Redis](https://www.nuget.org/packages/RateLimitEngine.Redis) | 1.0.1 | Peyman Salimi | Redis-backed distributed rate limiting infrastructure for RateLimitEngine. |
| 2026-10-22 18:11:34 | [JsonPropertyAttribute](https://www.nuget.org/packages/JsonPropertyAttribute) | 0.0.1 | AXCWG | Store complex CLR properties in a single TEXT column with System.Text.Json: mar… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

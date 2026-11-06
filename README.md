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

## Latest list — 2026-11-06 15:19 UTC

New packages created between 2026-11-06 14:22 UTC and 2026-11-06 15:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-06T15-19-54-973449Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-06 14:25:53 | [specht.mcp](https://www.nuget.org/packages/specht.mcp) | 0.5.12-preview | Rodney Littles, II | An MCP server that gives a coding agent the verdict of the specht its repositor… |
| 2026-11-06 14:37:30 | [EhLib.WinForms.Trial](https://www.nuget.org/packages/EhLib.WinForms.Trial) | 2.0.6 | Dmitriy V. Bolshakov | EhLib.WinForms - Trial Edition. For evaluation purposes only. |
| 2026-11-06 14:38:54 | [Provance.Storage.EntityFrameworkCore](https://www.nuget.org/packages/Provance.Storage.EntityFrameworkCore) | 0.1.0 | H. Id Brahim | Entity Framework Core store for PROVANCE tamper-evident ledgers: SQL Server, Po… |
| 2026-11-06 14:46:33 | [Reactive.Compiler](https://www.nuget.org/packages/Reactive.Compiler) | 1.0.0 | Reactive.Compiler | Source generators and analyzers for Reactive. |
| 2026-11-06 14:49:24 | [Ekom.Printer](https://www.nuget.org/packages/Ekom.Printer) | 1.0.0 | Vettvangur | Optional HTML picking-slip queue and rendering for Ekom. |
| 2026-11-06 14:49:25 | [BccCode.PubSub.AspNetCore](https://www.nuget.org/packages/BccCode.PubSub.AspNetCore) | 1.0.49 | BCC Code | ASP.NET Core helpers for bcc-pubsub subscribers: verify the signed X-PubSub-Tok… |
| 2026-11-06 14:50:44 | [NSail.Localization.Testing](https://www.nuget.org/packages/NSail.Localization.Testing) | 0.1.547 | Leonardo Porro,Emmanuel Arias | NSail.Localization.Testing, part of NSail Stack: a .NET modular-monolith framew… |
| 2026-11-06 14:50:50 | [NSail.Harness.OpenObserve](https://www.nuget.org/packages/NSail.Harness.OpenObserve) | 0.1.546 | Leonardo Porro,Emmanuel Arias | NSail.Harness.OpenObserve, part of NSail Stack: a .NET modular-monolith framewo… |
| 2026-11-06 14:51:33 | [Whatfix.Mobile.Android.Binding](https://www.nuget.org/packages/Whatfix.Mobile.Android.Binding) | 0.1.3 | Whatfix Mobile Team | Internal Android binding used by Whatfix.Mobile.Maui. |
| 2026-11-06 14:51:34 | [Whatfix.Mobile.iOS.Binding](https://www.nuget.org/packages/Whatfix.Mobile.iOS.Binding) | 0.1.3 | Whatfix Mobile Team | Internal iOS binding used by Whatfix.Mobile.Maui. |
| 2026-11-06 14:51:35 | [Whatfix.Mobile.Maui](https://www.nuget.org/packages/Whatfix.Mobile.Maui) | 0.1.3 | Whatfix Mobile Team | Thin .NET MAUI wrapper for the native Whatfix Android and iOS SDKs. |
| 2026-11-06 14:56:30 | [OpenCodeDotNet.Sdk.Extensions](https://www.nuget.org/packages/OpenCodeDotNet.Sdk.Extensions) | 1.0.0 | Deniz İrgin | Dependency injection for the unofficial OpenCode .NET SDK: AddOpenCode register… |
| 2026-11-06 14:56:31 | [OpenCodeDotNet.Sdk](https://www.nuget.org/packages/OpenCodeDotNet.Sdk) | 1.0.0 | Deniz İrgin | Unofficial .NET SDK for OpenCode: a typed client for the OpenCode 2.x server HT… |
| 2026-11-06 15:00:08 | [SkiaUi.Maui.Markdown](https://www.nuget.org/packages/SkiaUi.Maui.Markdown) | 1.8.0 | Rafal Kukla | A drawn Markdown view for SkiaUi.Maui: headings, lists, tables, code, quotes, a… |
| 2026-11-06 15:00:10 | [SkiaUi.Maui.Markdown.Math](https://www.nuget.org/packages/SkiaUi.Maui.Markdown.Math) | 1.8.0 | Rafal Kukla | Formulas for SkiaUi.Maui.Markdown: LaTeX drawn with CSharpMath, in documents th… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

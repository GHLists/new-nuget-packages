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

## Latest list — 2026-10-12 14:20 UTC

New packages created between 2026-10-12 13:21 UTC and 2026-10-12 14:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-12T14-20-45-285088Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-12 13:28:28 | [Crypto.Net.Templates](https://www.nuget.org/packages/Crypto.Net.Templates) | 1.1.0 | Gravicode Studios, Kang Fadhil | dotnet new templates for Crypto.Net: cnet-console, cnet-worker, cnet-webapi, cn… |
| 2026-10-12 13:31:45 | [EfCore.TamperEvident.AspNetCore](https://www.nuget.org/packages/EfCore.TamperEvident.AspNetCore) | 2.0.0 | Furkan Akca | ASP.NET Core integration for EfCore.TamperEvident: a Liquid Glass audit dashboa… |
| 2026-10-12 13:31:46 | [EfCore.TamperEvident.Cli](https://www.nuget.org/packages/EfCore.TamperEvident.Cli) | 2.0.0 | Furkan Akca | A .NET tool for auditors: verifies EfCore.TamperEvident evidence bundles offlin… |
| 2026-10-12 13:33:12 | [EAC.Plugin.FeatureFolder](https://www.nuget.org/packages/EAC.Plugin.FeatureFolder) | 1.0.1 | EAC.Plugin.FeatureFolder | Roslyn analyzer and codefix for feature-folder namespace placement conventions. |
| 2026-10-12 13:33:17 | [EAC.Plugin.Localization](https://www.nuget.org/packages/EAC.Plugin.Localization) | 1.0.1 | EAC.Plugin.Localization | Roslyn analyzers for localization adoption and hardcoded user-facing message si… |
| 2026-10-12 13:33:22 | [EAC.Plugin.Naming](https://www.nuget.org/packages/EAC.Plugin.Naming) | 1.0.1 | EAC.Plugin.Naming | Roslyn analyzers and code fixes for deterministic naming conventions. |
| 2026-10-12 13:33:31 | [Eternet.Agents.Control.Plans.Abstractions](https://www.nuget.org/packages/Eternet.Agents.Control.Plans.Abstractions) | 2.0.18 | Eternet | Host-neutral contracts for EAC plan execution, backends, diagnostics, and evide… |
| 2026-10-12 13:33:40 | [EAC.Plugin.BuiltInRecipes](https://www.nuget.org/packages/EAC.Plugin.BuiltInRecipes) | 1.0.1 | Eternet | Built-in EAC recipe and guidance suggestion plugin contributions. |
| 2026-10-12 13:33:46 | [EAC.Plugin.Contracts](https://www.nuget.org/packages/EAC.Plugin.Contracts) | 1.0.1 | EAC.Plugin.Contracts | Roslyn analyzers, code fixes, and runtime remediation for public contract guida… |
| 2026-10-12 13:33:51 | [EAC.Plugin.Crud.Relational](https://www.nuget.org/packages/EAC.Plugin.Crud.Relational) | 1.0.1 | Eternet | EAC plugin with relational pipeline migration and manual retry migration transf… |
| 2026-10-12 13:33:56 | [EAC.Plugin.DependencyInjection](https://www.nuget.org/packages/EAC.Plugin.DependencyInjection) | 1.0.1 | EAC.Plugin.DependencyInjection | Roslyn analyzers and runtime metadata for semantic dependency-injection registr… |
| 2026-10-12 13:34:01 | [EAC.Plugin.DotNet](https://www.nuget.org/packages/EAC.Plugin.DotNet) | 1.0.1 | EAC.Plugin.DotNet | Roslyn analyzers and runtime metadata for EAC-owned .NET reliability diagnostic… |
| 2026-10-12 13:34:08 | [EAC.Plugin.EternetMediatorGenerator](https://www.nuget.org/packages/EAC.Plugin.EternetMediatorGenerator) | 1.0.1 | EAC.Plugin.EternetMediatorGen… | Runtime recipes and compatibility remediation for diagnostics emitted by Eterne… |
| 2026-10-12 13:34:12 | [EAC.Plugin.Git](https://www.nuget.org/packages/EAC.Plugin.Git) | 1.0.1 | Eternet | Built-in Git repository maintenance runtime plugin for nested EAC CLI operation… |
| 2026-10-12 13:34:17 | [EAC.Plugin.Maintenance](https://www.nuget.org/packages/EAC.Plugin.Maintenance) | 1.0.1 | Eternet | Built-in repository normalization and .NET code maintenance operations for EAC. |
| 2026-10-12 13:34:22 | [EAC.Plugin.Mediator](https://www.nuget.org/packages/EAC.Plugin.Mediator) | 1.0.1 | EAC.Plugin.Mediator | Roslyn analyzers, code fixes, and runtime transformations for Eternet.Mediator… |
| 2026-10-12 13:34:29 | [EAC.Plugin.Networking](https://www.nuget.org/packages/EAC.Plugin.Networking) | 1.0.1 | Eternet | EAC plugin for networking diagnostics and HttpClient lifetime remediation recip… |
| 2026-10-12 13:34:33 | [EAC.Plugin.OData](https://www.nuget.org/packages/EAC.Plugin.OData) | 1.0.1 | EAC.Plugin.OData | Roslyn analyzers for Eternet OData and query-service read-shape rules. |
| 2026-10-12 13:34:38 | [EAC.Plugin.Outbox](https://www.nuget.org/packages/EAC.Plugin.Outbox) | 1.0.1 | Eternet | EAC plugin for target-agnostic outbox diagnostics. |
| 2026-10-12 13:34:43 | [EAC.Plugin.Plans](https://www.nuget.org/packages/EAC.Plugin.Plans) | 1.0.1 | Eternet | Built-in EAC plan-folder plugin operations and compatibility metadata. |
| 2026-10-12 13:34:49 | [EAC.Plugin.Review](https://www.nuget.org/packages/EAC.Plugin.Review) | 1.0.1 | Eternet | EAC plugin with source-only review diagnostics such as repo-root portability de… |
| 2026-10-12 13:34:56 | [EAC.Plugin.Search](https://www.nuget.org/packages/EAC.Plugin.Search) | 1.0.1 | Eternet | Built-in knowledge search runtime plugin for hybrid lexical and semantic retrie… |
| 2026-10-12 13:35:01 | [EAC.Plugin.Validation](https://www.nuget.org/packages/EAC.Plugin.Validation) | 1.0.1 | Eternet | EAC plugin that reserves validation remediation metadata and built-in capabilit… |
| 2026-10-12 13:35:35 | [Eternet.Agents.Control.WorkspaceHost](https://www.nuget.org/packages/Eternet.Agents.Control.WorkspaceHost) | 2.1.1 | Eternet | Private prepared diagnostic worker host for EAC plan and workspace sessions. |
| 2026-10-12 13:35:41 | [EAC.Plugin.AnalyzerCatalog](https://www.nuget.org/packages/EAC.Plugin.AnalyzerCatalog) | 1.0.1 | Eternet | EAC Analyzer catalog plugin that declares the analyzer packages required by EAC… |
| 2026-10-12 13:45:07 | [ESCPOS_NET_J](https://www.nuget.org/packages/ESCPOS_NET_J) | 0.1.0 | Jonathan Soderberg, Luke Pair… | .NET 10 implementation of ESC/POS command generation and integration with therm… |
| 2026-10-12 13:45:25 | [Termin.Graphics](https://www.nuget.org/packages/Termin.Graphics) | 0.5.2 | Termin contributors | Windows x64 D3D11 runtime and C# bindings for Termin Graphics. |
| 2026-10-12 13:47:10 | [RP.WpfStyledWindow](https://www.nuget.org/packages/RP.WpfStyledWindow) | 1.0.0 | Roman Padura | A customizable WPF Window with rounded corners, a styled title bar and configur… |
| 2026-10-12 13:48:09 | [DynamicDave.Umbraco.ContentHealth](https://www.nuget.org/packages/DynamicDave.Umbraco.ContentHealth) | 18.0.2 | DynamicDave | Finds broken internal links in Umbraco content: links to deleted, trashed or un… |
| 2026-10-12 13:51:25 | [Dijitalya.Imaging](https://www.nuget.org/packages/Dijitalya.Imaging) | 1.0.0 | Dijitalya | Image codecs and processing in pure C# with no dependencies and no native code.… |
| 2026-10-12 13:53:00 | [Termin.Graphics.Wpf](https://www.nuget.org/packages/Termin.Graphics.Wpf) | 0.5.2 | Termin contributors | WPF hosts for the Termin Graphics Windows D3D11 runtime. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

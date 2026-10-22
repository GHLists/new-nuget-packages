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

## Latest list — 2026-10-22 04:19 UTC

New packages created between 2026-10-22 03:22 UTC and 2026-10-22 04:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-22T04-19-15-349756Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-22 03:22:33 | [NetSlice.Cli](https://www.nuget.org/packages/NetSlice.Cli) | 1.0.0 | x64silva | Enterprise CLI tool to scaffold Vertical Slice Architecture endpoints in NetSli… |
| 2026-10-22 03:22:37 | [Rocket.Surgery.AssemblyInfo](https://www.nuget.org/packages/Rocket.Surgery.AssemblyInfo) | 2026.10.3 | David Driscoll,Rocket Surgeon… | Package Description |
| 2026-10-22 03:43:08 | [JvmBridge.Testing](https://www.nuget.org/packages/JvmBridge.Testing) | 26.10.22.2272 | void-community | Test helpers for JvmBridge agents on xUnit v3: checksum-pinned JDKs, javac and… |
| 2026-10-22 03:43:09 | [JvmBridge.Templates](https://www.nuget.org/packages/JvmBridge.Templates) | 26.10.22.2272 | void-community | The jvmbridge-agent template for dotnet new: a NativeAOT JVM agent with a decla… |
| 2026-10-22 03:47:29 | [accesskit-dotnet](https://www.nuget.org/packages/accesskit-dotnet) | 0.23.1.8 | drasticactions | .NET bindings for AccessKit |
| 2026-10-22 03:47:45 | [accesskit-dotnet.avalonia](https://www.nuget.org/packages/accesskit-dotnet.avalonia) | 0.23.1.8 | drasticactions | Avalonia AccessKit Support |
| 2026-10-22 03:52:29 | [Egap.Documents.Html](https://www.nuget.org/packages/Egap.Documents.Html) | 2.0.0 | Lars Dytterud | HTML for Egap.Documents: HTML and XHTML read into the document model through th… |
| 2026-10-22 03:52:29 | [Egap.Documents.Markdown](https://www.nuget.org/packages/Egap.Documents.Markdown) | 2.0.0 | Lars Dytterud | Markdown for Egap.Documents: CommonMark and GitHub Markdown read into the docum… |
| 2026-10-22 03:59:39 | [TedToolkit.DependencyInjection](https://www.nuget.org/packages/TedToolkit.DependencyInjection) | 2026.10.22 | TedToolkit | Compile-time service registration and dependency modules for Microsoft.Extensio… |
| 2026-10-22 04:03:55 | [VikashKumar.XrmToolBox.DiagnosticsWorkbench](https://www.nuget.org/packages/VikashKumar.XrmToolBox.DiagnosticsWorkbench) | 1.2026.10.1 | Vikash Kumar | Dataverse Developer Diagnostics Workbench turns plug-in trace logs into actiona… |
| 2026-10-22 04:03:56 | [AcnhModding.BfevLibrary](https://www.nuget.org/packages/AcnhModding.BfevLibrary) | 1.0.0 | Arch Leaders | ACNH Modding fork of BfevLibrary with EventFlowToCode serialization fixes. Base… |
| 2026-10-22 04:11:40 | [Zhomfr.Helpers.SmartFile](https://www.nuget.org/packages/Zhomfr.Helpers.SmartFile) | 0.4.0 | zhuolyan (Oleg Zhuravskiy) | Helpers for working with file streams. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

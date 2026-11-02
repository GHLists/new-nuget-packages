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

## Latest list — 2026-11-02 22:21 UTC

New packages created between 2026-11-02 21:21 UTC and 2026-11-02 22:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-02T22-21-10-730353Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-02 21:33:01 | [Kapusch.RevenueCatUI.iOS](https://www.nuget.org/packages/Kapusch.RevenueCatUI.iOS) | 1.0.0 | Kapusch | Thin .NET iOS interop for RevenueCat Paywalls (RevenueCatUI), on top of the Keb… |
| 2026-11-02 21:39:30 | [RazorFmt.Cli](https://www.nuget.org/packages/RazorFmt.Cli) | 0.1.0 | vybraan | Experimental formatter for Razor (.razor and .cshtml) markup and C#. |
| 2026-11-02 21:47:37 | [OptionsGuard](https://www.nuget.org/packages/OptionsGuard) | 1.0.0 | OptionsGuard contributors | Validação de configuração no startup para aplicações .NET. Faça sua app falhar… |
| 2026-11-02 21:52:02 | [Distaff](https://www.nuget.org/packages/Distaff) | 0.1.0-alpha | Jeff Nyman | Command line player for Loom (DOS EGA, FM Towns, DOS VGA CD): dotnet tool insta… |
| 2026-11-02 21:52:03 | [Distaff.Audio](https://www.nuget.org/packages/Distaff.Audio) | 0.1.0-alpha | Jeff Nyman | Decoders for the CD audio tracks Loom's CD releases play from files: FLAC, and… |
| 2026-11-02 21:52:04 | [Distaff.Scumm](https://www.nuget.org/packages/Distaff.Scumm) | 0.1.0-alpha | Jeff Nyman | The SCUMM interpreter for Loom (EGA, VGA CD and FM Towns), ported from ScummVM. |
| 2026-11-02 21:54:37 | [Ef.Mems](https://www.nuget.org/packages/Ef.Mems) | 1.0.0 | pyrami | In-memory cache layer for Entity Framework Core for single-writer applications.… |
| 2026-11-02 22:04:18 | [Senparc.Ncf.IsolatedRuntime](https://www.nuget.org/packages/Senparc.Ncf.IsolatedRuntime) | 0.1.0-preview1 | NeuCharFramework | NeuCharFramework shared isolated runtime providers. |
| 2026-11-02 22:06:40 | [Senparc.Xncf.Workspace](https://www.nuget.org/packages/Senparc.Xncf.Workspace) | 0.2.4 | Senparc.Xncf.Workspace | Package Description |
| 2026-11-02 22:08:00 | [Jeninnet.FileQuery.Tooling](https://www.nuget.org/packages/Jeninnet.FileQuery.Tooling) | 2.0.0 | Tarek Najem | Build-tooling SDK for Jeninnet.FileQuery: classify, validate, and tokenize patt… |
| 2026-11-02 22:08:00 | [Jeninnet.FileQuery.Analyzers](https://www.nuget.org/packages/Jeninnet.FileQuery.Analyzers) | 2.0.0 | Tarek Najem | Roslyn analyzer and code fix for Jeninnet.FileQuery pattern literals. Detects m… |
| 2026-11-02 22:08:01 | [Jeninnet.FileQuery.Build](https://www.nuget.org/packages/Jeninnet.FileQuery.Build) | 2.0.0 | Tarek Najem | MSBuild integration for Jeninnet.FileQuery: validate FileQueryPatterns at evalu… |
| 2026-11-02 22:08:02 | [Jeninnet.FileQuery.Tool](https://www.nuget.org/packages/Jeninnet.FileQuery.Tool) | 2.0.0 | Tarek Najem | Terminal file discovery tool built on Jeninnet.FileQuery. Matches GitIgnore, Gl… |
| 2026-11-02 22:08:03 | [Jeninnet.FileQuery.FileProviders](https://www.nuget.org/packages/Jeninnet.FileQuery.FileProviders) | 2.0.0 | Tarek Najem | Query Microsoft.Extensions.FileProviders sources with Jeninnet.FileQuery: physi… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-01 23:20 UTC

New packages created between 2026-11-01 22:21 UTC and 2026-11-01 23:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-01T23-20-27-525817Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-01 22:28:57 | [Vek.Blazor.DataGrid](https://www.nuget.org/packages/Vek.Blazor.DataGrid) | 1.0.0 | AMIN SABAGHI | Data grid components for Blazor and .NET 10. |
| 2026-11-01 22:28:58 | [Vek.WPF.DataGrid](https://www.nuget.org/packages/Vek.WPF.DataGrid) | 1.0.0 | AMIN SABAGHI | Native data grid components for WPF and .NET 10. |
| 2026-11-01 22:30:15 | [AetherDevel.NodifyAvalonia](https://www.nuget.org/packages/AetherDevel.NodifyAvalonia) | 7.0.1 | miroiu, bandysc, aether-devel | The core controls for a node based editor (designed for MVVM) for Avalonia 12 /… |
| 2026-11-01 22:41:37 | [XISOSharp.Tool](https://www.nuget.org/packages/XISOSharp.Tool) | 1.5.0 | XISOSharp.Cli | XISOSharp command-line tool: create, extract, list, rewrite, compress and archi… |
| 2026-11-01 22:47:42 | [AgdirLabs.Email.Extensions.DependencyInjection](https://www.nuget.org/packages/AgdirLabs.Email.Extensions.DependencyInjection) | 0.1.0 | Agdir AS | Registers the Agdir Email client with Microsoft.Extensions.DependencyInjection:… |
| 2026-11-01 22:47:43 | [AgdirLabs.Email](https://www.nuget.org/packages/AgdirLabs.Email) | 0.1.0 | Agdir AS | Official .NET SDK for Agdir Email — programmatic SMTP for developers, hosted in… |
| 2026-11-01 22:51:54 | [ProjectZ.Diagnostics](https://www.nuget.org/packages/ProjectZ.Diagnostics) | 2026.11.1.1 | Project-Z | Optional standalone native crash observer and dump capture for Project-Z applic… |
| 2026-11-01 22:51:56 | [ProjectZ.ModelImport](https://www.nuget.org/packages/ProjectZ.ModelImport) | 2026.11.1.1 | Project-Z | Optional Assimp OBJ/FBX model importing for Project-Z applications. |
| 2026-11-01 22:51:57 | [ProjectZ.WebView2](https://www.nuget.org/packages/ProjectZ.WebView2) | 2026.11.1.1 | Project-Z | Optional WebView2 HTML5 hosting for Project-Z applications. |
| 2026-11-01 22:51:58 | [ProjectZ.XamlTools](https://www.nuget.org/packages/ProjectZ.XamlTools) | 2026.11.1.1 | Project-Z | Optional build-time XAML conversion and native scene compiler tools for Project… |
| 2026-11-01 22:55:01 | [Singulink.Net.Http.Api.Client.Native](https://www.nuget.org/packages/Singulink.Net.Http.Api.Client.Native) | 4.1.0 | Singulink | iOS keychain and web authentication session support for Singulink.Net.Http.Api.… |
| 2026-11-01 23:10:59 | [Eleven19.IonDotnet](https://www.nuget.org/packages/Eleven19.IonDotnet) | 0.1.0 | amazon-ion | A .NET implementation of Amazon Ion. http://amzn.github.io/ion-docs/ |
| 2026-11-01 23:11:55 | [XLibur.Fonts.PinataLabs](https://www.nuget.org/packages/XLibur.Fonts.PinataLabs) | 0.800.0 | XLibur Contributors | See release notes https://github.com/XLibur/XLibur/releases/tag/v0.800.0 Pinata… |
| 2026-11-01 23:12:44 | [Kubata.CityFix.Common](https://www.nuget.org/packages/Kubata.CityFix.Common) | 1.0.0 | Marharyta Kubata | Reusable building blocks for ASP.NET Core applications: paging over IQueryable,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

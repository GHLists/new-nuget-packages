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

## Latest list — 2026-11-27 06:19 UTC

New packages created between 2026-11-27 05:19 UTC and 2026-11-27 06:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-27T06-19-41-069597Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-27 05:26:42 | [PurpleAirAPI](https://www.nuget.org/packages/PurpleAirAPI) | 2026.11.26 | Carlos Santos | PurpleAir API C# bindings with C++ backend |
| 2026-11-27 06:04:20 | [Plex.Studio.Export](https://www.nuget.org/packages/Plex.Studio.Export) | 8.0.1 | Tom Lee | A dependency-free .NET 8 document exporter: describe a document once (headings,… |
| 2026-11-27 06:06:15 | [Gtk4.MarkupCompiler](https://www.nuget.org/packages/Gtk4.MarkupCompiler) | 1.0.0.26331 | Microsoft, Piero Viano | Build-time WPF XAML markup compiler for the Gtk4.Wpf compatibility layer. |
| 2026-11-27 06:06:22 | [Gtk4.PresentationFramework](https://www.nuget.org/packages/Gtk4.PresentationFramework) | 1.0.0.26331 | Microsoft, Piero Viano | Package Description |
| 2026-11-27 06:06:25 | [Gtk4.WindowsBase](https://www.nuget.org/packages/Gtk4.WindowsBase) | 1.0.0.26331 | Microsoft, Piero Viano | Package Description |
| 2026-11-27 06:06:28 | [Gtk4.Wpf](https://www.nuget.org/packages/Gtk4.Wpf) | 1.0.0.26331 | Microsoft, Piero Viano | Meta-package: add one PackageReference to run an existing WPF app on GTK 4 with… |
| 2026-11-27 06:06:31 | [Net4x.Html2Markdown](https://www.nuget.org/packages/Net4x.Html2Markdown) | 1.0.0.26330 | Html2Markdown.Library | Package Description |
| 2026-11-27 06:06:34 | [Net4x.RewriteGitHistory](https://www.nuget.org/packages/Net4x.RewriteGitHistory) | 2.3.0.26330 | RewriteGitHistory.Library | Package Description |
| 2026-11-27 06:07:55 | [DbRelay.MySql](https://www.nuget.org/packages/DbRelay.MySql) | 0.3.0 | DbRelay contributors | MySQL and MariaDB storage provider for DbRelay (MySqlConnector): transactional… |
| 2026-11-27 06:07:57 | [DbRelay.Oracle](https://www.nuget.org/packages/DbRelay.Oracle) | 0.3.0 | DbRelay contributors | Oracle storage provider for DbRelay (ODP.NET Core): transactional outbox insert… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

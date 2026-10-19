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

## Latest list — 2026-10-19 14:22 UTC

New packages created between 2026-10-19 13:20 UTC and 2026-10-19 14:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-19T14-22-31-312379Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-19 13:24:23 | [ContractWatcher.SDK](https://www.nuget.org/packages/ContractWatcher.SDK) | 1.0.0 | a1unade | .NET SDK for integrating applications with ContractWatcher. |
| 2026-10-19 13:33:04 | [Meziantou.Framework.HumanReadableSerializer.Html](https://www.nuget.org/packages/Meziantou.Framework.HumanReadableSerializer.Html) | 1.0.0 | meziantou | Formats the HTML values (text/html) serialized by Meziantou.Framework.HumanRead… |
| 2026-10-19 13:38:58 | [Nordiska.PdfEngine.Native](https://www.nuget.org/packages/Nordiska.PdfEngine.Native) | 0.1.0 | Nordiska Team 2 | Native pdf_engine library (PDF generation + signing) for win-x64 and linux-x64.… |
| 2026-10-19 13:43:43 | [Beresta.Markdown.Wpf](https://www.nuget.org/packages/Beresta.Markdown.Wpf) | 0.8.0 | Porohkun | Fast native Markdown viewer for WPF, no browser or FlowDocument: virtualized fo… |
| 2026-10-19 13:53:19 | [NMF-AnyText-AspnetCore](https://www.nuget.org/packages/NMF-AnyText-AspnetCore) | 3.0.10 | Georg Hinkel | This package contains the AnyText bindings for ASP.NET Core |
| 2026-10-19 13:58:26 | [Aiursoft.Kanban.Client](https://www.nuget.org/packages/Aiursoft.Kanban.Client) | 10.0.0 | kanban | Manage Kanban boards, columns and cards using a personal API key. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

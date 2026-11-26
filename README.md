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

## Latest list — 2026-11-26 23:21 UTC

New packages created between 2026-11-26 22:20 UTC and 2026-11-26 23:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-26T23-21-29-881917Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-26 22:34:24 | [Skywithin.DevKit](https://www.nuget.org/packages/Skywithin.DevKit) | 0.3.0 | Max Vagner | A markdown backlog in your repository (backlog/items/*.md with frontmatter) and… |
| 2026-11-26 22:40:51 | [IOViewer.Cli.any](https://www.nuget.org/packages/IOViewer.Cli.any) | 0.4.2 | mahach666 | Command line tool for generating standalone interactive 3D WebGL/HTML BIM & CAD… |
| 2026-11-26 22:40:53 | [IOViewer.Cli.linux-x64](https://www.nuget.org/packages/IOViewer.Cli.linux-x64) | 0.4.2 | mahach666 | Command line tool for generating standalone interactive 3D WebGL/HTML BIM & CAD… |
| 2026-11-26 22:40:55 | [IOViewer.Cli.osx-arm64](https://www.nuget.org/packages/IOViewer.Cli.osx-arm64) | 0.4.2 | mahach666 | Command line tool for generating standalone interactive 3D WebGL/HTML BIM & CAD… |
| 2026-11-26 22:40:56 | [IOViewer.Cli.win-x64](https://www.nuget.org/packages/IOViewer.Cli.win-x64) | 0.4.2 | mahach666 | Command line tool for generating standalone interactive 3D WebGL/HTML BIM & CAD… |
| 2026-11-26 22:42:43 | [Gravicode.Science.DaskNet.Kafka](https://www.nuget.org/packages/Gravicode.Science.DaskNet.Kafka) | 2.5.0 | Gravicode Studios | Apache Kafka for Dask.Net streaming: consumer-group sources with checkpointed o… |
| 2026-11-26 22:46:32 | [Umbraco.Community.Formulate.Extensions.SendEmail](https://www.nuget.org/packages/Umbraco.Community.Formulate.Extensions.SendEmail) | 5.0.0 | Nicholas Westby, Jamie Pollock | An email notification extension for Formulate, an advanced form builder for Umb… |
| 2026-11-26 22:46:33 | [Umbraco.Community.Formulate.Extensions.PlainJavaScriptTemplate](https://www.nuget.org/packages/Umbraco.Community.Formulate.Extensions.PlainJavaScriptTemplate) | 5.0.0 | Nicholas Westby, Jamie Pollock | A plain JavaScript template extension for Formulate, an advanced form builder f… |
| 2026-11-26 22:46:33 | [Umbraco.Community.Formulate.Extensions.SendData](https://www.nuget.org/packages/Umbraco.Community.Formulate.Extensions.SendData) | 5.0.0 | Nicholas Westby, Jamie Pollock | A data sending extension for Formulate, an advanced form builder for Umbraco. |
| 2026-11-26 22:46:34 | [Umbraco.Community.Formulate.Web](https://www.nuget.org/packages/Umbraco.Community.Formulate.Web) | 5.0.0 | Nicholas Westby, Jamie Pollock | Web functionality for Formulate, an advanced form builder for Umbraco. |
| 2026-11-26 22:46:34 | [Umbraco.Community.Formulate.Core](https://www.nuget.org/packages/Umbraco.Community.Formulate.Core) | 5.0.0 | Nicholas Westby, Jamie Pollock | Core functionality for Formulate, an advanced form builder for Umbraco. |
| 2026-11-26 22:46:34 | [Umbraco.Community.Formulate.BackOffice](https://www.nuget.org/packages/Umbraco.Community.Formulate.BackOffice) | 5.0.0 | Nicholas Westby, Jamie Pollock | Backoffice functionality for Formulate, an advanced form builder for Umbraco. |
| 2026-11-26 22:46:35 | [Umbraco.Community.Formulate](https://www.nuget.org/packages/Umbraco.Community.Formulate) | 5.0.0 | Nicholas Westby, Jamie Pollock | An advanced form builder for Umbraco. |
| 2026-11-26 22:46:35 | [Umbraco.Community.Formulate.Extensions.StoreData](https://www.nuget.org/packages/Umbraco.Community.Formulate.Extensions.StoreData) | 5.0.0 | Nicholas Westby, Jamie Pollock | A data storage extension for Formulate, an advanced form builder for Umbraco. |
| 2026-11-26 23:08:50 | [ModiImaging](https://www.nuget.org/packages/ModiImaging) | 1.1.1 | TonyRoma | Reads Microsoft Document Imaging (.mdi) files and extracts their text, without… |
| 2026-11-26 23:08:51 | [ModiImaging.Drawing](https://www.nuget.org/packages/ModiImaging.Drawing) | 1.1.1 | TonyRoma | Rendering, printing and export (vector PDF through Microsoft Print to PDF, imag… |
| 2026-11-26 23:08:52 | [ModiImaging.Ocr](https://www.nuget.org/packages/ModiImaging.Ocr) | 1.1.1 | TonyRoma | OCR for MDI/EMF/TIFF/image pages using the OCR engine built into Windows 10/11… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

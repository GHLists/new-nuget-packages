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

## Latest list — 2026-10-18 18:19 UTC

New packages created between 2026-10-18 17:19 UTC and 2026-10-18 18:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-18T18-19-28-825794Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-18 17:22:55 | [Plugin.Maui.SignaturePad](https://www.nuget.org/packages/Plugin.Maui.SignaturePad) | 0.1.0 | Mykhailo Davydenko | A signature pad for .NET MAUI with natural, pen-like ink: the stroke width foll… |
| 2026-10-18 17:26:45 | [Raghom.Toolkit](https://www.nuget.org/packages/Raghom.Toolkit) | 1.0.0 | Raghom Technologies | A lightweight, production-ready .NET utility toolkit providing reusable extensi… |
| 2026-10-18 17:32:10 | [Egap.Documents](https://www.nuget.org/packages/Egap.Documents) | 1.1.0 | Lars Dytterud | Flow documents for .NET: one editable document model with Markdown, DOCX and HT… |
| 2026-10-18 17:32:10 | [Egap.Pdf.Conversion](https://www.nuget.org/packages/Egap.Pdf.Conversion) | 1.1.0 | Lars Dytterud | The bridge between Egap.Documents and Egap.Pdf: flow documents saved as PDF wit… |
| 2026-10-18 17:32:11 | [Egap.Pdf](https://www.nuget.org/packages/Egap.Pdf) | 1.4.0 | Lars Dytterud | A fully managed, MIT-licensed PDF library for .NET. |
| 2026-10-18 17:35:19 | [AHSW.EventLog.Contracts](https://www.nuget.org/packages/AHSW.EventLog.Contracts) | 1.0.0 | Alex Holenko | Interfaces, enums, and shared contracts for the EventLog library. |
| 2026-10-18 17:37:26 | [DataverseCartographer](https://www.nuget.org/packages/DataverseCartographer) | 1.0.0 | AmraouiH | Dataverse Cartographer draws an interactive map of a Dynamics 365 / Dataverse o… |
| 2026-10-18 17:52:28 | [Modern.Ribbon.Additional](https://www.nuget.org/packages/Modern.Ribbon.Additional) | 2.2.0 | YYXIsLucky | Modern.Ribbon is a WPF Ribbon control library that provides a modern and custom… |
| 2026-10-18 18:10:37 | [Egorozh.Windows.ImageOperations](https://www.nuget.org/packages/Egorozh.Windows.ImageOperations) | 10.0.0 | Egorozh | Windows image operations |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

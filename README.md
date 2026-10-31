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

## Latest list — 2026-10-31 06:19 UTC

New packages created between 2026-10-31 05:19 UTC and 2026-10-31 06:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-31T06-19-00-922883Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-31 05:40:37 | [RecursiveAI.OneOcr.Models](https://www.nuget.org/packages/RecursiveAI.OneOcr.Models) | 1.0.0 | Recursive AI, LLC | Model weights for RecursiveAI.OneOcr. The recognizer, the page detector and the… |
| 2026-10-31 05:40:38 | [RecursiveAI.OneOcr](https://www.nuget.org/packages/RecursiveAI.OneOcr) | 1.0.0 | Recursive AI, LLC | Local, deterministic OCR for .NET with no dependencies beyond the base class li… |
| 2026-10-31 05:40:39 | [RecursiveAI.OneOcr.Models.Documents](https://www.nuget.org/packages/RecursiveAI.OneOcr.Models.Documents) | 1.0.0 | Recursive AI, LLC | Document extraction weights for RecursiveAI.OneOcr: invoice, receipt and key-va… |
| 2026-10-31 05:40:40 | [RecursiveAI.OneOcr.Llm](https://www.nuget.org/packages/RecursiveAI.OneOcr.Llm) | 1.0.0 | Recursive AI, LLC | Opt-in language-model vision for RecursiveAI.OneOcr: Anthropic, OpenAI, OpenAI-… |
| 2026-10-31 05:40:41 | [RecursiveAI.OneOcr.Training](https://www.nuget.org/packages/RecursiveAI.OneOcr.Training) | 1.0.0 | Recursive AI, LLC | Fine-tuning for RecursiveAI.OneOcr recognition models from your own documents:… |
| 2026-10-31 05:40:42 | [RecursiveAI.OneOcr.Pdf](https://www.nuget.org/packages/RecursiveAI.OneOcr.Pdf) | 1.0.0 | Recursive AI, LLC | PDF bridge for RecursiveAI.OneOcr: text-layer words where a page has them, loca… |
| 2026-10-31 05:40:44 | [RecursiveAI.OneOcr.Tool](https://www.nuget.org/packages/RecursiveAI.OneOcr.Tool) | 1.0.0 | Recursive AI, LLC | The oneocr command-line tool: fine-tune a recognition model from your own docum… |
| 2026-10-31 05:52:05 | [FS.GG.Execution.Contracts](https://www.nuget.org/packages/FS.GG.Execution.Contracts) | 0.3.1 | FS-GG | Portable bounded process requests, monotonic budgets, retained session contract… |
| 2026-10-31 05:55:55 | [Superroute.SWidget](https://www.nuget.org/packages/Superroute.SWidget) | 0.2.0 | Goodneo Solutions | sWidget for .NET: widgets configured in the Superroute back office, loaded by t… |
| 2026-10-31 05:55:55 | [Superroute.SWidget.WinForms](https://www.nuget.org/packages/Superroute.SWidget.WinForms) | 0.2.0 | Goodneo Solutions | sWidget for Windows Forms: SwidgetControl, the widget configured in the Superro… |
| 2026-10-31 05:55:56 | [Superroute.SWidget.Wpf](https://www.nuget.org/packages/Superroute.SWidget.Wpf) | 0.2.0 | Goodneo Solutions | sWidget for WPF: SwidgetControl, the widget configured in the Superroute back o… |
| 2026-10-31 05:56:47 | [FS.GG.Execution.Processes](https://www.nuget.org/packages/FS.GG.Execution.Processes) | 0.3.1 | FS-GG | Caller-retained BCL process sessions with bounded observation and explicit best… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

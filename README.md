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

## Latest list — 2026-10-31 03:20 UTC

New packages created between 2026-10-31 02:20 UTC and 2026-10-31 03:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-31T03-20-53-025008Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-31 02:28:30 | [UniversalOffice.Converter](https://www.nuget.org/packages/UniversalOffice.Converter) | 0.9.2 | Eric Kono | Convert DOCX, XLSX, PPTX and PDF files to HTML, PDF or Markdown in .NET, withou… |
| 2026-10-31 02:37:31 | [Moka.AI](https://www.nuget.org/packages/Moka.AI) | 0.3.0 | jacobwi, BCat, Moka | Provider-agnostic AI chat services with streaming, context builders, and plugga… |
| 2026-10-31 02:37:31 | [Moka.AI.Onnx](https://www.nuget.org/packages/Moka.AI.Onnx) | 0.3.0 | jacobwi, BCat, Moka | ONNX Runtime GenAI provider for Moka.AI — run AI models fully in-process with n… |
| 2026-10-31 03:01:11 | [Toskar](https://www.nuget.org/packages/Toskar) | 0.4.0 | Yeix.io | The official .NET SDK for Toskar: local AI across your own computers. |
| 2026-10-31 03:10:24 | [TochiRes.Errors](https://www.nuget.org/packages/TochiRes.Errors) | 0.1.11 | T0chi | Shared typed errors and stable error codes used in official tochiResources proe… |
| 2026-10-31 03:13:32 | [Fomoxa.Net.WebSockets](https://www.nuget.org/packages/Fomoxa.Net.WebSockets) | 0.1.0 | Fomoxa Protocol | WebSocket transport and listener for Fomoxa.Net: RFC 6455 on a non-blocking byt… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

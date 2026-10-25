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

## Latest list — 2026-10-25 09:19 UTC

New packages created between 2026-10-25 08:21 UTC and 2026-10-25 09:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-25T09-19-26-918481Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-25 08:27:28 | [Parlam.ContentHub.Umbraco](https://www.nuget.org/packages/Parlam.ContentHub.Umbraco) | 0.0.10 | Parlam | Backoffice extension that opens the Parlam Content Hub translation app from Umb… |
| 2026-10-25 08:39:56 | [dotVault.Cli](https://www.nuget.org/packages/dotVault.Cli) | 2026.10.25.81 | software.tirol | CLI für den Secrets-Tresor dotVault: Anmeldung im Browser, Werte lesen und schr… |
| 2026-10-25 08:46:06 | [Nextmail](https://www.nuget.org/packages/Nextmail) | 0.0.1 | Nextmail | The official .NET SDK for the Nextmail API. Send email and broadcasts, work wit… |
| 2026-10-25 08:59:13 | [OlmaxPdf](https://www.nuget.org/packages/OlmaxPdf) | 1.3.1 | Oleg Maximenko | Tool to view and perform common modifications to PDFs. Based on PDFium. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-28 12:18 UTC

New packages created between 2026-10-28 11:19 UTC and 2026-10-28 12:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-28T12-18-46-016951Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-28 11:20:44 | [Jakar.SqlBuilder](https://www.nuget.org/packages/Jakar.SqlBuilder) | 10.2.0 | Tyler Stegmaier | Easy Sql Building |
| 2026-10-28 11:31:13 | [SecureTool](https://www.nuget.org/packages/SecureTool) | 1.1.1 | SenseiKiritof | Secure Console Tool |
| 2026-10-28 11:34:30 | [Nedussa.Guidelines.Shared.v300](https://www.nuget.org/packages/Nedussa.Guidelines.Shared.v300) | 3.5.1 | Tracy Rooks and Jonathan Tayl… | Gives executable projects the guidelines that nudge the AI, from local file sto… |
| 2026-10-28 11:37:01 | [MercadoPublico](https://www.nuget.org/packages/MercadoPublico) | 1.0.0 | Jorge Luis Saraiva Ruas | Cliente de la API pública de Mercado Público (ChileCompra): licitaciones, órden… |
| 2026-10-28 11:46:22 | [ConsoleMonster.Templates](https://www.nuget.org/packages/ConsoleMonster.Templates) | 2.1.0 | Przemyslaw Klys | dotnet new templates for ConsoleMonster: "consolemonster" creates a console app… |
| 2026-10-28 11:46:24 | [ConsoleMonster.PowerShell.Display](https://www.nuget.org/packages/ConsoleMonster.PowerShell.Display) | 2.1.0 | Przemyslaw Klys | Optional type-scoped, runspace-owned default display adapter for ConsoleMonster. |
| 2026-10-28 11:46:26 | [ConsoleMonster.Markdown](https://www.nuget.org/packages/ConsoleMonster.Markdown) | 2.1.0 | Przemyslaw Klys | Markdown display and widget, frame and recording export for ConsoleMonster, pow… |
| 2026-10-28 11:46:29 | [ConsoleMonster.Hosting](https://www.nuget.org/packages/ConsoleMonster.Hosting) | 2.1.0 | Przemyslaw Klys | A live ConsoleMonster dashboard for .NET generic host applications: services.Ad… |
| 2026-10-28 11:46:31 | [ConsoleMonster.Graphics](https://www.nuget.org/packages/ConsoleMonster.Graphics) | 2.1.0 | Przemyslaw Klys | Portable PNG, GIF and APNG exports for ConsoleMonster, powered by ChartForgeX. |
| 2026-10-28 11:46:35 | [ConsoleMonster.Extensions.Logging](https://www.nuget.org/packages/ConsoleMonster.Extensions.Logging) | 2.1.0 | Przemyslaw Klys | A Microsoft.Extensions.Logging provider for ConsoleMonster: log lines with Cons… |
| 2026-10-28 11:54:26 | [Sadq.Connect](https://www.nuget.org/packages/Sadq.Connect) | 1.0.0 | Sadq | Official .NET client for the Sadq e-signature Integration API: the Invitation m… |
| 2026-10-28 11:55:23 | [Zespy.EzPay.InvoiceEvidence](https://www.nuget.org/packages/Zespy.EzPay.InvoiceEvidence) | 1.6.0 | Zespy | Portable EZ invoice evidence profiles and offline independent verification. |
| 2026-10-28 12:06:43 | [NebriaChip.Vault.Win](https://www.nuget.org/packages/NebriaChip.Vault.Win) | 1.0.0 | toras9000 | A wrapper for the Windows Credential Store API |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-14 11:20 UTC

New packages created between 2026-10-14 10:19 UTC and 2026-10-14 11:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-14T11-20-12-336233Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-14 10:37:01 | [Aml.Editor.Plugin.MtpControl](https://www.nuget.org/packages/Aml.Editor.Plugin.MtpControl) | 1.0.1 | Vincent Schmitt | This plugin makes it possible to monitor or operate a single MTP-compliant Proc… |
| 2026-10-14 10:43:20 | [Pythia.Tagger.LiteDB](https://www.nuget.org/packages/Pythia.Tagger.LiteDB) | 12.1.1 | Daniele Fusi | Pythia taggers LiteDB components. |
| 2026-10-14 10:44:02 | [SheetStream.AspNetCore](https://www.nuget.org/packages/SheetStream.AspNetCore) | 0.3.0 | P4 Software | ASP.NET Core helpers for SheetStream: return a streamed .xlsx download from a m… |
| 2026-10-14 10:46:18 | [Amakora.Nexra](https://www.nuget.org/packages/Amakora.Nexra) | 1.0.0 | Amakora Group | Client for the Nexra platform API: integrations, flows, runs, connections, trig… |
| 2026-10-14 10:47:06 | [MailMartinSil](https://www.nuget.org/packages/MailMartinSil) | 1.0.0 | Martin Šíl | .NET SDK for mail-martinsil, a Resend-compatible email API on Amazon SES. |
| 2026-10-14 11:00:16 | [Asico.EmailService.Test2](https://www.nuget.org/packages/Asico.EmailService.Test2) | 1.0.5 | Vasudevan | Asico Mail Service [TEST2] |
| 2026-10-14 11:07:08 | [CorvusRE](https://www.nuget.org/packages/CorvusRE) | 2.0.2 | Albasha0x0 | MCP server and command line for reverse engineering .NET assemblies and native… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-19 13:22 UTC

New packages created between 2026-11-19 12:19 UTC and 2026-11-19 13:22 UTC.

[Full CSV](data/new-nuget-packages-2026-11-19T13-22-00-568534Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-19 12:24:02 | [CoreIdml.Cli](https://www.nuget.org/packages/CoreIdml.Cli) | 0.0.8 | Eduard Paul | coreidml: command line and MCP server for Adobe InDesign IDML files. Summaries… |
| 2026-11-19 12:24:02 | [CoreIdml](https://www.nuget.org/packages/CoreIdml) | 1.0.0 | Eduard Paul | Read, edit and write Adobe InDesign IDML files without InDesign. Untouched part… |
| 2026-11-19 12:24:03 | [CoreIdml.Pdf](https://www.nuget.org/packages/CoreIdml.Pdf) | 1.0.0 | Eduard Paul | Export Adobe InDesign IDML documents to PDF and rebuild editable IDML from PDF,… |
| 2026-11-19 12:30:07 | [ZplHelper](https://www.nuget.org/packages/ZplHelper) | 0.1.0 | RMP Software and BinaryKits c… | Render Zebra ZPL labels locally to PNG with SkiaSharp. |
| 2026-11-19 13:00:04 | [AwsEmulator.Testcontainers](https://www.nuget.org/packages/AwsEmulator.Testcontainers) | 0.1.0 | efimov-agent | Testcontainers module for the official AWS Emulator (aws/aws-emulator): builds… |
| 2026-11-19 13:01:00 | [GroupDocs.Watermark.Net48](https://www.nuget.org/packages/GroupDocs.Watermark.Net48) | 26.11.0 | Aspose | GroupDocs.Watermark for .NET is a powerful document watermarking API to add ima… |
| 2026-11-19 13:03:13 | [LinqPDF](https://www.nuget.org/packages/LinqPDF) | 1.3.0 | LinqPDF | Create PDFs in .NET 8, 9 and 10 on Windows and Linux with zero third-party pack… |
| 2026-11-19 13:07:43 | [Ab4d.SharpEngine.IfcLite](https://www.nuget.org/packages/Ab4d.SharpEngine.IfcLite) | 5.0.1075 | AB4D | Ab4d.SharpEngine.IfcLite library can import BIM 3D objects from ifc files and u… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-11 15:20 UTC

New packages created between 2026-11-11 14:21 UTC and 2026-11-11 15:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-11T15-20-09-648695Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-11 14:29:22 | [RapiDoc.AspNetCore](https://www.nuget.org/packages/RapiDoc.AspNetCore) | 0.1.0 | Mrinmoy Majumdar | RapiDoc for ASP.NET Core: serves an interactive OpenAPI reference (<rapi-doc>)… |
| 2026-11-11 14:31:22 | [Skrypton.Windows](https://www.nuget.org/packages/Skrypton.Windows) | 1.7.4 | Ben Hauman | Skrypton on Windows (.NET): the Windows host services (processes, clipboard, di… |
| 2026-11-11 14:31:23 | [Skrypton.Windows.NetFx](https://www.nuget.org/packages/Skrypton.Windows.NetFx) | 1.7.4 | Ben Hauman | Skrypton on Windows (.NET Framework 4.8.1): the Windows host services (processe… |
| 2026-11-11 14:41:33 | [MatriksIQ.Reference.Assemblies](https://www.nuget.org/packages/MatriksIQ.Reference.Assemblies) | 6.0.0.7 | Matriks Finansal Teknolojiler… | MatriksIQ algo gelistirme icin referans assembly'ler (Matriks.Core, Matriks.Ind… |
| 2026-11-11 14:45:43 | [Derail](https://www.nuget.org/packages/Derail) | 0.1.0 | Fredrik Hagen Fasteraune | Result, Option and Validation monads built on C# union types, for railway-orien… |
| 2026-11-11 14:46:17 | [FlashXlsx](https://www.nuget.org/packages/FlashXlsx) | 1.0.0 | Jetonpeche | Ultra-fast, lightweight streaming XLSX engine for .NET 10. Built for extreme th… |
| 2026-11-11 15:05:03 | [Messaia.Net.Pdf.Impl.IronPdf](https://www.nuget.org/packages/Messaia.Net.Pdf.Impl.IronPdf) | 10.3.0-beta01 | Fouad Messaia | IronPDF PDF Service Implementation |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

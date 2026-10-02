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

## Latest list — 2026-10-02 12:20 UTC

New packages created between 2026-10-02 11:22 UTC and 2026-10-02 12:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-02T12-20-32-43843Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-02 11:23:36 | [RetryMesh.Http](https://www.nuget.org/packages/RetryMesh.Http) | 0.1.0 | LuddeSkoglund | Prevent retry storms and retry amplification across .NET microservices. Coordin… |
| 2026-10-02 11:28:58 | [otsom.fs.OAuth](https://www.nuget.org/packages/otsom.fs.OAuth) | 0.1.1 | otsom.fs.OAuth | Package Description |
| 2026-10-02 11:37:40 | [Lokad.DocxEdit](https://www.nuget.org/packages/Lokad.DocxEdit) | 0.1.0 | Lokad | Stream-first .docx reader and patch editor for coding agents. |
| 2026-10-02 11:37:44 | [Fuaran.Compute.ColumnOps](https://www.nuget.org/packages/Fuaran.Compute.ColumnOps) | 0.36.0 | Andrew J. Willshire | Fuaran.Compute.ColumnOps — a columnar op-algebra over Fuaran.Core.Column's Tabl… |
| 2026-10-02 11:37:51 | [Fuaran.Compute.Conformance](https://www.nuget.org/packages/Fuaran.Compute.Conformance) | 0.36.0 | Andrew J. Willshire | Fuaran.Compute.Conformance — the law families over the dataframe layer, beside… |
| 2026-10-02 11:37:51 | [Fuaran.Compute.DataFrame](https://www.nuget.org/packages/Fuaran.Compute.DataFrame) | 0.36.0 | Andrew J. Willshire | Fuaran.Compute.DataFrame — the declarative-compute layer over Fuaran.Core.Colum… |
| 2026-10-02 11:37:51 | [Fuaran.Compute.PipelineQuery](https://www.nuget.org/packages/Fuaran.Compute.PipelineQuery) | 0.36.0 | Andrew J. Willshire | Fuaran.Compute.PipelineQuery — a registered pipeline query: a Fuaran.Core.Query… |
| 2026-10-02 11:59:32 | [Kentico.Xperience.Labs.SimpleStats.Admin](https://www.nuget.org/packages/Kentico.Xperience.Labs.SimpleStats.Admin) | 1.0.0-prerelease-1 | Kentico Software | Shows basic charts about Xperience by Kentico data in the administration. |
| 2026-10-02 12:05:00 | [AllInOneAccessibility.Blazor](https://www.nuget.org/packages/AllInOneAccessibility.Blazor) | 1.0.0 | Skynet Technologies USA LLC | Website accessibility widget for improving WCAG 2.0, 2.1, 2.2 and ADA, EAA comp… |
| 2026-10-02 12:09:45 | [EternalGarden.Rzeka.Reporting](https://www.nuget.org/packages/EternalGarden.Rzeka.Reporting) | 1.2.0 | Maria Aurelia Heine | Opt-in crash reporting for rzeka. Sends the causal story of a failing spell (st… |
| 2026-10-02 12:10:21 | [otsom.fs.OAuth.Telegram](https://www.nuget.org/packages/otsom.fs.OAuth.Telegram) | 0.1.1 | otsom.fs.OAuth.Telegram | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

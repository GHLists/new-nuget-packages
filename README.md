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

## Latest list — 2026-10-18 03:21 UTC

New packages created between 2026-10-18 02:21 UTC and 2026-10-18 03:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-18T03-21-46-384128Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-18 02:22:08 | [Darkspyre.ML.Tokenizers](https://www.nuget.org/packages/Darkspyre.ML.Tokenizers) | 2.0.1.1 | Microsoft,Darkspyre Studios | Darkspyre's source-compatible Microsoft.ML.Tokenizers fork with corrected Sente… |
| 2026-10-18 02:32:43 | [Mesa.Foundation](https://www.nuget.org/packages/Mesa.Foundation) | 1.0.0 | Rayscale | Foundational abstractions, primitives, and shared utilities |
| 2026-10-18 02:48:40 | [ZXingCpp.Angle](https://www.nuget.org/packages/ZXingCpp.Angle) | 1.0.0 | hixiong123 | Unofficial fork of zxing-cpp 3.1.1 / ZXingCpp 0.5.3: adds linear barcode detect… |
| 2026-10-18 03:03:35 | [ReportWright.Data.Json](https://www.nuget.org/packages/ReportWright.Data.Json) | 1.0.0 | ReportWright contributors | REST/JSON and JSON-file data provider for ReportWright reports, with an element… |
| 2026-10-18 03:03:36 | [ReportWright.Design](https://www.nuget.org/packages/ReportWright.Design) | 1.0.0 | ReportWright contributors | Designer-side model services over the DocWright report definition: reversible c… |
| 2026-10-18 03:03:36 | [ReportWright.Blazor.Designer](https://www.nuget.org/packages/ReportWright.Blazor.Designer) | 1.0.0 | ReportWright contributors | The ReportWright report designer component for Blazor WebAssembly: design surfa… |
| 2026-10-18 03:03:37 | [ReportWright.Blazor](https://www.nuget.org/packages/ReportWright.Blazor) | 1.0.0 | ReportWright contributors | Shared Blazor chrome for the ReportWright viewer and designer: the inline SVG i… |
| 2026-10-18 03:03:38 | [ReportWright.Data.SystemData](https://www.nuget.org/packages/ReportWright.Data.SystemData) | 1.0.0 | ReportWright contributors | Bridges System.Data (DataTable, DataSet, IDataReader) to ReportWright reports a… |
| 2026-10-18 03:03:39 | [ReportWright.Blazor.Viewer](https://www.nuget.org/packages/ReportWright.Blazor.Viewer) | 1.0.0 | ReportWright contributors | The ReportWright report viewer component for Blazor WebAssembly and Blazor Serv… |
| 2026-10-18 03:03:39 | [ReportWright.AspNetCore](https://www.nuget.org/packages/ReportWright.AspNetCore) | 1.0.0 | ReportWright contributors | ASP.NET Core host for ReportWright: MapReportWright endpoints for report load a… |
| 2026-10-18 03:03:40 | [ReportWright.Data.SqlServer](https://www.nuget.org/packages/ReportWright.Data.SqlServer) | 1.0.0 | ReportWright contributors | Microsoft SQL Server and Azure SQL data provider for ReportWright reports: para… |
| 2026-10-18 03:03:41 | [ReportWright.Data.Csv](https://www.nuget.org/packages/ReportWright.Data.Csv) | 1.0.0 | ReportWright contributors | CSV and delimited-file data provider for ReportWright reports, with type infere… |
| 2026-10-18 03:03:42 | [ReportWright.Data.Abstractions](https://www.nuget.org/packages/ReportWright.Data.Abstractions) | 1.0.0 | ReportWright contributors | The data-source seam ReportWright providers implement: connect, test and discov… |
| 2026-10-18 03:03:43 | [ReportWright.Data.Xml](https://www.nuget.org/packages/ReportWright.Data.Xml) | 1.0.0 | ReportWright contributors | XML data provider for ReportWright reports: the XmlData a report embeds in its… |
| 2026-10-18 03:11:36 | [JWTConfig](https://www.nuget.org/packages/JWTConfig) | 1.0.0 | JWTConfig | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

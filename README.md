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

## Latest list — 2026-10-17 06:19 UTC

New packages created between 2026-10-17 05:20 UTC and 2026-10-17 06:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-17T06-19-16-776612Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-17 05:31:28 | [ELF.Modules.Excel.Abstractions](https://www.nuget.org/packages/ELF.Modules.Excel.Abstractions) | 0.9.1 | ELF INTERNATIONAL EXPRESS CO.… | Excel 匯入匯出契約與模型，不含任何 Excel 函式庫依賴。 |
| 2026-10-17 05:31:29 | [ELF.Modules.Excel](https://www.nuget.org/packages/ELF.Modules.Excel) | 0.9.1 | ELF INTERNATIONAL EXPRESS CO.… | Excel 匯入匯出實作：ClosedXML 全量、MiniExcel 流式與模板、ExcelDataReader 讀取，另支援 CSV／TSV／固定寬度文字… |
| 2026-10-17 05:32:22 | [ResoLoop](https://www.nuget.org/packages/ResoLoop) | 0.1.0 | orange3134 | Agent-first CLI loop for Resonite development through ResoniteLink and Flux-SDK. |
| 2026-10-17 05:38:29 | [Lagosystem.Modules.NET](https://www.nuget.org/packages/Lagosystem.Modules.NET) | 0.1.3 | Lagosystem | Open-source .NET library providing reusable modules, extensions, helpers, and u… |
| 2026-10-17 05:55:16 | [Themia.ETax.Withholding.Testing](https://www.nuget.org/packages/Themia.ETax.Withholding.Testing) | 0.33.0 | Sarawut Phaekuntod | Conformance tests for Themia.ETax.Withholding's IWithholdingCertificateStore: i… |
| 2026-10-17 05:55:30 | [Themia.ETax.Withholding.Data](https://www.nuget.org/packages/Themia.ETax.Withholding.Data) | 0.33.0 | Sarawut Phaekuntod | Database helpers for Themia.ETax.Withholding: the required immutability trigger… |
| 2026-10-17 05:55:39 | [Themia.ETax.Withholding](https://www.nuget.org/packages/Themia.ETax.Withholding) | 0.33.0 | Sarawut Phaekuntod | Neutral Thai withholding tax certificate (50 bis) core: withholding math in sat… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

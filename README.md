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

## Latest list — 2026-10-20 10:19 UTC

New packages created between 2026-10-20 09:21 UTC and 2026-10-20 10:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-20T10-19-40-428119Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-20 09:27:21 | [MDNN](https://www.nuget.org/packages/MDNN) | 2.0.0 | SilM4r | Neural network library for C#, written from scratch: Dense, Conv, MaxPool and R… |
| 2026-10-20 09:27:29 | [MDNN.Plotting](https://www.nuget.org/packages/MDNN.Plotting) | 2.0.0 | SilM4r | Loss charts for MDNN training runs (ScottPlot). Call model.Train.UseLossChart()… |
| 2026-10-20 09:28:18 | [Yatros.Common.Data](https://www.nuget.org/packages/Yatros.Common.Data) | 0.1.0 | Yatros | Tầng truy cập dữ liệu dùng chung cho nền tảng Yatros: phiên làm việc với DB, ra… |
| 2026-10-20 09:29:00 | [Yatros.Common.Data.Oracle](https://www.nuget.org/packages/Yatros.Common.Data.Oracle) | 0.1.0 | Yatros | Phần hỗ trợ Oracle cho Yatros.Common.Data: nạp ngữ cảnh audit qua application c… |
| 2026-10-20 09:38:02 | [EJoyer.SDK.User](https://www.nuget.org/packages/EJoyer.SDK.User) | 1.0.0 | Javxp | private sdk |
| 2026-10-20 10:00:21 | [Loglet](https://www.nuget.org/packages/Loglet) | 1.0.0 | AscendantWare e.K. | Loglet – A lightweight, high-performance logging library for .NET, designed for… |
| 2026-10-20 10:10:05 | [Moberg.Beacon.AI.Embeddings.Onnx](https://www.nuget.org/packages/Moberg.Beacon.AI.Embeddings.Onnx) | 4.6.0 | Moberg | Local in-process ONNX text embeddings for Beacon semantic retrieval. Optional a… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-27 04:21 UTC

New packages created between 2026-11-27 03:20 UTC and 2026-11-27 04:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-27T04-21-16-66674Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-27 03:49:27 | [SS.PaddleOCR.ModelProvider](https://www.nuget.org/packages/SS.PaddleOCR.ModelProvider) | 1.0.0 | sdcb | OCR model contracts (IPaddleOcrModelProvider / PaddleOcrModelBundle). |
| 2026-11-27 03:49:29 | [SS.PaddleOCR.Models.TextLineOrientation](https://www.nuget.org/packages/SS.PaddleOCR.Models.TextLineOrientation) | 1.0.0 | sdcb | Embedded PP-LCNet text-line orientation (CLS) model for PP-OCR. |
| 2026-11-27 03:49:32 | [SS.PaddleOCR.Models.ChineseV6Tiny](https://www.nuget.org/packages/SS.PaddleOCR.Models.ChineseV6Tiny) | 1.0.0 | sdcb | Embedded PP-OCRv6 tiny Chinese DET+REC+dictionary models. |
| 2026-11-27 03:49:35 | [SS.PaddleOCR.Models.ChineseV6Small](https://www.nuget.org/packages/SS.PaddleOCR.Models.ChineseV6Small) | 1.0.0 | sdcb | Embedded PP-OCRv6 small Chinese DET+REC+dictionary models. |
| 2026-11-27 03:49:39 | [SS.PaddleOCR.Models.ChineseV6Medium](https://www.nuget.org/packages/SS.PaddleOCR.Models.ChineseV6Medium) | 1.0.0 | sdcb | Embedded PP-OCRv6 medium Chinese DET+REC+dictionary models. |
| 2026-11-27 03:49:42 | [SS.PaddleOCR.Models.KoreanV5Mobile](https://www.nuget.org/packages/SS.PaddleOCR.Models.KoreanV5Mobile) | 1.0.0 | sdcb | Embedded PP-OCRv5 mobile Korean DET+REC+dictionary models. |
| 2026-11-27 03:49:44 | [SS.PaddleOCR](https://www.nuget.org/packages/SS.PaddleOCR) | 1.0.0 | sdcb | Pure C# PP-OCRv5 and PP-OCRv6 inference (DET + CLS + REC). Cross-platform hand-… |
| 2026-11-27 03:50:50 | [Stockfish.Uci](https://www.nuget.org/packages/Stockfish.Uci) | 0.1.0 | Rodrigo Alarcón | A modern, strongly typed .NET client for Universal Chess Interface engines, des… |
| 2026-11-27 04:02:02 | [CRules](https://www.nuget.org/packages/CRules) | 0.2.0 | ape-byte | A lightweight C#-style rule executor built on DynamicExpresso public APIs. Supp… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

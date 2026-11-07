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

## Latest list — 2026-11-07 07:19 UTC

New packages created between 2026-11-07 06:19 UTC and 2026-11-07 07:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-07T07-19-00-501958Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-07 06:20:49 | [Torque.Http.Newtonsoft](https://www.nuget.org/packages/Torque.Http.Newtonsoft) | 0.7.0 | Truespar | Encodes objects as Torque TQBF records exactly as Newtonsoft.Json serializes th… |
| 2026-11-07 06:33:22 | [Simple3D.Core](https://www.nuget.org/packages/Simple3D.Core) | 0.3.0 | Marius Muntean | Portable opaque 3D scenes, meshes, cameras, software depth rendering and pickin… |
| 2026-11-07 06:33:24 | [Simple3D.Maui](https://www.nuget.org/packages/Simple3D.Maui) | 0.3.0 | Marius Muntean | Interactive SkiaSharp 3D scene control for .NET MAUI on iOS, Android and Mac Ca… |
| 2026-11-07 06:41:56 | [Mediana.Documents.Spreadsheets](https://www.nuget.org/packages/Mediana.Documents.Spreadsheets) | 0.1.24 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-07 06:41:59 | [Mediana.Codecs.Gif](https://www.nuget.org/packages/Mediana.Codecs.Gif) | 0.1.24 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-07 06:42:00 | [Mediana.Documents.Xls](https://www.nuget.org/packages/Mediana.Documents.Xls) | 0.1.24 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-07 06:42:01 | [Mediana.Containers.Ogg](https://www.nuget.org/packages/Mediana.Containers.Ogg) | 0.1.24 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-07 06:42:02 | [Mediana.Documents.Xlsx](https://www.nuget.org/packages/Mediana.Documents.Xlsx) | 0.1.24 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-07 06:42:03 | [Mediana.Codecs.Tiff](https://www.nuget.org/packages/Mediana.Codecs.Tiff) | 0.1.24 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-07 06:42:04 | [Mediana.Codecs.Opus](https://www.nuget.org/packages/Mediana.Codecs.Opus) | 0.1.24 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-07 06:42:05 | [Mediana.Codecs.Bmp](https://www.nuget.org/packages/Mediana.Codecs.Bmp) | 0.1.24 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-07 06:42:06 | [Mediana.Codecs.Hevc](https://www.nuget.org/packages/Mediana.Codecs.Hevc) | 0.1.24 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-07 06:42:07 | [Mediana.Documents.Presentation](https://www.nuget.org/packages/Mediana.Documents.Presentation) | 0.1.24 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-07 06:42:08 | [Mediana.Codecs.Vorbis](https://www.nuget.org/packages/Mediana.Codecs.Vorbis) | 0.1.24 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-07 06:42:11 | [Mediana.Documents](https://www.nuget.org/packages/Mediana.Documents) | 0.1.24 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-07 06:42:40 | [Rechunk](https://www.nuget.org/packages/Rechunk) | 0.1.0 | Challa Ravindranath | Dedup and revision aware ingestion for RAG pipelines in .NET. Exact hash, SimHa… |
| 2026-11-07 06:42:41 | [Rechunk.SemanticKernel](https://www.nuget.org/packages/Rechunk.SemanticKernel) | 0.1.0 | Challa Ravindranath | Registers Rechunk on a Semantic Kernel builder. |
| 2026-11-07 06:42:42 | [Rechunk.Storage.Redis](https://www.nuget.org/packages/Rechunk.Storage.Redis) | 0.1.0 | Challa Ravindranath | Redis storage for the Rechunk shared fingerprint store, revisions, audit log an… |
| 2026-11-07 06:42:42 | [Rechunk.Storage.Sqlite](https://www.nuget.org/packages/Rechunk.Storage.Sqlite) | 0.1.0 | Challa Ravindranath | SQLite storage for the Rechunk shared fingerprint store, revisions, audit log a… |
| 2026-11-07 06:42:43 | [Rechunk.VectorData](https://www.nuget.org/packages/Rechunk.VectorData) | 0.1.0 | Challa Ravindranath | Rechunk writer for any Microsoft.Extensions.VectorData collection. Upserts and… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-20 09:21 UTC

New packages created between 2026-10-20 08:22 UTC and 2026-10-20 09:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-20T09-21-51-018148Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-20 08:44:51 | [Rays.Avalonias](https://www.nuget.org/packages/Rays.Avalonias) | 1.1.70.1020 | Rays.Avalonias | Package Description |
| 2026-10-20 08:46:27 | [Rays.Sukis](https://www.nuget.org/packages/Rays.Sukis) | 1.1.70.1020 | Rays.Sukis | Package Description |
| 2026-10-20 08:47:22 | [SmartTableSync.Templates](https://www.nuget.org/packages/SmartTableSync.Templates) | 0.5.1 | Ruslan Sidoriako | dotnet new template for SmartTableSync: an Azure Function that syncs tables fro… |
| 2026-10-20 08:56:50 | [XFiler.YandexDisk.Client](https://www.nuget.org/packages/XFiler.YandexDisk.Client) | 9.0.0 | XFiler Community | .NET library wrapper of Yandex Desktop RestAPI. See https://tech.yandex.ru/disk… |
| 2026-10-20 08:59:00 | [Wisdom.Office](https://www.nuget.org/packages/Wisdom.Office) | 1.0.0 | Wisdom | Word/Excel/PDF 统一读写与转换门面。Unified facade for reading, writing and converting Wor… |
| 2026-10-20 08:59:38 | [Wisdom.Pdf](https://www.nuget.org/packages/Wisdom.Pdf) | 1.0.0 | Wisdom | 自研 PDF 生成、解析、文本表格提取与字体嵌入。Self-contained PDF writer, renderer, font subsetter an… |
| 2026-10-20 08:59:53 | [Wisdom.Word](https://www.nuget.org/packages/Wisdom.Word) | 1.0.0 | Wisdom | 自研 DOCX 读写、模板填充与旧版 DOC 读取。Self-contained DOCX reader/writer, template engine an… |
| 2026-10-20 09:09:26 | [Rays.Shell.Abstractions](https://www.nuget.org/packages/Rays.Shell.Abstractions) | 1.0.0 | Rays.Shell.Abstractions | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

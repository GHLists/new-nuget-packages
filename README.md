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

## Latest list — 2026-10-05 02:19 UTC

New packages created between 2026-10-05 01:19 UTC and 2026-10-05 02:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-05T02-19-11-561421Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-05 01:20:05 | [Vestigium.Helpers.ClosedXml](https://www.nuget.org/packages/Vestigium.Helpers.ClosedXml) | 1.0.0 | Vestigium | ClosedXML write-first Excel workbooks for Vestigium hosts. |
| 2026-10-05 01:21:19 | [Vestigium.Helpers.Csv](https://www.nuget.org/packages/Vestigium.Helpers.Csv) | 1.0.0 | Vestigium | RFC 4180 CSV / TSV for Vestigium hosts. Separate from ClosedXml. |
| 2026-10-05 01:22:26 | [Vestigium.Helpers.Encryption](https://www.nuget.org/packages/Vestigium.Helpers.Encryption) | 1.3.1 | Vestigium | Authenticated encryption helpers (AES-256-GCM, ChaCha20-Poly1305, AES-256-CBC+H… |
| 2026-10-05 01:22:32 | [LsMsgPack](https://www.nuget.org/packages/LsMsgPack) | 2026.10.5.3 | Louis Somers | MsgPack serializer and deserializer for .NET classes (like the xml and json ser… |
| 2026-10-05 01:22:34 | [LsMsgPack.AspNet.Mvc](https://www.nuget.org/packages/LsMsgPack.AspNet.Mvc) | 2026.10.5.3 | Louis Somers | MsgPack model binding (LtMsgPack) and action result for ASP.NET MVC 5 controlle… |
| 2026-10-05 01:22:35 | [LsMsgPack.AspNet.WebApi](https://www.nuget.org/packages/LsMsgPack.AspNet.WebApi) | 2026.10.5.3 | Louis Somers | MsgPack MediaTypeFormatter (LtMsgPack) for ASP.NET Web API 2 and for HttpClient… |
| 2026-10-05 01:22:37 | [LsMsgPack.AspNetCore](https://www.nuget.org/packages/LsMsgPack.AspNetCore) | 2026.10.5.3 | Louis Somers | Input and output formatters (LtMsgPack) for ASP.NET Core MVC / Web API controll… |
| 2026-10-05 01:22:38 | [LsMsgPack.Core](https://www.nuget.org/packages/LsMsgPack.Core) | 2026.10.5.3 | Louis Somers | The parts shared by the LsMsgPack serializers: settings, the indexed schema and… |
| 2026-10-05 01:22:40 | [LtMsgPack](https://www.nuget.org/packages/LtMsgPack) | 2026.10.5.3 | Louis Somers | Fast MsgPack serializer for .NET classes, writes and reads the same data as LsM… |
| 2026-10-05 01:23:28 | [Webority.Push](https://www.nuget.org/packages/Webority.Push) | 0.1.0 | Webority Technologies | Direct mobile push for Webority products: Firebase Cloud Messaging HTTP v1 (And… |
| 2026-10-05 02:08:48 | [EmbedIO-Neo.Cli](https://www.nuget.org/packages/EmbedIO-Neo.Cli) | 1.0.0 | William Smith,EmbedIO CLI con… | EmbedIO-Neo command-line development server. |
| 2026-10-05 02:08:48 | [EmbedIO-Neo.JsonServer](https://www.nuget.org/packages/EmbedIO-Neo.JsonServer) | 1.0.0 | William Smith,EmbedIO contrib… | JSON file-backed REST module for EmbedIO-Neo. |
| 2026-10-05 02:08:49 | [EmbedIO-Neo](https://www.nuget.org/packages/EmbedIO-Neo) | 1.0.0 | William Smith,EmbedIO contrib… | EmbedIO-Neo, a compatibility-focused fork of the EmbedIO cross-platform, module… |
| 2026-10-05 02:08:49 | [EmbedIO-Neo.Testing](https://www.nuget.org/packages/EmbedIO-Neo.Testing) | 1.0.0 | William Smith,EmbedIO contrib… | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

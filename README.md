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

## Latest list — 2026-11-24 15:21 UTC

New packages created between 2026-11-24 14:20 UTC and 2026-11-24 15:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-24T15-21-42-507484Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-24 14:41:34 | [CoreGame.SharedMeta.Inspector.Mcp](https://www.nuget.org/packages/CoreGame.SharedMeta.Inspector.Mcp) | 0.49.0 | CoreGame.IO | Preview: the API may change in minor versions. MCP endpoint over the SharedMeta… |
| 2026-11-24 14:41:35 | [CoreGame.SharedMeta.Inspector.Nats](https://www.nuget.org/packages/CoreGame.SharedMeta.Inspector.Nats) | 0.49.0 | CoreGame.IO | Preview: the API may change in minor versions. NATS JetStream broker for the Sh… |
| 2026-11-24 14:41:37 | [CoreGame.SharedMeta.Inspector.Service](https://www.nuget.org/packages/CoreGame.SharedMeta.Inspector.Service) | 0.49.0 | CoreGame.IO | Preview: the API may change in minor versions. Standalone SharedMeta Inspector:… |
| 2026-11-24 14:41:40 | [CoreGame.SharedMeta.Inspector](https://www.nuget.org/packages/CoreGame.SharedMeta.Inspector) | 0.49.0 | CoreGame.IO | Preview: the API may change in minor versions. Silo-side call inspector: captur… |
| 2026-11-24 14:44:32 | [TesseractOCRPdf](https://www.nuget.org/packages/TesseractOCRPdf) | 5.5.3 | Kees van Spelde | Optional PDF OCR extensions for TesseractOCR Engine and EnginePool, using PDFiu… |
| 2026-11-24 14:53:19 | [OmniBuf.Grpc](https://www.nuget.org/packages/OmniBuf.Grpc) | 0.1.6 | OmniBuf Contributors | Detached Grpc.Core.Api marshaller integration for OmniBuf v1 DRAFT-1 binary ser… |
| 2026-11-24 14:56:42 | [ZeroAlloc.Memory](https://www.nuget.org/packages/ZeroAlloc.Memory) | 0.1.0 | Markism-JA | Zero-allocation unmanaged memory allocators, linear arenas, mirrored virtual-me… |
| 2026-11-24 15:07:11 | [SecureRedact.Ner](https://www.nuget.org/packages/SecureRedact.Ner) | 1.3.0 | Sanket Singh | CPU-only Named Entity Recognition (NER) PII detection plugin for SecureRedact (… |
| 2026-11-24 15:10:24 | [Defra.Livestock.Sdk.Submissions](https://www.nuget.org/packages/Defra.Livestock.Sdk.Submissions) | 0.1.0 | Defra | The submission process shared by LIS BE4FE services: draft submissions per CPH… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

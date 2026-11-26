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

## Latest list — 2026-11-26 13:19 UTC

New packages created between 2026-11-26 12:21 UTC and 2026-11-26 13:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-26T13-19-12-778509Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-26 12:31:07 | [Openlayer.Guardrails.Onnx](https://www.nuget.org/packages/Openlayer.Guardrails.Onnx) | 0.1.0 | Openlayer | Model-based guardrails for Openlayer.Guardrails on ONNX Runtime: English and Br… |
| 2026-11-26 12:31:08 | [Openlayer.Guardrails](https://www.nuget.org/packages/Openlayer.Guardrails) | 0.1.0 | Openlayer | Guardrails for LLM apps: PII and CPNI detection, redaction and keyed pseudonymi… |
| 2026-11-26 12:41:17 | [Messager.NET.Core](https://www.nuget.org/packages/Messager.NET.Core) | 2.0.0 | NovoDwarf | Core contracts for Messager.NET. |
| 2026-11-26 12:41:17 | [Messager.NET](https://www.nuget.org/packages/Messager.NET) | 2.0.0 | NovoDwarf | Runtime implementation for Messager.NET. |
| 2026-11-26 12:41:18 | [Messager.NET.Autofac](https://www.nuget.org/packages/Messager.NET.Autofac) | 2.0.0 | NovoDwarf | Autofac integration for Messager.NET. |
| 2026-11-26 12:41:18 | [Messager.NET.Microsoft.DependencyInjection](https://www.nuget.org/packages/Messager.NET.Microsoft.DependencyInjection) | 2.0.0 | NovoDwarf | Microsoft.Extensions.DependencyInjection integration for Messager.NET. |
| 2026-11-26 12:44:17 | [CSharpUtil.Extensions.Json](https://www.nuget.org/packages/CSharpUtil.Extensions.Json) | 0.2.0 | Yeung | JSON helpers for CSharpUtil.Extensions: shape checks, strict System.Text.Json v… |
| 2026-11-26 12:45:27 | [Nanov.OpenTelemetry.Summary.Instrumentation](https://www.nuget.org/packages/Nanov.OpenTelemetry.Summary.Instrumentation) | 1.0.0 | Dimitar Nanov | Shared bridge that turns any source histogram instrument into a Nanov.OpenTelem… |
| 2026-11-26 12:45:28 | [Nanov.OpenTelemetry.Summary.Instrumentation.AspNetCore](https://www.nuget.org/packages/Nanov.OpenTelemetry.Summary.Instrumentation.AspNetCore) | 1.0.0 | Dimitar Nanov | Turnkey instrumentation that bridges the built-in ASP.NET Core http.server.requ… |
| 2026-11-26 12:45:28 | [Nanov.OpenTelemetry.Summary.Instrumentation.Http](https://www.nuget.org/packages/Nanov.OpenTelemetry.Summary.Instrumentation.Http) | 1.0.0 | Dimitar Nanov | Turnkey instrumentation that bridges the built-in HttpClient http.client.reques… |
| 2026-11-26 12:53:38 | [ElevenLabs.Net](https://www.nuget.org/packages/ElevenLabs.Net) | 1.0.0 | ElevenLabs | The official C# SDK for ElevenLabs. |
| 2026-11-26 12:53:39 | [ElevenLabs.AspNetCore](https://www.nuget.org/packages/ElevenLabs.AspNetCore) | 1.0.0 | ElevenLabs | ASP.NET Core integration for the ElevenLabs .NET SDK: attach a Speech Engine se… |
| 2026-11-26 13:01:26 | [TesseractOCRPdfImageMagick](https://www.nuget.org/packages/TesseractOCRPdfImageMagick) | 5.5.4 | Kees van Spelde | Optional PDF OCR extensions for TesseractOCR Engine and EnginePool, using Image… |
| 2026-11-26 13:01:46 | [TesseractOCRPdfSkiaSharp](https://www.nuget.org/packages/TesseractOCRPdfSkiaSharp) | 5.5.4 | Kees van Spelde | Optional PDF OCR extensions for TesseractOCR Engine and EnginePool, using PDFiu… |
| 2026-11-26 13:04:33 | [Avig.OpenXml](https://www.nuget.org/packages/Avig.OpenXml) | 0.3.2 | Marcus Lindh | The package layer under Avig.Kalkyl, Avig.Ord and Avig.Bildspel: reads and writ… |
| 2026-11-26 13:09:17 | [GeregeSystems.EidMongolia.AspNetCore](https://www.nuget.org/packages/GeregeSystems.EidMongolia.AspNetCore) | 0.17.0 | Gerege Systems LLC | ASP.NET Core adapter for the eID Mongolia relying-party SDK: services.AddEidMon… |
| 2026-11-26 13:09:32 | [GeregeSystems.EidMongolia](https://www.nuget.org/packages/GeregeSystems.EidMongolia) | 0.17.0 | Gerege Systems LLC | eID Mongolia relying-party SDK for .NET (server side): RP-API client (Bearer, m… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

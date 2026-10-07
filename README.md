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

## Latest list — 2026-10-07 19:20 UTC

New packages created between 2026-10-07 18:20 UTC and 2026-10-07 19:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-07T19-20-01-040081Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-07 18:22:53 | [ElBruno.LocalEmbeddings.EmbeddingGemma](https://www.nuget.org/packages/ElBruno.LocalEmbeddings.EmbeddingGemma) | 1.6.4 | Bruno Capuano | Local text embedding generation using Google's EmbeddingGemma 2 model and ONNX… |
| 2026-10-07 18:28:44 | [Bitenovac.RemoteBuildTool](https://www.nuget.org/packages/Bitenovac.RemoteBuildTool) | 0.0.1 | Radivoje Milutinovic | Content-hashed build, test and coverage pipeline for the Bitenovac repository. |
| 2026-10-07 18:33:27 | [ContractWatcher.Common](https://www.nuget.org/packages/ContractWatcher.Common) | 1.0.0 | a1unade | Shared contracts and common types used by ContractWatcher SDK and Core services. |
| 2026-10-07 18:38:38 | [VerizonApimaticV4SDK](https://www.nuget.org/packages/VerizonApimaticV4SDK) | 0.0.1 | Muhammad Rafay | Sample SDKs for Verizon by APIMatic |
| 2026-10-07 18:39:30 | [NucleusSms](https://www.nuget.org/packages/NucleusSms) | 1.0.1 | Nucleus | Provider-agnostic SMS send abstractions, options, provider registry, and DI ext… |
| 2026-10-07 18:39:34 | [NucleusSmsTwilio](https://www.nuget.org/packages/NucleusSmsTwilio) | 1.0.1 | Nucleus | Twilio provider package for NucleusSms — sends SMS through Twilio Programmable… |
| 2026-10-07 18:42:17 | [NucleusOtp](https://www.nuget.org/packages/NucleusOtp) | 1.0.1 | Nucleus | Typed client for the Nucleus platform service nucleus-otp-service (challenges,… |
| 2026-10-07 18:51:48 | [VzimaticV4SDK](https://www.nuget.org/packages/VzimaticV4SDK) | 0.0.2 | Muhammad Rafay | Sample SDKs for Verizon by APIMatic |
| 2026-10-07 18:54:18 | [LunaticPanel.DebugTool](https://www.nuget.org/packages/LunaticPanel.DebugTool) | 0.0.18 | Maksim Shimshon | Core Package for Lunatic Panel's PLugin |
| 2026-10-07 19:02:22 | [Genocs.Fonet](https://www.nuget.org/packages/Genocs.Fonet) | 3.0.1 | Nocco Giovanni Emanuele | Fonet library to build PDFs by transforming XML documents through XSLT. |
| 2026-10-07 19:02:22 | [Genocs.Fonet.XsltTransformer](https://www.nuget.org/packages/Genocs.Fonet.XsltTransformer) | 3.0.1 | Nocco Giovanni Emanuele | Fonet XSLT to PDF Transformer library. |
| 2026-10-07 19:06:17 | [MediaInfo.Analysis.Rtsp](https://www.nuget.org/packages/MediaInfo.Analysis.Rtsp) | 26.10.0 | yartat | MediaInfo(Lib) is a convenient unified display of the most relevant technical a… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

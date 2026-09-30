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

## Latest list — 2026-09-30 10:20 UTC

New packages created between 2026-09-30 09:22 UTC and 2026-09-30 10:20 UTC.

[Full CSV](data/new-nuget-packages-2026-09-30T10-20-25-946953Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-30 09:22:28 | [Pathway.DesignTokens](https://www.nuget.org/packages/Pathway.DesignTokens) | 10.0.1 | Ministry Brands | Design tokens for the Pathway design system: semantic colour with Light and Mid… |
| 2026-09-30 09:22:40 | [RsCommunication](https://www.nuget.org/packages/RsCommunication) | 0.1.0 | xioa-cn | PLC communication C# source bindings and Windows x64 native runtime. Copies the… |
| 2026-09-30 09:28:39 | [AdfDotNet](https://www.nuget.org/packages/AdfDotNet) | 1.0.0 | Guillermo Espert Carrasquer | Atlassian Document Format (ADF) for .NET: a typed document model, fluent builde… |
| 2026-09-30 09:29:33 | [AdfDotNet.Converters.Html](https://www.nuget.org/packages/AdfDotNet.Converters.Html) | 1.0.0 | Guillermo Espert Carrasquer | HTML to Atlassian Document Format (ADF) conversion and back for AdfDotNet, buil… |
| 2026-09-30 09:30:08 | [AdfDotNet.Converters.Markdown](https://www.nuget.org/packages/AdfDotNet.Converters.Markdown) | 1.0.0 | Guillermo Espert Carrasquer | Markdown to Atlassian Document Format (ADF) conversion and back for AdfDotNet,… |
| 2026-09-30 09:30:32 | [AdfDotNet.Core](https://www.nuget.org/packages/AdfDotNet.Core) | 1.0.0 | Guillermo Espert Carrasquer | Typed .NET document model for the Atlassian Document Format (ADF) used by Jira… |
| 2026-09-30 09:31:01 | [AdfDotNet.Json.Newtonsoft](https://www.nuget.org/packages/AdfDotNet.Json.Newtonsoft) | 1.0.0 | Guillermo Espert Carrasquer | Lossless Atlassian Document Format (ADF) JSON serialization for AdfDotNet, buil… |
| 2026-09-30 09:57:05 | [Zautha.AspNetCore](https://www.nuget.org/packages/Zautha.AspNetCore) | 0.1.0 | Zautha | Zautha for ASP.NET Core: authenticate API requests by their Zautha session toke… |
| 2026-09-30 10:12:19 | [ZeroVector.Core](https://www.nuget.org/packages/ZeroVector.Core) | 1.0.0 | Phong Võ | Pure C# high-throughput embedded Vector Database and SIMD similarity metric eng… |
| 2026-09-30 10:12:28 | [ZeroAgent.Core](https://www.nuget.org/packages/ZeroAgent.Core) | 1.0.0 | Phong Võ | Pure C# enterprise-grade cognitive AI Agent runtime (ReAct loop, tool registry,… |
| 2026-09-30 10:12:31 | [ZeroTokenizer.Core](https://www.nuget.org/packages/ZeroTokenizer.Core) | 1.0.0 | Phong Võ | Pure C# high-speed Byte-Pair Encoding (BPE), Tiktoken, and LLM context token bu… |
| 2026-09-30 10:14:28 | [pgtail](https://www.nuget.org/packages/pgtail) | 0.7.0 | Brandon Williams | Interactive PostgreSQL log tailer with auto-detection, filtering, semantic high… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

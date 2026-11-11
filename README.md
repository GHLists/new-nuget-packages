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

## Latest list — 2026-11-11 03:19 UTC

New packages created between 2026-11-11 02:20 UTC and 2026-11-11 03:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-11T03-19-47-226484Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-11 02:28:27 | [AstraHarness.Client](https://www.nuget.org/packages/AstraHarness.Client) | 1.0.0 | The Astra Harness authors | The .NET client for the Astra Harness public API: Responses with streaming, ses… |
| 2026-11-11 02:31:21 | [RecursiveAI.OneSpeech.Models.CamPlusEnglish](https://www.nuget.org/packages/RecursiveAI.OneSpeech.Models.CamPlusEnglish) | 1.0.0 | Recursive AI, LLC | Speech recognition for .NET. Managed transcription, timing and speaker recognit… |
| 2026-11-11 02:31:27 | [RecursiveAI.OneSpeech.Models.MoonshineStreamingTiny](https://www.nuget.org/packages/RecursiveAI.OneSpeech.Models.MoonshineStreamingTiny) | 1.0.0 | Recursive AI, LLC | Speech recognition for .NET. Managed transcription, timing and speaker recognit… |
| 2026-11-11 02:31:35 | [RecursiveAI.OneSpeech.Models.MoonshineBase](https://www.nuget.org/packages/RecursiveAI.OneSpeech.Models.MoonshineBase) | 1.0.0 | Recursive AI, LLC | Speech recognition for .NET. Managed transcription, timing and speaker recognit… |
| 2026-11-11 02:31:36 | [RecursiveAI.OneSpeech.Media](https://www.nuget.org/packages/RecursiveAI.OneSpeech.Media) | 1.0.0 | Recursive AI, LLC | Speech recognition for .NET. Managed transcription, timing and speaker recognit… |
| 2026-11-11 02:31:36 | [RecursiveAI.OneSpeech](https://www.nuget.org/packages/RecursiveAI.OneSpeech) | 1.0.0 | Recursive AI, LLC | Speech recognition for .NET. Managed transcription, timing and speaker recognit… |
| 2026-11-11 02:31:37 | [RecursiveAI.OneSpeech.Cli](https://www.nuget.org/packages/RecursiveAI.OneSpeech.Cli) | 1.0.0 | Recursive AI, LLC | Speech recognition for .NET. Managed transcription, timing and speaker recognit… |
| 2026-11-11 02:31:41 | [RecursiveAI.OneSpeech.Models.MoonshineTiny](https://www.nuget.org/packages/RecursiveAI.OneSpeech.Models.MoonshineTiny) | 1.0.0 | Recursive AI, LLC | Speech recognition for .NET. Managed transcription, timing and speaker recognit… |
| 2026-11-11 02:32:47 | [Soenneker.Vtracer.Linux](https://www.nuget.org/packages/Soenneker.Vtracer.Linux) | 11.0.3 | Jake Soenneker | A bundled VTracer command-line distribution for Linux x64. |
| 2026-11-11 02:41:29 | [Toolbelt.Blazor.WebAssembly.ExtensibleGateway](https://www.nuget.org/packages/Toolbelt.Blazor.WebAssembly.ExtensibleGateway) | 11.0.0 | J.Sakamoto | An alternative Blazor WebAssembly gateway server that can be extended with addi… |
| 2026-11-11 02:41:30 | [Toolbelt.Blazor.WebAssembly.ExtensibleGateway.Extension.ProjectTemplates](https://www.nuget.org/packages/Toolbelt.Blazor.WebAssembly.ExtensibleGateway.Extension.ProjectTemplates) | 11.0.0 | J.Sakamoto | Templates for a Blazor WebAssembly Extensible Gateway extension project. |
| 2026-11-11 02:41:32 | [Toolbelt.Blazor.WebAssembly.ExtensibleGateway.ImportMapExtension](https://www.nuget.org/packages/Toolbelt.Blazor.WebAssembly.ExtensibleGateway.ImportMapExtension) | 11.0.0 | J.Sakamoto | In a standalone Blazor WebAssembly app, edit a collocated JavaScript module and… |
| 2026-11-11 02:41:33 | [Toolbelt.Blazor.WebAssembly.ExtensibleGateway.UserSecretsExtension](https://www.nuget.org/packages/Toolbelt.Blazor.WebAssembly.ExtensibleGateway.UserSecretsExtension) | 11.0.0 | J.Sakamoto | An extension that enables the use of User Secrets in a Blazor WebAssembly Stand… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

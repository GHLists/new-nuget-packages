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

## Latest list — 2026-11-17 13:20 UTC

New packages created between 2026-11-17 12:18 UTC and 2026-11-17 13:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-17T13-20-12-453281Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-17 12:19:39 | [OpenDCP.Framework.CalculationNode](https://www.nuget.org/packages/OpenDCP.Framework.CalculationNode) | 0.8.1 | OpenDCP.Framework.Calculation… | Package Description |
| 2026-11-17 12:26:19 | [haruspex](https://www.nuget.org/packages/haruspex) | 0.0.0-placeholder | Richard Baker | Types across the database boundary: SQL Server database projects to TypeScript.… |
| 2026-11-17 12:28:54 | [Sharplight.Import.F5Tts](https://www.nuget.org/packages/Sharplight.Import.F5Tts) | 0.2.0 | Sharplight contributors | F5-TTS importer for Sharplight: reads the F5-TTS flow-matching text-to-speech c… |
| 2026-11-17 12:28:55 | [Sharplight.Hosting](https://www.nuget.org/packages/Sharplight.Hosting) | 0.2.0 | Sharplight contributors | Hosting for Sharplight models in servers and apps: a ModelHost built from optio… |
| 2026-11-17 12:28:55 | [Sharplight.Import.CosyVoice](https://www.nuget.org/packages/Sharplight.Import.CosyVoice) | 0.2.0 | Sharplight contributors | CosyVoice importer for Sharplight: reads FunAudioLLM's Fun-CosyVoice3 text-to-s… |
| 2026-11-17 12:28:58 | [Sharplight.Video](https://www.nuget.org/packages/Sharplight.Video) | 0.2.0 | Sharplight contributors | Video encoding and decoding for Sharplight with bundled LGPL FFmpeg libraries (… |
| 2026-11-17 12:28:58 | [Sharplight.Import.Ultralytics](https://www.nuget.org/packages/Sharplight.Import.Ultralytics) | 0.2.0 | Sharplight contributors | Ultralytics YOLO importer for Sharplight: reads the ONNX exports of YOLOv8, YOL… |
| 2026-11-17 12:28:59 | [Sharplight.Import.Snac](https://www.nuget.org/packages/Sharplight.Import.Snac) | 0.2.0 | Sharplight contributors | SNAC importer for Sharplight: reads the multi-scale neural audio codec checkpoi… |
| 2026-11-17 12:29:00 | [Sharplight.Import.Chatterbox](https://www.nuget.org/packages/Sharplight.Import.Chatterbox) | 0.2.0 | Sharplight contributors | Chatterbox importer for Sharplight: reads Resemble AI's Chatterbox text-to-spee… |
| 2026-11-17 12:29:01 | [Sharplight.Import.Kokoro](https://www.nuget.org/packages/Sharplight.Import.Kokoro) | 0.2.0 | Sharplight contributors | Kokoro importer for Sharplight: reads the Kokoro-82M text-to-speech checkpoint… |
| 2026-11-17 12:29:03 | [Sharplight.DesignTokens](https://www.nuget.org/packages/Sharplight.DesignTokens) | 0.2.0 | Sharplight contributors | The Sharplight design tokens for web UIs: CSS custom properties (colours for da… |
| 2026-11-17 12:29:04 | [Sharplight.Vulkan.MoltenVK](https://www.nuget.org/packages/Sharplight.Vulkan.MoltenVK) | 0.2.0 | Sharplight contributors | MoltenVK (Vulkan on Metal) for Sharplight.Vulkan on macOS Apple Silicon: libMol… |
| 2026-11-17 12:29:05 | [Sharplight.Import.HuggingFace](https://www.nuget.org/packages/Sharplight.Import.HuggingFace) | 0.2.0 | Sharplight contributors | Hugging Face checkpoint importer (safetensors + config.json + tokenizer files)… |
| 2026-11-17 12:31:31 | [Lumen.Templates](https://www.nuget.org/packages/Lumen.Templates) | 0.1.0 | HinaKalo | dotnet new templates for Avalonia 12 apps built with Lumen.UI: lumen-app (AppSh… |
| 2026-11-17 12:31:32 | [Lumen.UI](https://www.nuget.org/packages/Lumen.UI) | 0.1.0 | HinaKalo | A modern, token-driven component library for Avalonia built on top of FluentThe… |
| 2026-11-17 12:55:23 | [OpenDCP.Framework.DataTypes.Analytical](https://www.nuget.org/packages/OpenDCP.Framework.DataTypes.Analytical) | 0.3.0 | OpenDCP.Framework.DataTypes.A… | Package Description |
| 2026-11-17 12:55:59 | [Lifeblood.any](https://www.nuget.org/packages/Lifeblood.any) | 0.7.14 | DAWG Tools | Roslyn powered C# and Unity code analysis CLI for semantic graphs, architecture… |
| 2026-11-17 12:56:01 | [Lifeblood.win-x64](https://www.nuget.org/packages/Lifeblood.win-x64) | 0.7.14 | DAWG Tools | Roslyn powered C# and Unity code analysis CLI for semantic graphs, architecture… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

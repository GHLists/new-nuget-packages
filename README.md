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

## Latest list — 2026-11-02 19:21 UTC

New packages created between 2026-11-02 18:23 UTC and 2026-11-02 19:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-02T19-21-21-034146Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-02 18:32:34 | [GeminiGatewayClient](https://www.nuget.org/packages/GeminiGatewayClient) | 2.0.1 | Osg-Junue | Lightweight, AOT-friendly .NET client for the Gemini API with Microsoft.Extensi… |
| 2026-11-02 18:45:37 | [DotSee.ErrorRadar](https://www.nuget.org/packages/DotSee.ErrorRadar) | 17.0.4 | DotSee Web Services | Watches an Umbraco site's own logging, groups repeating warnings and failures s… |
| 2026-11-02 18:49:35 | [NockMon.HardwareSensors](https://www.nuget.org/packages/NockMon.HardwareSensors) | 0.2.0 | nockawa | NockMon plugin: CPU, motherboard, GPU and memory sensors (temperatures, fan spe… |
| 2026-11-02 18:51:00 | [Rcinel.Translate](https://www.nuget.org/packages/Rcinel.Translate) | 0.1.0 | CodeIsNotEvil | Loads a translation set for a language and translates with Translate("UUIDv7",… |
| 2026-11-02 18:51:00 | [Rcinel.Translate.Core](https://www.nuget.org/packages/Rcinel.Translate.Core) | 0.1.0 | CodeIsNotEvil | Reads and writes RcinelTranslate projects: UUIDv7 keyed translation files, revi… |
| 2026-11-02 18:53:31 | [Woosh.Wisp](https://www.nuget.org/packages/Woosh.Wisp) | 1.0.0 | Woosh AS | Build a wisp for Woosh: commands, cards, presses and a server's events over one… |
| 2026-11-02 18:53:32 | [Woosh.Wisp.Hosting](https://www.nuget.org/packages/Woosh.Wisp.Hosting) | 1.0.0 | Woosh AS | Run a Woosh wisp in a .NET host: its line opens and closes with the host, its o… |
| 2026-11-02 19:00:21 | [BenScr.NeuralNetworks](https://www.nuget.org/packages/BenScr.NeuralNetworks) | 1.0.0 | Ben Schneider | CPU dense neural networks with deterministic initialization, mini-batch gradien… |
| 2026-11-02 19:04:38 | [BenScr.Console](https://www.nuget.org/packages/BenScr.Console) | 1.0.0 | Ben Schneider | C++20 terminal output, validated ANSI controls, redirected-stream handling and… |
| 2026-11-02 19:05:41 | [Ozakboy.Ai.ClaudeCli](https://www.nuget.org/packages/Ozakboy.Ai.ClaudeCli) | 0.1.0 | ozakboy | Ozakboy.Ai.Abstractions 的本地實作:把已安裝的 Claude Code CLI 當作子行程執行(claude --print --ou… |
| 2026-11-02 19:10:38 | [BenScr.Noise](https://www.nuget.org/packages/BenScr.Noise) | 1.0.0 | Ben Schneider | C++20 deterministic seeded 2D and 3D coherent value noise, normalized fractal c… |
| 2026-11-02 19:14:28 | [BenScr.Serialization](https://www.nuget.org/packages/BenScr.Serialization) | 1.0.0 | Ben Schneider | Bounded JSON, XML and MessagePack serialization, typed conversion and authentic… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

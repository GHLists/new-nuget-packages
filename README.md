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

## Latest list — 2026-10-17 09:20 UTC

New packages created between 2026-10-17 08:19 UTC and 2026-10-17 09:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-17T09-20-35-725478Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-17 08:23:05 | [TempLock](https://www.nuget.org/packages/TempLock) | 0.9.1 | Volker Hänsel | Hardened trial/evaluation licensing for Windows desktop apps: time-limited tria… |
| 2026-10-17 08:41:20 | [Orbyss.Foundation.Web.Presentation](https://www.nuget.org/packages/Orbyss.Foundation.Web.Presentation) | 0.3.6 | Orbyss | Selectable native browser recovery pages, admitted error presentation and share… |
| 2026-10-17 09:03:52 | [Aiursoft.AlertCenter.SDK](https://www.nuget.org/packages/Aiursoft.AlertCenter.SDK) | 10.0.0 | Aiursoft.AlertCenter.SDK | Report alerts to Aiursoft AlertCenter using AiurProtocol. |
| 2026-10-17 09:04:57 | [Oscova.Agents.Plugins.Browser](https://www.nuget.org/packages/Oscova.Agents.Plugins.Browser) | 2.0.0 | Oscova | Visible browser navigation, page reading and interaction for Oscova Agents. |
| 2026-10-17 09:05:01 | [Oscova.Agents.Plugins.Docker](https://www.nuget.org/packages/Oscova.Agents.Plugins.Docker) | 2.0.0 | Oscova | Docker execution for shell commands run by Oscova Agents, with shared image man… |
| 2026-10-17 09:05:04 | [Oscova.Agents.Plugins.ElevenLabs](https://www.nuget.org/packages/Oscova.Agents.Plugins.ElevenLabs) | 2.0.0 | Oscova | ElevenLabs speech recognition and synthesis for Oscova Agents, using a saved El… |
| 2026-10-17 09:05:17 | [Oscova.Agents.Plugins.LocalSpeechRecognition](https://www.nuget.org/packages/Oscova.Agents.Plugins.LocalSpeechRecognition) | 2.0.0 | Oscova | Oscova Agents plugin providing local Whisper recognition. |
| 2026-10-17 09:05:19 | [Oscova.Agents.Plugins.LocalSpeechRecognition.Cuda](https://www.nuget.org/packages/Oscova.Agents.Plugins.LocalSpeechRecognition.Cuda) | 2.0.0 | Oscova | NVIDIA CUDA local speech recognition for Windows x64 and Linux x64. Requires an… |
| 2026-10-17 09:05:22 | [Oscova.Agents.Plugins.LocalSpeechSynthesis](https://www.nuget.org/packages/Oscova.Agents.Plugins.LocalSpeechSynthesis) | 2.0.0 | Oscova | Oscova Agents plugin providing local Kokoro synthesis. |
| 2026-10-17 09:05:24 | [Oscova.Agents.Plugins.LocalSpeechSynthesis.Cuda](https://www.nuget.org/packages/Oscova.Agents.Plugins.LocalSpeechSynthesis.Cuda) | 2.0.0 | Oscova | NVIDIA CUDA local speech synthesis for Windows x64 and Linux x64. Requires an N… |
| 2026-10-17 09:05:29 | [Oscova.Agents.Plugins.Mxc](https://www.nuget.org/packages/Oscova.Agents.Plugins.Mxc) | 2.0.0 | Oscova | Microsoft MXC operating-system containment for shell commands run by Oscova Age… |
| 2026-10-17 09:05:31 | [Oscova.Agents.Plugins.OpenAI](https://www.nuget.org/packages/Oscova.Agents.Plugins.OpenAI) | 2.0.0 | Oscova | OpenAI speech recognition and synthesis for Oscova Agents, using a saved OpenAI… |
| 2026-10-17 09:06:22 | [Oscova.Agents.App.osx-x64](https://www.nuget.org/packages/Oscova.Agents.App.osx-x64) | 3.3.0 | Oscova | The oscova command that installs, starts and manages Oscova, a self-hosted AI a… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

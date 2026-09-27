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

## Latest list — 2026-09-27 22:22 UTC

New packages created between 2026-09-27 21:21 UTC and 2026-09-27 22:22 UTC.

[Full CSV](data/new-nuget-packages-2026-09-27T22-22-17-161365Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-27 21:22:22 | [Gravicode.MediaPipeNet.Tasks.Core](https://www.nuget.org/packages/Gravicode.MediaPipeNet.Tasks.Core) | 0.3.0 | Gravicode Studios, Kang Fadhil | MediaPipe.NET task foundations shared by the vision, audio and text tasks: Base… |
| 2026-09-27 21:22:24 | [Gravicode.MediaPipeNet.Tasks.Audio](https://www.nuget.org/packages/Gravicode.MediaPipeNet.Tasks.Audio) | 0.3.0 | Gravicode Studios, Kang Fadhil | MediaPipe.NET audio tasks: AudioClassifier (YAMNet, 521 AudioSet classes) and V… |
| 2026-09-27 21:22:25 | [Gravicode.MediaPipeNet.Tasks.Text](https://www.nuget.org/packages/Gravicode.MediaPipeNet.Tasks.Text) | 0.3.0 | Gravicode Studios, Kang Fadhil | MediaPipe.NET text tasks: TextClassifier (MobileBERT and average word-embedding… |
| 2026-09-27 21:22:34 | [Gravicode.MediaPipeNet.Models.Audio](https://www.nuget.org/packages/Gravicode.MediaPipeNet.Models.Audio) | 0.3.0 | Gravicode Studios, Kang Fadhil | Audio models for MediaPipe.NET: YAMNet audio event classifier (521 AudioSet cla… |
| 2026-09-27 21:22:38 | [Gravicode.MediaPipeNet.Models.ImageEmbedding](https://www.nuget.org/packages/Gravicode.MediaPipeNet.Models.ImageEmbedding) | 0.3.0 | Gravicode Studios, Kang Fadhil | Image embedding model for MediaPipe.NET: MobileNet V3 small (1024-D feature vec… |
| 2026-09-27 21:22:42 | [Gravicode.MediaPipeNet.Models.Quantized](https://www.nuget.org/packages/Gravicode.MediaPipeNet.Models.Quantized) | 0.3.0 | Gravicode Studios, Kang Fadhil | Reduced-precision variants of the MediaPipe.NET models: FP16 (half size, best o… |
| 2026-09-27 21:22:45 | [Gravicode.MediaPipeNet.Models.Text](https://www.nuget.org/packages/Gravicode.MediaPipeNet.Models.Text) | 0.3.0 | Gravicode Studios, Kang Fadhil | Text models for MediaPipe.NET: MobileBERT and average-word sentiment classifier… |
| 2026-09-27 21:24:35 | [Goodtocode.Agents.Playbook.Prompting](https://www.nuget.org/packages/Goodtocode.Agents.Playbook.Prompting) | 1.2.3 | Robert Good | Universal, prompt-based Collect/Evaluate/Record tools for Goodtocode.Agents.Pla… |
| 2026-09-27 21:41:35 | [Beetech.Adv.Abstractions](https://www.nuget.org/packages/Beetech.Adv.Abstractions) | 1.0.0 | Beetech Auto-ID Team | Open, zero-dependency hardware driver abstractions and contracts for Beetech Un… |
| 2026-09-27 21:41:54 | [Beetech.Adv.SmartSdk](https://www.nuget.org/packages/Beetech.Adv.SmartSdk) | 1.0.0 | Beetech.Adv.SmartSdk | Beetech Universal RFID & IoT SmartSdk Client for AdvSmartSdk Native Engine |
| 2026-09-27 21:42:02 | [Beetech.Adv.Automation](https://www.nuget.org/packages/Beetech.Adv.Automation) | 1.0.0 | AnhDV | Beetech Advanced Industrial Automation & Fieldbus Library - Native drivers for… |
| 2026-09-27 21:42:13 | [Beetech.Adv.Printers](https://www.nuget.org/packages/Beetech.Adv.Printers) | 1.0.0 | AnhDV | Beetech Advanced RFID Label Printer Engine - Native ZPL II, Sato SBPL, and Dire… |
| 2026-09-27 21:42:22 | [Beetech.Adv.Vision](https://www.nuget.org/packages/Beetech.Adv.Vision) | 1.0.0 | AnhDV | Beetech Advanced Computer Vision & Optical Sensor Fusion Engine - RTSP/ONVIF fr… |
| 2026-09-27 21:42:30 | [Beetech.Adv.Station](https://www.nuget.org/packages/Beetech.Adv.Station) | 1.0.0 | AnhDV | Beetech Advanced Industrial Station Pipeline & Fusion Orchestrator - Determinis… |
| 2026-09-27 21:54:08 | [BulletHero.SDK](https://www.nuget.org/packages/BulletHero.SDK) | 1.0.0 | vertoker | The open level and save data model of the game Bullet Hero: models, JSON and bi… |
| 2026-09-27 21:57:14 | [EntityFrameworkCore.Encrypted.AwsKms](https://www.nuget.org/packages/EntityFrameworkCore.Encrypted.AwsKms) | 2.0.1-beta | starushykart | AWS KMS envelope encryption for EntityFrameworkCore.Encrypted |
| 2026-09-27 22:16:19 | [Universal.Xiaomi.MiMo.Client](https://www.nuget.org/packages/Universal.Xiaomi.MiMo.Client) | 1.0.0 | Andrew Ong | Client for the Xiaomi MiMo API. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

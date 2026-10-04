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

## Latest list — 2026-10-04 23:21 UTC

New packages created between 2026-10-04 22:20 UTC and 2026-10-04 23:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-04T23-21-18-255623Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-04 22:32:43 | [Tracera.Core](https://www.nuget.org/packages/Tracera.Core) | 1.0.0 | Tracera <contact@tracera.dev> | Tracera Autotest adapter core for .NET (HTTP, flush, log, dotenv, Env, session,… |
| 2026-10-04 22:33:22 | [Tracera.NUnit](https://www.nuget.org/packages/Tracera.NUnit) | 1.0.0 | Tracera <contact@tracera.dev> | Tracera Autotest adapter for NUnit |
| 2026-10-04 22:33:59 | [Tracera.Xunit](https://www.nuget.org/packages/Tracera.Xunit) | 1.0.0 | Tracera <contact@tracera.dev> | Tracera Autotest adapter for xUnit.net v3 |
| 2026-10-04 22:34:30 | [Tracera.Reqnroll](https://www.nuget.org/packages/Tracera.Reqnroll) | 1.0.0 | Tracera <contact@tracera.dev> | Tracera Autotest adapter for Reqnroll |
| 2026-10-04 22:35:59 | [NousToolCalling](https://www.nuget.org/packages/NousToolCalling) | 0.1.0 | Murat Ay | Prompt-based (Nous-style) tool calling for IChatClient. Makes on-prem / OpenAI-… |
| 2026-10-04 22:36:00 | [NousToolCalling.AgentFramework](https://www.nuget.org/packages/NousToolCalling.AgentFramework) | 0.1.0 | Murat Ay | Composition helpers for Nous-style tool calling with Microsoft Agent Framework:… |
| 2026-10-04 22:48:46 | [StreamNest](https://www.nuget.org/packages/StreamNest) | 1.0.0 | Esmail Almarrani | A high-performance, zero-dependency asynchronous stream collection for .NET sup… |
| 2026-10-04 22:49:53 | [KafkaWrapper](https://www.nuget.org/packages/KafkaWrapper) | 1.0.0-CI-20261004-2… | KafkaWrapper | Package Description |
| 2026-10-04 22:54:31 | [Bullmark.Sdk](https://www.nuget.org/packages/Bullmark.Sdk) | 0.1.0 | Bullmark | Honour a Bullmark voucher from your own checkout — inspect, redeem, release, an… |
| 2026-10-04 22:55:31 | [EncDotNet.S100.Collections](https://www.nuget.org/packages/EncDotNet.S100.Collections) | 0.24.0 | Phillip Hoff | Libraries for manipulating S-100 based nautical charts. |
| 2026-10-04 23:04:07 | [Arjo.Umbraco.WeglotTranslator](https://www.nuget.org/packages/Arjo.Umbraco.WeglotTranslator) | 1.0.0 | Arjo.dev | Weglot-powered machine translation for Umbraco 17+: translated pages served fro… |
| 2026-10-04 23:09:33 | [PanoramicData.Aruba.Api](https://www.nuget.org/packages/PanoramicData.Aruba.Api) | 1.1.2 | Panoramic Data Limited | .NET 10 API client for HPE Aruba Networking Central (New Central): monitoring,… |
| 2026-10-04 23:13:02 | [Senviok](https://www.nuget.org/packages/Senviok) | 1.0.0 | Senviok | Official .NET SDK for the Senviok API - Transactional Email, SMS, WhatsApp, OTP… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

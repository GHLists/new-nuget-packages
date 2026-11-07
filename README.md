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

## Latest list — 2026-11-07 11:21 UTC

New packages created between 2026-11-07 10:19 UTC and 2026-11-07 11:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-07T11-21-52-979508Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-07 10:21:02 | [O24Engine.Analyzer](https://www.nuget.org/packages/O24Engine.Analyzer) | 2.0.16 | Linh Nguyen | Roslyn source generators and analyzers for O24Engine. |
| 2026-11-07 10:21:07 | [O24Engine.Analyzer.Grpc](https://www.nuget.org/packages/O24Engine.Analyzer.Grpc) | 2.0.14 | Linh Nguyen | Roslyn source generators and analyzers for O24Engine gRPC. |
| 2026-11-07 10:30:08 | [uTPro.Feature.TextToSpeech](https://www.nuget.org/packages/uTPro.Feature.TextToSpeech) | 18.0.0 | T4VN | "Listen to this article" for Umbraco 17 and 18. Drop one ViewComponent line int… |
| 2026-11-07 10:30:44 | [uTPro.Feature.TextToSpeech.Kokoro](https://www.nuget.org/packages/uTPro.Feature.TextToSpeech.Kokoro) | 18.0.0 | T4VN | Kokoro offline voice engine for uTPro.Feature.TextToSpeech. Adds natural-soundi… |
| 2026-11-07 10:31:17 | [uTPro.Feature.TextToSpeech.Piper](https://www.nuget.org/packages/uTPro.Feature.TextToSpeech.Piper) | 18.0.0 | T4VN | Piper offline voice engine for uTPro.Feature.TextToSpeech. Adds fast, fully loc… |
| 2026-11-07 10:34:50 | [Likyly](https://www.nuget.org/packages/Likyly) | 1.0.0 | LIKYLY | Product recommendations for your site ("You may also like", "Recommended for yo… |
| 2026-11-07 10:36:11 | [uTPro.Feature.AdProtect](https://www.nuget.org/packages/uTPro.Feature.AdProtect) | 18.0.0 | T4VN | Invalid-click protection and ad-serving control for Umbraco sites monetized wit… |
| 2026-11-07 10:36:29 | [Hostily.Captcha](https://www.nuget.org/packages/Hostily.Captcha) | 0.2.0 | connect - Media & Teledienst | Server-side client for hostily Captcha (captcha.hostily.de): verify the token o… |
| 2026-11-07 10:36:30 | [Hostily.Captcha.AspNetCore](https://www.nuget.org/packages/Hostily.Captcha.AspNetCore) | 0.2.0 | connect - Media & Teledienst | ASP.NET Core integration for hostily Captcha: [HostilyCaptcha] filter and the h… |
| 2026-11-07 10:57:19 | [BunnyLoader.ModSdk](https://www.nuget.org/packages/BunnyLoader.ModSdk) | 0.3.1 | BL Editor contributors | Self-contained compile-time BunnyLoader API and deterministic format 3 source p… |
| 2026-11-07 10:57:43 | [Fp.Mail](https://www.nuget.org/packages/Fp.Mail) | 0.1.0 | Financial Partners | Send e-mail (HTML or text, with attachments up to 150 MB) through Microsoft Gra… |
| 2026-11-07 11:14:35 | [HAKICODE.Workbench.Plugin.BrowserAgent](https://www.nuget.org/packages/HAKICODE.Workbench.Plugin.BrowserAgent) | 1.0.5 | HAKICODE | Cho trợ lý tự mở trang web, bấm và điền trong trình duyệt riêng, người dùng xem… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

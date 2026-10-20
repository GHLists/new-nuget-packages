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

## Latest list — 2026-10-20 12:22 UTC

New packages created between 2026-10-20 11:22 UTC and 2026-10-20 12:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-20T12-22-46-718874Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-20 11:46:32 | [Bit.Bcrdt.Server](https://www.nuget.org/packages/Bit.Bcrdt.Server) | 11.0.0-pre-10 | bit platform | The ASP.NET Core relays for bit Bcrdt: the SignalR hub the Bit.Bcrdt.SignalR tr… |
| 2026-10-20 11:46:34 | [Bit.Bcrdt.Testing](https://www.nuget.org/packages/Bit.Bcrdt.Testing) | 11.0.0-pre-10 | bit platform | Test support for bit Bcrdt: a deterministic, seeded network simulator with loss… |
| 2026-10-20 11:46:35 | [Bit.BevTools.Server](https://www.nuget.org/packages/Bit.BevTools.Server) | 11.0.0-pre-10 | bit platform | Blazor Server (interactive server / circuits) instrumentation for bit BevTools:… |
| 2026-10-20 11:46:38 | [Bit.Belemetry.Hangfire](https://www.nuget.org/packages/Bit.Belemetry.Hangfire) | 11.0.0-pre-10 | bit platform | Bit.Belemetry.Hangfire |
| 2026-10-20 11:46:43 | [Bit.Borm.FluentValidation](https://www.nuget.org/packages/Bit.Borm.FluentValidation) | 11.0.0-pre-10 | bit platform | FluentValidation integration for Bit.Borm. UseFluentValidation() runs a model's… |
| 2026-10-20 11:49:02 | [Devinno.UI](https://www.nuget.org/packages/Devinno.UI) | 0.1.0 | Devinno | SkiaSharp 기반 .NET UI 라이브러리 (산업용 HMI 터치 패널·일반 앱). XML 마크업 + CSS 식 인라인 style + C#… |
| 2026-10-20 11:49:03 | [Devinno.UI.OpenTK](https://www.nuget.org/packages/Devinno.UI.OpenTK) | 0.1.0 | Devinno | Devinno.UI 의 OpenTK 창 어댑터 — ViewWindow 로 DvApp 을 창에 띄웁니다(터치 우선, 가상 키보드, CPU·Ope… |
| 2026-10-20 11:49:03 | [Devinno.UI.WinForms](https://www.nuget.org/packages/Devinno.UI.WinForms) | 0.1.0 | Devinno | Devinno.UI 의 WinForms 어댑터 — ViewControl 로 DvApp 을 폼에 올립니다(한글 IME 입력, 터치 모드 선택). |
| 2026-10-20 12:03:54 | [EasyTdd.Mcp](https://www.nuget.org/packages/EasyTdd.Mcp) | 6.0.2 | kazys | EasyTdd MCP server — AI-assistant-driven TDD code generation (builders, fluent… |
| 2026-10-20 12:09:29 | [KeyGuard](https://www.nuget.org/packages/KeyGuard) | 0.1.0 | KeyGuard | Official .NET SDK for KeyGuard license verification (verify, hardware fingerpri… |
| 2026-10-20 12:15:45 | [Zyga.SeriRestClient.Spectre](https://www.nuget.org/packages/Zyga.SeriRestClient.Spectre) | 0.2.0 | Szymon Zywert | Spectre.Console-based pretty JSON formatter for Zyga.SeriRestClient logs |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

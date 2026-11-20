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

## Latest list — 2026-11-20 18:19 UTC

New packages created between 2026-11-20 17:21 UTC and 2026-11-20 18:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-20T18-19-11-240509Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-20 17:31:02 | [WhaleGenie.Platform.Windows](https://www.nuget.org/packages/WhaleGenie.Platform.Windows) | 0.0.1-alpha1 | WhaleGenie.Platform.Windows | 鲸灵的 Windows 适配器：键鼠钩子、UI Automation、找图找色、OCR、浏览器、脚本宿主与手柄驱动。 |
| 2026-11-20 17:31:02 | [Csag.Extensions.Caching.InMemory](https://www.nuget.org/packages/Csag.Extensions.Caching.InMemory) | 4.0.0 | collana solutions AG | Strongly typed IMemoryCache<TCacheId> with enum cache identifiers, on top of Mi… |
| 2026-11-20 17:31:03 | [Csag.Extensions.Caching.Abstractions](https://www.nuget.org/packages/Csag.Extensions.Caching.Abstractions) | 4.0.0 | collana solutions AG | Strongly typed caching with enum cache identifiers instead of magic strings: th… |
| 2026-11-20 17:31:04 | [Csag.Extensions.Caching.Distributed](https://www.nuget.org/packages/Csag.Extensions.Caching.Distributed) | 4.0.0 | collana solutions AG | Strongly typed IDistributedCache<TCacheId> with enum cache identifiers, on top… |
| 2026-11-20 17:31:06 | [Csag.Extensions.Caching.RedisHybrid](https://www.nuget.org/packages/Csag.Extensions.Caching.RedisHybrid) | 4.0.0 | collana solutions AG | Strongly typed IDistributedCache<TCacheId> with enum cache identifiers that com… |
| 2026-11-20 17:37:23 | [WhaleGenie.Core](https://www.nuget.org/packages/WhaleGenie.Core) | 0.0.1-alpha1 | WhaleGenie.Core | 鲸灵（WhaleGenie）的宏引擎：动作语义、表达式、变量、设备契约与录制翻译。 |
| 2026-11-20 17:37:25 | [WhaleGenie.GraphicsCapture](https://www.nuget.org/packages/WhaleGenie.GraphicsCapture) | 0.0.1-alpha1 | WhaleGenie.GraphicsCapture | 鲸灵的画面获取：Graphics Capture、桌面复制、GDI 与 PrintWindow，以及会话缓存。 |
| 2026-11-20 17:41:45 | [Meai.CostGuard](https://www.nuget.org/packages/Meai.CostGuard) | 0.1.0 | sergey-mcarrow | Token-aware rate limiter, cost guard, and automatic fallback middleware for Mic… |
| 2026-11-20 17:43:57 | [Bydev.Sdk](https://www.nuget.org/packages/Bydev.Sdk) | 0.1.0 | 한비트 주식회사 | 데브 라이선스 API 공식 .NET SDK — 디바이스 로그인 · 토큰 회전 · 세션 리스 · licenseToken 검증 · 업데이트 확인 |
| 2026-11-20 17:50:43 | [Carahsoft.Calliope.Elm](https://www.nuget.org/packages/Carahsoft.Calliope.Elm) | 0.1.0 | Carahsoft.Calliope.Elm | Elm-style F# programs for Carahsoft.Calliope: pure init/update/view, commands,… |
| 2026-11-20 17:54:19 | [Stabilt.TellusTalk.Emulator.Client](https://www.nuget.org/packages/Stabilt.TellusTalk.Emulator.Client) | 0.7.0 | Stabilt AB | Reads what TellusTalk Emulator, a local stand-in for TellusTalk's K8 send API,… |
| 2026-11-20 18:13:21 | [EmmittJ.Aspire.Hosting.Terraform.Sdk](https://www.nuget.org/packages/EmmittJ.Aspire.Hosting.Terraform.Sdk) | 0.0.9 | EmmittJ | Terraform support for Aspire using EmmittJ.Terraform.Sdk. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-08 09:20 UTC

New packages created between 2026-11-08 08:20 UTC and 2026-11-08 09:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-08T09-20-45-082403Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-08 08:29:25 | [CSharpUtil.Extensions](https://www.nuget.org/packages/CSharpUtil.Extensions) | 0.1.0 | Yeung | Common .NET tools and helpers |
| 2026-11-08 08:53:22 | [Ojs.Api.Client](https://www.nuget.org/packages/Ojs.Api.Client) | 0.1.0-preview | Aldi | A .NET client library (written in VB.NET) for the Open Journal Systems (OJS) 3.… |
| 2026-11-08 08:59:35 | [Fp.Data](https://www.nuget.org/packages/Fp.Data) | 0.2.0 | Financial Partners | Building blocks for Entity Framework Core: base entities, automatic auditing an… |
| 2026-11-08 09:16:06 | [JyunoSdk](https://www.nuget.org/packages/JyunoSdk) | 0.2.0 | jyunrcaea | Jyuno SDK: 대화형 Jyuno 프롬프트, 스크립트 실행/검사, Native JS(JavaScript) 변환, 그리고 Jyuno 언어 서… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

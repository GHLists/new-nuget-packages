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

## Latest list — 2026-11-06 12:19 UTC

New packages created between 2026-11-06 11:21 UTC and 2026-11-06 12:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-06T12-19-02-127111Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-06 11:22:56 | [Jyuno](https://www.nuget.org/packages/Jyuno) | 1.0.0 | jyunrcaea | C# 프로그램에 안전한 플러그인(스크립트) 기능을 쉽게 추가하기 위한 작고 가벼운 언어 Jyuno의 인터프리터입니다. |
| 2026-11-06 11:57:48 | [KeyInteractive.Licensing](https://www.nuget.org/packages/KeyInteractive.Licensing) | 1.0.0 | KeyInteractive | Client side of the Key Interactive offline licensing, for applications: verifie… |
| 2026-11-06 11:57:51 | [KeyInteractive.Licensing.Issuing](https://www.nuget.org/packages/KeyInteractive.Licensing.Issuing) | 1.0.0 | KeyInteractive | SERVER-SIDE ONLY. Issues Key Interactive offline licenses and signs activation… |
| 2026-11-06 12:05:15 | [SFA.DAS.AssessorService.Messages](https://www.nuget.org/packages/SFA.DAS.AssessorService.Messages) | 0.1.305-prerelease-9 | ESFA | Assessor Service integration messages |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-13 16:19 UTC

New packages created between 2026-11-13 15:20 UTC and 2026-11-13 16:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-13T16-19-00-538223Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-13 15:26:14 | [Olve.Fuzzy](https://www.nuget.org/packages/Olve.Fuzzy) | 0.63.2 | Oliver Vea | Fuzzy logic with a fluent rule syntax: member functions, rules and centroid def… |
| 2026-11-13 15:27:32 | [YADIS.OhioT1DM.Models](https://www.nuget.org/packages/YADIS.OhioT1DM.Models) | 1.0.0 | N. Batchaev | Data models (DTOs) for the OhioT1DM dataset annotated for XML and MessagePack s… |
| 2026-11-13 15:29:07 | [TNID.NET](https://www.nuget.org/packages/TNID.NET) | 0.1.0 | Codevia Solutions s.r.o. | A minimal, dependency-free implementation of the TNID 1.0 core format. |
| 2026-11-13 15:32:53 | [Medical.Bpjs](https://www.nuget.org/packages/Medical.Bpjs) | 1.1.0 | Gravicode Studios (Kang Fadhi… | Medical.Net BPJS Kesehatan (Indonesian national health insurance, JKN): INA-CBG… |
| 2026-11-13 15:46:34 | [NDM-Logger](https://www.nuget.org/packages/NDM-Logger) | 1.0.0 | Joe Swindell | Serilog sink setup that sends log entries to NDM-Logging-API, queued in memory… |
| 2026-11-13 15:46:54 | [Auxilia.BackVial.Entities](https://www.nuget.org/packages/Auxilia.BackVial.Entities) | 1.0.0 | Auxilia | Entidades compartidas de BackVial. |
| 2026-11-13 15:48:17 | [D3sk.ChatUi.Avalonia](https://www.nuget.org/packages/D3sk.ChatUi.Avalonia) | 0.2.0 | neijix | D3SKHAND's chat for Avalonia: ChatView with the virtualized transcript, working… |
| 2026-11-13 15:48:17 | [D3sk.ChatUi](https://www.nuget.org/packages/D3sk.ChatUi) | 0.2.0 | neijix | D3SKHAND's chat rules with no UI types: the session that folds D3sk.AgentCli tu… |
| 2026-11-13 15:52:08 | [NkkinSoft.Shimmer.Maui](https://www.nuget.org/packages/NkkinSoft.Shimmer.Maui) | 1.0.0 | NkkinSoft.Shimmer.Maui | Cross-platform skeleton loading for .NET MAUI with theme-aware gradients and re… |
| 2026-11-13 15:54:43 | [SFA.DAS.EmploymentVerificationService.Messages](https://www.nuget.org/packages/SFA.DAS.EmploymentVerificationService.Messages) | 0.1.6-prerelease-61 | SFA.DAS.EmploymentVerificatio… | Package Description |
| 2026-11-13 15:57:02 | [Hegel.FSharp](https://www.nuget.org/packages/Hegel.FSharp) | 0.2.0 | David R. MacIver | Property-based testing for F#, driven by the Hegel engine (libhegel): F# genera… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

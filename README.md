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

## Latest list — 2026-11-27 08:21 UTC

New packages created between 2026-11-27 07:20 UTC and 2026-11-27 08:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-27T08-21-31-142042Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-27 07:39:40 | [Vouch.Time](https://www.nuget.org/packages/Vouch.Time) | 0.4.0 | BaryoDev | Time helpers for Vouch with no dependencies: 5.Minutes(), 1.March(2026).At(10,… |
| 2026-11-27 07:41:22 | [PowerAutomateFlowAuditor](https://www.nuget.org/packages/PowerAutomateFlowAuditor) | 1.0.1 | Apoorv Gupta | Audit Power Automate Cloud Flows in Dataverse to detect critical performance an… |
| 2026-11-27 07:47:26 | [Eternet.AspNetCore.Components](https://www.nuget.org/packages/Eternet.AspNetCore.Components) | 1.0.0 | Eternet.AspNetCore.Components | Blazor component bases that cancel their work when the circuit closes, plus the… |
| 2026-11-27 07:47:35 | [Limbo.Umbraco.Core](https://www.nuget.org/packages/Limbo.Umbraco.Core) | 17.0.0-alpha001 | Anders Bjerner | Internal package at Limbo. Install at your own risk. |
| 2026-11-27 07:54:26 | [complexMathPacket](https://www.nuget.org/packages/complexMathPacket) | 1.0.0 | Veronika | Библиотека комплексных чисел: +, -, *, / |
| 2026-11-27 07:55:43 | [CodecHub.DevToys](https://www.nuget.org/packages/CodecHub.DevToys) | 1.0.4 | CodecHub | Unified encoder/decoder workbench: URL, HTML, Unicode, JSON, Base64/32/58, Hex,… |
| 2026-11-27 07:56:57 | [Qore.BaseQore](https://www.nuget.org/packages/Qore.BaseQore) | 1.1.0 | BOC | Base Quc library containing repositories, filters, services, utilities, caching… |
| 2026-11-27 08:11:33 | [ObserverMessage](https://www.nuget.org/packages/ObserverMessage) | 0.1.0 | ivanzanolla | Lightweight in-process event bus (publish/subscribe) for .NET, built on TPL Dat… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

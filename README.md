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

## Latest list — 2026-10-07 11:20 UTC

New packages created between 2026-10-07 10:21 UTC and 2026-10-07 11:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-07T11-20-57-779865Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-07 10:27:56 | [Juit.Jurisprudence](https://www.nuget.org/packages/Juit.Jurisprudence) | 1.0.0 | loud-technology and contribut… | Modern, strongly typed .NET SDK for Juit Jurisprudence search and artifact down… |
| 2026-10-07 10:28:50 | [Hexalith.Parties.AdminPortal](https://www.nuget.org/packages/Hexalith.Parties.AdminPortal) | 1.2.1 | Hexalith Contributors | FrontComposer-hosted Blazor administration portal for Hexalith.Parties. |
| 2026-10-07 10:28:50 | [Hexalith.Parties.ConsumerPortal](https://www.nuget.org/packages/Hexalith.Parties.ConsumerPortal) | 1.2.1 | Hexalith Contributors | FrontComposer-hosted Blazor consumer portal for Hexalith.Parties. |
| 2026-10-07 10:36:21 | [EpcQr.Net](https://www.nuget.org/packages/EpcQr.Net) | 1.0.0 | Israel Iyonsi | Correct, zero-dependency builder and parser for the EPC069-12 "Scan2Pay" QR pay… |
| 2026-10-07 10:36:25 | [SwiftMt.Net](https://www.nuget.org/packages/SwiftMt.Net) | 1.0.0 | Israel Iyonsi | Correct, zero-dependency parser for SWIFT FIN MT messages (MT103, MT101, MT202)… |
| 2026-10-07 10:38:36 | [FrogLogic](https://www.nuget.org/packages/FrogLogic) | 0.1.0 | FrogLogic contributors | Lightweight, generic, single-pass data cleaning and diagnostics for IEnumerable… |
| 2026-10-07 10:45:00 | [Saci](https://www.nuget.org/packages/Saci) | 0.17.0 | saci | saci - Software Agent for Continuous Improvement: autonomous triager, developer… |
| 2026-10-07 10:45:35 | [LilyDesignSystem.Blazor.LinkPicker](https://www.nuget.org/packages/LilyDesignSystem.Blazor.LinkPicker) | 0.1.0 | Joel Parker Henderson | Lily Design System Blazor link picker: an icon button (a home icon) opening a d… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

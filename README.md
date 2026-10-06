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

## Latest list — 2026-10-06 10:19 UTC

New packages created between 2026-10-06 09:20 UTC and 2026-10-06 10:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-06T10-19-25-074861Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-06 09:31:16 | [Lokad.Jq](https://www.nuget.org/packages/Lokad.Jq) | 0.1.0 | Lokad | Embeddable jq runtime for .NET with host-mediated IO. See docs/COMPATIBILITY_MA… |
| 2026-10-06 09:40:56 | [CardCQ.Engine.Abstractions](https://www.nuget.org/packages/CardCQ.Engine.Abstractions) | 0.1.0 | Thomas Volden | Abstractions (commands, queries, events and handlers) for the CardCQ engine. Us… |
| 2026-10-06 09:53:53 | [Ansight.Motion](https://www.nuget.org/packages/Ansight.Motion) | 1.7.0 | Ansight AI | App-fed shake and accelerometer evidence for Ansight. |
| 2026-10-06 10:06:27 | [OnTheFlySettings.AWSSecretManager.Client](https://www.nuget.org/packages/OnTheFlySettings.AWSSecretManager.Client) | 1.0.0 | Shantanu | Client for OnTheFlySettings endpoints. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

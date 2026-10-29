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

## Latest list — 2026-10-29 23:20 UTC

New packages created between 2026-10-29 22:19 UTC and 2026-10-29 23:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-29T23-20-53-583334Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-29 22:41:09 | [NuGetAzCredentialsProvider](https://www.nuget.org/packages/NuGetAzCredentialsProvider) | 0.1.0 | Fredrik Arvidsson | NuGet credential plugin that authenticates to NuGet feeds using Azure CLI login |
| 2026-10-29 22:48:56 | [TRNRun](https://www.nuget.org/packages/TRNRun) | 0.9.1 | Natural Resources Canada / Re… | Run, monitor, and orchestrate batches of TRNSYS simulations |
| 2026-10-29 22:50:05 | [JsTimeline.Blazor](https://www.nuget.org/packages/JsTimeline.Blazor) | 1.0.0 | werddomain | Flash CS4-style animation timeline for Blazor: the timeline-runtime and timelin… |
| 2026-10-29 22:50:06 | [Infrawrench.BulkInstances](https://www.nuget.org/packages/Infrawrench.BulkInstances) | 1.0.0 | Infrawrench LLC | AWS EC2 instance attributes and pricing, with full history, from Infrawrench. |
| 2026-10-29 22:58:09 | [Umbricians.LiveView](https://www.nuget.org/packages/Umbricians.LiveView) | 0.1.0 | Umbricians | A real-time Live View dashboard for the Umbraco Settings section, charting acti… |
| 2026-10-29 23:12:12 | [QX](https://www.nuget.org/packages/QX) | 0.1.1 | QDave | Build native Habbo extensions with G-Earth, live game state, typed actions, Wir… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

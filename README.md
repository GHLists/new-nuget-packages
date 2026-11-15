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

## Latest list — 2026-11-15 23:20 UTC

New packages created between 2026-11-15 22:19 UTC and 2026-11-15 23:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-15T23-20-08-625973Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-15 22:20:25 | [DefangLabs.DefangScaleway](https://www.nuget.org/packages/DefangLabs.DefangScaleway) | 2.12.1 | Defang | Deploy containerized services to Scaleway with Pulumi. |
| 2026-11-15 22:20:42 | [eGraphicsCloud.Plugins.CustomValidationControls](https://www.nuget.org/packages/eGraphicsCloud.Plugins.CustomValidationControls) | 3.17.88 | Ibrar Tariq | eGraphicsCloud.Plugins.CustomValidationControls provides validation controls al… |
| 2026-11-15 22:56:02 | [dev-orchestrator-cli](https://www.nuget.org/packages/dev-orchestrator-cli) | 0.2.0 | Dev Orchestrator | Dev Orchestrator CLI (devorch): a .NET tool driven by the API's OpenAPI documen… |
| 2026-11-15 23:01:57 | [Nethermind.Libp2p.Protocols.KadDht](https://www.nuget.org/packages/Nethermind.Libp2p.Protocols.KadDht) | 1.1.4 | Nethermind | A libp2p implementation for .NET |
| 2026-11-15 23:12:26 | [Oneverse.Lazers](https://www.nuget.org/packages/Oneverse.Lazers) | 0.1.0 | Emmanuel Ilori, Oneverse | Server-side .NET SDK for Lazers Signal Protocol v1. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-05 01:19 UTC

New packages created between 2026-11-05 00:21 UTC and 2026-11-05 01:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-05T01-19-34-620388Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-05 00:28:14 | [ProofStudio.Common](https://www.nuget.org/packages/ProofStudio.Common) | 0.3.0-beta | Cormier Solutions LLC | Shared ProofStudio types: JSON settings, the project document envelope that pre… |
| 2026-11-05 00:28:17 | [ProofStudio.Editor](https://www.nuget.org/packages/ProofStudio.Editor) | 0.3.0-beta | Cormier Solutions LLC | Self-hosted ProofStudio browser integrations: proof form, authoring, form confi… |
| 2026-11-05 00:28:19 | [ProofStudio.Plugins](https://www.nuget.org/packages/ProofStudio.Plugins) | 0.3.0-beta | Cormier Solutions LLC | Server-side ProofStudio plugins for ASP.NET Core hosts. Background removal (sol… |
| 2026-11-05 00:28:40 | [ProofStudio.Remote](https://www.nuget.org/packages/ProofStudio.Remote) | 0.3.0-beta | Cormier Solutions LLC | Server-side .NET client for a hosted ProofStudio instance: B2B client-credentia… |
| 2026-11-05 00:33:42 | [Flare.Components.Scheduler.Ical](https://www.nuget.org/packages/Flare.Components.Scheduler.Ical) | 0.52.0 | FrigaT | Optional local RFC 5545 recurrence adapter for standalone Flare Scheduler clien… |
| 2026-11-05 00:33:43 | [Flare.Components.Scheduler](https://www.nuget.org/packages/Flare.Components.Scheduler) | 0.52.0 | FrigaT | Generic calendar scheduling UI with provider-owned events and resource timeline… |
| 2026-11-05 00:36:58 | [Umbraco.Community.ArchivedUsers](https://www.nuget.org/packages/Umbraco.Community.ArchivedUsers) | 18.0.0 | Pascal Meyer | Adds an Archived area to the Umbraco Users section. Archive leavers so they lea… |
| 2026-11-05 00:43:42 | [FastCdc](https://www.nuget.org/packages/FastCdc) | 2.0.0 | Whaliin | Content-defined chunking (FastCDC) for .NET |
| 2026-11-05 00:52:05 | [Carandev.WhatsApp.Sdk](https://www.nuget.org/packages/Carandev.WhatsApp.Sdk) | 0.1.0 | Carlos Gomez | .NET SDK for Meta's WhatsApp Cloud API: typed clients, host-agnostic webhook ve… |
| 2026-11-05 00:55:06 | [Pubb.Server](https://www.nuget.org/packages/Pubb.Server) | 0.3.0 | Pubb | .NET server SDK for Pubb realtime publishing and private/presence channel autho… |
| 2026-11-05 01:09:54 | [ProofStudio.Plugins.BackgroundRemoval](https://www.nuget.org/packages/ProofStudio.Plugins.BackgroundRemoval) | 0.3.0-beta | Cormier Solutions LLC | Server-side background removal for ASP.NET Core hosts of the ProofStudio editor… |
| 2026-11-05 01:12:12 | [XCGF.Data](https://www.nuget.org/packages/XCGF.Data) | 0.1.1 | mastertnt | XML schema (XSD) describing XCGF archetypes (data types, equipments, entities,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

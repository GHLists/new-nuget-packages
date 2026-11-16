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

## Latest list — 2026-11-16 07:20 UTC

New packages created between 2026-11-16 06:19 UTC and 2026-11-16 07:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-16T07-20-43-843334Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-16 06:27:14 | [SAEA.Sockets.Pipeline](https://www.nuget.org/packages/SAEA.Sockets.Pipeline) | 26.11.16.1 | yswenli | SAEA.Sockets.Pipeline is a bidirectional channel pipeline with pluggable frame… |
| 2026-11-16 06:50:16 | [Cratis.Scene.Design](https://www.nuget.org/packages/Cratis.Scene.Design) | 6.0.0 | Cratis | Scene Design: the catalogue that grounds a design, design operations lowered to… |
| 2026-11-16 06:50:17 | [Cratis.Scene.Screenplay](https://www.nuget.org/packages/Cratis.Scene.Screenplay) | 6.0.0 | Cratis | The two-way bridge between Screenplay and Scene: Screenplay syntax converted in… |
| 2026-11-16 06:50:17 | [Cratis.Scene.Design.AI](https://www.nuget.org/packages/Cratis.Scene.Design.AI) | 6.0.0 | Cratis | Scene Design with AI: a tool loop over the design catalogue and the Screenplay… |
| 2026-11-16 07:00:17 | [ProofStudio.DisplayForm](https://www.nuget.org/packages/ProofStudio.DisplayForm) | 0.5.5-beta | Cormier Solutions LLC | Standalone rendered forms for .NET Core and .NET Framework 4.8 hosts, returning… |
| 2026-11-16 07:03:13 | [ProofStudio.Plugins.Compression](https://www.nuget.org/packages/ProofStudio.Plugins.Compression) | 0.5.5-beta | Cormier Solutions LLC | Bounded GZIP compression for optional per-token Proof Studio remote transport. |
| 2026-11-16 07:03:16 | [ProofStudio.Plugins.Encryption](https://www.nuget.org/packages/ProofStudio.Plugins.Encryption) | 0.5.5-beta | Cormier Solutions LLC | Authenticated encryption for optional per-token Proof Studio remote transport. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

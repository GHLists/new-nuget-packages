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

## Latest list — 2026-10-18 10:21 UTC

New packages created between 2026-10-18 09:19 UTC and 2026-10-18 10:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-18T10-21-28-123748Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-18 09:25:16 | [Meshmakers.Octo.Services.Methods](https://www.nuget.org/packages/Meshmakers.Octo.Services.Methods) | 3.5.30 | meshmakers GmbH and Contribut… | CK method handler SDK: typed handlers on top of the OctoMesh CK method wire con… |
| 2026-10-18 09:51:09 | [Ruben2776.R3](https://www.nuget.org/packages/Ruben2776.R3) | 1.3.1 | Cysharp | The evolution of dotnet/reactive and UniRx. |
| 2026-10-18 09:55:51 | [AuthGuard.Sdk](https://www.nuget.org/packages/AuthGuard.Sdk) | 1.0.0 | AuthGuard | Client SDK for AuthGuard, a software licensing platform. Every server reply is… |
| 2026-10-18 10:11:39 | [a2n.Vista.Adapters.TanStackTable](https://www.nuget.org/packages/a2n.Vista.Adapters.TanStackTable) | 0.0.5 | Anwar Minarso | Vista adapter for TanStack Table (React, Vue, Solid). |
| 2026-10-18 10:12:43 | [Arc56.Generated.shashank6-alt.Vaarush](https://www.nuget.org/packages/Arc56.Generated.shashank6-alt.Vaarush) | 1.0.1.2026101810 | shashank6-alt | Generated ARC-56 Algorand smart-contract clients for shashank6-alt/Vaarush. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-08 08:21 UTC

New packages created between 2026-10-08 07:19 UTC and 2026-10-08 08:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-08T08-21-36-176423Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-08 07:21:15 | [Idearia.CommonDomain](https://www.nuget.org/packages/Idearia.CommonDomain) | 1.0.1 | Idearia Soluciones | Modelos compartidos entre las aplicaciones de Idearia. |
| 2026-10-08 07:40:32 | [Speckle.Bundle.Spec](https://www.nuget.org/packages/Speckle.Bundle.Spec) | 1.4.0 | Speckle | Speckle bundle format vocabulary: generated Rel/NodeKind enums, catalog rows, t… |
| 2026-10-08 07:52:04 | [Velsigil.Client](https://www.nuget.org/packages/Velsigil.Client) | 1.0.1 | Velsigil | Official .NET client for the Velsigil license server: online validation with Ed… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

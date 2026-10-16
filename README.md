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

## Latest list — 2026-10-16 13:20 UTC

New packages created between 2026-10-16 12:22 UTC and 2026-10-16 13:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-16T13-20-09-30912Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-16 12:24:17 | [DigitalWonderlab.Licensing](https://www.nuget.org/packages/DigitalWonderlab.Licensing) | 1.0.0 | Digital Wonderlab | Offline licence checking for Digital Wonderlab packages: verifies RSA-signed li… |
| 2026-10-16 12:24:45 | [Benevia.Core.Automation](https://www.nuget.org/packages/Benevia.Core.Automation) | 0.10.3 | Benevia Software | Triggers and subscribers: queue background work when business records change. |
| 2026-10-16 12:30:53 | [libfabric.win-x64](https://www.nuget.org/packages/libfabric.win-x64) | 2.6.13.107 | Intel Corporation | libfabric libfabric |
| 2026-10-16 12:32:03 | [libfabric.linux-x64](https://www.nuget.org/packages/libfabric.linux-x64) | 2.6.13.112 | Intel Corporation | libfabric libfabric |
| 2026-10-16 12:45:46 | [Coworkee.Workflows.Elsa.Studio](https://www.nuget.org/packages/Coworkee.Workflows.Elsa.Studio) | 0.0.1.28 | fgilde | Elsa Studio, the visual workflow designer, as an app of its own that signs in a… |
| 2026-10-16 12:45:58 | [Polhem.Api.Server](https://www.nuget.org/packages/Polhem.Api.Server) | 1.7.0 | Polhem contributors | The server side of the Polhem JSON-RPC API: the dispatcher setup, the access an… |
| 2026-10-16 12:46:13 | [Polhem.UI.ApiBridge](https://www.nuget.org/packages/Polhem.UI.ApiBridge) | 1.7.0 | Polhem contributors | Connects Polhem front ends to a Polhem backend: the client connection state and… |
| 2026-10-16 12:47:44 | [deppoc.linux-arm64](https://www.nuget.org/packages/deppoc.linux-arm64) | 0.0.1 | Roman Jámbor | Unsafe experimental tool. Do not use. |
| 2026-10-16 12:47:54 | [deppoc.linux-x64](https://www.nuget.org/packages/deppoc.linux-x64) | 0.0.1 | Roman Jámbor | Unsafe experimental tool. Do not use. |
| 2026-10-16 12:48:01 | [deppoc.osx-arm64](https://www.nuget.org/packages/deppoc.osx-arm64) | 0.0.1 | Roman Jámbor | Unsafe experimental tool. Do not use. |
| 2026-10-16 12:48:09 | [deppoc.osx-x64](https://www.nuget.org/packages/deppoc.osx-x64) | 0.0.1 | Roman Jámbor | Unsafe experimental tool. Do not use. |
| 2026-10-16 12:48:19 | [deppoc.win-arm64](https://www.nuget.org/packages/deppoc.win-arm64) | 0.0.1 | Roman Jámbor | Unsafe experimental tool. Do not use. |
| 2026-10-16 12:48:29 | [deppoc.win-x64](https://www.nuget.org/packages/deppoc.win-x64) | 0.0.1 | Roman Jámbor | Unsafe experimental tool. Do not use. |
| 2026-10-16 12:48:30 | [deppoc](https://www.nuget.org/packages/deppoc) | 0.0.1 | Roman Jámbor | Unsafe experimental tool. Do not use. |
| 2026-10-16 13:01:26 | [BoustrophedonDotnetWrapper](https://www.nuget.org/packages/BoustrophedonDotnetWrapper) | 0.1.3 | BoustrophedonDotnetWrapper | Cartesian coverage paths using the Boustrophedon C core. Linux x64. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

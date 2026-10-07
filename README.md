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

## Latest list — 2026-10-07 22:20 UTC

New packages created between 2026-10-07 21:20 UTC and 2026-10-07 22:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-07T22-20-48-12914Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-07 21:33:34 | [Cosmos.Kernel.Drivers](https://www.nuget.org/packages/Cosmos.Kernel.Drivers) | 3.0.90 | CosmosOS | The drivers Cosmos ships, written over the driver kit: the PCI host, the PCI Ex… |
| 2026-10-07 21:42:31 | [Cosmos.Network.Telnet](https://www.nuget.org/packages/Cosmos.Network.Telnet) | 1.0.0 | Cosmos | Telnet server for Cosmos Gen3 kernels: every client gets a console session and… |
| 2026-10-07 21:46:59 | [VungleSDKForWPF](https://www.nuget.org/packages/VungleSDKForWPF) | 7.1.2 | Liftoff,Inc. | To get up and running with Vungle, you'll need to create an account with Vungle… |
| 2026-10-07 21:57:11 | [Fantury.SimpleMediator](https://www.nuget.org/packages/Fantury.SimpleMediator) | 1.0.0 | Fantury Software | Simple mediator implementation in .NET, In-process messaging with no dependenci… |
| 2026-10-07 22:05:25 | [Lasagna](https://www.nuget.org/packages/Lasagna) | 0.0.1-beta | Lasagna contributors | Save and reuse individual files and file bundles in .NET projects. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

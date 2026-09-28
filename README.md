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

## Latest list — 2026-09-28 13:23 UTC

New packages created between 2026-09-28 12:21 UTC and 2026-09-28 13:23 UTC.

[Full CSV](data/new-nuget-packages-2026-09-28T13-23-15-113625Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-28 12:30:41 | [Arc56.Generated.mritnycodes.verithread](https://www.nuget.org/packages/Arc56.Generated.mritnycodes.verithread) | 1.0.1.2026092812 | mritnycodes | Generated ARC-56 Algorand smart-contract clients for mritnycodes/verithread. |
| 2026-09-28 12:37:41 | [WhatFYN](https://www.nuget.org/packages/WhatFYN) | 1.0.0 | George Paoli | ASP.NET Core output formatter that returns only the JSON fields the client asks… |
| 2026-09-28 12:43:04 | [TaefTestAdapter](https://www.nuget.org/packages/TaefTestAdapter) | 1.0.0 | Axel Rietschin Software Devel… | Enables Visual Studio's testing tools (Test Explorer, vstest.console.exe) with… |
| 2026-09-28 12:45:05 | [Tamp.Components](https://www.nuget.org/packages/Tamp.Components) | 1.17.0 | Scott Singleton | Reusable Tamp build components (ADR 0020): tool-agnostic target-shape interface… |
| 2026-09-28 12:45:06 | [Tamp.Components.NetCli.V10](https://www.nuget.org/packages/Tamp.Components.NetCli.V10) | 1.17.0 | Scott Singleton | Concrete dotnet SDK bodies for the Tamp.Components target shapes (ADR 0020): ID… |
| 2026-09-28 13:06:01 | [ICEPAY.Checkout](https://www.nuget.org/packages/ICEPAY.Checkout) | 1.0.0 | ICEPAY | Official .NET SDK for the ICEPAY Checkout API. |
| 2026-09-28 13:07:27 | [Universal.Microsoft.Foundry.Client](https://www.nuget.org/packages/Universal.Microsoft.Foundry.Client) | 1.0.0 | Andrew Ong | Standalone HTTP client for Microsoft Foundry project discovery and OpenAI, Anth… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

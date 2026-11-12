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

## Latest list — 2026-11-12 13:21 UTC

New packages created between 2026-11-12 12:21 UTC and 2026-11-12 13:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-12T13-21-57-517456Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-12 12:32:12 | [Ceejay.Connect](https://www.nuget.org/packages/Ceejay.Connect) | 0.1.0 | Community Studios | The CEEJAY Connect client for C# games: link a player to their Discord account,… |
| 2026-11-12 12:32:50 | [Ceejay](https://www.nuget.org/packages/Ceejay) | 0.1.0 | Community Studios | Call the CEEJAY API from your C# server, and verify the webhooks and shop deliv… |
| 2026-11-12 12:41:07 | [Vettvangur.AiChat](https://www.nuget.org/packages/Vettvangur.AiChat) | 1.0.0 | Vettvangur | Pluggable AI chat engine, streaming endpoint and conversation log for Umbraco s… |
| 2026-11-12 12:55:56 | [Umbraco.Community.GoatCounter](https://www.nuget.org/packages/Umbraco.Community.GoatCounter) | 0.0.1 | Andy Cross | GoatCounter analytics for Umbraco: a backoffice dashboard, a Views tab on every… |
| 2026-11-12 13:00:15 | [Dora.Shared.Security](https://www.nuget.org/packages/Dora.Shared.Security) | 1.0.4 | Hwx | Package Description |
| 2026-11-12 13:00:30 | [Dora.Shared.Hosting](https://www.nuget.org/packages/Dora.Shared.Hosting) | 1.0.4 | Hwx | Package Description |
| 2026-11-12 13:01:08 | [FlashCsv](https://www.nuget.org/packages/FlashCsv) | 1.0.0 | jetonpeche | Ultra high-performance, zero-allocation CSV parser, streamer, and serializer fo… |
| 2026-11-12 13:04:48 | [EAC.Plugin.EntraRegistration](https://www.nuget.org/packages/EAC.Plugin.EntraRegistration) | 0.1.0 | Eternet | Optional Microsoft Entra app registration and localhost redirect guidance for E… |
| 2026-11-12 13:14:49 | [Bitwarden.Server.Sdk.Service.Abstractions](https://www.nuget.org/packages/Bitwarden.Server.Sdk.Service.Abstractions) | 0.1.0 | Bitwarden Inc. | How a package configures every Bitwarden service that references it. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

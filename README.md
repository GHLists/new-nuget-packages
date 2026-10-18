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

## Latest list — 2026-10-18 02:21 UTC

New packages created between 2026-10-18 01:19 UTC and 2026-10-18 02:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-18T02-21-51-611303Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-18 01:28:51 | [Soenneker.Firmware.SeaPilot](https://www.nuget.org/packages/Soenneker.Firmware.SeaPilot) | 4.0.2 | Jake Soenneker | Seagate firmware discovery and downloads using OpenSeaChest and stealth browser… |
| 2026-10-18 01:29:18 | [Codyps.Zpl](https://www.nuget.org/packages/Codyps.Zpl) | 0.3.1 | Cody P Schafer | Local ZPL parsing and rendering to PNG, SVG, PDF and grayscale, powered by the… |
| 2026-10-18 01:32:29 | [DevWithMJ.QuickBooks.Mcp](https://www.nuget.org/packages/DevWithMJ.QuickBooks.Mcp) | 0.1.1 | quickbooks-mcp | MCP server for QuickBooks Desktop (Windows). Read-only by default. |
| 2026-10-18 01:58:15 | [PilotTestHost.Sdk](https://www.nuget.org/packages/PilotTestHost.Sdk) | 0.2.0 | mahach666 | Контракты и атрибуты для тестов, выполняющихся внутри клиента Pilot |
| 2026-10-18 01:58:17 | [PilotUITesting](https://www.nuget.org/packages/PilotUITesting) | 0.2.0 | mahach666 | Библиотека для сквозных UI-тестов модулей Pilot-ICE / Pilot-BIM: запуск клиента… |
| 2026-10-18 02:11:47 | [PgTtl](https://www.nuget.org/packages/PgTtl) | 0.1.0 | PgTtl contributors | Deletes expired rows from PostgreSQL tables with a ttl_expires_at timestamp col… |
| 2026-10-18 02:13:06 | [Mesa.Templates.Framework](https://www.nuget.org/packages/Mesa.Templates.Framework) | 1.0.0 | Rayscale | Project template for creating Mesa frameworks. |
| 2026-10-18 02:13:48 | [UnicoreSoftwareSolutions.ProjectTemplate.Web](https://www.nuget.org/packages/UnicoreSoftwareSolutions.ProjectTemplate.Web) | 1.0.0 | Unicore Software Solutions | A template for creating ASP.NET Core web applications. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

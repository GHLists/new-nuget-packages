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

## Latest list — 2026-11-01 01:19 UTC

New packages created between 2026-11-01 00:18 UTC and 2026-11-01 01:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-01T01-19-21-940884Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-01 00:43:55 | [Biz.Bizadm.S2Protocol.NET](https://www.nuget.org/packages/Biz.Bizadm.S2Protocol.NET) | 1.0.0 | SeongSikChae | Pure .NET port of Blizzard s2protocol: decode and encode StarCraft II replays (… |
| 2026-11-01 00:52:18 | [Platform.Maui.Web.Essentials](https://www.nuget.org/packages/Platform.Maui.Web.Essentials) | 0.1.0-alpha-0001 | aritchie,redth | MAUI Essentials for the browser: preferences, device info, connectivity, clipbo… |
| 2026-11-01 00:52:19 | [Platform.Maui.Web](https://www.nuget.org/packages/Platform.Maui.Web) | 0.1.0-alpha-0001 | aritchie,redth | A .NET MAUI backend for the browser. Runs MAUI apps on WebAssembly, rendering r… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

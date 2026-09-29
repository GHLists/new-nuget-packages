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

## Latest list — 2026-09-29 05:19 UTC

New packages created between 2026-09-29 04:19 UTC and 2026-09-29 05:19 UTC.

[Full CSV](data/new-nuget-packages-2026-09-29T05-19-12-971254Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-29 04:20:12 | [Syncfusion.Blazor.A2UI](https://www.nuget.org/packages/Syncfusion.Blazor.A2UI) | 35.1.37 | Syncfusion Inc. | Syncfusion® Blazor A2UI Library is a thin Blazor renderer for the A2UI v0.9 pro… |
| 2026-09-29 04:20:20 | [airtaxi.MonoGame.Framework.Compute.iOS](https://www.nuget.org/packages/airtaxi.MonoGame.Framework.Compute.iOS) | 3.8.3 | MonoGame Team | Unofficial iOS build of the MonoGame Compute fork runtime (cpt-max/MonoGame 3.8… |
| 2026-09-29 04:26:02 | [ZeroAudio.Core](https://www.nuget.org/packages/ZeroAudio.Core) | 1.1.0 | Phong Võ (kzxl) | Sovereign Pure C# Audio Engineering & DSP Engine for .NET: WAV/RIFF streaming,… |
| 2026-09-29 04:31:37 | [Netprof](https://www.nuget.org/packages/Netprof) | 0.1.0 | Alex Overstreet | .NET Instrumentation Library |
| 2026-09-29 04:37:20 | [GreenDox.Configurations.Api.Proxy](https://www.nuget.org/packages/GreenDox.Configurations.Api.Proxy) | 1.87.0 | Configurations.Api.Proxy | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

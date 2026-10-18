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

## Latest list — 2026-10-18 20:22 UTC

New packages created between 2026-10-18 19:18 UTC and 2026-10-18 20:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-18T20-22-59-19824Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-18 19:27:42 | [Novolis.Simulation.Logic](https://www.nuget.org/packages/Novolis.Simulation.Logic) | 2026.1.1.60 | Novolis | Deterministic, framework-neutral digital logic circuits for Novolis. |
| 2026-10-18 19:30:28 | [XUnitAssured.Jsonata](https://www.nuget.org/packages/XUnitAssured.Jsonata) | 6.36.0 | Carlos Andrew Costa Bezerra | JSONata expressions for XUnitAssured: select, transform and assert on the JSON… |
| 2026-10-18 19:36:49 | [LilyDesignSystem.Blazor.LocaleTranslations](https://www.nuget.org/packages/LilyDesignSystem.Blazor.LocaleTranslations) | 0.1.0 | Joel Parker Henderson | Lily Design System locale translations for Blazor: the 46 per-locale label pack… |
| 2026-10-18 19:37:09 | [Stormancer.Server.Plugins.Xsolla](https://www.nuget.org/packages/Stormancer.Server.Plugins.Xsolla) | 0.1.0.8-pre | Stormancer | Xsolla plugin for Stormancer server applications. |
| 2026-10-18 19:53:03 | [CodeBrix.Platform.PlayTest.WebGpu.ApacheLicenseForever](https://www.nuget.org/packages/CodeBrix.Platform.PlayTest.WebGpu.ApacheLicenseForever) | 1.0.291.1177 | Jeremy Ellis and contributors | Real WebGPU devices for PlayTest runs of applications that use the WebGpu add-i… |
| 2026-10-18 19:56:20 | [CodeBrix.Platform.WebGpu.ApacheLicenseForever](https://www.nuget.org/packages/CodeBrix.Platform.WebGpu.ApacheLicenseForever) | 1.0.291.1177 | Jeremy Ellis and contributors | Adds a WebGPU render view to your app: put a WebGpuRenderView in a page, handle… |
| 2026-10-18 20:02:56 | [DotnetCronner.AspNetCore](https://www.nuget.org/packages/DotnetCronner.AspNetCore) | 0.2.0 | Malte | ASP.NET Core integration for DotnetCronner: health checks reporting whether the… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

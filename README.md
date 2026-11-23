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

## Latest list — 2026-11-23 06:19 UTC

New packages created between 2026-11-23 05:19 UTC and 2026-11-23 06:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-23T06-19-21-788009Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-23 05:43:44 | [MyMathLibrary22](https://www.nuget.org/packages/MyMathLibrary22) | 1.0.0 | Manikanta | My mathematical operations library |
| 2026-11-23 05:44:19 | [Immons.Tools.AspNetCore.SessionReplay.Hangfire](https://www.nuget.org/packages/Immons.Tools.AspNetCore.SessionReplay.Hangfire) | 0.5.0 | Artur Malendowicz "Immons" | Hangfire filter for Immons.Tools.AspNetCore.SessionReplay: every failed attempt… |
| 2026-11-23 05:44:19 | [Immons.Tools.AspNetCore.SessionReplay](https://www.nuget.org/packages/Immons.Tools.AspNetCore.SessionReplay) | 0.5.0 | Artur Malendowicz "Immons" | Server-side SDK of the self-hosted Session Replay backend (Immons.Tools.Maui.Se… |
| 2026-11-23 05:47:15 | [Umbricians.FeatureFlags](https://www.nuget.org/packages/Umbricians.FeatureFlags) | 18.0.0 | Umbricians | Switch the site's feature flags on and off from the Umbraco backoffice, for eve… |
| 2026-11-23 05:51:03 | [Aid.Xlsx](https://www.nuget.org/packages/Aid.Xlsx) | 1.0.0 | Distaid | A .NET library for reading, creating, and editing Excel workbooks. |
| 2026-11-23 05:51:42 | [MelangeDB.Testing](https://www.nuget.org/packages/MelangeDB.Testing) | 0.4.0 | Tyler Loy | The reducer test kit: a real MelangeDB engine over a throwaway directory, drive… |
| 2026-11-23 05:51:43 | [MelangeDB.Mcp](https://www.nuget.org/packages/MelangeDB.Mcp) | 0.4.0 | Tyler Loy | Optional agent surface: a Model Context Protocol endpoint in the host's own pip… |
| 2026-11-23 05:55:48 | [RasterAlpha.Rgba32](https://www.nuget.org/packages/RasterAlpha.Rgba32) | 0.1.0 | js-upup | Convert packed RGBA8 buffers between straight and premultiplied alpha in place.… |
| 2026-11-23 06:01:20 | [DevExpress.AIIntegration.Agents.Workflows](https://www.nuget.org/packages/DevExpress.AIIntegration.Agents.Workflows) | 26.2.2-beta | Developer Express Inc. | Target Platform/Framework: Cross-Platform DevExpress Product Libraries Used: De… |
| 2026-11-23 06:01:59 | [DevExpress.Xpo.Services](https://www.nuget.org/packages/DevExpress.Xpo.Services) | 26.2.2-beta | Developer Express Inc. | Target Platform/Framework: Desktop, Web, Mobile DevExpress Product Libraries Us… |
| 2026-11-23 06:03:43 | [DevExpress.Printing.Remote](https://www.nuget.org/packages/DevExpress.Printing.Remote) | 26.2.2-beta | Developer Express Inc. | Target Platform/Framework: Cross-Platform DevExpress Product Libraries Used: Co… |
| 2026-11-23 06:07:53 | [DevExpress.AIIntegration.WinForms.Common](https://www.nuget.org/packages/DevExpress.AIIntegration.WinForms.Common) | 26.2.2-beta | Developer Express Inc. | Target Platform/Framework: Cross-Platform DevExpress Product Libraries Used: De… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

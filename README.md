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

## Latest list — 2026-11-08 21:20 UTC

New packages created between 2026-11-08 20:21 UTC and 2026-11-08 21:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-08T21-20-07-231265Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-08 20:27:56 | [SkiaGameRendering.Brutal.OGL](https://www.nuget.org/packages/SkiaGameRendering.Brutal.OGL) | 0.22.0 | SkiaGameRendering.Brutal.OGL | GPU SkiaSharp rendering into an OpenGL texture for BRUTAL apps (OpenGL 3.3+), w… |
| 2026-11-08 20:46:13 | [GM.FileStorage.Catalog.Scheduling](https://www.nuget.org/packages/GM.FileStorage.Catalog.Scheduling) | 4.3.0 | Giorgi Metskhvarishvili | Scheduled jobs for GM.FileStorage.Catalog on GM.Scheduling: delete the bytes qu… |
| 2026-11-08 20:47:59 | [UseAllBusiness.Ui.Controls](https://www.nuget.org/packages/UseAllBusiness.Ui.Controls) | 1.0.0 | Agostinho Marcos Garcia Silve… | Ui Controls Enterprise - Single package containing the entire ecosystem of UI C… |
| 2026-11-08 20:49:36 | [LanQueue](https://www.nuget.org/packages/LanQueue) | 0.2.0 | Jason Wood | Headless, capability-routed job runner for your own LAN machines: key-only SSH,… |
| 2026-11-08 21:02:52 | [E2E.Expo](https://www.nuget.org/packages/E2E.Expo) | 0.9.0 | hardkoded | Expo Simulators (hosted iOS and Android simulators) for the community .NET port… |
| 2026-11-08 21:02:53 | [E2E.GitHub](https://www.nuget.org/packages/E2E.GitHub) | 0.9.0 | hardkoded | GitHub pull request comment reporter for the community .NET port of the e2e age… |
| 2026-11-08 21:02:56 | [E2E.Acp](https://www.nuget.org/packages/E2E.Acp) | 0.9.0 | hardkoded | Runs agent steps on any coding agent that speaks the Agent Client Protocol, for… |
| 2026-11-08 21:02:58 | [E2E.BrowserStack](https://www.nuget.org/packages/E2E.BrowserStack) | 0.9.0 | hardkoded | BrowserStack App Automate real iOS and Android devices for the community .NET p… |
| 2026-11-08 21:04:43 | [NetEvolve.Pulse.AspNetCore.Grpc](https://www.nuget.org/packages/NetEvolve.Pulse.AspNetCore.Grpc) | 0.84.106 | NetEvolve, samtrion | ASP.NET Core gRPC integration for the Pulse CQRS mediator. Provides the PulseGr… |
| 2026-11-08 21:07:05 | [Kea.IpAudit.NetMQ](https://www.nuget.org/packages/Kea.IpAudit.NetMQ) | 1.0.2 | Solvation | Typed, schema-validated ZeroMQ lease event consumers for the Kea IP Audit hook. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

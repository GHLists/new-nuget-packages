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

## Latest list — 2026-10-02 14:19 UTC

New packages created between 2026-10-02 13:21 UTC and 2026-10-02 14:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-02T14-19-50-387219Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-02 13:21:59 | [CW.Assistant.Extensions.Docs](https://www.nuget.org/packages/CW.Assistant.Extensions.Docs) | 26.10.1 | CW | Versioned offline extension implementation documentation for coding agents and… |
| 2026-10-02 13:22:23 | [CW.Assistant.Extensions.Tekla.2025](https://www.nuget.org/packages/CW.Assistant.Extensions.Tekla.2025) | 26.10.1 | CW.Assistant.Extensions.Tekla | Package Description |
| 2026-10-02 13:22:40 | [DtoFlow.Integration](https://www.nuget.org/packages/DtoFlow.Integration) | 1.0.0 | DTO Flow | Integrate DTO Flow into your .NET application to upload and download partner fi… |
| 2026-10-02 13:26:55 | [FS.GG.Wasm.Browser](https://www.nuget.org/packages/FS.GG.Wasm.Browser) | 0.1.1 | FS.GG Contributors | Typed, Fable-compatible browser protocol and runtime for shared FS.GG WebAssemb… |
| 2026-10-02 13:26:55 | [FS.GG.Wasm.Contracts](https://www.nuget.org/packages/FS.GG.Wasm.Contracts) | 0.1.1 | FS.GG Contributors | Typed, Fable-compatible ABI profiles and validation contracts for shared FS.GG… |
| 2026-10-02 13:43:32 | [otsom.fs.OAuth.Keycloak](https://www.nuget.org/packages/otsom.fs.OAuth.Keycloak) | 0.1.1 | otsom.fs.OAuth.Keycloak | Package Description |
| 2026-10-02 13:51:36 | [VL.Installer.Inno](https://www.nuget.org/packages/VL.Installer.Inno) | 0.0.1-alpha | vvvv | Reference this pack to automatically create an installer on the export of the a… |
| 2026-10-02 13:53:01 | [PinguApps.Aspire.Hosting.RabbitMQ.Railway](https://www.nuget.org/packages/PinguApps.Aspire.Hosting.RabbitMQ.Railway) | 1.0.0 | PinguApps | Deploy standard Aspire RabbitMQ resources to Railway with private AMQP and auth… |
| 2026-10-02 13:54:35 | [SolutionExtender](https://www.nuget.org/packages/SolutionExtender) | 1.0.0 | SolutionExtender contributors | Capture versioned deployment metadata for PAC solutions and reconcile unmanaged… |
| 2026-10-02 13:55:17 | [SI.WA.UI.960](https://www.nuget.org/packages/SI.WA.UI.960) | 1.0.0 | seriiiastreb@gmail.com | "Retro" 960 theme for the WA.Core Blazor UI: the fluid 960 grid system (12 colu… |
| 2026-10-02 13:55:29 | [SI.WA.UI.Core](https://www.nuget.org/packages/SI.WA.UI.Core) | 1.0.0 | seriiiastreb@gmail.com | Theme-neutral core of the WA.Core Blazor UI: services (forms, views, charts, wo… |
| 2026-10-02 13:55:40 | [SI.WA.UI.Public](https://www.nuget.org/packages/SI.WA.UI.Public) | 1.0.0 | seriiiastreb@gmail.com | Public site for the WA.Core Blazor UI: the landing page signed-out visitors see… |
| 2026-10-02 13:55:51 | [SI.WA.UI.SB2](https://www.nuget.org/packages/SI.WA.UI.SB2) | 1.0.0 | seriiiastreb@gmail.com | SB Admin 2 theme for the WA.Core Blazor UI: the look of the original WA Angular… |
| 2026-10-02 13:56:02 | [SI.WA.UI.Sneat](https://www.nuget.org/packages/SI.WA.UI.Sneat) | 1.0.0 | seriiiastreb@gmail.com | Sneat (Bootstrap 5) theme for the WA.Core Blazor UI: the shared FViewer markup… |
| 2026-10-02 14:07:00 | [Sunsetless.Ews](https://www.nuget.org/packages/Sunsetless.Ews) | 1.0.0 | Sunsetless | Keep your EWS Managed API code and run it on Microsoft Graph. Commercial licens… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

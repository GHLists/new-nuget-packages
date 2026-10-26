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

## Latest list — 2026-10-26 13:22 UTC

New packages created between 2026-10-26 12:20 UTC and 2026-10-26 13:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-26T13-22-22-01229Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-26 12:23:28 | [Devolutions.Agent.Identity.Authority](https://www.nuget.org/packages/Devolutions.Agent.Identity.Authority) | 2026.10.26 | Devolutions Inc. | Agent-facing protocol rules shared by every Devolutions Agent Identity authority |
| 2026-10-26 12:27:00 | [ALKsPersonalUI](https://www.nuget.org/packages/ALKsPersonalUI) | 1.0.1 | Andreas Liepins Krusager | Custom tactile dark-mode UI library for Blazor: windows, 3D buttons, inputs, mo… |
| 2026-10-26 12:34:18 | [Indigina.Dcm.Packer.Client](https://www.nuget.org/packages/Indigina.Dcm.Packer.Client) | 1.0.0 | Indigina | Package contains client for Dcm.Packer service. |
| 2026-10-26 12:34:19 | [Indigina.Dcm.Packer.WebApi](https://www.nuget.org/packages/Indigina.Dcm.Packer.WebApi) | 1.0.0 | Indigina | Package contains web api for Dcm.Packer service. |
| 2026-10-26 12:40:12 | [CodeCrush.MeshCore.Core](https://www.nuget.org/packages/CodeCrush.MeshCore.Core) | 0.1.0 | Emmanuel Robles | Transport-agnostic MeshCore companion-protocol client: framing, channel message… |
| 2026-10-26 12:40:13 | [CodeCrush.MeshCore.Serial](https://www.nuget.org/packages/CodeCrush.MeshCore.Serial) | 0.1.0 | Emmanuel Robles | USB serial transport for CodeCrush.MeshCore.Core. |
| 2026-10-26 12:59:07 | [PlcSimulator.Lite](https://www.nuget.org/packages/PlcSimulator.Lite) | 2.2.10 | UseThink | PLC Simulator Lite - lightweight industrial protocol simulation engine for net4… |
| 2026-10-26 13:12:10 | [Tqsdk.net](https://www.nuget.org/packages/Tqsdk.net) | 1.0.0 | zhuoxiaoqiang | 天勤 TqSdk 的 C# 复刻。第一阶段：行情服务器通信（WebSocket + 认证 + 行情订阅）。 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

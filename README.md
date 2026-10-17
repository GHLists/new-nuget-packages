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

## Latest list — 2026-10-17 02:18 UTC

New packages created between 2026-10-17 01:19 UTC and 2026-10-17 02:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-17T02-18-56-785643Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-17 01:41:38 | [XiaQue.Sdk.QQBot](https://www.nuget.org/packages/XiaQue.Sdk.QQBot) | 0.1.1 | XiaQue | 面向 QQ 机器人官方接口和网关 WebSocket 协议的非官方 .NET 开发工具包，提供身份认证、接口调用和网关事件接收能力。 |
| 2026-10-17 01:43:42 | [XiaQue.Sdk.QQBot.Connector](https://www.nuget.org/packages/XiaQue.Sdk.QQBot.Connector) | 1.1.1 | XiaQue | 面向 QQ 机器人第三方智能体接入的非官方 .NET 扫码连接器，通过扫码绑定获取机器人应用凭据，可独立于主开发工具包使用。 |
| 2026-10-17 01:43:52 | [Moquestra.CaseConverter](https://www.nuget.org/packages/Moquestra.CaseConverter) | 1.0.0 | Moquestra | A string extension library for PascalCase, camelCase, and snake_case conversion. |
| 2026-10-17 01:50:11 | [CamusDB.OpenTelemetry](https://www.nuget.org/packages/CamusDB.OpenTelemetry) | 0.15.4 | CamusDB | CamusDB.OpenTelemetry registers the CamusDB.Client activity source and meter wi… |
| 2026-10-17 01:58:58 | [Fuxion.Tool](https://www.nuget.org/packages/Fuxion.Tool) | 0.7.2 | Oscar Jimenez | fx, the tool of the Fuxion workspace: its repositories, the shared build of .NE… |
| 2026-10-17 01:59:40 | [OvoUi.Tab](https://www.nuget.org/packages/OvoUi.Tab) | 1.0.2 | tiouo | Animated, detachable tab hosts and tab windows for Avalonia applications. |
| 2026-10-17 01:59:41 | [OvoUi.SmoothScroll](https://www.nuget.org/packages/OvoUi.SmoothScroll) | 1.0.2 | tiouo | Smooth scrolling, panning, multi-touch zoom, elastic overscroll and composition… |
| 2026-10-17 02:01:54 | [Meziantou.Framework.SnapshotTesting.Imaging](https://www.nuget.org/packages/Meziantou.Framework.SnapshotTesting.Imaging) | 1.0.0 | meziantou | Enables verification of images using file-based snapshots, based on Meziantou.F… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

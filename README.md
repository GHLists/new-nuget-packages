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

## Latest list — 2026-11-25 14:21 UTC

New packages created between 2026-11-25 13:21 UTC and 2026-11-25 14:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-25T14-21-43-13273Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-25 13:24:36 | [Beesharp.Cli](https://www.nuget.org/packages/Beesharp.Cli) | 0.2.9 | detachmode | Command-line tool (beesharp) for running load-test presets headlessly and inspe… |
| 2026-11-25 13:47:12 | [JiksLib](https://www.nuget.org/packages/JiksLib) | 2.0.0 | 许兴逸 Seng Jik | 综合杂项工具库。 |
| 2026-11-25 13:55:24 | [Byterelic.Core](https://www.nuget.org/packages/Byterelic.Core) | 0.1.0 | coppr.tech | An embeddable content-addressable Blob store for .NET: it stores each Blob unde… |
| 2026-11-25 13:55:25 | [Byterelic.Integrations.S3](https://www.nuget.org/packages/Byterelic.Integrations.S3) | 0.1.0 | coppr.tech | The Byterelic Backend for S3-compatible storage. |
| 2026-11-25 13:57:33 | [LuminaUI.Markdown](https://www.nuget.org/packages/LuminaUI.Markdown) | 0.7.0 | LuminaUI Contributors | Lumina-themed Markdown document renderer for Avalonia and LuminaUI. |
| 2026-11-25 14:00:18 | [Bsa.MediaKit](https://www.nuget.org/packages/Bsa.MediaKit) | 1.0.0 | Bsa | Media toolkit in pure C#: probe media files, extract audio, prepare 16 kHz mono… |
| 2026-11-25 14:08:02 | [OpenRobot.Edge.Event.Client](https://www.nuget.org/packages/OpenRobot.Edge.Event.Client) | 0.1.0 | OpenRobot | Edge 事件订阅客户端：通过 IPC 订阅业务事件、执行回调并回报 ACK；不依赖 AppSdk。 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

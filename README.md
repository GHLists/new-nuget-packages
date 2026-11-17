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

## Latest list — 2026-11-17 15:20 UTC

New packages created between 2026-11-17 14:19 UTC and 2026-11-17 15:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-17T15-20-22-717051Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-17 14:26:46 | [VL.Polynesia](https://www.nuget.org/packages/VL.Polynesia) | 0.36.244-preview | Polynesia | Integrated Polynesia rendering and Tide simulation nodes for vvvv gamma. Window… |
| 2026-11-17 14:28:16 | [MailPier.Cli](https://www.nuget.org/packages/MailPier.Cli) | 0.1.0 | Solutions Group Unlimited LLC | The mailpier command: forward the webhooks your MailPier Inbox environment catc… |
| 2026-11-17 14:31:59 | [Nanosandbox.Sdk](https://www.nuget.org/packages/Nanosandbox.Sdk) | 0.2.0 | DevDone Labs | BCL-only .NET protocol client for the nanosandbox helper (nanosb-protocol v1.0.… |
| 2026-11-17 14:32:09 | [Wick.Core](https://www.nuget.org/packages/Wick.Core) | 1.0.0 | ivanjx | Fine-grained reactive state for .NET: tracked properties, collections, derived… |
| 2026-11-17 14:32:10 | [Wick.Blazor](https://www.nuget.org/packages/Wick.Blazor) | 1.0.0 | ivanjx | Blazor components that re-render only when the Wick reactive state they read ch… |
| 2026-11-17 14:35:22 | [Umbraco.Community.SuperValueConverters](https://www.nuget.org/packages/Umbraco.Community.SuperValueConverters) | 5.0.0 | Callum Whyte | A collection of powerful property value converters for cleaner code in Umbraco |
| 2026-11-17 14:45:18 | [Gurux.MQTT.Avalonia](https://www.nuget.org/packages/Gurux.MQTT.Avalonia) | 9.0.2611.1701 | Gurux Ltd | Avalonia settings editor for Gurux MQTT media. |
| 2026-11-17 14:45:35 | [Gurux.MQTT.Blazor](https://www.nuget.org/packages/Gurux.MQTT.Blazor) | 9.0.2611.1701 | Gurux Ltd | Optional Blazor settings components for Gurux media libraries. |
| 2026-11-17 14:45:52 | [Gurux.MQTT.Maui](https://www.nuget.org/packages/Gurux.MQTT.Maui) | 9.0.2611.1701 | Gurux Ltd | Native MAUI settings editor for Gurux MQTT media. |
| 2026-11-17 14:46:20 | [FileManagerNet](https://www.nuget.org/packages/FileManagerNet) | 1.0.0 | FileManagerNet Contributors | A free, open-source (MIT) Windows-Explorer-style file manager control for ASP.N… |
| 2026-11-17 15:01:55 | [AshGodfrey.NugetTrustedPublishingSample](https://www.nuget.org/packages/AshGodfrey.NugetTrustedPublishingSample) | 0.0.1 | Speakeasy | Pet Store Sample: Sample API used to exercise NuGet trusted publishing from Git… |
| 2026-11-17 15:10:48 | [MetadataSharp](https://www.nuget.org/packages/MetadataSharp) | 1.0.0 | SeNS | Reads image metadata (EXIF with MakerNotes, IPTC, XMP, ICC profiles, comments,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

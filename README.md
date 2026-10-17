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

## Latest list — 2026-10-17 05:20 UTC

New packages created between 2026-10-17 04:18 UTC and 2026-10-17 05:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-17T05-20-11-408066Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-17 04:30:57 | [Grantry.Sdk](https://www.nuget.org/packages/Grantry.Sdk) | 0.1.0 | Grantry | Identity, access and entitlements for .NET desktop applications: sign-in, verif… |
| 2026-10-17 04:53:53 | [Xemele.Tool.linux-x64](https://www.nuget.org/packages/Xemele.Tool.linux-x64) | 0.1.0 | Xemele contributors | Managed net10.0 XML and HTML toolkit with streaming, XPath, validation and cont… |
| 2026-10-17 04:53:54 | [Xemele.Tool.osx-arm64](https://www.nuget.org/packages/Xemele.Tool.osx-arm64) | 0.1.0 | Xemele contributors | Managed net10.0 XML and HTML toolkit with streaming, XPath, validation and cont… |
| 2026-10-17 04:53:55 | [Xemele.Tool.win-x64](https://www.nuget.org/packages/Xemele.Tool.win-x64) | 0.1.0 | Xemele contributors | Managed net10.0 XML and HTML toolkit with streaming, XPath, validation and cont… |
| 2026-10-17 04:53:56 | [Xemele.Tool.any](https://www.nuget.org/packages/Xemele.Tool.any) | 0.1.0 | Xemele contributors | Managed net10.0 XML and HTML toolkit with streaming, XPath, validation and cont… |
| 2026-10-17 04:53:57 | [Xemele](https://www.nuget.org/packages/Xemele) | 0.1.0 | Xemele contributors | Managed net10.0 XML and HTML toolkit with streaming, XPath, validation and cont… |
| 2026-10-17 04:53:58 | [Xemele.Tool](https://www.nuget.org/packages/Xemele.Tool) | 0.1.0 | Xemele contributors | Managed net10.0 XML and HTML toolkit with streaming, XPath, validation and cont… |
| 2026-10-17 05:01:25 | [GregsEx](https://www.nuget.org/packages/GregsEx) | 0.1.0 | Sébastien Ros | Bounded RegularCore-1-experimental, ECMAScript2025, XSD 1.1 (2012-04-05 Appendi… |
| 2026-10-17 05:04:04 | [DesktopHost.Files](https://www.nuget.org/packages/DesktopHost.Files) | 0.1.0 | iyulab | Durable file writes for a local .NET host: atomic replace that a shared reader… |
| 2026-10-17 05:12:18 | [CodeBridge.Abstractions](https://www.nuget.org/packages/CodeBridge.Abstractions) | 0.6.0 | Christian Alexander Albarraci… | Core abstractions and protocol contracts for CodeBridge microcontroller integra… |
| 2026-10-17 05:12:20 | [CodeBridge.Blazor](https://www.nuget.org/packages/CodeBridge.Blazor) | 0.6.0 | Christian Alexander Albarraci… | Blazor components for CodeBridge boards: live status, pin toggles, analog gauge… |
| 2026-10-17 05:12:21 | [CodeBridge.Designer.WinForms](https://www.nuget.org/packages/CodeBridge.Designer.WinForms) | 0.6.0 | Christian Alexander Albarraci… | Native WinForms Toolbox controls and visual designer for CodeBridge flows. |
| 2026-10-17 05:12:23 | [CodeBridge.ESP32](https://www.nuget.org/packages/CodeBridge.ESP32) | 0.6.0 | Christian Alexander Albarraci… | ESP32 board implementation for CodeBridge using Serial or WiFi transports. |
| 2026-10-17 05:12:24 | [CodeBridge.Flow](https://www.nuget.org/packages/CodeBridge.Flow) | 0.6.0 | Christian Alexander Albarraci… | Visual flow document model, block catalog, validation, presets, and runtime for… |
| 2026-10-17 05:12:25 | [CodeBridge.HomeAssistant](https://www.nuget.org/packages/CodeBridge.HomeAssistant) | 0.6.0 | Christian Alexander Albarraci… | Home Assistant integration for CodeBridge boards: MQTT discovery, switches, lig… |
| 2026-10-17 05:12:26 | [CodeBridge.Hosting](https://www.nuget.org/packages/CodeBridge.Hosting) | 0.6.0 | Christian Alexander Albarraci… | Dependency-injection friendly CodeBridge board service for ASP.NET Core, Blazor… |
| 2026-10-17 05:12:28 | [CodeBridge.Mcp](https://www.nuget.org/packages/CodeBridge.Mcp) | 0.6.0 | Christian Alexander Albarraci… | MCP server for CodeBridge: lets an AI assistant learn a board (pins, capabiliti… |
| 2026-10-17 05:12:29 | [CodeBridge.PlatformIO](https://www.nuget.org/packages/CodeBridge.PlatformIO) | 0.6.0 | Christian Alexander Albarraci… | Code mode for CodeBridge boards: creates, builds and uploads PlatformIO firmwar… |
| 2026-10-17 05:12:30 | [CodeBridge.Transport](https://www.nuget.org/packages/CodeBridge.Transport) | 0.6.0 | Christian Alexander Albarraci… | Serial and network transport implementations for CodeBridge boards. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

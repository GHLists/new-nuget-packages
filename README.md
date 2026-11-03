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

## Latest list — 2026-11-03 03:19 UTC

New packages created between 2026-11-03 02:20 UTC and 2026-11-03 03:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-03T03-19-05-307753Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-03 02:29:40 | [SocketJack.Unity](https://www.nuget.org/packages/SocketJack.Unity) | 2026.11.2.2 | hheiroww | Authoritative multiplayer networking for Unity and dedicated .NET servers. Boun… |
| 2026-11-03 02:30:33 | [Hikari.ImGui](https://www.nuget.org/packages/Hikari.ImGui) | 1.93.0 | Least Action Technologies Inc… | Pure C# re-implementation of Dear ImGui v1.93.0-docking with zero native depend… |
| 2026-11-03 02:31:08 | [CodeWF.Avalonia.Motion](https://www.nuget.org/packages/CodeWF.Avalonia.Motion) | 12.2.48.1 | 沙漠尽头的狼 | Avalonia 动效引擎：弹簧物理（闭式解、可中断保速）、声明式弹簧过渡、动效分级（Full/Reduced/Off）与常驻循环。移植自 TKCode.Ar… |
| 2026-11-03 02:35:34 | [TerribleSettingsAuditor](https://www.nuget.org/packages/TerribleSettingsAuditor) | 1.0.24 | TerribleSettingsAuditor | Package Description |
| 2026-11-03 02:37:57 | [CoreOne.Http](https://www.nuget.org/packages/CoreOne.Http) | 1.0.0 | Juan Lopez | Package Description |
| 2026-11-03 02:49:12 | [Helpers.ApolloHelper](https://www.nuget.org/packages/Helpers.ApolloHelper) | 1.0.0 | ljy | Apollo配置中心帮助类 |
| 2026-11-03 03:03:28 | [vaishali-jain.ClimateTool](https://www.nuget.org/packages/vaishali-jain.ClimateTool) | 1.0.0 | mcpserverapp1 | An MCP server using the MCP C# SDK. |
| 2026-11-03 03:03:51 | [vaishali-jain.ClimateTool.linux-arm64](https://www.nuget.org/packages/vaishali-jain.ClimateTool.linux-arm64) | 1.0.0 | mcpserverapp1 | An MCP server using the MCP C# SDK. |
| 2026-11-03 03:04:08 | [vaishali-jain.ClimateTool.linux-musl-x64](https://www.nuget.org/packages/vaishali-jain.ClimateTool.linux-musl-x64) | 1.0.0 | mcpserverapp1 | An MCP server using the MCP C# SDK. |
| 2026-11-03 03:04:28 | [vaishali-jain.ClimateTool.osx-arm64](https://www.nuget.org/packages/vaishali-jain.ClimateTool.osx-arm64) | 1.0.0 | mcpserverapp1 | An MCP server using the MCP C# SDK. |
| 2026-11-03 03:04:41 | [vaishali-jain.ClimateTool.win-x64](https://www.nuget.org/packages/vaishali-jain.ClimateTool.win-x64) | 1.0.0 | mcpserverapp1 | An MCP server using the MCP C# SDK. |
| 2026-11-03 03:04:53 | [vaishali-jain.ClimateTool.linux-x64](https://www.nuget.org/packages/vaishali-jain.ClimateTool.linux-x64) | 1.0.0 | mcpserverapp1 | An MCP server using the MCP C# SDK. |
| 2026-11-03 03:05:07 | [vaishali-jain.ClimateTool.win-arm64](https://www.nuget.org/packages/vaishali-jain.ClimateTool.win-arm64) | 1.0.0 | mcpserverapp1 | An MCP server using the MCP C# SDK. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

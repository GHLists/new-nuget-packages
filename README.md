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

## Latest list — 2026-11-13 12:19 UTC

New packages created between 2026-11-13 11:21 UTC and 2026-11-13 12:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-13T12-19-57-870677Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-13 11:33:11 | [FileBasedApp.Toolkit.Spectre](https://www.nuget.org/packages/FileBasedApp.Toolkit.Spectre) | 1.4.0 | FileBasedApp.Toolkit.Spectre | Spectre.Console output factories and Spectre.Console.Cli settings helpers for f… |
| 2026-11-13 11:33:13 | [FileBasedApp.Toolkit.SimpleExec](https://www.nuget.org/packages/FileBasedApp.Toolkit.SimpleExec) | 1.4.0 | FileBasedApp.Toolkit.SimpleEx… | Fluent command runners and testable SimpleExec wrappers for file-based apps. |
| 2026-11-13 11:45:21 | [Credfeto.ChangeLog.Mcp](https://www.nuget.org/packages/Credfeto.ChangeLog.Mcp) | 1.10.214.2878-chang… | Mark Ridgwell | Changelog manager MCP server dotnet tool. |
| 2026-11-13 11:45:21 | [Credfeto.ChangeLog.Mcp.linux-arm64](https://www.nuget.org/packages/Credfeto.ChangeLog.Mcp.linux-arm64) | 1.10.214.2878-chang… | Mark Ridgwell | Changelog manager MCP server dotnet tool. |
| 2026-11-13 11:45:21 | [Credfeto.ChangeLog.Mcp.osx-x64](https://www.nuget.org/packages/Credfeto.ChangeLog.Mcp.osx-x64) | 1.10.214.2878-chang… | Mark Ridgwell | Changelog manager MCP server dotnet tool. |
| 2026-11-13 11:45:21 | [Credfeto.ChangeLog.Mcp.linux-x64](https://www.nuget.org/packages/Credfeto.ChangeLog.Mcp.linux-x64) | 1.10.214.2878-chang… | Mark Ridgwell | Changelog manager MCP server dotnet tool. |
| 2026-11-13 11:45:21 | [Credfeto.ChangeLog.Mcp.osx-arm64](https://www.nuget.org/packages/Credfeto.ChangeLog.Mcp.osx-arm64) | 1.10.214.2878-chang… | Mark Ridgwell | Changelog manager MCP server dotnet tool. |
| 2026-11-13 11:45:21 | [Credfeto.ChangeLog.Mcp.win-arm64](https://www.nuget.org/packages/Credfeto.ChangeLog.Mcp.win-arm64) | 1.10.214.2878-chang… | Mark Ridgwell | Changelog manager MCP server dotnet tool. |
| 2026-11-13 11:45:22 | [Credfeto.ChangeLog.Mcp.win-x64](https://www.nuget.org/packages/Credfeto.ChangeLog.Mcp.win-x64) | 1.10.214.2878-chang… | Mark Ridgwell | Changelog manager MCP server dotnet tool. |
| 2026-11-13 11:58:03 | [E2E.TUnit](https://www.nuget.org/packages/E2E.TUnit) | 0.11.0 | hardkoded | TUnit fixture for the E2E .NET port. Each test gets an engine session, and the… |
| 2026-11-13 11:58:05 | [E2E.Mobile.TUnit](https://www.nuget.org/packages/E2E.Mobile.TUnit) | 0.11.0 | hardkoded | MobileAppTest for the E2E .NET port: a ready base class that installs the app,… |
| 2026-11-13 11:58:17 | [E2E.WinApp.TUnit](https://www.nuget.org/packages/E2E.WinApp.TUnit) | 0.11.0 | hardkoded | WinAppTest for the E2E .NET port: a ready base class that launches a Windows de… |
| 2026-11-13 12:07:37 | [LanguageExtended](https://www.nuget.org/packages/LanguageExtended) | 2.3.1 | Jonas Schlag | Package Description |
| 2026-11-13 12:11:11 | [MechaOnion.Tool](https://www.nuget.org/packages/MechaOnion.Tool) | 0.1.0 | MechaOnion | CLI .NET global tool para gerar projetos e módulos MechaOnion com host ASP.NET… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

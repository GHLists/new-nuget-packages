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

## Latest list — 2026-10-27 21:21 UTC

New packages created between 2026-10-27 20:20 UTC and 2026-10-27 21:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-27T21-21-35-51672Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-27 20:32:37 | [Enigma.Avalonia.Mobile](https://www.nuget.org/packages/Enigma.Avalonia.Mobile) | 1.3.0 | Josué Clément | Enigma.Avalonia.Mobile gives Avalonia 12 mobile applications, Android first and… |
| 2026-10-27 20:37:08 | [MaksIT.IdentityHub.Contracts](https://www.nuget.org/packages/MaksIT.IdentityHub.Contracts) | 3.0.0 | MaksIT | Shared API contracts (DTOs) for MaksIT Identity Hub API and client. |
| 2026-10-27 20:37:40 | [KDPika.LicenseSdk](https://www.nuget.org/packages/KDPika.LicenseSdk) | 2.1.0 | KDPika | KDPika Licensing client with signed device binding, floating leases and usage c… |
| 2026-10-27 20:51:33 | [Hexalith.Timesheets.ReadModels](https://www.nuget.org/packages/Hexalith.Timesheets.ReadModels) | 2.0.2 | Hexalith Contributors | Shared Timesheets read-model helpers and persisted EventStore payloads. |
| 2026-10-27 20:59:52 | [PackageCascade](https://www.nuget.org/packages/PackageCascade) | 0.1.0 | GoSim | Plan releases for solutions containing packable .NET projects. |
| 2026-10-27 21:01:31 | [Driftcheck](https://www.nuget.org/packages/Driftcheck) | 0.1.0 | Wilson Vargas Marín | Local MCP server that compares a mobile app screen (Android or iOS Simulator) w… |
| 2026-10-27 21:03:24 | [Snail.MCP.Figma.any](https://www.nuget.org/packages/Snail.MCP.Figma.any) | 0.2.0 | orldev | Local MCP server that gives AI agents 141 tools for reading and editing Figma.… |
| 2026-10-27 21:03:26 | [Snail.MCP.Figma.linux-arm64](https://www.nuget.org/packages/Snail.MCP.Figma.linux-arm64) | 0.2.0 | orldev | Local MCP server that gives AI agents 141 tools for reading and editing Figma.… |
| 2026-10-27 21:03:27 | [Snail.MCP.Figma.linux-x64](https://www.nuget.org/packages/Snail.MCP.Figma.linux-x64) | 0.2.0 | orldev | Local MCP server that gives AI agents 141 tools for reading and editing Figma.… |
| 2026-10-27 21:03:31 | [Snail.MCP.Figma.win-x64](https://www.nuget.org/packages/Snail.MCP.Figma.win-x64) | 0.2.0 | orldev | Local MCP server that gives AI agents 141 tools for reading and editing Figma.… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-18 08:19 UTC

New packages created between 2026-10-18 07:19 UTC and 2026-10-18 08:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-18T08-19-25-202286Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-18 07:31:35 | [Eternet.Agents.Control.Cli.any](https://www.nuget.org/packages/Eternet.Agents.Control.Cli.any) | 3.0.2 | Eternet | Local deterministic agent harness CLI for Eternet mediator diagnostics and reme… |
| 2026-10-18 07:32:05 | [Eternet.Agents.Control.Cli.linux-arm64](https://www.nuget.org/packages/Eternet.Agents.Control.Cli.linux-arm64) | 3.0.2 | Eternet | Local deterministic agent harness CLI for Eternet mediator diagnostics and reme… |
| 2026-10-18 07:32:41 | [Eternet.Agents.Control.Cli.linux-musl-arm64](https://www.nuget.org/packages/Eternet.Agents.Control.Cli.linux-musl-arm64) | 3.0.2 | Eternet | Local deterministic agent harness CLI for Eternet mediator diagnostics and reme… |
| 2026-10-18 07:33:08 | [Eternet.Agents.Control.Cli.linux-musl-x64](https://www.nuget.org/packages/Eternet.Agents.Control.Cli.linux-musl-x64) | 3.0.2 | Eternet | Local deterministic agent harness CLI for Eternet mediator diagnostics and reme… |
| 2026-10-18 07:33:33 | [InertiaCore.TypeGen](https://www.nuget.org/packages/InertiaCore.TypeGen) | 0.3.0 | Creator-Solutions | Generates TypeScript declarations for InertiaCore [InertiaPage] props. |
| 2026-10-18 07:33:37 | [Eternet.Agents.Control.Cli.linux-x64](https://www.nuget.org/packages/Eternet.Agents.Control.Cli.linux-x64) | 3.0.2 | Eternet | Local deterministic agent harness CLI for Eternet mediator diagnostics and reme… |
| 2026-10-18 07:33:48 | [Eternet.Agents.Control.Cli.osx-arm64](https://www.nuget.org/packages/Eternet.Agents.Control.Cli.osx-arm64) | 3.0.2 | Eternet | Local deterministic agent harness CLI for Eternet mediator diagnostics and reme… |
| 2026-10-18 07:34:14 | [Eternet.Agents.Control.Cli.win-arm64](https://www.nuget.org/packages/Eternet.Agents.Control.Cli.win-arm64) | 3.0.2 | Eternet | Local deterministic agent harness CLI for Eternet mediator diagnostics and reme… |
| 2026-10-18 07:35:07 | [Eternet.Agents.Control.Cli.win-x64](https://www.nuget.org/packages/Eternet.Agents.Control.Cli.win-x64) | 3.0.2 | Eternet | Local deterministic agent harness CLI for Eternet mediator diagnostics and reme… |
| 2026-10-18 07:37:14 | [Lagun271.RobotStudio.PcSdk.Ref](https://www.nuget.org/packages/Lagun271.RobotStudio.PcSdk.Ref) | 26.3.11794 | Lagun271 | Compile-time reference assemblies for the ABB PC SDK (ABB.Robotics.Controllers.… |
| 2026-10-18 07:37:16 | [Lagun271.RobotStudio.RspakTool](https://www.nuget.org/packages/Lagun271.RobotStudio.RspakTool) | 26.3.11794 | Lagun271 | RobotStudio distribution package tool (RspakTool.exe) from the ABB RobotStudio… |
| 2026-10-18 07:37:23 | [Lagun271.RobotStudio.Sdk.Ref](https://www.nuget.org/packages/Lagun271.RobotStudio.Sdk.Ref) | 26.3.11794 | Lagun271 | Compile-time reference assemblies from the ABB RobotStudio SDK (ABB.Robotics.Ro… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-26 00:21 UTC

New packages created between 2026-10-25 23:22 UTC and 2026-10-26 00:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-26T00-21-25-43395Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-25 23:31:17 | [LibTmux.Workspace.Cli](https://www.nuget.org/packages/LibTmux.Workspace.Cli) | 0.1.0 | Tony Narlock | A native tmux workspace manager with tmuxp-compatible commands. |
| 2026-10-25 23:31:17 | [LibTmux.FSharp](https://www.nuget.org/packages/LibTmux.FSharp) | 0.1.0 | Tony Narlock | F# task functions and pure snapshot queries over LibTmux handles. |
| 2026-10-25 23:31:18 | [LibTmux.Testing](https://www.nuget.org/packages/LibTmux.Testing) | 0.1.0 | Tony Narlock | Scoped tmux servers, sessions and windows that clean themselves up, for testing… |
| 2026-10-25 23:31:18 | [LibTmux](https://www.nuget.org/packages/LibTmux) | 0.1.0 | Tony Narlock | A typed, async-first client for the tmux terminal multiplexer. Drive servers, s… |
| 2026-10-25 23:31:19 | [LibTmux.Mcp](https://www.nuget.org/packages/LibTmux.Mcp) | 0.1.0 | Tony Narlock | A Model Context Protocol server that lets an assistant drive tmux through LibTm… |
| 2026-10-25 23:31:19 | [LibTmux.Extensions.DependencyInjection](https://www.nuget.org/packages/LibTmux.Extensions.DependencyInjection) | 0.1.0 | Tony Narlock | Registers a LibTmux server handle and its options with Microsoft.Extensions.Dep… |
| 2026-10-25 23:31:20 | [LibTmux.Workspace](https://www.nuget.org/packages/LibTmux.Workspace) | 0.1.0 | Tony Narlock | Builds tmux sessions from tmuxp workspace files, on top of LibTmux. |
| 2026-10-25 23:31:20 | [LibTmux.Query.Json](https://www.nuget.org/packages/LibTmux.Query.Json) | 0.1.0 | Tony Narlock | System.Text.Json support for LibTmux query documents. The core library does not… |
| 2026-10-25 23:44:31 | [Morph.Wopi](https://www.nuget.org/packages/Morph.Wopi) | 1.23.0 | https://github.com/Papyrine/M… | Morph's editor as a WOPI client for ASP.NET Core: the discovery a WOPI host rea… |
| 2026-10-26 00:13:34 | [Snail.Toolkit.RabbitMQ.Workflow](https://www.nuget.org/packages/Snail.Toolkit.RabbitMQ.Workflow) | 0.1.0 | orldev | Step-by-step workflows over RabbitMQ queues on top of Snail.Toolkit.RabbitMQ: a… |
| 2026-10-26 00:16:14 | [LVGL.Net.Templates](https://www.nuget.org/packages/LVGL.Net.Templates) | 0.2.0 | Kang Fadhil (Gravicode Studio… | dotnet new templates for LVGL.Net: an LVGL application that runs in a desktop w… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-05 08:20 UTC

New packages created between 2026-10-05 07:19 UTC and 2026-10-05 08:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-05T08-20-03-559648Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-05 07:20:16 | [OptiCli.Mcp](https://www.nuget.org/packages/OptiCli.Mcp) | 0.9.0-preview | opticli contributors | Preview. An MCP server for Optimizely CMS 12: editors connect Claude to the sit… |
| 2026-10-05 07:22:17 | [GenHTTP.Modules.Git](https://www.nuget.org/packages/GenHTTP.Modules.Git) | 0.1.0 | Andreas Nägeli | Serves virtual git repositories over smart HTTP from a GenHTTP handler. Clones,… |
| 2026-10-05 07:26:03 | [TedToolkit.CppBindings.Occt.Windows](https://www.nuget.org/packages/TedToolkit.CppBindings.Occt.Windows) | 2026.10.5 | TedToolkit | Generated OCCT bindings for the pinned Windows x64 native artifact. |
| 2026-10-05 07:34:56 | [DKNet.Aspire.Hosting.WebsiteHook](https://www.nuget.org/packages/DKNet.Aspire.Hosting.WebsiteHook) | 0.1.0 | drunkcoding.net | .NET Aspire hosting integration for the website-hook API and its optional UI. |
| 2026-10-05 07:39:34 | [WinForms.Markdown](https://www.nuget.org/packages/WinForms.Markdown) | 1.0.0 | Winner-Timothy Bolorunduro | A native, lightweight Markdown control for Windows Forms that renders Markdown… |
| 2026-10-05 07:45:32 | [CodeAlta.Tui](https://www.nuget.org/packages/CodeAlta.Tui) | 1.0.0 | Alexandre Mutel | CodeAlta TUI: a keyboard-first terminal UI for agentic AI coding on your local… |
| 2026-10-05 07:45:33 | [CodeAlta.Tui.linux-x64](https://www.nuget.org/packages/CodeAlta.Tui.linux-x64) | 1.0.0 | Alexandre Mutel | CodeAlta TUI: a keyboard-first terminal UI for agentic AI coding on your local… |
| 2026-10-05 07:45:35 | [CodeAlta.Tui.linux-arm64](https://www.nuget.org/packages/CodeAlta.Tui.linux-arm64) | 1.0.0 | Alexandre Mutel | CodeAlta TUI: a keyboard-first terminal UI for agentic AI coding on your local… |
| 2026-10-05 07:45:37 | [CodeAlta.Tui.win-x64](https://www.nuget.org/packages/CodeAlta.Tui.win-x64) | 1.0.0 | Alexandre Mutel | CodeAlta TUI: a keyboard-first terminal UI for agentic AI coding on your local… |
| 2026-10-05 07:45:40 | [CodeAlta.Tui.win-arm64](https://www.nuget.org/packages/CodeAlta.Tui.win-arm64) | 1.0.0 | Alexandre Mutel | CodeAlta TUI: a keyboard-first terminal UI for agentic AI coding on your local… |
| 2026-10-05 07:45:41 | [CodeAlta.Tui.linux-musl-x64](https://www.nuget.org/packages/CodeAlta.Tui.linux-musl-x64) | 1.0.0 | Alexandre Mutel | CodeAlta TUI: a keyboard-first terminal UI for agentic AI coding on your local… |
| 2026-10-05 07:45:43 | [CodeAlta.Tui.linux-musl-arm64](https://www.nuget.org/packages/CodeAlta.Tui.linux-musl-arm64) | 1.0.0 | Alexandre Mutel | CodeAlta TUI: a keyboard-first terminal UI for agentic AI coding on your local… |
| 2026-10-05 07:45:45 | [CodeAlta.Tui.osx-x64](https://www.nuget.org/packages/CodeAlta.Tui.osx-x64) | 1.0.0 | Alexandre Mutel | CodeAlta TUI: a keyboard-first terminal UI for agentic AI coding on your local… |
| 2026-10-05 07:45:47 | [CodeAlta.Tui.osx-arm64](https://www.nuget.org/packages/CodeAlta.Tui.osx-arm64) | 1.0.0 | Alexandre Mutel | CodeAlta TUI: a keyboard-first terminal UI for agentic AI coding on your local… |
| 2026-10-05 07:54:54 | [Hexalith.FrontComposer.Contracts.UI](https://www.nuget.org/packages/Hexalith.FrontComposer.Contracts.UI) | 4.6.0 | Hexalith | Blazor and Fluent UI rendering contracts for Hexalith FrontComposer. |
| 2026-10-05 07:54:58 | [Hexalith.FrontComposer.Shell](https://www.nuget.org/packages/Hexalith.FrontComposer.Shell) | 4.6.0 | Hexalith | Package Description |
| 2026-10-05 07:55:00 | [Hexalith.FrontComposer.Testing](https://www.nuget.org/packages/Hexalith.FrontComposer.Testing) | 4.6.0 | Hexalith | Adopter-facing bUnit test host, fakes, builders, and assertions for Hexalith Fr… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

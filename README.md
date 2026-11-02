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

## Latest list — 2026-11-02 15:18 UTC

New packages created between 2026-11-02 14:21 UTC and 2026-11-02 15:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-02T15-18-56-767102Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-02 14:34:57 | [Wip.Abstractions](https://www.nuget.org/packages/Wip.Abstractions) | 0.0.2 | Ricardo Medeiros | Typed contracts for WiP capabilities, descriptors, artifacts, sessions, policie… |
| 2026-11-02 14:34:58 | [Wip.Agent.Basic](https://www.nuget.org/packages/Wip.Agent.Basic) | 0.0.2 | Ricardo Medeiros | Packable baseline agents for WiP runtime composition and deterministic sample e… |
| 2026-11-02 14:35:00 | [Wip.Artifacts.Local](https://www.nuget.org/packages/Wip.Artifacts.Local) | 0.0.2 | Ricardo Medeiros | Local filesystem persistence for WiP artifacts and descriptors. |
| 2026-11-02 14:35:02 | [Wip.Bones](https://www.nuget.org/packages/Wip.Bones) | 0.0.2 | Ricardo Medeiros | Block Dominoes domain types, identifiers, and game engine for the WIP Bones wor… |
| 2026-11-02 14:35:03 | [Wip.Bones.Agents](https://www.nuget.org/packages/Wip.Bones.Agents) | 0.0.2 | Ricardo Medeiros | Agent capabilities and per-player knowledge stores for the WIP Bones workflow. |
| 2026-11-02 14:35:05 | [Wip.Bones.ModelProviders.DeepSeek](https://www.nuget.org/packages/Wip.Bones.ModelProviders.DeepSeek) | 0.0.2 | Ricardo Medeiros | DeepSeek model provider adapters for WIP Bones agent stages. |
| 2026-11-02 14:35:07 | [Wip.Builder](https://www.nuget.org/packages/Wip.Builder) | 0.0.2 | Ricardo Medeiros | Registration APIs for WiP capabilities, policies, and workflows. |
| 2026-11-02 14:35:08 | [Wip.Modus](https://www.nuget.org/packages/Wip.Modus) | 0.0.2 | Ricardo Medeiros | WiP bridge for Modus plugin discovery, diagnostics, and run manifest capture. |
| 2026-11-02 14:35:10 | [Wip.Policy.LocalSafe](https://www.nuget.org/packages/Wip.Policy.LocalSafe) | 0.0.2 | Ricardo Medeiros | Default local-safe policy enforcing dangerous-command denial, workspace boundar… |
| 2026-11-02 14:35:11 | [Wip.Runtime](https://www.nuget.org/packages/Wip.Runtime) | 0.0.2 | Ricardo Medeiros | Runtime orchestration primitives for WiP session lifecycle and event emission. |
| 2026-11-02 14:35:13 | [Wip.Shell](https://www.nuget.org/packages/Wip.Shell) | 0.0.2 | Ricardo Medeiros | Interactive WiP shell loop with global/session command routing. |
| 2026-11-02 14:35:15 | [Wip.Shell.E2E](https://www.nuget.org/packages/Wip.Shell.E2E) | 0.0.2 | Ricardo Medeiros | Shared E2E compliance registry and aggregated behavior-proof gates for WIP requ… |
| 2026-11-02 14:35:17 | [Wip.ShellHost](https://www.nuget.org/packages/Wip.ShellHost) | 0.0.2 | Ricardo Medeiros | WiP shell host startup and shutdown orchestration with plugin lifecycle integra… |
| 2026-11-02 14:35:18 | [Wip.Tools.Shell](https://www.nuget.org/packages/Wip.Tools.Shell) | 0.0.2 | Ricardo Medeiros | Controlled shell command execution constrained to worktree with policy gate and… |
| 2026-11-02 14:35:20 | [Wip.Validation.DotNet](https://www.nuget.org/packages/Wip.Validation.DotNet) | 0.0.2 | Ricardo Medeiros | Dotnet build/test validator with persisted ValidationReport artifacts for WiP s… |
| 2026-11-02 14:35:21 | [Wip.Workspaces.Git](https://www.nuget.org/packages/Wip.Workspaces.Git) | 0.0.2 | Ricardo Medeiros | Git-backed workspace provider for WiP session isolation, diff hashing, and gate… |
| 2026-11-02 14:39:34 | [yocto.Wpf](https://www.nuget.org/packages/yocto.Wpf) | 3.0.0 | MILL5,Contributors | WPF XAML markup extension ({yocto:Resolve}) that resolves view models and servi… |
| 2026-11-02 14:51:33 | [TildeMail.Plugin.Xmpp](https://www.nuget.org/packages/TildeMail.Plugin.Xmpp) | 0.5.0 | tom (tom@orivega.io) | XMPP chat accounts for TildeMail: a tmail plugin bundle, not a library. Unzip p… |
| 2026-11-02 15:02:32 | [Byungmeo.Calendar.WinUI](https://www.nuget.org/packages/Byungmeo.Calendar.WinUI) | 0.2.0 | byungmeo | Extensible WinUI 3 month calendar with multi-day events and developer-owned int… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

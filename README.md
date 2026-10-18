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

## Latest list — 2026-10-18 07:19 UTC

New packages created between 2026-10-18 06:20 UTC and 2026-10-18 07:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-18T07-19-55-414191Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-18 06:38:42 | [AvaloniaWebview.React](https://www.nuget.org/packages/AvaloniaWebview.React) | 0.16.2 | Avalonia.React contributors | Build React frontends hosted in Avalonia 12 using Avalonia's native WebView and… |
| 2026-10-18 06:38:43 | [AvaloniaWebview.React.SourceGenerator](https://www.nuget.org/packages/AvaloniaWebview.React.SourceGenerator) | 0.16.2 | Avalonia.React contributors | Generates C# API interfaces from TypeScript declaration files for AvaloniaWebvi… |
| 2026-10-18 06:38:44 | [AvaloniaWebview.React.Vite](https://www.nuget.org/packages/AvaloniaWebview.React.Vite) | 0.16.2 | Avalonia.React contributors | Vite development server integration for AvaloniaWebview.React desktop apps. |
| 2026-10-18 06:44:48 | [aweXpect.Snapshots.PublicApi](https://www.nuget.org/packages/aweXpect.Snapshots.PublicApi) | 0.3.0 | aweXpect | Public API snapshots for aweXpect. |
| 2026-10-18 06:45:04 | [aweXpect.Snapshots.DiffEngine](https://www.nuget.org/packages/aweXpect.Snapshots.DiffEngine) | 0.3.0 | aweXpect | Opens a diff tool with DiffEngine for snapshots of aweXpect.Snapshots that are… |
| 2026-10-18 06:57:05 | [Tedd.SMB3](https://www.nuget.org/packages/Tedd.SMB3) | 1.0.0 | tedd | Managed SMB 3.1.1 client and file server for .NET 10 on Windows and Linux, with… |
| 2026-10-18 07:14:46 | [TauriKit.Credentials](https://www.nuget.org/packages/TauriKit.Credentials) | 0.22.0 | iyulab | Secrets in the Windows Credential Manager under the same entries the tauri-kit-… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

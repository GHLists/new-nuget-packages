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

## Latest list — 2026-10-13 02:21 UTC

New packages created between 2026-10-13 01:20 UTC and 2026-10-13 02:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-13T02-21-24-354133Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-13 01:32:44 | [Jex.Cli](https://www.nuget.org/packages/Jex.Cli) | 3.0.0 | JerryLuo | Command-line tool for the Jex Clean Architecture template: create projects (jex… |
| 2026-10-13 01:40:56 | [Mokaterm.Abstractions](https://www.nuget.org/packages/Mokaterm.Abstractions) | 0.2.0 | Moka | Contracts for Mokaterm plugins and modules: protocols, sessions, terminals, fil… |
| 2026-10-13 01:40:58 | [Mokaterm.Plugin.Sdk](https://www.nuget.org/packages/Mokaterm.Plugin.Sdk) | 0.2.0 | Moka | Builds a Mokaterm plugin: packs a Razor class library into a .mokaplugin with i… |
| 2026-10-13 01:40:59 | [Mokaterm.Plugin.Templates](https://www.nuget.org/packages/Mokaterm.Plugin.Templates) | 0.2.0 | Moka | dotnet new template for Mokaterm plugins: an app tool, a System view page or a… |
| 2026-10-13 01:41:01 | [Mokaterm.UI.Common](https://www.nuget.org/packages/Mokaterm.UI.Common) | 0.2.0 | Moka | Shared Blazor building blocks for Mokaterm plugins and modules: UI contribution… |
| 2026-10-13 02:09:07 | [YS.Knife.Document.Converter.Xlsx2Pdf](https://www.nuget.org/packages/YS.Knife.Document.Converter.Xlsx2Pdf) | 0.0.122 | Pengbo Yang | Package Description |
| 2026-10-13 02:11:04 | [Vouchfx.Community.JsonRpc](https://www.nuget.org/packages/Vouchfx.Community.JsonRpc) | 1.0.0 | vouchfx-community | JSON-RPC 2.0 over HTTP step provider for vouchfx — invokes a method and asserts… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-07 18:20 UTC

New packages created between 2026-10-07 17:22 UTC and 2026-10-07 18:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-07T18-20-34-356698Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-07 17:23:43 | [Confluent.SchemaRegistry.Encryption.AliCloud](https://www.nuget.org/packages/Confluent.SchemaRegistry.Encryption.AliCloud) | 2.16.0 | Confluent Inc. | Provides field-level encryption for use with Confluent Schema Registry using Al… |
| 2026-10-07 17:24:30 | [YetAnotherClaudeAgentSdk](https://www.nuget.org/packages/YetAnotherClaudeAgentSdk) | 1.0.0 | Elias Bachaalany,macsux | .NET SDK for the Claude Code CLI: QueryAsync(), a bidirectional client, hooks,… |
| 2026-10-07 17:25:21 | [LunaticPanel.Core.Utils.Abstraction](https://www.nuget.org/packages/LunaticPanel.Core.Utils.Abstraction) | 0.0.18 | Maksim Shimshon | Core Package for Lunatic Panel's PLugin |
| 2026-10-07 17:32:23 | [LunaticPanel.Core.Utils](https://www.nuget.org/packages/LunaticPanel.Core.Utils) | 0.0.18 | Maksim Shimshon | Core Package for Lunatic Panel's PLugin |
| 2026-10-07 17:39:49 | [Bakobo.Fiki](https://www.nuget.org/packages/Bakobo.Fiki) | 0.0.1 | Bakobo | Name reserved for fiki (RFC 9421 HTTP message signatures). Empty placeholder; s… |
| 2026-10-07 17:41:17 | [LunaticPanel.Package.Server](https://www.nuget.org/packages/LunaticPanel.Package.Server) | 0.0.18 | Maksim Shimshon | Core Package for Lunatic Panel's PLugin |
| 2026-10-07 17:46:58 | [LunaticPanel.PackageManager.Keys](https://www.nuget.org/packages/LunaticPanel.PackageManager.Keys) | 0.0.18 | LunaticPanel.PackageManager.K… | Package Description |
| 2026-10-07 17:52:24 | [LunaticPanel.Engine.Keys](https://www.nuget.org/packages/LunaticPanel.Engine.Keys) | 0.0.18 | Maksim Shimshon | Core Package for Lunatic Panel's PLugin |
| 2026-10-07 17:52:45 | [CommunityAbp.ProgressiveDelivery.OpenIddict](https://www.nuget.org/packages/CommunityAbp.ProgressiveDelivery.OpenIddict) | 0.3.0 | Kori Francis | OpenIddict integration for CommunityAbp.ProgressiveDelivery: find Client subjec… |
| 2026-10-07 17:53:17 | [SudokuGen](https://www.nuget.org/packages/SudokuGen) | 1.0.0 | kw.dev gmbh | A fast sudoku puzzle generator. .NET port of petewritescode/sudoku-gen: transfo… |
| 2026-10-07 17:57:02 | [YellowDogMan.Splat.NET](https://www.nuget.org/packages/YellowDogMan.Splat.NET) | 1.0.0 | Splat.NET | Package Description |
| 2026-10-07 17:58:22 | [Singulink.FulcrumFS.Local](https://www.nuget.org/packages/Singulink.FulcrumFS.Local) | 2.0.0 | Singulink | Local file system implementation of the FulcrumFS repository. |
| 2026-10-07 17:59:04 | [nuget-manager](https://www.nuget.org/packages/nuget-manager) | 0.1.0 | ManagedCode | Review and update NuGet package families in .NET workspaces. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

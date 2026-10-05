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

## Latest list — 2026-10-05 16:19 UTC

New packages created between 2026-10-05 15:18 UTC and 2026-10-05 16:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-05T16-19-51-062023Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-05 15:20:27 | [BugFixer.Core](https://www.nuget.org/packages/BugFixer.Core) | 0.1.1 | Murat Bolulu | Framework-agnostic BugFixer core: options, recursive sensitive-data masking, de… |
| 2026-10-05 15:20:28 | [BugFixer.Abstractions](https://www.nuget.org/packages/BugFixer.Abstractions) | 0.1.1 | Murat Bolulu | Transport-neutral contracts (bug event model, publisher, fingerprint and maskin… |
| 2026-10-05 15:20:29 | [BugFixer.AspNetCore](https://www.nuget.org/packages/BugFixer.AspNetCore) | 0.1.1 | Murat Bolulu | Drop-in production exception collection for ASP.NET Core. Implements IException… |
| 2026-10-05 15:20:30 | [BugFixer.Client](https://www.nuget.org/packages/BugFixer.Client) | 0.1.1 | Murat Bolulu | HTTP transport for BugFixer: resilient typed client that ships bug events and s… |
| 2026-10-05 15:24:25 | [Umbraco.Community.RichDictionary](https://www.nuget.org/packages/Umbraco.Community.RichDictionary) | 1.0.0 | Jack Stunell | Edit Umbraco dictionary values with a rich text (Tiptap) or Markdown editor ins… |
| 2026-10-05 15:24:36 | [SandBottle.NET](https://www.nuget.org/packages/SandBottle.NET) | 1.0.1 | Newton | ASP.NET Core 的結構化紀錄：Loki、請求紀錄、SQL 指令紀錄與例外通報。 |
| 2026-10-05 15:24:42 | [Atlas.AspNetCore](https://www.nuget.org/packages/Atlas.AspNetCore) | 1.0.0 | Atlas | Framework-native ASP.NET Core authentication, DI, and authorization for Atlas —… |
| 2026-10-05 15:26:53 | [Nyxel](https://www.nuget.org/packages/Nyxel) | 0.0.1 | Nyxel contributors | Reserved for Nyxel, a game scripting language that compiles to ordinary .NET as… |
| 2026-10-05 15:27:47 | [Hubertech.Belgium](https://www.nuget.org/packages/Hubertech.Belgium) | 0.1.0 | Dampsey | Belgian administrative identifiers and rules for .NET: enterprise number (BCE/K… |
| 2026-10-05 15:35:32 | [SysMaster.Library](https://www.nuget.org/packages/SysMaster.Library) | 1.0.1 | Winnigames2024 | SysMaster is designed for the convenient management of the system and additiona… |
| 2026-10-05 15:56:07 | [AnkitRana.XrmToolBox.DeploymentDoctor](https://www.nuget.org/packages/AnkitRana.XrmToolBox.DeploymentDoctor) | 1.0.0 | Ankit Rana | Find out why a form, view, web resource, workflow or cloud flow deployed with a… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

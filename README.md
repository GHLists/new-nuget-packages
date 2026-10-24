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

## Latest list — 2026-10-24 20:19 UTC

New packages created between 2026-10-24 19:20 UTC and 2026-10-24 20:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-24T20-19-33-551153Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-24 19:30:18 | [SharpView.Cli](https://www.nuget.org/packages/SharpView.Cli) | 0.3.0 | Stanislav Tadtaev | Source-backed analysis of ASP.NET Core Web APIs for people and agents: the MSBu… |
| 2026-10-24 19:30:30 | [Nyra.DSharpPlus](https://www.nuget.org/packages/Nyra.DSharpPlus) | 0.2.0 | Akinori107 | DSharpPlus adapter for Nyra, a Lavalink v4.2+ and NodeLink v3.9+ client. |
| 2026-10-24 19:30:30 | [Nyra.DSharpPlus.Nightly](https://www.nuget.org/packages/Nyra.DSharpPlus.Nightly) | 0.2.0 | Akinori107 | DSharpPlus Nightly adapter for Nyra, a Lavalink v4.2+ and NodeLink v3.9+ client. |
| 2026-10-24 19:30:31 | [Nyra.DiscordNet](https://www.nuget.org/packages/Nyra.DiscordNet) | 0.2.0 | Akinori107 | Discord.Net adapter for Nyra, a Lavalink v4.2+ and NodeLink v3.9+ client. |
| 2026-10-24 19:36:47 | [Meziantou.Framework.Pdf](https://www.nuget.org/packages/Meziantou.Framework.Pdf) | 1.0.0 | meziantou | Fully managed PDF library for .NET, written from ISO 32000-2: an object model,… |
| 2026-10-24 19:36:56 | [Meziantou.Framework.WebPlatform.PdfRendering](https://www.nuget.org/packages/Meziantou.Framework.WebPlatform.PdfRendering) | 1.0.0 | meziantou | Prints the documents of Meziantou.Framework.WebPlatform to PDF with Meziantou.F… |
| 2026-10-24 19:42:38 | [LANCommander.Plugins.GOG](https://www.nuget.org/packages/LANCommander.Plugins.GOG) | 1.0.0 | LANCommander | Links GOG accounts to a LANCommander server and imports the games they own. |
| 2026-10-24 19:45:18 | [LocalRun](https://www.nuget.org/packages/LocalRun) | 0.1.0 | Salefou | Try a library change in the services that consume it as a NuGet package, across… |
| 2026-10-24 19:46:21 | [Caly.PdfPig.Fonts](https://www.nuget.org/packages/Caly.PdfPig.Fonts) | 1.0.0 | BobLd | Substitute font programs for the 14 PDF Standard fonts (Foxit and Liberation). |
| 2026-10-24 19:51:41 | [MMCA.Common.Aws](https://www.nuget.org/packages/MMCA.Common.Aws) | 1.255.0 | Ivan Ball | MMCA framework: the AWS adapter. S3-compatible file storage (AWS S3, Cloudflare… |
| 2026-10-24 19:51:41 | [MMCA.Common.Azure](https://www.nuget.org/packages/MMCA.Common.Azure) | 1.255.0 | Ivan Ball | MMCA framework: the Microsoft Azure adapter. Key Vault configuration, the Blob… |
| 2026-10-24 19:51:44 | [MMCA.Common.Testing.Azure](https://www.nuget.org/packages/MMCA.Common.Testing.Azure) | 1.255.0 | Ivan Ball | MMCA framework Azure test infrastructure: the Service Bus emulator broker-parit… |
| 2026-10-24 20:00:43 | [MintPlayer.Versioning.MSBuild](https://www.nuget.org/packages/MintPlayer.Versioning.MSBuild) | 1.0.0 | MintPlayer | Sets a project's Version from the highest <PackageId>/v<version> git tag reacha… |
| 2026-10-24 20:06:52 | [CFGBINManager](https://www.nuget.org/packages/CFGBINManager) | 1.0.0 | The-RealBobi | Managed T2B and RDBNP record API with lossless CFG interchange. |
| 2026-10-24 20:09:22 | [Packata.Database](https://www.nuget.org/packages/Packata.Database) | 0.49.0 | Cédric L. Charlier | Shared database connections, provider composition and curated connector acquisi… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

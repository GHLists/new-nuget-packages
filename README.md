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

## Latest list — 2026-10-28 13:20 UTC

New packages created between 2026-10-28 12:18 UTC and 2026-10-28 13:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-28T13-20-12-987723Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-28 12:20:30 | [TGateway.OpcDaServer](https://www.nuget.org/packages/TGateway.OpcDaServer) | 2.3.20 | TGateway.OpcDaServer | Package Description |
| 2026-10-28 12:22:48 | [Oddin.OddsFeedSdk](https://www.nuget.org/packages/Oddin.OddsFeedSdk) | 1.1.37 | Oddin.gg | Oddin.gg Odds Feed SDK for .NET |
| 2026-10-28 12:27:22 | [BringYourOwnAgent.Relay](https://www.nuget.org/packages/BringYourOwnAgent.Relay) | 0.0.3 | ultrathinker | The site's side of the BYOA «direct» link, ready-made for an ASP.NET Core site:… |
| 2026-10-28 12:42:51 | [Verify.OfficeIMO](https://www.nuget.org/packages/Verify.OfficeIMO) | 0.1.0 | https://github.com/VerifyTest… | Extends Verify (https://github.com/VerifyTests/Verify) to allow verification vi… |
| 2026-10-28 12:46:34 | [Cx.Dummy.Package](https://www.nuget.org/packages/Cx.Dummy.Package) | 1.0.0 | Checkmarx | Internal package used by Checkmarx to test SCA risk detection. It contains no f… |
| 2026-10-28 12:47:18 | [Alcifra.ModuleAbi](https://www.nuget.org/packages/Alcifra.ModuleAbi) | 1.25.0 | Hebel Consulting | The contract industry modules build against: registration, mask seeding, facts,… |
| 2026-10-28 12:47:38 | [Moonwell.Areas](https://www.nuget.org/packages/Moonwell.Areas) | 0.3.0 | mdlsvensson | Areas that units enter, stay in and leave, for Moonwell maps. |
| 2026-10-28 12:47:38 | [Moonwell.Maths](https://www.nuget.org/packages/Moonwell.Maths) | 0.3.0 | mdlsvensson | Vectors, angles, interpolation, shapes and raycasts for Moonwell maps. |
| 2026-10-28 12:47:38 | [Moonwell.Physics](https://www.nuget.org/packages/Moonwell.Physics) | 0.3.0 | mdlsvensson | Missiles, knockback, walls and ballistics for Moonwell maps. |
| 2026-10-28 12:47:39 | [Moonwell.Input](https://www.nuget.org/packages/Moonwell.Input) | 0.3.0 | mdlsvensson | Each player's mouse and camera for Moonwell maps. |
| 2026-10-28 12:47:40 | [Moonwell.Interactions](https://www.nuget.org/packages/Moonwell.Interactions) | 0.3.0 | mdlsvensson | Interactions, gizmos and finding for Moonwell maps. |
| 2026-10-28 12:47:40 | [Moonwell.Terrain](https://www.nuget.org/packages/Moonwell.Terrain) | 0.3.0 | mdlsvensson | Terrain height, pathing and ground raycasts for Moonwell maps. |
| 2026-10-28 12:49:15 | [Skail.ApplicationTemplate.CSharp](https://www.nuget.org/packages/Skail.ApplicationTemplate.CSharp) | 1.0.0 | Skail Team | Template for Skail Project. |
| 2026-10-28 12:53:22 | [Avalonia.Controls.Markdown.Mermaid](https://www.nuget.org/packages/Avalonia.Controls.Markdown.Mermaid) | 12.4.0 | AvaloniaUI OÜ | Mermaid diagram rendering for Avalonia.Controls.Markdown, drawn natively withou… |
| 2026-10-28 12:54:12 | [AppWeaver.Contexts](https://www.nuget.org/packages/AppWeaver.Contexts) | 1.0.0 | Team AppWeaver | Shared interfaces and default implementations for current user and tenant conte… |
| 2026-10-28 12:55:29 | [OptiCli.Mcp.Cms13](https://www.nuget.org/packages/OptiCli.Mcp.Cms13) | 0.26.0 | opticli contributors | An MCP server for Optimizely CMS 13 (for CMS 12, use OptiCli.Mcp): editors conn… |
| 2026-10-28 12:58:35 | [Pilz.Updating.Ui.Avalonia](https://www.nuget.org/packages/Pilz.Updating.Ui.Avalonia) | 5.0.0 | Pilz.Updating.Ui.Avalonia | Package Description |
| 2026-10-28 13:10:19 | [ImageDull.ImageSharp](https://www.nuget.org/packages/ImageDull.ImageSharp) | 2.1.14 | ImageDull contributors | A cross-platform, 2D image manipulation library for .NET. A fork of ImageSharp |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

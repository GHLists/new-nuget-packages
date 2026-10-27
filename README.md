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

## Latest list — 2026-10-27 18:20 UTC

New packages created between 2026-10-27 17:21 UTC and 2026-10-27 18:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-27T18-20-22-107465Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-27 17:22:11 | [PictureSharp.Jxl](https://www.nuget.org/packages/PictureSharp.Jxl) | 0.7.2 | Artur Pelzak | Pure C# JPEG XL plugin for PictureSharp. Version 0.7.2 detects and identifies J… |
| 2026-10-27 17:28:55 | [Lunate.Extensions.Subagents](https://www.nuget.org/packages/Lunate.Extensions.Subagents) | 0.1.0 | SubagentsExtension | The subagents extension for Lunate: one tool that runs a child agent through th… |
| 2026-10-27 17:28:59 | [lunate](https://www.nuget.org/packages/lunate) | 0.1.0 | lunate | A native C# coding agent for the terminal. |
| 2026-10-27 17:39:36 | [Prime.Architecture.Authorization](https://www.nuget.org/packages/Prime.Architecture.Authorization) | 1.0.0 | Prime | Autorização por recurso e permissão (recurso:acao) para ASP.NET Core, baseada e… |
| 2026-10-27 17:51:30 | [FileVault.WebDav](https://www.nuget.org/packages/FileVault.WebDav) | 0.4.0-beta | XFiler Community | WebDAV provider for FileVault. Implements IFileProvider over any WebDAV server… |
| 2026-10-27 17:51:31 | [FileVault.S3](https://www.nuget.org/packages/FileVault.S3) | 0.4.0-beta | XFiler Community | S3-compatible object storage provider for FileVault (AWS S3, Cloudflare R2, Bac… |
| 2026-10-27 17:51:32 | [FileVault.Dropbox](https://www.nuget.org/packages/FileVault.Dropbox) | 0.4.0-beta | XFiler Community | Dropbox provider for FileVault. Implements IFileProvider over the Dropbox HTTP… |
| 2026-10-27 17:51:33 | [FileVault.OneDrive](https://www.nuget.org/packages/FileVault.OneDrive) | 0.4.0-beta | XFiler Community | OneDrive provider for FileVault (personal and work/school accounts). Implements… |
| 2026-10-27 17:52:11 | [Prime.Architecture.Authorization.EntityFramework](https://www.nuget.org/packages/Prime.Architecture.Authorization.EntityFramework) | 1.0.0 | Prime | Persistência em banco (Entity Framework Core) para o Prime.Architecture.Authori… |
| 2026-10-27 17:53:15 | [ConventionMapper.Testing.EntityFrameworkCore](https://www.nuget.org/packages/ConventionMapper.Testing.EntityFrameworkCore) | 1.10.0 | Katragadda | Database checks for mappings into EF Core entities: DatabaseAssert.SavesRoundTr… |
| 2026-10-27 17:59:28 | [Kinetix.Web.OpenTelemetry](https://www.nuget.org/packages/Kinetix.Web.OpenTelemetry) | 10.1.1 | JabX | Utilitaires Kinetix OpenTelemetry pour ASP.NET Core. |
| 2026-10-27 18:06:36 | [PeachDrawing.Win2D](https://www.nuget.org/packages/PeachDrawing.Win2D) | 0.9.25-preview1 | PeachDrawing.Win2D | A Win2D Canvas for PeachDrawing.Core - draw shapes, gradients, clips, layers, t… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

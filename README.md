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

## Latest list — 2026-10-02 08:22 UTC

New packages created between 2026-10-02 07:21 UTC and 2026-10-02 08:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-02T08-22-18-111091Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-02 07:32:04 | [Infometeos.Hand.Service.Client](https://www.nuget.org/packages/Infometeos.Hand.Service.Client) | 10.0.0 | Infometeos | Клиент микросервиса данных HAND (Height Above Nearest Drainage) |
| 2026-10-02 07:36:45 | [MbUtils.Testcontainers.RustFS](https://www.nuget.org/packages/MbUtils.Testcontainers.RustFS) | 1.0.0 | Bence Molnár | Unofficial Testcontainers module for RustFS, an S3-compatible object store. |
| 2026-10-02 07:46:21 | [FluentAvalonia.MarkdownRender](https://www.nuget.org/packages/FluentAvalonia.MarkdownRender) | 12.1.3.1 | RYCBStudio | Avalonia / FluentAvalonia 风格的 Markdown 渲染组件，支持标题、列表、引用、代码高亮、图片、内联 HTML、GitHub 风… |
| 2026-10-02 07:47:23 | [PosInformatique.Foundations.Emailing.Mailjet](https://www.nuget.org/packages/PosInformatique.Foundations.Emailing.Mailjet) | 1.3.0 | Gilles TOURREAU | Provides an IEmailProvider implementation for PosInformatique.Foundations.Email… |
| 2026-10-02 08:04:52 | [OidcForge](https://www.nuget.org/packages/OidcForge) | 4.2.0 | Brock Allen,Dominick Baier,Ya… | OpenID Connect and OAuth 2.0 Framework for ASP.NET Core (maintained fork of Ide… |
| 2026-10-02 08:04:53 | [OidcForge.AspNetIdentity](https://www.nuget.org/packages/OidcForge.AspNetIdentity) | 4.2.0 | Brock Allen,Dominick Baier,Ya… | ASP.NET Core Identity integration (maintained fork of IdentityServer4) |
| 2026-10-02 08:04:53 | [OidcForge.EntityFramework](https://www.nuget.org/packages/OidcForge.EntityFramework) | 4.2.0 | Brock Allen,Dominick Baier,Sc… | EntityFramework persistence configuration APIs (maintained fork of IdentityServ… |
| 2026-10-02 08:04:54 | [OidcForge.EntityFramework.Storage](https://www.nuget.org/packages/OidcForge.EntityFramework.Storage) | 4.2.0 | Brock Allen,Dominick Baier,Sc… | EntityFramework persistence layer (maintained fork of IdentityServer4) |
| 2026-10-02 08:04:55 | [OidcForge.Storage](https://www.nuget.org/packages/OidcForge.Storage) | 4.2.0 | Brock Allen,Dominick Baier,Ya… | Storage interfaces and models (maintained fork of IdentityServer4) |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

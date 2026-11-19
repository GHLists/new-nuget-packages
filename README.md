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

## Latest list — 2026-11-19 21:21 UTC

New packages created between 2026-11-19 20:20 UTC and 2026-11-19 21:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-19T21-21-04-260857Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-19 20:27:25 | [TencentCloudSDKIntlEN.Makers](https://www.nuget.org/packages/TencentCloudSDKIntlEN.Makers) | 3.0.1429 | Tencent Cloud API Team | Tencent Cloud API 3.0 SDK for .NET |
| 2026-11-19 20:33:54 | [WillStrohl.API.oEmbed](https://www.nuget.org/packages/WillStrohl.API.oEmbed) | 0.5.5 | Upendo Ventures, LLC | A .NET Framework wrapper for the oEmbed open format, with provider routing, una… |
| 2026-11-19 20:42:29 | [MarkMpn.Sql4Cds.LanguageServer](https://www.nuget.org/packages/MarkMpn.Sql4Cds.LanguageServer) | 10.6.0 | Mark Carrington | SQL 4 CDS language server, used by the SQL 4 CDS Power Platform ToolBox tool |
| 2026-11-19 20:43:32 | [Serval](https://www.nuget.org/packages/Serval) | 0.1.0 | Caprine Logic | An async controller web framework built on Microsoft.Extensions.Hosting. |
| 2026-11-19 20:43:33 | [Serval.Authentication](https://www.nuget.org/packages/Serval.Authentication) | 0.1.0 | Caprine Logic | Composable authentication, sessions, password hashing, and authorization for Se… |
| 2026-11-19 20:43:33 | [Serval.OAuth](https://www.nuget.org/packages/Serval.OAuth) | 0.1.0 | Caprine Logic | OAuth 2.0 clients and OpenID Connect provider sign-in for Serval. |
| 2026-11-19 20:43:34 | [Serval.SignedUrls](https://www.nuget.org/packages/Serval.SignedUrls) | 0.1.0 | Caprine Logic | Signed route URLs with readable payloads, validation, and optional expiration f… |
| 2026-11-19 20:43:35 | [Serval.Jobs](https://www.nuget.org/packages/Serval.Jobs) | 0.1.0 | Caprine Logic | Scoped, recurring background jobs with periodic and cron schedules for Serval. |
| 2026-11-19 20:43:36 | [Serval.SocketIO](https://www.nuget.org/packages/Serval.SocketIO) | 0.1.0 | Caprine Logic | Socket.IO 4.x events, namespaces, rooms, and acknowledgements over HTTP polling… |
| 2026-11-19 20:43:36 | [Serval.Savanna](https://www.nuget.org/packages/Serval.Savanna) | 0.1.0 | Caprine Logic | Compiled, strongly typed HTML views for Serval. |
| 2026-11-19 20:43:37 | [Serval.Vite](https://www.nuget.org/packages/Serval.Vite) | 0.1.0 | Caprine Logic | Generated Vite asset lookups with production manifests and development HMR supp… |
| 2026-11-19 20:43:38 | [Serval.Transport.HttpListener](https://www.nuget.org/packages/Serval.Transport.HttpListener) | 0.1.0 | Caprine Logic | HTTP listener and WebSocket transport for Serval using System.Net.HttpListener. |
| 2026-11-19 20:43:40 | [Serval.Transport.Kestrel](https://www.nuget.org/packages/Serval.Transport.Kestrel) | 0.1.0 | Caprine Logic | Kestrel HTTP/1.1, HTTP/2, HTTP/3, and WebSocket transport for Serval. |
| 2026-11-19 20:45:37 | [sfx](https://www.nuget.org/packages/sfx) | 0.0.1 | Mirco De Zorzi | A k9s-style terminal UI for Azure Service Fabric clusters: browse nodes, applic… |
| 2026-11-19 20:54:14 | [EcoSQL.Connect](https://www.nuget.org/packages/EcoSQL.Connect) | 1.0.0 | Sleddie | Package Description |
| 2026-11-19 20:56:14 | [SyntaxCircus.AspNetCore.IndexNow](https://www.nuget.org/packages/SyntaxCircus.AspNetCore.IndexNow) | 0.1.0 | Syntax Circus LLC | Ownership verification, sitemap previews, and explicit IndexNow URL submission… |
| 2026-11-19 21:08:26 | [uSupport.Automate](https://www.nuget.org/packages/uSupport.Automate) | 17.0.0 | Lantzify | Umbraco Automate triggers and actions for uSupport. |
| 2026-11-19 21:09:50 | [Nazor.Accessibility](https://www.nuget.org/packages/Nazor.Accessibility) | 0.1.0-alpha | Nazor | Nazor: native desktop UI for .NET written with Razor components and NSS styles.… |
| 2026-11-19 21:10:32 | [Nazor.Animation](https://www.nuget.org/packages/Nazor.Animation) | 0.1.0-alpha | Nazor | Nazor: native desktop UI for .NET written with Razor components and NSS styles.… |
| 2026-11-19 21:11:17 | [Nazor.Application](https://www.nuget.org/packages/Nazor.Application) | 0.1.0-alpha | Nazor | Nazor: native desktop UI for .NET written with Razor components and NSS styles.… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

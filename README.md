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

## Latest list — 2026-10-06 22:20 UTC

New packages created between 2026-10-06 21:18 UTC and 2026-10-06 22:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-06T22-20-40-01831Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-06 21:20:18 | [Cashera](https://www.nuget.org/packages/Cashera) | 1.0.0 | Flam3y | Payment gateway cashera.cash - accepting payments with USDT settlement |
| 2026-10-06 21:20:29 | [Cashera.AspNetCore](https://www.nuget.org/packages/Cashera.AspNetCore) | 1.0.0 | Flam3y | Cashera support for ASP.NET Core |
| 2026-10-06 21:23:21 | [Reimaginate.DataHub.Dataverse.VirtualTables.Abstractions](https://www.nuget.org/packages/Reimaginate.DataHub.Dataverse.VirtualTables.Abstractions) | 1.4.5 | Reimaginate | Abstractions for DataHub Dataverse virtual table integrations and mediator-base… |
| 2026-10-06 21:29:17 | [Crono.ffmpeg.Nativo.win-x64](https://www.nuget.org/packages/Crono.ffmpeg.Nativo.win-x64) | 1.0.0 | Crono | Ejecutable nativo ffmpeg para plataforma win-x64 |
| 2026-10-06 21:29:48 | [Crono.tesseract.Nativo.win-x64](https://www.nuget.org/packages/Crono.tesseract.Nativo.win-x64) | 1.0.0 | Crono | Ejecutable nativo tesseract para plataforma win-x64 |
| 2026-10-06 21:56:21 | [Axiom.LWSE.Testing](https://www.nuget.org/packages/Axiom.LWSE.Testing) | 0.1.0 | DeadMoon0 | Part of the Axiom family. Runs an LWSE server in memory for tests: the applicat… |
| 2026-10-06 21:56:33 | [uaParser.Net.AspNetCore](https://www.nuget.org/packages/uaParser.Net.AspNetCore) | 2.0.0 | Dariuosh | ASP.NET Core integration for uaParser.Net: an injectable, per-request ClientInf… |
| 2026-10-06 21:57:03 | [Axiom.LWSE.Http](https://www.nuget.org/packages/Axiom.LWSE.Http) | 0.1.0 | DeadMoon0 | Part of the Axiom family. The HTTP/1.1 module of LWSE: compiled URI-template ro… |
| 2026-10-06 22:00:26 | [AStarDev.FunctionalParadigm](https://www.nuget.org/packages/AStarDev.FunctionalParadigm) | 0.1.4 | Jason Barden | A collection of useful functional programming extensions. |
| 2026-10-06 22:04:11 | [Arkheide.Essential.Culture.Blazor](https://www.nuget.org/packages/Arkheide.Essential.Culture.Blazor) | 1.3.0 | ArkheideSystem | Scoped localization and reactive text components for server-rendered Blazor app… |
| 2026-10-06 22:04:18 | [Axiom.LWSE.Hosting](https://www.nuget.org/packages/Axiom.LWSE.Hosting) | 0.1.0 | DeadMoon0 | Part of the Axiom family. Runs an LWSE server in the .NET generic host: ports,… |
| 2026-10-06 22:04:24 | [Axiom.LWSE.Auth.Usci](https://www.nuget.org/packages/Axiom.LWSE.Auth.Usci) | 0.1.0 | DeadMoon0 | Part of the Axiom family. USCI tokens for LWSE: signed bearer tokens whose key… |
| 2026-10-06 22:04:34 | [Axiom.LWSE.WebSockets](https://www.nuget.org/packages/Axiom.LWSE.WebSockets) | 0.1.0 | DeadMoon0 | Part of the Axiom family. WebSockets for LWSE: upgrade endpoints on the HTTP mo… |
| 2026-10-06 22:04:44 | [Axiom.LWSE.ReverseProxy](https://www.nuget.org/packages/Axiom.LWSE.ReverseProxy) | 0.1.0 | DeadMoon0 | Part of the Axiom family. A reverse proxy for LWSE: routes and clusters in code… |
| 2026-10-06 22:04:54 | [Axiom.LWSE.ApiDocs](https://www.nuget.org/packages/Axiom.LWSE.ApiDocs) | 0.1.0 | DeadMoon0 | Part of the Axiom family. Documents a server's HTTP API: an explorer page and O… |
| 2026-10-06 22:07:25 | [Axiom.LDB.Core](https://www.nuget.org/packages/Axiom.LDB.Core) | 0.1.0 | DeadMoon0 | Part of the Axiom family. The LDB database: tables with typed columns in fixed-… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

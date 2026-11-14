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

## Latest list — 2026-11-14 21:21 UTC

New packages created between 2026-11-14 20:21 UTC and 2026-11-14 21:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-14T21-21-01-752532Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-14 20:24:26 | [Sabota](https://www.nuget.org/packages/Sabota) | 0.3.0 | danlup71 | Mutation testing for F# using AST discovery and source-text mutations. Friendly… |
| 2026-11-14 20:25:56 | [ArsenalImageMounter.Native](https://www.nuget.org/packages/ArsenalImageMounter.Native) | 3.13.369 | Arsenal Recon | Arsenal Image Mounter Native Library dependencies |
| 2026-11-14 20:28:32 | [ArtifactD.ClientFeedback](https://www.nuget.org/packages/ArtifactD.ClientFeedback) | 1.4.1 | Aurora | Queue and upload crash, curated errors, user feedback, and best-effort usage ev… |
| 2026-11-14 20:31:26 | [BccCode.ChangeHistory](https://www.nuget.org/packages/BccCode.ChangeHistory) | 0.1.12 | BCC | Business events, typed history and valid periods for EF Core on PostgreSQL: one… |
| 2026-11-14 20:31:27 | [BccCode.ChangeHistory.Hosting](https://www.nuget.org/packages/BccCode.ChangeHistory.Hosting) | 0.1.12 | BCC | ASP.NET Core and Wolverine integration for BccCode.ChangeHistory: the business… |
| 2026-11-14 20:31:37 | [NetWasm.App.Ref](https://www.nuget.org/packages/NetWasm.App.Ref) | 0.14.0 | Zion Sati | Reference assemblies for NetWasm.App, the framework libraries of the NetWasm ne… |
| 2026-11-14 20:31:38 | [NetWasm.App.Runtime](https://www.nuget.org/packages/NetWasm.App.Runtime) | 0.14.0 | Zion Sati | Implementations of NetWasm.App, the framework libraries of the NetWasm netwasm0… |
| 2026-11-14 20:35:51 | [Holos.Foundation.Abp.Application](https://www.nuget.org/packages/Holos.Foundation.Abp.Application) | 0.1.0 | Jesús Alejandro Molina Peñahe… | Clases base de servicios de aplicación para ASP.NET Boilerplate: CRUD con compa… |
| 2026-11-14 20:35:51 | [Holos.Foundation.Abp.EntityFrameworkCore](https://www.nuget.org/packages/Holos.Foundation.Abp.EntityFrameworkCore) | 0.1.0 | Jesús Alejandro Molina Peñahe… | Compañía activa implícita para ASP.NET Boilerplate (Abp.*): filtro global y asi… |
| 2026-11-14 20:35:52 | [Holos.Foundation.Abp.Domain](https://www.nuget.org/packages/Holos.Foundation.Abp.Domain) | 0.1.0 | Jesús Alejandro Molina Peñahe… | Interfaces de dominio sin dependencias: entidades con compañía y entradas que p… |
| 2026-11-14 21:06:30 | [Electrical.Dynamics](https://www.nuget.org/packages/Electrical.Dynamics) | 1.3.0 | Gravicode Studios (Kang Fadhi… | Power system dynamics (RMS) for Electrical.Net: detailed synchronous machines (… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

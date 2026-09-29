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

## Latest list — 2026-09-29 02:22 UTC

New packages created between 2026-09-29 01:21 UTC and 2026-09-29 02:22 UTC.

[Full CSV](data/new-nuget-packages-2026-09-29T02-22-42-034686Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-29 01:25:53 | [Praveen.XrmToolbox.P7mAttachmentConverter](https://www.nuget.org/packages/Praveen.XrmToolbox.P7mAttachmentConverter) | 1.0.0.3 | Praveen Kumar Ellappa | Finds .p7m (PKCS#7/S-MIME) attachments on Dynamics 365 records and converts the… |
| 2026-09-29 01:38:20 | [Tamp.Conformance](https://www.nuget.org/packages/Tamp.Conformance) | 0.1.0 | Scott Singleton | Agentic ADR-conformance review for Tamp builds. Compares a repo's code against… |
| 2026-09-29 01:45:15 | [ServiceMantle.Web](https://www.nuget.org/packages/ServiceMantle.Web) | 0.2.0 | ServiceMantle.Web | ASP.NET Core hosting integration for ServiceMantle. |
| 2026-09-29 01:45:15 | [ServiceMantle.Discovery](https://www.nuget.org/packages/ServiceMantle.Discovery) | 0.2.0 | ServiceMantle.Discovery | Optional snapshot-bound Consul client and registration contracts for ServiceMan… |
| 2026-09-29 01:45:19 | [ServiceMantle.Logging](https://www.nuget.org/packages/ServiceMantle.Logging) | 0.2.0 | ServiceMantle.Logging | Serilog hosting, sanitizing console output, and an opt-in Grafana Loki sink for… |
| 2026-09-29 01:45:20 | [ServiceMantle.Persistence.Relational](https://www.nuget.org/packages/ServiceMantle.Persistence.Relational) | 0.2.0 | ServiceMantle.Persistence.Rel… | EF Core models and shared installation, configuration, and encrypted Data Prote… |
| 2026-09-29 01:49:15 | [Brows.ProcessAgent](https://www.nuget.org/packages/Brows.ProcessAgent) | 1.0.0 | Ken Yourek | Launch processes and asynchronously collect their standard output and standard… |
| 2026-09-29 01:49:17 | [Brows.ProcessAgent.Windows](https://www.nuget.org/packages/Brows.ProcessAgent.Windows) | 1.0.0 | Ken Yourek | Launch processes and asynchronously collect their standard output and standard… |
| 2026-09-29 01:49:36 | [OpenCIFS.Protocol](https://www.nuget.org/packages/OpenCIFS.Protocol) | 0.1.1 | OpenCIFS Contributors | Shared OpenCIFS SMB/CIFS protocol models, codecs, and wire-format foundations. |
| 2026-09-29 01:49:38 | [OpenCIFS.Security](https://www.nuget.org/packages/OpenCIFS.Security) | 0.1.1 | OpenCIFS Contributors | Shared OpenCIFS NTLMv2, SPNEGO, signing, encryption, and key-derivation helpers. |
| 2026-09-29 01:49:41 | [OpenCIFS.Transport](https://www.nuget.org/packages/OpenCIFS.Transport) | 0.1.1 | OpenCIFS Contributors | Shared OpenCIFS direct-TCP, NetBIOS session-service, and framing helpers. |
| 2026-09-29 01:49:44 | [OpenCIFS.Client](https://www.nuget.org/packages/OpenCIFS.Client) | 0.1.1 | OpenCIFS Contributors | Managed OpenCIFS direct-TCP SMB 2.0.2 through bounded SMB 3.0.2 client library. |
| 2026-09-29 01:49:46 | [OpenCIFS.Server](https://www.nuget.org/packages/OpenCIFS.Server) | 0.1.1 | OpenCIFS Contributors | Managed OpenCIFS direct-TCP SMB 2.0.2 through bounded SMB 3.0.2 server library. |
| 2026-09-29 01:53:01 | [Flowsy.Db.Unity.Postgres](https://www.nuget.org/packages/Flowsy.Db.Unity.Postgres) | 1.0.0 | Flowsy | PostgreSQL provider integration for Flowsy.Db.Unity. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

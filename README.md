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

## Latest list — 2026-11-17 11:19 UTC

New packages created between 2026-11-17 10:20 UTC and 2026-11-17 11:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-17T11-19-40-456905Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-17 10:23:13 | [Sequrus.Cli](https://www.nuget.org/packages/Sequrus.Cli) | 0.2.0 | vdasus | Command-line tool for Sequrus: generate keys, encrypt, decrypt and re-encrypt v… |
| 2026-11-17 10:23:14 | [Sequrus.Configuration](https://www.nuget.org/packages/Sequrus.Configuration) | 0.2.0 | vdasus | Microsoft.Extensions.Configuration integration for Sequrus: decrypts sq1: value… |
| 2026-11-17 10:23:14 | [Sequrus](https://www.nuget.org/packages/Sequrus) | 0.2.0 | vdasus | Encrypt and decrypt strings and connection-string secrets with AES-256-GCM. The… |
| 2026-11-17 10:23:41 | [RealtimeBpmAnalyzer](https://www.nuget.org/packages/RealtimeBpmAnalyzer) | 6.2.0 | David Lepaux | Offline BPM analysis of PCM samples, in pure managed C#: the .NET port of the r… |
| 2026-11-17 10:26:34 | [PowerCraft.Sites.Core](https://www.nuget.org/packages/PowerCraft.Sites.Core) | 0.1.1 | The Code Kitchen | Typed kernel for PowerCraft.Sites: builds a markdown content tree into a themed… |
| 2026-11-17 10:34:46 | [OpenDCP.Framework.AuditTrail](https://www.nuget.org/packages/OpenDCP.Framework.AuditTrail) | 0.1.0 | OpenDCP.Framework.AuditTrail | Package Description |
| 2026-11-17 10:38:36 | [DigiTFactory.Libraries.Analyzers.Storage](https://www.nuget.org/packages/DigiTFactory.Libraries.Analyzers.Storage) | 0.1.1 | DigiTFactory.Libraries.Analyz… | Roslyn analyzers for the Storage layer (DigiTFactory EDM quality gates QG-3xx). |
| 2026-11-17 10:39:58 | [Valt0](https://www.nuget.org/packages/Valt0) | 1.0.0 | BYTE 1620 | .NET client for Valt0. Fetches secrets from a local Valt0 vault at runtime, so… |
| 2026-11-17 10:49:26 | [BillionSend](https://www.nuget.org/packages/BillionSend) | 0.1.0 | BillionSend | The official .NET client for the BillionSend email API: send email, run inboxes… |
| 2026-11-17 10:50:16 | [Lark.OapiClient](https://www.nuget.org/packages/Lark.OapiClient) | 0.0.1 | Kingcean Tuan | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-10-19 21:19 UTC

New packages created between 2026-10-19 20:23 UTC and 2026-10-19 21:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-19T21-19-15-993397Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-19 20:29:57 | [Cratis.Arc.Connections.Azure](https://www.nuget.org/packages/Cratis.Arc.Connections.Azure) | 22.131.0 | all contributors | Microsoft Entra ID authentication for the Cratis Arc HTTP connection resolver:… |
| 2026-10-19 20:44:02 | [LogStream.AspNetCore](https://www.nuget.org/packages/LogStream.AspNetCore) | 1.0.0 | Samir Medeiros | Middleware ASP.NET Core que regista request/response correlacionados (TraceId/S… |
| 2026-10-19 20:44:02 | [LogStream.Serilog.Kafka](https://www.nuget.org/packages/LogStream.Serilog.Kafka) | 1.0.0 | Samir Medeiros | Sink Serilog para Kafka (um tópico por aplicação) usado pelo LogStream. |
| 2026-10-19 20:48:42 | [CodeFusion.Security.Bcrypt](https://www.nuget.org/packages/CodeFusion.Security.Bcrypt) | 1.0.0 | Krystian Pawłow | Fast, allocation-free bcrypt for .NET: up to five hashes interleaved per thread… |
| 2026-10-19 20:57:14 | [Starlings.Models.Kev](https://www.nuget.org/packages/Starlings.Models.Kev) | 0.3.0 | StarlingHq | Kev decision models (jaredpalmer/kev-0.8b and jaredpalmer/kev-4b, Kev 1.0) on O… |
| 2026-10-19 20:57:21 | [Starlings.Models.QwenChat](https://www.nuget.org/packages/Starlings.Models.QwenChat) | 0.3.0 | StarlingHq | Qwen/Qwen3-0.6B (revision c1899de2, thinking disabled) and Qwen/Qwen2.5-0.5B-In… |
| 2026-10-19 20:58:44 | [Sagara.Build.Versioning](https://www.nuget.org/packages/Sagara.Build.Versioning) | 1.0.0 | Jon Sagara | MSBuild-only package that versions your projects the way the .NET SDK does: NuG… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

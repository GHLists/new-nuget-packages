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

## Latest list — 2026-11-20 23:21 UTC

New packages created between 2026-11-20 22:21 UTC and 2026-11-20 23:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-20T23-21-53-795779Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-20 22:25:53 | [Eternet.WebAutomation.Parser.Contracts](https://www.nuget.org/packages/Eternet.WebAutomation.Parser.Contracts) | 1.0.0 | Eternet | Gateway contracts for the bank statement parser. |
| 2026-11-20 22:27:19 | [UIAGen](https://www.nuget.org/packages/UIAGen) | 1.0.0 | Piotr Filipowicz | Build-time code generator that turns Windows COM Type Libraries (TLB/DLL/EXE/Pr… |
| 2026-11-20 22:32:38 | [ManiaAPI.Dedimania](https://www.nuget.org/packages/ManiaAPI.Dedimania) | 2.11.0 | BigBang1112 | Wrapper for the Dedimania records API (dedimania.net). Part of the ManiaAPI.NET… |
| 2026-11-20 22:47:31 | [Mediana.Codecs.Pnm](https://www.nuget.org/packages/Mediana.Codecs.Pnm) | 0.1.31 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-20 22:47:35 | [Mediana.Images.Metadata](https://www.nuget.org/packages/Mediana.Images.Metadata) | 0.1.31 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-20 22:47:39 | [Mediana.Codecs.Tga](https://www.nuget.org/packages/Mediana.Codecs.Tga) | 0.1.31 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-20 22:47:41 | [Mediana.Codecs.OpenExr](https://www.nuget.org/packages/Mediana.Codecs.OpenExr) | 0.1.31 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-20 22:47:43 | [Mediana.Codecs.Qoi](https://www.nuget.org/packages/Mediana.Codecs.Qoi) | 0.1.31 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-20 23:07:53 | [Dataverse.Fluent.Testing](https://www.nuget.org/packages/Dataverse.Fluent.Testing) | 1.2.0 | Craig Franchuk | A fake transport for unit testing code that uses Dataverse.Fluent: route reques… |
| 2026-11-20 23:07:54 | [Dataverse.Fluent.Schema](https://www.nuget.org/packages/Dataverse.Fluent.Schema) | 1.2.0 | Craig Franchuk | Checks Dataverse.Fluent models against an environment's metadata: columns, type… |
| 2026-11-20 23:07:56 | [Dataverse.Fluent.Tool](https://www.nuget.org/packages/Dataverse.Fluent.Tool) | 1.2.0 | Craig Franchuk | The dataverse-fluent command: checks a project's Dataverse.Fluent models agains… |
| 2026-11-20 23:09:05 | [Instatus.Otel](https://www.nuget.org/packages/Instatus.Otel) | 0.1.0 | Instatus | Error tracking, logs, traces and metrics for .NET apps, built on OpenTelemetry,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

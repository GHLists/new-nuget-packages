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

## Latest list — 2026-10-20 01:21 UTC

New packages created between 2026-10-20 00:20 UTC and 2026-10-20 01:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-20T01-21-39-301519Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-20 00:38:42 | [VerifyAnything](https://www.nuget.org/packages/VerifyAnything) | 0.1.0 | OpenVerify contributors | VerifyAnything DRAFT VCP and Provider Contract wire SDK |
| 2026-10-20 00:39:20 | [ghts.MoleculasDeDesarrollo](https://www.nuget.org/packages/ghts.MoleculasDeDesarrollo) | 1.0.0 | Ulises-Farias | Development Molecules: a small pattern + DI helper to add the client's post-MVP… |
| 2026-10-20 00:46:32 | [LiquidGlass.Maui](https://www.nuget.org/packages/LiquidGlass.Maui) | 1.0.0 | shayann07 | .NET MAUI adapter for LiquidGlass: a GlassSurface view that refracts the app's… |
| 2026-10-20 00:59:19 | [Gravicode.Biotech.Net.Workflows](https://www.nuget.org/packages/Gravicode.Biotech.Net.Workflows) | 0.2.0 | Gravicode Studios | Snakemake/Nextflow-style workflow engine in C#: rules with file and in-memory i… |
| 2026-10-20 00:59:29 | [Gravicode.Biotech.Net.Data](https://www.nuget.org/packages/Gravicode.Biotech.Net.Data) | 0.2.0 | Gravicode Studios | Cloud data connectors for NCBI E-utilities, UniProt, RCSB PDB, AlphaFold DB and… |
| 2026-10-20 00:59:30 | [Gravicode.Biotech.Net.Gpu](https://www.nuget.org/packages/Gravicode.Biotech.Net.Gpu) | 0.2.0 | Gravicode Studios | GPU kernels on ILGPU (CUDA, OpenCL, CPU accelerator): all-vs-all Smith-Waterman… |
| 2026-10-20 01:05:03 | [CommonExceptionsTest](https://www.nuget.org/packages/CommonExceptionsTest) | 1.0.0 | circle08 | Package Description |
| 2026-10-20 01:05:15 | [SmartTableSync](https://www.nuget.org/packages/SmartTableSync) | 0.5.0 | Ruslan Sidoriako | A self-configuring sync engine for SQL tables Azure SQL Data Sync can't handle… |
| 2026-10-20 01:05:17 | [SmartTableSync.Scaffold](https://www.nuget.org/packages/SmartTableSync.Scaffold) | 0.5.0 | Ruslan Sidoriako | Manual schema-scaffolding CLI for SmartTableSync - introspects a table (or gene… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-10 21:19 UTC

New packages created between 2026-11-10 20:20 UTC and 2026-11-10 21:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-10T21-19-12-090736Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-10 20:21:27 | [UnambitiousFx.Myelin](https://www.nuget.org/packages/UnambitiousFx.Myelin) | 1.0.0 | UnambitiousFx | SSRF-safe outbound HTTP for .NET: resolves names itself, refuses private, loopb… |
| 2026-11-10 20:30:00 | [3DEngine.GlobalIllumination](https://www.nuget.org/packages/3DEngine.GlobalIllumination) | 6.2.30 | EggyStudio | Global illumination, cascades of light probes over the scene's distance field a… |
| 2026-11-10 20:31:40 | [SmodbusTcp](https://www.nuget.org/packages/SmodbusTcp) | 0.1.0 | Owain Cleaver | A small, modular Modbus TCP server library for .NET |
| 2026-11-10 20:31:42 | [SmodbusTcp.Kestrel](https://www.nuget.org/packages/SmodbusTcp.Kestrel) | 0.1.0 | Owain Cleaver | Kestrel integration for the SmodbusTcp Modbus TCP server library. |
| 2026-11-10 20:35:53 | [grate-mariadb](https://www.nuget.org/packages/grate-mariadb) | 2.3.0 | Erik A. Brandstadmoen | grate - sql for the 20s grate is a no-code, low-fi database migration tool, ins… |
| 2026-11-10 20:35:55 | [grate-oracle](https://www.nuget.org/packages/grate-oracle) | 2.3.0 | Erik A. Brandstadmoen | grate - sql for the 20s grate is a no-code, low-fi database migration tool, ins… |
| 2026-11-10 20:35:56 | [grate-postgresql](https://www.nuget.org/packages/grate-postgresql) | 2.3.0 | Erik A. Brandstadmoen | grate - sql for the 20s grate is a no-code, low-fi database migration tool, ins… |
| 2026-11-10 20:36:01 | [grate-sqlite](https://www.nuget.org/packages/grate-sqlite) | 2.3.0 | Erik A. Brandstadmoen | grate - sql for the 20s grate is a no-code, low-fi database migration tool, ins… |
| 2026-11-10 20:36:06 | [grate-sqlserver](https://www.nuget.org/packages/grate-sqlserver) | 2.3.0 | Erik A. Brandstadmoen | grate - sql for the 20s grate is a no-code, low-fi database migration tool, ins… |
| 2026-11-10 20:48:44 | [Verisoft.Core.ConfigurationStorage](https://www.nuget.org/packages/Verisoft.Core.ConfigurationStorage) | 1.1.21 | Verisoft.Core.ConfigurationSt… | Package Description |
| 2026-11-10 21:05:34 | [GitHttpBackend.Configuration](https://www.nuget.org/packages/GitHttpBackend.Configuration) | 11.0.0 | Zefek | Loads application configuration from a directory of a git repository served by… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

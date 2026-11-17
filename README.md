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

## Latest list — 2026-11-17 17:21 UTC

New packages created between 2026-11-17 16:21 UTC and 2026-11-17 17:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-17T17-21-30-21386Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-17 16:21:32 | [AzCfg](https://www.nuget.org/packages/AzCfg) | 0.1.0 | AzCfg.Cli | Local manager for Azure App Configuration and Key Vault: sync configs with loca… |
| 2026-11-17 16:33:21 | [PicoCalcNano.Display](https://www.nuget.org/packages/PicoCalcNano.Display) | 0.1.0 | Stéphane Sibué | Display driver for the Clockwork PicoCalc on .NET nanoFramework. Community proj… |
| 2026-11-17 16:45:37 | [Microsoft.Copilot.SDK](https://www.nuget.org/packages/Microsoft.Copilot.SDK) | 2.0.0 | Microsoft | SDK for programmatic control of GitHub Copilot CLI |
| 2026-11-17 16:51:59 | [PicoCalcNano.SdCard](https://www.nuget.org/packages/PicoCalcNano.SdCard) | 0.1.0 | Stéphane Sibué | SD card (SPI) and FAT16/FAT32 file system driver for the Clockwork PicoCalc on… |
| 2026-11-17 16:52:48 | [PicoCalcNano.Sound](https://www.nuget.org/packages/PicoCalcNano.Sound) | 0.1.0 | Stéphane Sibué | Sound driver for the Clockwork PicoCalc on .NET nanoFramework: beeps, notes and… |
| 2026-11-17 17:01:02 | [KvAsm.Client](https://www.nuget.org/packages/KvAsm.Client) | 0.3.0 | Eli Belash | .NET client for KvAsm, the gRPC key-value server written in x86-64 assembly: Ge… |
| 2026-11-17 17:05:18 | [PicoCalcNano.Console](https://www.nuget.org/packages/PicoCalcNano.Console) | 0.1.0 | Stéphane Sibué | Text console for the Clockwork PicoCalc on .NET nanoFramework: line editing, hi… |
| 2026-11-17 17:05:34 | [SqlSource](https://www.nuget.org/packages/SqlSource) | 0.1.0 | Michael Crawford | C# SQL query source generator. |
| 2026-11-17 17:05:35 | [SqlSource.Tool](https://www.nuget.org/packages/SqlSource.Tool) | 0.1.0 | Michael Crawford | The sqlsource command of the SqlSource C# SQL query source generator. |
| 2026-11-17 17:08:45 | [SharpTypst.DependencyInjection](https://www.nuget.org/packages/SharpTypst.DependencyInjection) | 0.15.1.3 | m3scalinum | Microsoft.Extensions.DependencyInjection integration for SharpTypst: register t… |
| 2026-11-17 17:08:46 | [SharpTypst.Templates.Generator](https://www.nuget.org/packages/SharpTypst.Templates.Generator) | 0.15.1.3 | m3scalinum | Source generator for SharpTypst templates: turns a template.toml manifest into… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

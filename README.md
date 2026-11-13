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

## Latest list — 2026-11-13 11:21 UTC

New packages created between 2026-11-13 10:22 UTC and 2026-11-13 11:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-13T11-21-11-469339Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-13 10:25:49 | [PocketCsvReader.Markdown](https://www.nuget.org/packages/PocketCsvReader.Markdown) | 2.76.1 | Cédric L. Charlier | PocketCsvReader.Markdown extends PocketCsvReader with a streaming reader for Gi… |
| 2026-11-13 10:29:23 | [MachinaXX.Ratchet.Measure.DotNet](https://www.nuget.org/packages/MachinaXX.Ratchet.Measure.DotNet) | 1.79.0 | Alan Benington | The .NET measurement command for Ratchet's test suite measurement: it runs a so… |
| 2026-11-13 10:40:22 | [CodeChops.Idioma](https://www.nuget.org/packages/CodeChops.Idioma) | 0.1.0 | CodeChops (@Code-Chops), Max… | Translations for any .NET app, written in C#: a class per language, or one-line… |
| 2026-11-13 10:48:22 | [Energinet.DataHub.ProcessManager.Orchestrations.MeteringPoints.Abstractions](https://www.nuget.org/packages/Energinet.DataHub.ProcessManager.Orchestrations.MeteringPoints.Abstractions) | 1.0.0-alpha-717 | Energinet-DataHub | [Release Notes](https://github.com/Energinet-DataHub/opengeh-process-manager/bl… |
| 2026-11-13 11:15:10 | [Olve.WebGPU.Browser](https://www.nuget.org/packages/Olve.WebGPU.Browser) | 0.1.0 | Oliver Vea | Olve.WebGPU in the browser: links Emscripten's emdawnwebgpu port into a .NET We… |
| 2026-11-13 11:15:12 | [Olve.WebGPU](https://www.nuget.org/packages/Olve.WebGPU) | 0.1.0 | Oliver Vea | A faithful C# mapping of WebGPU, generated from Dawn's webgpu.h. Callers need n… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

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

## Latest list — 2026-11-21 16:21 UTC

New packages created between 2026-11-21 15:21 UTC and 2026-11-21 16:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-21T16-21-39-227132Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-21 15:37:58 | [x402.Client.Nano](https://www.nuget.org/packages/x402.Client.Nano) | 0.0.3 | Michiel Post | x402 Payment Required Client implementation for Nano (XNO) |
| 2026-11-21 15:45:16 | [OneDevice.Master.Abstract](https://www.nuget.org/packages/OneDevice.Master.Abstract) | 3.0.0 | OneDevice.Master.Abstract | Package Description |
| 2026-11-21 15:45:17 | [OneDevice.Master.Factory](https://www.nuget.org/packages/OneDevice.Master.Factory) | 3.0.0 | OneDevice.Master.Factory | Package Description |
| 2026-11-21 15:45:18 | [OneDevice.Master.IoLink](https://www.nuget.org/packages/OneDevice.Master.IoLink) | 3.0.0 | OneDevice.Master.IoLink | Package Description |
| 2026-11-21 15:59:38 | [Material3Shapes](https://www.nuget.org/packages/Material3Shapes) | 1.0.0 | Matvey | UI-библиотека компонентов и фигур в стиле Google Material 3 (Material You и Mat… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

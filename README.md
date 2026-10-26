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

## Latest list — 2026-10-26 05:21 UTC

New packages created between 2026-10-26 04:21 UTC and 2026-10-26 05:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-26T05-21-19-787859Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-26 04:24:08 | [AutoModeCodeGenerator.Conventions.SqlSugar](https://www.nuget.org/packages/AutoModeCodeGenerator.Conventions.SqlSugar) | 1.0.1 | mccj | Optional SqlSugar-oriented string templates and mixin snippets for AutoModeCode… |
| 2026-10-26 04:31:02 | [PinataLabs.Typography](https://www.nuget.org/packages/PinataLabs.Typography) | 0.1.0 | PinataLabs | A cross-platform library for loading and laying out fonts for processing and me… |
| 2026-10-26 04:50:02 | [NextLevel.Communicator](https://www.nuget.org/packages/NextLevel.Communicator) | 1.0.0 | NextLevel | Channels between NextLevel services on MassTransit and RabbitMQ: broadcast with… |
| 2026-10-26 04:52:43 | [Meziantou.Framework.Barcodes](https://www.nuget.org/packages/Meziantou.Framework.Barcodes) | 1.0.0 | meziantou | QR and barcode generation with SVG, PNG, and console renderers |
| 2026-10-26 04:52:43 | [Meziantou.Framework.Imaging.Barcodes](https://www.nuget.org/packages/Meziantou.Framework.Imaging.Barcodes) | 1.0.0 | meziantou | Renders and draws the QR codes and barcodes of Meziantou.Framework.Barcodes wit… |
| 2026-10-26 04:58:40 | [cmd.Interactive.MenusCore](https://www.nuget.org/packages/cmd.Interactive.MenusCore) | 0.1.0 | JuliHyro Studios | A flexible interactive menu library for .NET console applications, featuring ne… |
| 2026-10-26 05:06:38 | [Wslc.Testcontainers.Modules.Azurite](https://www.nuget.org/packages/Wslc.Testcontainers.Modules.Azurite) | 0.7.0 | Nick Nadolski | Azurite module for Wslc.Testcontainers: typed builder, Azure Storage endpoints… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

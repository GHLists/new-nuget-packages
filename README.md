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

## Latest list — 2026-10-28 15:20 UTC

New packages created between 2026-10-28 14:21 UTC and 2026-10-28 15:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-28T15-20-16-920568Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-28 14:26:14 | [ISC.FoxERP.Common](https://www.nuget.org/packages/ISC.FoxERP.Common) | 1.0.0 | FPT Telecom - ISC | Response wrapper, error code chung, exception middleware, InsideMenu traceabili… |
| 2026-10-28 14:26:31 | [BlackSharp.UI.Avalonia.TreeDataGrid](https://www.nuget.org/packages/BlackSharp.UI.Avalonia.TreeDataGrid) | 1.2.6 | Blacktempel, Fidarit Mullayan… | TreeDataGrid displays hierarchical and tabular data in a single Avalonia contro… |
| 2026-10-28 14:34:24 | [TransferX.Domain](https://www.nuget.org/packages/TransferX.Domain) | 3.0.0 | TransferX | Domain models for the TransferX plugin SDK |
| 2026-10-28 14:34:25 | [TransferX.Provider.Abstractions](https://www.nuget.org/packages/TransferX.Provider.Abstractions) | 3.0.0 | TransferX | Plugin abstractions for TransferX provider development. Referencing TransferX.C… |
| 2026-10-28 14:34:26 | [TransferX.Transfer.Abstractions](https://www.nuget.org/packages/TransferX.Transfer.Abstractions) | 3.0.0 | TransferX | Plugin abstractions for TransferX transfer command development |
| 2026-10-28 14:36:57 | [DynamicDave.Umbraco.MapToRedirect](https://www.nuget.org/packages/DynamicDave.Umbraco.MapToRedirect) | 18.0.1 | DynamicDave | Turns a CSV of old and new URLs into Umbraco redirects. Can also generate the C… |
| 2026-10-28 14:47:30 | [Fergi](https://www.nuget.org/packages/Fergi) | 0.1.1-alpha1 | Devon Burriss | Fergi: selectors, document operations and patches over the Fnode core. Pure and… |
| 2026-10-28 14:47:31 | [Fergi.Tool](https://www.nuget.org/packages/Fergi.Tool) | 0.1.1-alpha1 | Devon Burriss | The fergi command line (dotnet tool): validate and run mapping files. .NET only… |
| 2026-10-28 14:57:56 | [SA.Umbraco.MediaPreview](https://www.nuget.org/packages/SA.Umbraco.MediaPreview) | 1.0.0 | suedeapple | Adds a Preview action to Umbraco media cards that opens the media item in a fly… |
| 2026-10-28 15:07:51 | [OpenAC.Net.NFSe.Web](https://www.nuget.org/packages/OpenAC.Net.NFSe.Web) | 1.8.1 | Projeto OpenAC .Net | Integração da OpenAC.Net.NFSe com DI, logging e serviços do ASP.NET Core. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

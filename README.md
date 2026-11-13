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

## Latest list — 2026-11-13 23:21 UTC

New packages created between 2026-11-13 22:19 UTC and 2026-11-13 23:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-13T23-21-33-619194Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-13 22:19:46 | [NumSharp.Interop.TorchSharp](https://www.nuget.org/packages/NumSharp.Interop.TorchSharp) | 0.81.0 | Eli Belash, Haiping Chen, Mei… | Interop between NumSharp NDArray and TorchSharp tensors (.NET bindings for libt… |
| 2026-11-13 22:27:15 | [HtmlToOpenXml.CssInliner](https://www.nuget.org/packages/HtmlToOpenXml.CssInliner) | 1.0.0 | Olivier Nizet | Extension library to HtmlToOpenXml to support CSS stylesheet. |
| 2026-11-13 22:32:45 | [Medical.HuggingFace](https://www.nuget.org/packages/Medical.HuggingFace) | 1.3.0 | Gravicode Studios (Kang Fadhi… | Medical.Net on Hugging Face via HF.Net (GraviTransformers): local transformer m… |
| 2026-11-13 22:45:37 | [AbpPlugin.Sdk](https://www.nuget.org/packages/AbpPlugin.Sdk) | 0.1.1 | AbpPlugin contributors | What a plugin references to run in an AbpPlugin host: its entry, registrations,… |
| 2026-11-13 22:45:38 | [AbpPlugin.Sign](https://www.nuget.org/packages/AbpPlugin.Sign) | 0.1.1 | AbpPlugin contributors | Signs plugin packages for an AbpPlugin host and makes signing keys: what a buil… |
| 2026-11-13 22:45:38 | [AbpPlugin.Packaging](https://www.nuget.org/packages/AbpPlugin.Packaging) | 0.1.1 | AbpPlugin contributors | The package format of AbpPlugin: signing keys and their IDs, a package's digest… |
| 2026-11-13 22:45:39 | [AbpPlugin](https://www.nuget.org/packages/AbpPlugin) | 0.1.1 | AbpPlugin contributors | A plugin host for ABP applications: installs signed plugin packages at run time… |
| 2026-11-13 22:45:39 | [AbpPlugin.Build](https://www.nuget.org/packages/AbpPlugin.Build) | 0.1.1 | AbpPlugin contributors | Builds a plugin for an AbpPlugin host into the folder and the zip the host inst… |
| 2026-11-13 22:58:32 | [PolishOpenData.Bdl](https://www.nuget.org/packages/PolishOpenData.Bdl) | 1.8.0 | JacekSmi | Typed .NET client for the GUS Bank Danych Lokalnych (BDL) API: find voivodeship… |
| 2026-11-13 22:58:34 | [PolishOpenData.Ceidg](https://www.nuget.org/packages/PolishOpenData.Ceidg) | 1.8.0 | JacekSmi | Typed .NET client for the CEIDG v3 API (Centralna Ewidencja i Informacja o Dzia… |
| 2026-11-13 22:58:35 | [PolishOpenData.Geo.Nts](https://www.nuget.org/packages/PolishOpenData.Geo.Nts) | 1.8.0 | JacekSmi | NetTopologySuite adapter for PolishOpenData: turns the WKT parcel boundary from… |
| 2026-11-13 23:02:53 | [Dloizides.Approvals](https://www.nuget.org/packages/Dloizides.Approvals) | 0.1.0 | DLoizides | Maker-checker (four-eyes) approval rule: refuses an approver who contributed to… |
| 2026-11-13 23:06:02 | [Sondor.AspNetCore](https://www.nuget.org/packages/Sondor.AspNetCore) | 0.1.0 | Sondor Dev | One consistent RFC 9457 problem response for an ASP.NET Core API: a failed Sond… |
| 2026-11-13 23:11:01 | [Identity.Authorization.AspNetCore](https://www.nuget.org/packages/Identity.Authorization.AspNetCore) | 0.1.0 | DLoizides | ASP.NET Core wiring for the Identity.Abstractions permission model: a perm:name… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

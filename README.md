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

## Latest list — 2026-10-28 14:21 UTC

New packages created between 2026-10-28 13:20 UTC and 2026-10-28 14:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-28T14-21-23-884061Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-28 13:24:46 | [RaidiantAI.Analytics](https://www.nuget.org/packages/RaidiantAI.Analytics) | 0.1.0 | Raidiant LLC | Send a tool's usage to Raidiant AI from a .NET server, with a tool key. |
| 2026-10-28 13:28:05 | [GBX.NET.Builders](https://www.nuget.org/packages/GBX.NET.Builders) | 2.5.0 | BigBang1112 | Generated fluent builders that create GBX.NET nodes for a selected game version. |
| 2026-10-28 13:28:11 | [GBX.NET.CLI](https://www.nuget.org/packages/GBX.NET.CLI) | 0.1.0 | BigBang1112 | A command-line interface for inspecting and transforming Gbx files with GBX.NET. |
| 2026-10-28 13:41:34 | [erpya-local-printing-all-in-one-dotnet](https://www.nuget.org/packages/erpya-local-printing-all-in-one-dotnet) | 2.0.0-rc | Yamel Senih | This package adds support to Fiscal Printer sing The Factory HKA and other prov… |
| 2026-10-28 13:54:20 | [Xamarin.AndroidX.Camera.Viewfinder.Compose](https://www.nuget.org/packages/Xamarin.AndroidX.Camera.Viewfinder.Compose) | 1.6.2 | Microsoft | .NET for Android and MAUI bindings for the Android Java library 'androidx.camer… |
| 2026-10-28 13:54:22 | [Xamarin.AndroidX.Camera.Viewfinder.View](https://www.nuget.org/packages/Xamarin.AndroidX.Camera.Viewfinder.View) | 1.6.2 | Microsoft | .NET for Android and MAUI bindings for the Android Java library 'androidx.camer… |
| 2026-10-28 13:54:54 | [Xamarin.AndroidX.Test.Espresso.Idling.Resource](https://www.nuget.org/packages/Xamarin.AndroidX.Test.Espresso.Idling.Resource) | 3.7.0 | Microsoft | .NET for Android and MAUI bindings for the Android Java library 'androidx.test.… |
| 2026-10-28 13:56:38 | [OptimaJet.Workflow.Api.Template](https://www.nuget.org/packages/OptimaJet.Workflow.Api.Template) | 23.0.0 | Optimajet Limited | Creates a .NET solution that hosts the Workflow Engine HTTP API with a selected… |
| 2026-10-28 14:03:46 | [Thalos.NET.Ollama](https://www.nuget.org/packages/Thalos.NET.Ollama) | 0.20.0 | Marcel Roozekrans | Ollama embedding generator for Thalos.NET. |
| 2026-10-28 14:08:45 | [Axios.Net](https://www.nuget.org/packages/Axios.Net) | 0.1.0 | FrenchyApps42, Sikelio | An axios-like HTTP client for .NET: Axios.Get<T>(url), Axios.Create(config), in… |
| 2026-10-28 14:12:07 | [Aspose.Medical.Dicom.Web.AspNetCore](https://www.nuget.org/packages/Aspose.Medical.Dicom.Web.AspNetCore) | 26.10.0 | Aspose | ASP.NET Core hosting integration for Aspose.Medical DICOMweb applications, incl… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

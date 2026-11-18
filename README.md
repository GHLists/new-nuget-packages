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

## Latest list — 2026-11-18 04:20 UTC

New packages created between 2026-11-18 03:21 UTC and 2026-11-18 04:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-18T04-20-35-425853Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-18 03:40:20 | [Aspire.Hosting.Azure.Kubernetes](https://www.nuget.org/packages/Aspire.Hosting.Azure.Kubernetes) | 17.0.0 | Microsoft | Azure Kubernetes Service (AKS) resource types for Aspire. |
| 2026-11-18 03:41:31 | [Aspire.Hosting.Dotnet](https://www.nuget.org/packages/Aspire.Hosting.Dotnet) | 17.0.0 | Microsoft | C# and .NET application support for Aspire. |
| 2026-11-18 03:41:37 | [Aspire.Hosting.Go](https://www.nuget.org/packages/Aspire.Hosting.Go) | 17.0.0 | Microsoft | Go support for Aspire. |
| 2026-11-18 03:41:44 | [Aspire.Hosting.Kubernetes](https://www.nuget.org/packages/Aspire.Hosting.Kubernetes) | 17.0.0 | Microsoft | Kubernetes publishing for Aspire. |
| 2026-11-18 03:44:35 | [CefSharp.Avalonia.Windows](https://www.nuget.org/packages/CefSharp.Avalonia.Windows) | 1.3.0 | CefBrowser | Windows (x64) native binaries (CEF runtime + CefBrowser.Native host) for CefSha… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

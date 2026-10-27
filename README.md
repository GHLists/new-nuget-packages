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

## Latest list — 2026-10-27 20:20 UTC

New packages created between 2026-10-27 19:21 UTC and 2026-10-27 20:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-27T20-20-40-152119Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-27 19:27:08 | [SeoWebChecker.Umbraco](https://www.nuget.org/packages/SeoWebChecker.Umbraco) | 1.0.0 | SEOWebChecker | Comprehensive on-page search engine optimization (SEO) diagnostics, meta tag an… |
| 2026-10-27 19:27:15 | [ISU.Redux.Library](https://www.nuget.org/packages/ISU.Redux.Library) | 1.1.8 | Redux Contributors | A .NET library for computational problems, solvers, verifiers, reductions, and… |
| 2026-10-27 19:47:14 | [Soenneker.Pinterest.OpenApiClient](https://www.nuget.org/packages/Soenneker.Pinterest.OpenApiClient) | 11.0.1 | Jake Soenneker | A generated OpenAPI client for Pinterest. |
| 2026-10-27 19:49:44 | [TencentCloudSDK.Cvd](https://www.nuget.org/packages/TencentCloudSDK.Cvd) | 3.0.1528 | Tencent Cloud API Team | Tencent Cloud API 3.0 SDK for .NET |
| 2026-10-27 19:50:31 | [Soenneker.Pinterest.HttpClients](https://www.nuget.org/packages/Soenneker.Pinterest.HttpClients) | 11.0.1 | Jake Soenneker | A thread-safe singleton HttpClient for Pinterest's OpenAPI integration. |
| 2026-10-27 19:50:47 | [Google.Shopping.Merchant.Reviews.V1](https://www.nuget.org/packages/Google.Shopping.Merchant.Reviews.V1) | 1.0.0-beta01 | Google LLC | Programmatically manage your Merchant Center Accounts. |
| 2026-10-27 19:50:50 | [Google.Cloud.Observability.V1](https://www.nuget.org/packages/Google.Cloud.Observability.V1) | 1.0.0-beta01 | Google LLC | Provides functionality for configuring the observability scope, which controls… |
| 2026-10-27 19:50:52 | [Google.Cloud.DesignCenter.V1](https://www.nuget.org/packages/Google.Cloud.DesignCenter.V1) | 1.0.0-beta01 | Google LLC | Design and share deployable application architectures. |
| 2026-10-27 19:53:33 | [Simplepage.Umbraco.SafeMedia](https://www.nuget.org/packages/Simplepage.Umbraco.SafeMedia) | 1.0.0 | Simplepage Ltd | Refuses unsafe SVG uploads in Umbraco before they are stored. Parses rather tha… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

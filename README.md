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

## Latest list — 2026-10-02 04:19 UTC

New packages created between 2026-10-02 03:19 UTC and 2026-10-02 04:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-02T04-19-45-645887Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-02 03:27:55 | [Webority.Email.Graph](https://www.nuget.org/packages/Webority.Email.Graph) | 0.23.0 | Webority Technologies | Microsoft 365 inbound mail for Webority.Email over Webority.Graph: reads messag… |
| 2026-10-02 03:44:17 | [CodeBrix.Platform.PlayTest.ApacheLicenseForever](https://www.nuget.org/packages/CodeBrix.Platform.PlayTest.ApacheLicenseForever) | 1.0.275.207 | Jeremy Ellis and contributors | Playwright-style application tests on a fixed, cross-platform virtual Skia scre… |
| 2026-10-02 03:46:37 | [Webority.Support.Ai](https://www.nuget.org/packages/Webority.Support.Ai) | 0.4.0 | Webority Technologies | AI for Webority support: the chat tools a product's assistant uses to list, rea… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.

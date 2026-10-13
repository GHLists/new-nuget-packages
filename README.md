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

## Latest list — 2026-10-13 19:22 UTC

New packages created between 2026-10-13 18:19 UTC and 2026-10-13 19:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-13T19-22-21-557684Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-13 18:36:50 | [SjolystInnovation.AppKit.Email](https://www.nuget.org/packages/SjolystInnovation.AppKit.Email) | 0.1.0 | Sjølyst Innovation AS | Transactional email through Brevo, with reply-to, attachments, a send result in… |
| 2026-10-13 18:47:09 | [Blacus.DataTools](https://www.nuget.org/packages/Blacus.DataTools) | 1.0.1 | Blacus | A lightweight, zero-dependency, and highly optimized .NET 10 library designed t… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
